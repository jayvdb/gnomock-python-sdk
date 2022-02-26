# Mysql

This object describes MySQL container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** | Database name to create. | [optional]  if omitted the server will use the default value of "mydb"
**user** | **str** | User to create in the container. | [optional]  if omitted the server will use the default value of "gnomock"
**password** | **str** | New user&#39;s password. | [optional]  if omitted the server will use the default value of "gnomick"
**queries** | **[str]** | A list of queries to execute while setting up the container.  | [optional] 
**queries_files** | **[str]** | SQL files to execute while setting up container state. | [optional] 
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


