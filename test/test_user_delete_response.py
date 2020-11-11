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
from stytch.models.user_delete_response import UserDeleteResponse  # noqa: E501
from stytch.rest import ApiException

class TestUserDeleteResponse(unittest.TestCase):
    """UserDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserDeleteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = stytch.models.user_delete_response.UserDeleteResponse()  # noqa: E501
        if include_optional :
            return UserDeleteResponse(
                request_id = 'request-id-test-d9642d25-ec34-4319-8d17-d819c9b1f6e3', 
                user_id = 'user-test-b8797f2c-a93c-11ea-bb37-0242ac130002'
            )
        else :
            return UserDeleteResponse(
        )

    def testUserDeleteResponse(self):
        """Test UserDeleteResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
