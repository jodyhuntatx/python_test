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
from conjur.api.policies_api import PoliciesApi  # noqa: E501
from conjur.rest import ApiException


class TestPoliciesApi(unittest.TestCase):
    """PoliciesApi unit test stubs"""

    def setUp(self):
        self.api = conjur.api.policies_api.PoliciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_load_policy(self):
        """Test case for load_policy

        Adds data to the existing Conjur policy.  # noqa: E501
        """
        pass

    def test_replace_policy(self):
        """Test case for replace_policy

        Loads or replaces a Conjur policy document.  # noqa: E501
        """
        pass

    def test_update_policy(self):
        """Test case for update_policy

        Modifies an existing Conjur policy.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
