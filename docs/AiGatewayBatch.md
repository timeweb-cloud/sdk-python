# AiGatewayBatch

Батч

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID батча | [optional] 
**object** | **object** | Тип объекта | [optional] 
**endpoint** | **object** | Эндпоинт запросов батча | [optional] 
**model** | **object** | Модель батча. На этапе &#x60;validating&#x60; может быть &#x60;null&#x60; | [optional] 
**input_file_id** | **object** | ID входного файла | [optional] 
**output_file_id** | **object** | ID файла результатов — когда батч выполнен | [optional] 
**error_file_id** | **object** | ID файла с ошибками отдельных запросов, если они были | [optional] 
**completion_window** | **object** | Срок выполнения | [optional] 
**status** | **object** | Статус батча. &#x60;cancelling&#x60; — отмена выполняется, может занять несколько минут | [optional] 
**created_at** | **object** | Время создания, Unix-время в секундах | [optional] 
**completed_at** | **object** | Время завершения, Unix-время в секундах | [optional] 
**expires_at** | **object** | Крайний срок выполнения, Unix-время в секундах | [optional] 
**request_counts** | [**AiGatewayBatchRequestCounts**](AiGatewayBatchRequestCounts.md) |  | [optional] 
**metadata** | **Dict[str, object]** | Метки батча из запроса | [optional] 
**usage** | **Dict[str, object]** | Расход токенов батча | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_batch import AiGatewayBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayBatch from a JSON string
ai_gateway_batch_instance = AiGatewayBatch.from_json(json)
# print the JSON string representation of the object
print AiGatewayBatch.to_json()

# convert the object into a dict
ai_gateway_batch_dict = ai_gateway_batch_instance.to_dict()
# create an instance of AiGatewayBatch from a dict
ai_gateway_batch_form_dict = ai_gateway_batch.from_dict(ai_gateway_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


