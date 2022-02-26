# Memcached

This object describes Memcached container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A list of key/value pairs to create in the container. | [optional] 
**byte_values** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | A list of key/value pairs to create in the container. Values are base64 strings. | [optional] 
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


