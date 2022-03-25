# coding: utf-8

"""
    Conjur

    This is an API definition for CyberArk Conjur Open Source. You can find out more at [Conjur.org](https://www.conjur.org/).  # noqa: E501

    The version of the OpenAPI document: 5.3.0
    Contact: conj_maintainers@cyberark.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from conjur.configuration import Configuration


class CreateHostTokenForm(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'cidr': 'list[str]',
        'count': 'int',
        'expiration': 'str',
        'host_factory': 'str'
    }

    attribute_map = {
        'cidr': 'cidr',
        'count': 'count',
        'expiration': 'expiration',
        'host_factory': 'host_factory'
    }

    def __init__(self, cidr=None, count=None, expiration=None, host_factory=None, local_vars_configuration=None):  # noqa: E501
        """CreateHostTokenForm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cidr = None
        self._count = None
        self._expiration = None
        self._host_factory = None
        self.discriminator = None

        if cidr is not None:
            self.cidr = cidr
        if count is not None:
            self.count = count
        self.expiration = expiration
        self.host_factory = host_factory

    @property
    def cidr(self):
        """Gets the cidr of this CreateHostTokenForm.  # noqa: E501

        Number of host tokens to create  # noqa: E501

        :return: The cidr of this CreateHostTokenForm.  # noqa: E501
        :rtype: list[str]
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateHostTokenForm.

        Number of host tokens to create  # noqa: E501

        :param cidr: The cidr of this CreateHostTokenForm.  # noqa: E501
        :type: list[str]
        """

        self._cidr = cidr

    @property
    def count(self):
        """Gets the count of this CreateHostTokenForm.  # noqa: E501

        Number of host tokens to create  # noqa: E501

        :return: The count of this CreateHostTokenForm.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this CreateHostTokenForm.

        Number of host tokens to create  # noqa: E501

        :param count: The count of this CreateHostTokenForm.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def expiration(self):
        """Gets the expiration of this CreateHostTokenForm.  # noqa: E501

        `ISO 8601 datetime` denoting a requested expiration time.  # noqa: E501

        :return: The expiration of this CreateHostTokenForm.  # noqa: E501
        :rtype: str
        """
        return self._expiration

    @expiration.setter
    def expiration(self, expiration):
        """Sets the expiration of this CreateHostTokenForm.

        `ISO 8601 datetime` denoting a requested expiration time.  # noqa: E501

        :param expiration: The expiration of this CreateHostTokenForm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and expiration is None:  # noqa: E501
            raise ValueError("Invalid value for `expiration`, must not be `None`")  # noqa: E501

        self._expiration = expiration

    @property
    def host_factory(self):
        """Gets the host_factory of this CreateHostTokenForm.  # noqa: E501

        Fully qualified host factory ID  # noqa: E501

        :return: The host_factory of this CreateHostTokenForm.  # noqa: E501
        :rtype: str
        """
        return self._host_factory

    @host_factory.setter
    def host_factory(self, host_factory):
        """Sets the host_factory of this CreateHostTokenForm.

        Fully qualified host factory ID  # noqa: E501

        :param host_factory: The host_factory of this CreateHostTokenForm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host_factory is None:  # noqa: E501
            raise ValueError("Invalid value for `host_factory`, must not be `None`")  # noqa: E501

        self._host_factory = host_factory

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateHostTokenForm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateHostTokenForm):
            return True

        return self.to_dict() != other.to_dict()