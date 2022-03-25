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
import datetime

import conjur
from conjur.models.certificate_json import CertificateJson  # noqa: E501
from conjur.rest import ApiException

class TestCertificateJson(unittest.TestCase):
    """CertificateJson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CertificateJson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = conjur.models.certificate_json.CertificateJson()  # noqa: E501
        if include_optional :
            return CertificateJson(
                certificate = '0'
            )
        else :
            return CertificateJson(
        )

    def testCertificateJson(self):
        """Test CertificateJson"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
