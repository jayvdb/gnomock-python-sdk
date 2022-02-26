# Localstack

This object describes Localstack container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | **[str]** | A list of localstack services to start | 
**s3_path** | **str** | Path to folder to setup initial S3 state. Top level folders are used as buckets; all child folders and files are uploaded as-is  | [optional] 
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


