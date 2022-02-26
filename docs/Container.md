# Container

This object is a Gnomock wrapper of a regular docker container. It uses the same container ID as docker, and adds bound ports information. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Container ID | [optional] 
**host** | **str** | Host of bound ports | [optional]  if omitted the server will use the default value of "localhost"
**ports** | [**NamedPorts**](NamedPorts.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


