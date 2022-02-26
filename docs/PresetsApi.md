# gnomock.PresetsApi

All URIs are relative to *http://127.0.0.1:23042*

Method | HTTP request | Description
------------- | ------------- | -------------
[**start_cassandra**](PresetsApi.md#start_cassandra) | **POST** /start/cassandra | Start a new Gnomock Cassandra preset.
[**start_cockroach_db**](PresetsApi.md#start_cockroach_db) | **POST** /start/cockroachdb | Start a new Gnomock CockroachDB preset.
[**start_elastic**](PresetsApi.md#start_elastic) | **POST** /start/elastic | Start a new Gnomock Elasticsearch container
[**start_influx_db**](PresetsApi.md#start_influx_db) | **POST** /start/influxdb | Start a new Gnomock InfluxDB preset.
[**start_kafka**](PresetsApi.md#start_kafka) | **POST** /start/kafka | Start a new Gnomock Kafka container
[**start_kubernetes**](PresetsApi.md#start_kubernetes) | **POST** /start/kubernetes | Start a new Gnomock lightweight kubernetes (k3s) preset. Use &#x60;host:&lt;kubeconfig-port&gt;/kubeconfig&#x60; to retrieve the kubeconfig file that should be used to connect to this container. 
[**start_localstack**](PresetsApi.md#start_localstack) | **POST** /start/localstack | Start a new Gnomock Localstack container
[**start_mariadb**](PresetsApi.md#start_mariadb) | **POST** /start/mariadb | Start a new Gnomock MariaDB container
[**start_memcached**](PresetsApi.md#start_memcached) | **POST** /start/memcached | Start a new Gnomock Memcached container
[**start_mongo**](PresetsApi.md#start_mongo) | **POST** /start/mongo | Start a new Gnomock MongoDB container
[**start_mssql**](PresetsApi.md#start_mssql) | **POST** /start/mssql | Start a new Gnomock Microsoft SQL Server container
[**start_mysql**](PresetsApi.md#start_mysql) | **POST** /start/mysql | Start a new Gnomock MySQL container
[**start_postgres**](PresetsApi.md#start_postgres) | **POST** /start/postgres | Start a new Gnomock Postgres container
[**start_rabbit_mq**](PresetsApi.md#start_rabbit_mq) | **POST** /start/rabbitmq | Start a new Gnomock RabbitMQ container
[**start_redis**](PresetsApi.md#start_redis) | **POST** /start/redis | Start a new Gnomock Redis container
[**start_splunk**](PresetsApi.md#start_splunk) | **POST** /start/splunk | Start a new Gnomock Splunk container
[**stop**](PresetsApi.md#stop) | **POST** /stop | Stop an existing Gnomock container


# **start_cassandra**
> Container start_cassandra(cassandra_request)

Start a new Gnomock Cassandra preset.

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.cassandra_request import CassandraRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    cassandra_request = CassandraRequest(
        preset=Cassandra(
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # CassandraRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Cassandra preset.
        api_response = api_instance.start_cassandra(cassandra_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_cassandra: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cassandra_request** | [**CassandraRequest**](CassandraRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_cockroach_db**
> Container start_cockroach_db(cockroachdb_request)

Start a new Gnomock CockroachDB preset.

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.cockroachdb_request import CockroachdbRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    cockroachdb_request = CockroachdbRequest(
        preset=Cockroachdb(
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # CockroachdbRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock CockroachDB preset.
        api_response = api_instance.start_cockroach_db(cockroachdb_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_cockroach_db: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cockroachdb_request** | [**CockroachdbRequest**](CockroachdbRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_elastic**
> Container start_elastic(elastic_request)

Start a new Gnomock Elasticsearch container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.elastic_request import ElasticRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    elastic_request = ElasticRequest(
        preset=Elastic(
            input_files=[
                "input_files_example",
            ],
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # ElasticRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Elasticsearch container
        api_response = api_instance.start_elastic(elastic_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_elastic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **elastic_request** | [**ElasticRequest**](ElasticRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_influx_db**
> Container start_influx_db(influxdb_request)

Start a new Gnomock InfluxDB preset.

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.influxdb_request import InfluxdbRequest
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    influxdb_request = InfluxdbRequest(
        preset=Influxdb(
            version="latest",
            username="gnomock",
            password="gnomock-password",
            org="gnomock-org",
            bucket="gnomock-bucket",
            auth_token="gnomock-influxdb-token",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # InfluxdbRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock InfluxDB preset.
        api_response = api_instance.start_influx_db(influxdb_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_influx_db: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **influxdb_request** | [**InfluxdbRequest**](InfluxdbRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_kafka**
> Container start_kafka(kafka_request)

Start a new Gnomock Kafka container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.kafka_request import KafkaRequest
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    kafka_request = KafkaRequest(
        preset=Kafka(
            messages=[
                KafkaMessages(
                    topic="alerts",
                    key="cpu",
                    value="high",
                    time=1588269752,
                ),
            ],
            messages_files=[
                "messages_files_example",
            ],
            topics=["alerts","events"],
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # KafkaRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Kafka container
        api_response = api_instance.start_kafka(kafka_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_kafka: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kafka_request** | [**KafkaRequest**](KafkaRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_kubernetes**
> Container start_kubernetes(kubernetes_request)

Start a new Gnomock lightweight kubernetes (k3s) preset. Use `host:<kubeconfig-port>/kubeconfig` to retrieve the kubeconfig file that should be used to connect to this container. 

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.kubernetes_request import KubernetesRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    kubernetes_request = KubernetesRequest(
        preset=Kubernetes(
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # KubernetesRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock lightweight kubernetes (k3s) preset. Use `host:<kubeconfig-port>/kubeconfig` to retrieve the kubeconfig file that should be used to connect to this container. 
        api_response = api_instance.start_kubernetes(kubernetes_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_kubernetes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_request** | [**KubernetesRequest**](KubernetesRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_localstack**
> Container start_localstack(localstack_request)

Start a new Gnomock Localstack container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.localstack_request import LocalstackRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    localstack_request = LocalstackRequest(
        preset=Localstack(
            services=["s3","ses"],
            s3_path="/home/gnomock/project/testdata/s3",
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # LocalstackRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Localstack container
        api_response = api_instance.start_localstack(localstack_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_localstack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **localstack_request** | [**LocalstackRequest**](LocalstackRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_mariadb**
> Container start_mariadb(mariadb_request)

Start a new Gnomock MariaDB container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.mariadb_request import MariadbRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    mariadb_request = MariadbRequest(
        preset=Mariadb(
            db="mydb",
            user="gnomock",
            password="p@s$w0rD",
            queries=["create table foo(bar int)","insert into foo(bar) values(1)"],
            queries_files=["/home/gnomock/project/testdata/mysql/queries.sql"],
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # MariadbRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock MariaDB container
        api_response = api_instance.start_mariadb(mariadb_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_mariadb: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mariadb_request** | [**MariadbRequest**](MariadbRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_memcached**
> Container start_memcached(memcached_request)

Start a new Gnomock Memcached container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.memcached_request import MemcachedRequest
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    memcached_request = MemcachedRequest(
        preset=Memcached(
            values={},
            byte_values={},
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # MemcachedRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Memcached container
        api_response = api_instance.start_memcached(memcached_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_memcached: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **memcached_request** | [**MemcachedRequest**](MemcachedRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_mongo**
> Container start_mongo(mongo_request)

Start a new Gnomock MongoDB container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.mongo_request import MongoRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    mongo_request = MongoRequest(
        preset=Mongo(
            data_path="/home/gnomock/project/testdata/mongo/data",
            user="gnomock",
            password="p@s$w0rD",
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # MongoRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock MongoDB container
        api_response = api_instance.start_mongo(mongo_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_mongo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mongo_request** | [**MongoRequest**](MongoRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_mssql**
> Container start_mssql(mssql_request)

Start a new Gnomock Microsoft SQL Server container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.mssql_request import MssqlRequest
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    mssql_request = MssqlRequest(
        preset=Mssql(
            db="mydb",
            password="p@s$w0rD",
            queries=["create table foo(bar int)","insert into foo(bar) values(1)"],
            queries_files=["/home/gnomock/project/testdata/mssql/queries.sql"],
            license=True,
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # MssqlRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Microsoft SQL Server container
        api_response = api_instance.start_mssql(mssql_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_mssql: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mssql_request** | [**MssqlRequest**](MssqlRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_mysql**
> Container start_mysql(mysql_request)

Start a new Gnomock MySQL container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.mysql_request import MysqlRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    mysql_request = MysqlRequest(
        preset=Mysql(
            db="mydb",
            user="gnomock",
            password="p@s$w0rD",
            queries=["create table foo(bar int)","insert into foo(bar) values(1)"],
            queries_files=["/home/gnomock/project/testdata/mysql/queries.sql"],
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # MysqlRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock MySQL container
        api_response = api_instance.start_mysql(mysql_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_mysql: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mysql_request** | [**MysqlRequest**](MysqlRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_postgres**
> Container start_postgres(postgres_request)

Start a new Gnomock Postgres container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.postgres_request import PostgresRequest
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    postgres_request = PostgresRequest(
        preset=Postgres(
            db="mydb",
            user="gnomock",
            password="p@s$w0rD",
            queries=["create table foo(bar int)","insert into foo(bar) values(1)"],
            queries_files=["/home/gnomock/project/testdata/postgres/queries.sql"],
            timezone="Europe/Paris",
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # PostgresRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Postgres container
        api_response = api_instance.start_postgres(postgres_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_postgres: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postgres_request** | [**PostgresRequest**](PostgresRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_rabbit_mq**
> Container start_rabbit_mq(rabbitmq_request)

Start a new Gnomock RabbitMQ container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.rabbitmq_request import RabbitmqRequest
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    rabbitmq_request = RabbitmqRequest(
        preset=Rabbitmq(
            user="gnomock",
            password="p@s$w0rD",
            version="latest",
            messages=[
                RabbitmqMessage(
                    queue="alerts",
                    content_type="text/plain",
                    string_body="high cpu",
                    body='YQ==',
                ),
            ],
            messages_files=[
                "messages_files_example",
            ],
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # RabbitmqRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock RabbitMQ container
        api_response = api_instance.start_rabbit_mq(rabbitmq_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_rabbit_mq: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rabbitmq_request** | [**RabbitmqRequest**](RabbitmqRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_redis**
> Container start_redis(redis_request)

Start a new Gnomock Redis container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.container import Container
from gnomock.model.redis_request import RedisRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    redis_request = RedisRequest(
        preset=Redis(
            values={},
            version="latest",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # RedisRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Redis container
        api_response = api_instance.start_redis(redis_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_redis: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redis_request** | [**RedisRequest**](RedisRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_splunk**
> Container start_splunk(splunk_request)

Start a new Gnomock Splunk container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.start_failed import StartFailed
from gnomock.model.invalid_start_request import InvalidStartRequest
from gnomock.model.splunk_request import SplunkRequest
from gnomock.model.container import Container
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    splunk_request = SplunkRequest(
        preset=Splunk(
            values=[
                SplunkValues(
                    event="something happened",
                    index="main",
                    source="web",
                    sourcetype="http",
                    time=1588269752,
                ),
            ],
            values_file="/home/gnomock/project/testdata/splunk/events.jsonl",
            accept_license=True,
            admin_password="p@s$w0rD",
            version="8.0.2.1",
        ),
        options=Options(
            timeout=60000000000,
            env=[
                "ENV_VAR_NAME=some-value",
            ],
            debug=False,
            container_name="gnomock",
            privileged=True,
            cmd=[
                "cmd_example",
            ],
            disable_cleanup=True,
            use_local_images_first=True,
            custom_named_ports=NamedPorts(
                key={
                    protocol="tcp",
                    port=35973,
                },
            ),
            auth="eyJ1c2VybmFtZSI6ImZvbyIsInBhc3N3b3JkIjoiYmFyIn0K",
        ),
    ) # SplunkRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Start a new Gnomock Splunk container
        api_response = api_instance.start_splunk(splunk_request)
        pprint(api_response)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->start_splunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **splunk_request** | [**SplunkRequest**](SplunkRequest.md)|  |

### Return type

[**Container**](Container.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container created successfully |  -  |
**400** | Invalid container configuration |  -  |
**500** | Start failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop**
> stop(stop_request)

Stop an existing Gnomock container

### Example


```python
import time
import gnomock
from gnomock.api import presets_api
from gnomock.model.stop_failed import StopFailed
from gnomock.model.invalid_stop_request import InvalidStopRequest
from gnomock.model.stop_request import StopRequest
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:23042
# See configuration.py for a list of all supported configuration parameters.
configuration = gnomock.Configuration(
    host = "http://127.0.0.1:23042"
)


# Enter a context with an instance of the API client
with gnomock.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = presets_api.PresetsApi(api_client)
    stop_request = StopRequest(
        id="f5d08dc84421",
    ) # StopRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Stop an existing Gnomock container
        api_instance.stop(stop_request)
    except gnomock.ApiException as e:
        print("Exception when calling PresetsApi->stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stop_request** | [**StopRequest**](StopRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Container stopped successfully |  -  |
**400** | Invalid stop request |  -  |
**500** | Stop failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

