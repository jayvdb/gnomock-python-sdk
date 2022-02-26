# Influxdb

This object describes InfluxDB container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Docker image tag (version) | [optional]  if omitted the server will use the default value of "latest"
**username** | **str** | Super-user name | [optional]  if omitted the server will use the default value of "gnomock"
**password** | **str** | Super-user password | [optional]  if omitted the server will use the default value of "gnomock-password"
**org** | **str** | Organization name | [optional]  if omitted the server will use the default value of "gnomock-org"
**bucket** | **str** | Default bucket name | [optional]  if omitted the server will use the default value of "gnomock-bucket"
**auth_token** | **str** | Database authentication token | [optional]  if omitted the server will use the default value of "gnomock-influxdb-token"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


