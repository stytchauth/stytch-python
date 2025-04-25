#!/usr/bin/env python3

import unittest
import warnings
from unittest import TestCase
from unittest.mock import MagicMock, patch

import jwt
import pydantic

from stytch.core.client_base import ClientBase
from stytch.consumer.client import Client
from stytch.b2b.client import Client as B2BClient



class CustomBaseURLClientRequests(TestCase):
    @patch("requests.post")
    def test_consumer_api_call_uses_custom_base_url(self, mock_post):
        """
        Verify Consumer client builds URLs with custom base URL + makes requests with that URL.
        We deliberately return an incomplete JSON body so Pydantic raises ValidationError; we catch it and still assert URL usage.
        """
        custom_url = "https://custom.api.example.com"
        # Mock minimal response
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"request_id": "id", "status_code": 200}
        mock_post.return_value = mock_resp

        client = Client("project-test-123", "secret", custom_base_url=custom_url, suppress_warnings=True)

        with self.assertRaises(pydantic.ValidationError):
            client.magic_links.email.login_or_create(email="test@example.com")

        # requests.post should have been invoked despite ValidationError
        self.assertTrue(mock_post.called)
        url_called = mock_post.call_args[0][0]
        self.assertTrue(url_called.startswith(custom_url + "/"))
        self.assertIn("/v1/magic_links/email/", url_called)

    @patch("requests.post")
    def test_b2b_api_call_uses_custom_base_url(self, mock_post):
        """
        Verify B2B client builds URLs with custom base URL + makes requests with that URL.
        We deliberately return an incomplete JSON body so Pydantic raises ValidationError; we catch it and still assert URL usage.
        """
        custom_url = "https://custom.api.example.com"
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {"request_id": "id", "status_code": 200}
        mock_post.return_value = mock_resp

        client = B2BClient("project-test-123", "secret", custom_base_url=custom_url, suppress_warnings=True)

        with self.assertRaises(pydantic.ValidationError):
            client.magic_links.email.login_or_signup(organization_id="org", email_address="test@example.com")

        self.assertTrue(mock_post.called)
        url_called = mock_post.call_args[0][0]
        self.assertTrue(url_called.startswith(custom_url + "/"))
        self.assertIn("/v1/b2b/magic_links/email/", url_called)

class ClientBaseBase(TestCase):
    def test_resolve_api_url_custom_base_url(self):
        """Test that custom_base_url is prioritized over environment."""
        # Arrange
        custom_url = "https://custom.api.example.com/"
        
        # Act
        result = ClientBase._resolve_api_url(
            "project-test-123", 
            "test", 
            custom_url, 
            True  # suppress_warnings
        )
        
        # Assert
        self.assertEqual(result, custom_url)
    
    def test_resolve_api_url_adds_trailing_slash(self):
        """Test that a trailing slash is added to custom_base_url if not present."""
        # Arrange
        custom_url = "https://custom.api.example.com"
        custom_url_with_slash = "https://custom.api.example.com/"
        
        # Act
        result1 = ClientBase._resolve_api_url(
            "project-test-123", 
            None, 
            custom_url, 
            True
        )
        result2 = ClientBase._resolve_api_url(
            "project-test-123", 
            None, 
            custom_url_with_slash, 
            True
        )
        
        # Assert
        self.assertEqual(result1, custom_url_with_slash)
        self.assertEqual(result2, custom_url_with_slash)
    
    def test_resolve_api_url_warning_when_both_provided(self):
        """Test that a warning is issued when both environment and custom_base_url are provided."""
        # Arrange
        custom_url = "https://custom.api.example.com"
        
        # Act
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            ClientBase._resolve_api_url("project-test-123", "test", custom_url, False)
            
            # Assert
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[0].category, Warning))
            self.assertIn("custom_base_url will take precedence", str(w[0].message))
    
    def test_resolve_api_url_environment_test(self):
        """Test that the correct URL is returned for test environment."""
        # Act
        result = ClientBase._resolve_api_url("project-test-123", "test", None, True)
        
        # Assert
        self.assertEqual(result, "https://test.stytch.com/")
    
    def test_resolve_api_url_environment_live(self):
        """Test that the correct URL is returned for live environment."""
        # Act
        result = ClientBase._resolve_api_url("project-test-123", "live", None, True)
        
        # Assert
        self.assertEqual(result, "https://api.stytch.com/")
    
    def test_resolve_api_url_auto_detection(self):
        """Test that environment is auto-detected based on project_id."""
        # Act
        result_live = ClientBase._resolve_api_url("project-live-123", None, None, True)
        result_test = ClientBase._resolve_api_url("project-test-123", None, None, True)
        
        # Assert
        self.assertEqual(result_live, "https://api.stytch.com/")
        self.assertEqual(result_test, "https://test.stytch.com/")

    def test_resolve_api_url_requires_https(self):
        """Test that custom_base_url must use HTTPS scheme."""
        # Arrange
        non_https_url = "http://custom.api.example.com"
        
        # Act & Assert
        with self.assertRaises(ValueError) as context:
            ClientBase._resolve_api_url(
                "project-test-123", 
                None, 
                non_https_url
            )
        
        # Verify the error message
        self.assertIn("HTTPS scheme", str(context.exception)) 
