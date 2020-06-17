# coding: utf-8

"""
    gnomock

    `gnomock` is an HTTP wrapper for [Gnomock](https://github.com/orlangure/gnomock) integration and end-to-end testing toolkit. It allows to use Gnomock outside of Go ecosystem. Not all Gnomock features exist in this wrapper, but official presets, as well as basic general configuration, are supported.   # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import gnomock
from gnomock.models.mssql_request import MssqlRequest  # noqa: E501
from gnomock.rest import ApiException

class TestMssqlRequest(unittest.TestCase):
    """MssqlRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MssqlRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = gnomock.models.mssql_request.MssqlRequest()  # noqa: E501
        if include_optional :
            return MssqlRequest(
                preset = gnomock.models.mssql.Mssql(
                    db = 'mydb', 
                    password = 'Gn0m!ck~', 
                    queries = ["create table foo(bar int)","insert into foo(bar) values(1)"], 
                    queries_files = ['/home/gnomock/project/testdata/mssql/queries'], 
                    license = True, 
                    version = 'latest', ), 
                options = gnomock.models.options.Options(
                    timeout = 60000000000, 
                    env = [
                        'ENV_VAR_NAME=some-value'
                        ], )
            )
        else :
            return MssqlRequest(
        )

    def testMssqlRequest(self):
        """Test MssqlRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
