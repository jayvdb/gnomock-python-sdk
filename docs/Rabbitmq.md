# Rabbitmq

This object describes a RabbitMQ container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | Set a user name | [optional]  if omitted the server will use the default value of "guest"
**password** | **str** | Set a password for a created user | [optional]  if omitted the server will use the default value of "guest"
**version** | **str** | RabbitMQ version. | [optional]  if omitted the server will use the default value of "3.8.5-alpine"
**messages** | [**[RabbitmqMessage]**](RabbitmqMessage.md) | A list of messages to send to RabbitMQ | [optional] 
**messages_files** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


