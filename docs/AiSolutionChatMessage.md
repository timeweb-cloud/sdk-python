# AiSolutionChatMessage

Сообщение из истории чата решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **object** | ID сообщения | 
**conversation_id** | **object** | ID разговора | 
**role** | **object** | Автор сообщения: &#x60;user&#x60;, &#x60;assistant&#x60; или &#x60;context-reset&#x60; — служебная отметка с пустым &#x60;content&#x60;, обозначающая место сброса контекста разговора | 
**content** | **object** | Текст сообщения | 
**created_at** | **object** | Дата и время сообщения | 

## Example

```python
from timeweb_cloud_api.models.ai_solution_chat_message import AiSolutionChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionChatMessage from a JSON string
ai_solution_chat_message_instance = AiSolutionChatMessage.from_json(json)
# print the JSON string representation of the object
print AiSolutionChatMessage.to_json()

# convert the object into a dict
ai_solution_chat_message_dict = ai_solution_chat_message_instance.to_dict()
# create an instance of AiSolutionChatMessage from a dict
ai_solution_chat_message_form_dict = ai_solution_chat_message.from_dict(ai_solution_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


