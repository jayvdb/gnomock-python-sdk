# Elastic

This object describes a Elasticsearch container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_files** | **[str]** | A list of files to ingest into Elasticsearch. File names are used as index names. Contents of the files need to be JSON objects placed one after the other.  | [optional] 
**version** | **str** | Elasticsearch version. | [optional]  if omitted the server will use the default value of "7.9.2"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


