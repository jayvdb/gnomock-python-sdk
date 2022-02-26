# Postgres

This object describes Postgres container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** | Database name to create. By default, &#x60;postgres&#x60; is used. | [optional] 
**user** | **str** | User to create in the container. By default, &#x60;postgres&#x60; is used with password &#x60;password&#x60;.  | [optional] 
**password** | **str** | New user&#39;s password. | [optional] 
**queries** | **[str]** | A list of queries to execute while setting up the container.  | [optional] 
**queries_files** | **[str]** | SQL files to execute while setting up container state. | [optional] 
**timezone** | **str** | The timezone in the container. | [optional] 
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


