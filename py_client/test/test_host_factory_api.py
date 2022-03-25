# coding: utf-8

"""
    Conjur

    This is an API definition for CyberArk Conjur Open Source. You can find out more at [Conjur.org](https://www.conjur.org/).  # noqa: E501

    The version of the OpenAPI document: 5.3.0
    Contact: conj_maintainers@cyberark.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import conjur
from conjur.api.host_factory_api import HostFactoryApi  # noqa: E501
from conjur.rest import ApiException


class TestHostFactoryApi(unittest.TestCase):
    """HostFactoryApi unit test stubs"""

    def setUp(self):
        self.api = conjur.api.host_factory_api.HostFactoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_host(self):
        """Test case for create_host

        Creates a Host using the Host Factory.  # noqa: E501
        """
        pass

    def test_create_token(self):
        """Test case for create_token

        Creates one or more host identity tokens.  # noqa: E501
        """
        pass

    def test_revoke_token(self):
        """Test case for revoke_token

        Revokes a token, immediately disabling it.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
