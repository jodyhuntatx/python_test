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
from conjur.api.certificate_authority_api import CertificateAuthorityApi  # noqa: E501
from conjur.rest import ApiException


class TestCertificateAuthorityApi(unittest.TestCase):
    """CertificateAuthorityApi unit test stubs"""

    def setUp(self):
        self.api = conjur.api.certificate_authority_api.CertificateAuthorityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sign(self):
        """Test case for sign

        Gets a signed certificate from the configured Certificate Authority service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
