# AiSolutionChatReply

Ответ агента решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **object** | ID разговора. У основного разговора решения — &#x60;solution-&lt;solution_id&gt;&#x60; | 
**reply** | **object** | Ответ агента | 
**model** | **object** | Модель, сгенерировавшая ответ. &#x60;null&#x60;, если агент её не сообщил | 

## Example

```python
from timeweb_cloud_api.models.ai_solution_chat_reply import AiSolutionChatReply

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionChatReply from a JSON string
ai_solution_chat_reply_instance = AiSolutionChatReply.from_json(json)
# print the JSON string representation of the object
print AiSolutionChatReply.to_json()

# convert the object into a dict
ai_solution_chat_reply_dict = ai_solution_chat_reply_instance.to_dict()
# create an instance of AiSolutionChatReply from a dict
ai_solution_chat_reply_form_dict = ai_solution_chat_reply.from_dict(ai_solution_chat_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


