# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Postgres(object):
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
        'db': 'str',
        'user': 'str',
        'password': 'str',
        'queries': 'list[str]',
        'queries_files': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'db': 'db',
        'user': 'user',
        'password': 'password',
        'queries': 'queries',
        'queries_files': 'queries_files',
        'version': 'version'
    }

    def __init__(self, db=None, user=None, password=None, queries=None, queries_files=None, version='latest', local_vars_configuration=None):  # noqa: E501
        """Postgres - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._db = None
        self._user = None
        self._password = None
        self._queries = None
        self._queries_files = None
        self._version = None
        self.discriminator = None

        if db is not None:
            self.db = db
        if user is not None:
            self.user = user
        if password is not None:
            self.password = password
        if queries is not None:
            self.queries = queries
        if queries_files is not None:
            self.queries_files = queries_files
        if version is not None:
            self.version = version

    @property
    def db(self):
        """Gets the db of this Postgres.  # noqa: E501

        Database name to create. By default, `postgres` is used.  # noqa: E501

        :return: The db of this Postgres.  # noqa: E501
        :rtype: str
        """
        return self._db

    @db.setter
    def db(self, db):
        """Sets the db of this Postgres.

        Database name to create. By default, `postgres` is used.  # noqa: E501

        :param db: The db of this Postgres.  # noqa: E501
        :type: str
        """

        self._db = db

    @property
    def user(self):
        """Gets the user of this Postgres.  # noqa: E501

        User to create in the container. By default, `postgres` is used with password `password`.   # noqa: E501

        :return: The user of this Postgres.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Postgres.

        User to create in the container. By default, `postgres` is used with password `password`.   # noqa: E501

        :param user: The user of this Postgres.  # noqa: E501
        :type: str
        """

        self._user = user

    @property
    def password(self):
        """Gets the password of this Postgres.  # noqa: E501

        New user's password.  # noqa: E501

        :return: The password of this Postgres.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Postgres.

        New user's password.  # noqa: E501

        :param password: The password of this Postgres.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def queries(self):
        """Gets the queries of this Postgres.  # noqa: E501

        A list of queries to execute while setting up the container.   # noqa: E501

        :return: The queries of this Postgres.  # noqa: E501
        :rtype: list[str]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this Postgres.

        A list of queries to execute while setting up the container.   # noqa: E501

        :param queries: The queries of this Postgres.  # noqa: E501
        :type: list[str]
        """

        self._queries = queries

    @property
    def queries_files(self):
        """Gets the queries_files of this Postgres.  # noqa: E501

        SQL files to execute while setting up container state.  # noqa: E501

        :return: The queries_files of this Postgres.  # noqa: E501
        :rtype: list[str]
        """
        return self._queries_files

    @queries_files.setter
    def queries_files(self, queries_files):
        """Sets the queries_files of this Postgres.

        SQL files to execute while setting up container state.  # noqa: E501

        :param queries_files: The queries_files of this Postgres.  # noqa: E501
        :type: list[str]
        """

        self._queries_files = queries_files

    @property
    def version(self):
        """Gets the version of this Postgres.  # noqa: E501

        Docker image tag (version)  # noqa: E501

        :return: The version of this Postgres.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Postgres.

        Docker image tag (version)  # noqa: E501

        :param version: The version of this Postgres.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, Postgres):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Postgres):
            return True

        return self.to_dict() != other.to_dict()
