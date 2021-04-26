# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.5.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Elastic(object):
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
        'input_files': 'list[str]',
        'version': 'str'
    }

    attribute_map = {
        'input_files': 'input_files',
        'version': 'version'
    }

    def __init__(self, input_files=None, version='7.9.2', local_vars_configuration=None):  # noqa: E501
        """Elastic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._input_files = None
        self._version = None
        self.discriminator = None

        if input_files is not None:
            self.input_files = input_files
        if version is not None:
            self.version = version

    @property
    def input_files(self):
        """Gets the input_files of this Elastic.  # noqa: E501

        A list of files to ingest into Elasticsearch. File names are used as index names. Contents of the files need to be JSON objects placed one after the other.   # noqa: E501

        :return: The input_files of this Elastic.  # noqa: E501
        :rtype: list[str]
        """
        return self._input_files

    @input_files.setter
    def input_files(self, input_files):
        """Sets the input_files of this Elastic.

        A list of files to ingest into Elasticsearch. File names are used as index names. Contents of the files need to be JSON objects placed one after the other.   # noqa: E501

        :param input_files: The input_files of this Elastic.  # noqa: E501
        :type: list[str]
        """

        self._input_files = input_files

    @property
    def version(self):
        """Gets the version of this Elastic.  # noqa: E501

        Elasticsearch version.  # noqa: E501

        :return: The version of this Elastic.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Elastic.

        Elasticsearch version.  # noqa: E501

        :param version: The version of this Elastic.  # noqa: E501
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
        if not isinstance(other, Elastic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Elastic):
            return True

        return self.to_dict() != other.to_dict()
