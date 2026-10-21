# AiSolutionConversation

Разговор с агентом решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **object** | ID разговора | 
**started_at** | **object** | Дата и время первого сообщения | 
**last_message_at** | **object** | Дата и время последнего сообщения | 
**messages_count** | **object** | Количество сообщений в разговоре | 

## Example

```python
from timeweb_cloud_api.models.ai_solution_conversation import AiSolutionConversation

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionConversation from a JSON string
ai_solution_conversation_instance = AiSolutionConversation.from_json(json)
# print the JSON string representation of the object
print AiSolutionConversation.to_json()

# convert the object into a dict
ai_solution_conversation_dict = ai_solution_conversation_instance.to_dict()
# create an instance of AiSolutionConversation from a dict
ai_solution_conversation_form_dict = ai_solution_conversation.from_dict(ai_solution_conversation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


