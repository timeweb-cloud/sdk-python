# AiGatewayResponseCreateRequest

Запрос Responses API в формате OpenAI. Остальные параметры OpenAI передаются модели как есть

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **object** | ID модели из &#x60;GET /v1/models&#x60; | 
**input** | **object** | Текст или массив входных элементов (сообщения, результаты вызова функций и т. п.) | 
**instructions** | **object** | Системные инструкции | [optional] 
**previous_response_id** | **object** | ID сохранённого ответа, чтобы продолжить диалог | [optional] 
**stream** | **object** | Отправлять ответ потоком типизированных событий Server-Sent Events | [optional] 
**background** | **object** | Выполнить запрос в фоне: результат получайте через &#x60;GET /v1/responses/{response_id}&#x60; | [optional] 
**store** | **object** | Сохранить ответ, чтобы получить его позже или продолжить диалог | [optional] 
**max_output_tokens** | **object** | Максимум выходных токенов | [optional] 
**tools** | **object** | Инструменты, которые может вызвать модель | [optional] 
**reasoning** | [**AiGatewayResponseCreateRequestReasoning**](AiGatewayResponseCreateRequestReasoning.md) |  | [optional] 
**text** | **Dict[str, object]** | Настройки формата текста ответа | [optional] 
**temperature** | **object** | Температура выборки | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_response_create_request import AiGatewayResponseCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayResponseCreateRequest from a JSON string
ai_gateway_response_create_request_instance = AiGatewayResponseCreateRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewayResponseCreateRequest.to_json()

# convert the object into a dict
ai_gateway_response_create_request_dict = ai_gateway_response_create_request_instance.to_dict()
# create an instance of AiGatewayResponseCreateRequest from a dict
ai_gateway_response_create_request_form_dict = ai_gateway_response_create_request.from_dict(ai_gateway_response_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


