# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class KafkaMessages(object):
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
        'topic': 'str',
        'key': 'str',
        'value': 'str',
        'time': 'float'
    }

    attribute_map = {
        'topic': 'topic',
        'key': 'key',
        'value': 'value',
        'time': 'time'
    }

    def __init__(self, topic=None, key=None, value=None, time=None, local_vars_configuration=None):  # noqa: E501
        """KafkaMessages - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._topic = None
        self._key = None
        self._value = None
        self._time = None
        self.discriminator = None

        self.topic = topic
        self.key = key
        self.value = value
        if time is not None:
            self.time = time

    @property
    def topic(self):
        """Gets the topic of this KafkaMessages.  # noqa: E501


        :return: The topic of this KafkaMessages.  # noqa: E501
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this KafkaMessages.


        :param topic: The topic of this KafkaMessages.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and topic is None:  # noqa: E501
            raise ValueError("Invalid value for `topic`, must not be `None`")  # noqa: E501

        self._topic = topic

    @property
    def key(self):
        """Gets the key of this KafkaMessages.  # noqa: E501


        :return: The key of this KafkaMessages.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this KafkaMessages.


        :param key: The key of this KafkaMessages.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this KafkaMessages.  # noqa: E501


        :return: The value of this KafkaMessages.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this KafkaMessages.


        :param value: The value of this KafkaMessages.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def time(self):
        """Gets the time of this KafkaMessages.  # noqa: E501

        timestamp in seconds  # noqa: E501

        :return: The time of this KafkaMessages.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this KafkaMessages.

        timestamp in seconds  # noqa: E501

        :param time: The time of this KafkaMessages.  # noqa: E501
        :type: float
        """

        self._time = time

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
        if not isinstance(other, KafkaMessages):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KafkaMessages):
            return True

        return self.to_dict() != other.to_dict()
