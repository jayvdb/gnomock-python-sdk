# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.4.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gnomock.configuration import Configuration


class Options(object):
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
        'timeout': 'int',
        'env': 'list[str]',
        'debug': 'bool',
        'container_name': 'str'
    }

    attribute_map = {
        'timeout': 'timeout',
        'env': 'env',
        'debug': 'debug',
        'container_name': 'container_name'
    }

    def __init__(self, timeout=None, env=None, debug=False, container_name=None, local_vars_configuration=None):  # noqa: E501
        """Options - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timeout = None
        self._env = None
        self._debug = None
        self._container_name = None
        self.discriminator = None

        if timeout is not None:
            self.timeout = timeout
        if env is not None:
            self.env = env
        if debug is not None:
            self.debug = debug
        if container_name is not None:
            self.container_name = container_name

    @property
    def timeout(self):
        """Gets the timeout of this Options.  # noqa: E501

        Wait timeout in nanoseconds  # noqa: E501

        :return: The timeout of this Options.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this Options.

        Wait timeout in nanoseconds  # noqa: E501

        :param timeout: The timeout of this Options.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def env(self):
        """Gets the env of this Options.  # noqa: E501

        Array of environment variables to set in the container  # noqa: E501

        :return: The env of this Options.  # noqa: E501
        :rtype: list[str]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this Options.

        Array of environment variables to set in the container  # noqa: E501

        :param env: The env of this Options.  # noqa: E501
        :type: list[str]
        """

        self._env = env

    @property
    def debug(self):
        """Gets the debug of this Options.  # noqa: E501

        Set to true to see logs inside the Gnomock container  # noqa: E501

        :return: The debug of this Options.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this Options.

        Set to true to see logs inside the Gnomock container  # noqa: E501

        :param debug: The debug of this Options.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def container_name(self):
        """Gets the container_name of this Options.  # noqa: E501

        Use a specific container name instead of a random one. In case a container with this name already exists, it is killed and replaced by a new container.   # noqa: E501

        :return: The container_name of this Options.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this Options.

        Use a specific container name instead of a random one. In case a container with this name already exists, it is killed and replaced by a new container.   # noqa: E501

        :param container_name: The container_name of this Options.  # noqa: E501
        :type: str
        """

        self._container_name = container_name

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
        if not isinstance(other, Options):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Options):
            return True

        return self.to_dict() != other.to_dict()
