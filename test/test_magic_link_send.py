# coding: utf-8

"""
    Stytch

    This is the Stytch api.  You can find out more about Stytch at  [stytch.com](https://stytch.com).   # noqa: E501

    The version of the OpenAPI document: v1
    Contact: hello@stytch.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import stytch
from stytch.models.magic_link_send import MagicLinkSend  # noqa: E501
from stytch.rest import ApiException

class TestMagicLinkSend(unittest.TestCase):
    """MagicLinkSend unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MagicLinkSend
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = stytch.models.magic_link_send.MagicLinkSend()  # noqa: E501
        if include_optional :
            return MagicLinkSend(
                user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002', 
                method_id = 'email-test-c1a1d554-a93c-11ea-bb37-0242ac130002', 
                magic_link_url = '0', 
                expiration_minutes = 10, 
                template_id = 'email-template-test-c1a1d554-a93c-11ea-bb37-0242ac130002', 
                attributes = stytch.models.attributes.Attributes(
                    ip_address = '10.1.10.1', 
                    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1', )
            )
        else :
            return MagicLinkSend(
                user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002',
                method_id = 'email-test-c1a1d554-a93c-11ea-bb37-0242ac130002',
        )

    def testMagicLinkSend(self):
        """Test MagicLinkSend"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
