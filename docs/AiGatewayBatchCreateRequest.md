# AiGatewayBatchCreateRequest

Запрос создания батча

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_id** | **object** | ID файла, загруженного с &#x60;purpose&#x3D;batch&#x60; | 
**endpoint** | **object** | Эндпоинт запросов батча — должен совпадать с &#x60;url&#x60; каждой строки входного файла | 
**completion_window** | **object** | Срок выполнения | 
**metadata** | **Dict[str, object]** | Ваши метки батча: пары «строка — строка» | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_batch_create_request import AiGatewayBatchCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayBatchCreateRequest from a JSON string
ai_gateway_batch_create_request_instance = AiGatewayBatchCreateRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewayBatchCreateRequest.to_json()

# convert the object into a dict
ai_gateway_batch_create_request_dict = ai_gateway_batch_create_request_instance.to_dict()
# create an instance of AiGatewayBatchCreateRequest from a dict
ai_gateway_batch_create_request_form_dict = ai_gateway_batch_create_request.from_dict(ai_gateway_batch_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


