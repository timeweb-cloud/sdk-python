# AiGatewayChatMessage

Сообщение диалога

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **object** | Роль автора сообщения | 
**content** | **object** | Текст сообщения или массив частей (&#x60;text&#x60;, &#x60;image_url&#x60;, &#x60;input_audio&#x60;, &#x60;file&#x60;) для моделей, которые их принимают | [optional] 
**name** | **object** | Имя автора сообщения | [optional] 
**tool_calls** | **object** | Вызовы функций (в сообщениях &#x60;assistant&#x60;) | [optional] 
**tool_call_id** | **object** | ID вызова функции, на который отвечает сообщение (в сообщениях &#x60;tool&#x60;) | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_chat_message import AiGatewayChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayChatMessage from a JSON string
ai_gateway_chat_message_instance = AiGatewayChatMessage.from_json(json)
# print the JSON string representation of the object
print AiGatewayChatMessage.to_json()

# convert the object into a dict
ai_gateway_chat_message_dict = ai_gateway_chat_message_instance.to_dict()
# create an instance of AiGatewayChatMessage from a dict
ai_gateway_chat_message_form_dict = ai_gateway_chat_message.from_dict(ai_gateway_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


