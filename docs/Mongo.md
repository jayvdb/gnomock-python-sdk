# Mongo

This object describes MongoDB container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_path** | **str** | Path to folder to setup initial container state. Each top level folder maps to a database, every separate file under it is a collection, and every line is a document in that collection.  | [optional] 
**user** | **str** | Username to create inside the container. | [optional] 
**password** | **str** | Password to set for the created user. | [optional] 
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


