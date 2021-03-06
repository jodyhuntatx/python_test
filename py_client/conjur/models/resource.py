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


class Resource(object):
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
        'annotations': 'list[str]',
        'created_at': 'str',
        'id': 'str',
        'owner': 'str',
        'permissions': 'list[ResourcePermissions]',
        'policy': 'str',
        'policy_versions': 'list[PolicyVersion]',
        'restricted_to': 'list[str]',
        'secrets': 'list[ResourceSecrets]'
    }

    attribute_map = {
        'annotations': 'annotations',
        'created_at': 'created_at',
        'id': 'id',
        'owner': 'owner',
        'permissions': 'permissions',
        'policy': 'policy',
        'policy_versions': 'policy_versions',
        'restricted_to': 'restricted_to',
        'secrets': 'secrets'
    }

    def __init__(self, annotations=None, created_at=None, id=None, owner=None, permissions=None, policy=None, policy_versions=None, restricted_to=None, secrets=None, local_vars_configuration=None):  # noqa: E501
        """Resource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._annotations = None
        self._created_at = None
        self._id = None
        self._owner = None
        self._permissions = None
        self._policy = None
        self._policy_versions = None
        self._restricted_to = None
        self._secrets = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if owner is not None:
            self.owner = owner
        if permissions is not None:
            self.permissions = permissions
        if policy is not None:
            self.policy = policy
        if policy_versions is not None:
            self.policy_versions = policy_versions
        if restricted_to is not None:
            self.restricted_to = restricted_to
        if secrets is not None:
            self.secrets = secrets

    @property
    def annotations(self):
        """Gets the annotations of this Resource.  # noqa: E501


        :return: The annotations of this Resource.  # noqa: E501
        :rtype: list[str]
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Resource.


        :param annotations: The annotations of this Resource.  # noqa: E501
        :type: list[str]
        """

        self._annotations = annotations

    @property
    def created_at(self):
        """Gets the created_at of this Resource.  # noqa: E501


        :return: The created_at of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Resource.


        :param created_at: The created_at of this Resource.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this Resource.  # noqa: E501


        :return: The id of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Resource.


        :param id: The id of this Resource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this Resource.  # noqa: E501


        :return: The owner of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Resource.


        :param owner: The owner of this Resource.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def permissions(self):
        """Gets the permissions of this Resource.  # noqa: E501


        :return: The permissions of this Resource.  # noqa: E501
        :rtype: list[ResourcePermissions]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this Resource.


        :param permissions: The permissions of this Resource.  # noqa: E501
        :type: list[ResourcePermissions]
        """

        self._permissions = permissions

    @property
    def policy(self):
        """Gets the policy of this Resource.  # noqa: E501


        :return: The policy of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this Resource.


        :param policy: The policy of this Resource.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def policy_versions(self):
        """Gets the policy_versions of this Resource.  # noqa: E501


        :return: The policy_versions of this Resource.  # noqa: E501
        :rtype: list[PolicyVersion]
        """
        return self._policy_versions

    @policy_versions.setter
    def policy_versions(self, policy_versions):
        """Sets the policy_versions of this Resource.


        :param policy_versions: The policy_versions of this Resource.  # noqa: E501
        :type: list[PolicyVersion]
        """

        self._policy_versions = policy_versions

    @property
    def restricted_to(self):
        """Gets the restricted_to of this Resource.  # noqa: E501


        :return: The restricted_to of this Resource.  # noqa: E501
        :rtype: list[str]
        """
        return self._restricted_to

    @restricted_to.setter
    def restricted_to(self, restricted_to):
        """Sets the restricted_to of this Resource.


        :param restricted_to: The restricted_to of this Resource.  # noqa: E501
        :type: list[str]
        """

        self._restricted_to = restricted_to

    @property
    def secrets(self):
        """Gets the secrets of this Resource.  # noqa: E501


        :return: The secrets of this Resource.  # noqa: E501
        :rtype: list[ResourceSecrets]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this Resource.


        :param secrets: The secrets of this Resource.  # noqa: E501
        :type: list[ResourceSecrets]
        """

        self._secrets = secrets

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
        if not isinstance(other, Resource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Resource):
            return True

        return self.to_dict() != other.to_dict()
