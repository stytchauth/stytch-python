import stytch
import pytest


class TestIntegration:
    """
    This tests runs through available api calls in the API

    Pass in your project id and secret to run this.
    """

    @pytest.mark.unit
    def test_full_user_flow(self, project_id, secret, email):
        # Instantiate stytch client with command line args
        stytch_client = stytch.Client(
            project_id=project_id,
            secret=secret,
            environment="test",
        )

        # Create a Stytch user.
        # curl -X POST https://api.stytch.com/v1/users -u project_id:secret
        # -d '{ email: "user@test.com", name : { first_name: "Nathan", last_name: "Chiu" } }'
        resp = stytch_client.Users.create(
            email=email, first_name="Nathan", last_name="Chiu"
        )
        assert resp.status_code == 201
        created_user_id = resp.json()["userId"]

        # Get that recently created user.
        # curl -X GET https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        resp = stytch_client.Users.get(created_user_id)
        assert resp.status_code == 200
        user_id = resp.json()["userId"]

        # Update that user's middle name.
        # curl -X PUT https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        # -d '{ name: { middle_name: "Big" } }'
        stytch_client.Users.update(user_id=user_id, middle_name="Middle")
        assert resp.status_code == 200

        # Check that update worked
        resp = stytch_client.Users.get(user_id)
        assert resp.status_code == 200
        user_data = resp.json()
        assert user_data["name"]["middleName"] == "Middle"

        # Get Pending Users
        # curl -X POST https://api.stytch.com/v1/users/pending -u projectId:secret
        resp = stytch_client.Users.get_pending_users(limit=1)
        assert resp.status_code == 200

        """
        Magic Link routes
        """
        user_id = user_data["userId"]
        email_id = user_data["emails"][0]["emailId"]
        assert email_id

        # Send magic link to email id
        # curl -X POST https://api.stytch.com/v1/magic_links/send -u projectId:secret
        # -d { method_id: "email-id-123", user_id: "user-id-123",
        #       magic_link_url: "https://test.com/login"}
        resp = stytch_client.MagicLinks.send(
            method_id=email_id,
            user_id=user_id,
            magic_link_url="https://test.com/login",
            attributes={
                "ip_address": "1.1.1.1",
                "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                + "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            },
        )
        assert resp.status_code == 200

        # Send magic link to email
        # curl -X POST https://api.stytch.com/v1/magic_links/send_by_email -u projectId:secret
        # -d { email: "sandbox@stytch.com", user_id: "user-id-123",
        #       magic_link_url: "https://test.com/login"}
        resp = stytch_client.MagicLinks.send_by_email(
            email="sandbox@stytch.com",
            magic_link_url="https://test.com/login",
        )
        assert resp.status_code == 200

        # Login or Create User
        # curl -X POST https://api.stytch.com/v1/magic_links/login_or_create -u projectId:secret
        # -d { email: "sandbox@stytch.com",
        #     signup_magic_link_url: "https://test.com/signup",
        #     login_magic_link_url: "https://test.com/login"}
        resp = stytch_client.MagicLinks.login_or_create(
            email="sandbox@stytch.com",
            login_magic_link_url="https://test.com/login",
            signup_magic_link_url="https://test.com/signup",
        )
        assert resp.status_code == 200

        # Invite By Email
        # curl -X POST https://api.stytch.com/v1/magic_links/invite_by_email -u projectId:secret
        # -d { email: "sandbox+1@stytch.com",
        #     magic_link_url: "https://test.com/invite"}
        resp = stytch_client.MagicLinks.invite_by_email(
            email="sandbox@stytch.com",
            magic_link_url="https://test.com/invite",
        )
        assert resp.status_code == 200

        # Revoke Invite By Email
        # curl -X POST https://api.stytch.com/v1/magic_links/revoke_invite -u projectId:secret
        # -d { email: "sandbox+1@stytch.com"}
        resp = stytch_client.MagicLinks.revoke_invite_by_email(
            email="sandbox@stytch.com",
        )
        assert resp.status_code == 200

        # TODO: Test this
        #  Authenticate that token
        # curl -X POST https://api.stytch.com/v1/magic_links/authenticate -u project_id:secret
        # -d '{ email: "user@test.com", name : { first_name: "Nathan", last_name: "Chiu" } }'
        # stytch_client.MagicLinks.authenticate()
        # stytch_client.MagicLinks.authenticate(token=token)

        # Delete the created test user.
        # curl -X DELETE https://api.stytch.com/v1/users/<user_id> -u project_id:secret
        resp = stytch_client.Users.delete(user_data["userId"])
        assert resp.status_code == 200
