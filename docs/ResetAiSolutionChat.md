# ResetAiSolutionChat

Параметры сброса контекста разговора

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **object** | ID разговора. Если не передать, сбрасывается основной разговор решения. Буквы, цифры и дефисы, до 64 символов | [optional] 

## Example

```python
from timeweb_cloud_api.models.reset_ai_solution_chat import ResetAiSolutionChat

# TODO update the JSON string below
json = "{}"
# create an instance of ResetAiSolutionChat from a JSON string
reset_ai_solution_chat_instance = ResetAiSolutionChat.from_json(json)
# print the JSON string representation of the object
print ResetAiSolutionChat.to_json()

# convert the object into a dict
reset_ai_solution_chat_dict = reset_ai_solution_chat_instance.to_dict()
# create an instance of ResetAiSolutionChat from a dict
reset_ai_solution_chat_form_dict = reset_ai_solution_chat.from_dict(reset_ai_solution_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


