# Mssql

This object describes Microsoft SQL Server container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | **bool** | Accept or decline Microsoft SQL Server license. | 
**db** | **str** | Database name to create. | [optional]  if omitted the server will use the default value of "mydb"
**password** | **str** | Superuser password. | [optional]  if omitted the server will use the default value of "Gn0m!ck~"
**queries** | **[str]** | A list of queries to execute while setting up the container.  | [optional] 
**queries_files** | **[str]** | SQL files to execute while setting up container state. | [optional] 
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


