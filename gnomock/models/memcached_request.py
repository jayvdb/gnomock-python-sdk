# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class MemcachedRequest(object):
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
        'preset': 'Memcached',
        'options': 'Options'
    }

    attribute_map = {
        'preset': 'preset',
        'options': 'options'
    }

    def __init__(self, preset=None, options=None, local_vars_configuration=None):  # noqa: E501
        """MemcachedRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._preset = None
        self._options = None
        self.discriminator = None

        if preset is not None:
            self.preset = preset
        if options is not None:
            self.options = options

    @property
    def preset(self):
        """Gets the preset of this MemcachedRequest.  # noqa: E501


        :return: The preset of this MemcachedRequest.  # noqa: E501
        :rtype: Memcached
        """
        return self._preset

    @preset.setter
    def preset(self, preset):
        """Sets the preset of this MemcachedRequest.


        :param preset: The preset of this MemcachedRequest.  # noqa: E501
        :type: Memcached
        """

        self._preset = preset

    @property
    def options(self):
        """Gets the options of this MemcachedRequest.  # noqa: E501


        :return: The options of this MemcachedRequest.  # noqa: E501
        :rtype: Options
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MemcachedRequest.


        :param options: The options of this MemcachedRequest.  # noqa: E501
        :type: Options
        """

        self._options = options

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
        if not isinstance(other, MemcachedRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MemcachedRequest):
            return True

        return self.to_dict() != other.to_dict()
