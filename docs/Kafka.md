# Kafka

This object describes a Kafka container. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**[KafkaMessages]**](KafkaMessages.md) | A list of messages to send to Kafka. | [optional] 
**messages_files** | **[str]** |  | [optional] 
**topics** | **[str]** | Topic names to create in Kafka. | [optional] 
**version** | **str** | Kafka version. | [optional]  if omitted the server will use the default value of "2.5.1-L0"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


