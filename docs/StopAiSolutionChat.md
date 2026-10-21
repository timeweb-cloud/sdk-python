# StopAiSolutionChat

Параметры остановки хода агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **object** | ID разговора. Если не передать, останавливается текущий ход основного разговора решения. Буквы, цифры и дефисы, до 64 символов | [optional] 

## Example

```python
from timeweb_cloud_api.models.stop_ai_solution_chat import StopAiSolutionChat

# TODO update the JSON string below
json = "{}"
# create an instance of StopAiSolutionChat from a JSON string
stop_ai_solution_chat_instance = StopAiSolutionChat.from_json(json)
# print the JSON string representation of the object
print StopAiSolutionChat.to_json()

# convert the object into a dict
stop_ai_solution_chat_dict = stop_ai_solution_chat_instance.to_dict()
# create an instance of StopAiSolutionChat from a dict
stop_ai_solution_chat_form_dict = stop_ai_solution_chat.from_dict(stop_ai_solution_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


