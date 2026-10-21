# AiGatewayResponse

Ответ Responses API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ответа. Передавайте его как есть в остальные запросы &#x60;/v1/responses&#x60; | [optional] 
**object** | **object** | Тип объекта | [optional] 
**created_at** | **object** | Время создания, Unix-время в секундах | [optional] 
**status** | **object** | Статус ответа: &#x60;queued&#x60;, &#x60;in_progress&#x60;, &#x60;completed&#x60;, &#x60;incomplete&#x60; (достигнут лимит выходных токенов), &#x60;failed&#x60;, &#x60;cancelling&#x60; (отмена выполняется), &#x60;cancelled&#x60; | [optional] 
**model** | **object** | Модель, которая ответила | [optional] 
**output** | **object** | Выходные элементы: сообщения, вызовы функций, рассуждения | [optional] 
**incomplete_details** | [**AiGatewayResponseIncompleteDetails**](AiGatewayResponseIncompleteDetails.md) |  | [optional] 
**usage** | [**AiGatewayResponseUsage**](AiGatewayResponseUsage.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_response import AiGatewayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayResponse from a JSON string
ai_gateway_response_instance = AiGatewayResponse.from_json(json)
# print the JSON string representation of the object
print AiGatewayResponse.to_json()

# convert the object into a dict
ai_gateway_response_dict = ai_gateway_response_instance.to_dict()
# create an instance of AiGatewayResponse from a dict
ai_gateway_response_form_dict = ai_gateway_response.from_dict(ai_gateway_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


