# AiSolutionChatStatus

Готовность чата решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ready** | **object** | Готов ли чат принимать сообщения | 
**reason** | **object** | Почему чат ещё не готов. Отсутствует, если чат готов. &#x60;unreachable&#x60; — до сервера не достучаться (разворачивается, выключен или нет публичного IP); &#x60;software_installing&#x60; — устанавливается ПО агента; &#x60;configuring&#x60; — агент настраивается; &#x60;install_failed&#x60; — установка ПО не удалась, пересоздайте решение; &#x60;machine_error&#x60; — сервер в состоянии ошибки, пересоздайте решение; &#x60;deleted&#x60; — решение удалено; &#x60;outdated&#x60; — сервер создан старой версией решения, пересоздайте решение | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_solution_chat_status import AiSolutionChatStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionChatStatus from a JSON string
ai_solution_chat_status_instance = AiSolutionChatStatus.from_json(json)
# print the JSON string representation of the object
print AiSolutionChatStatus.to_json()

# convert the object into a dict
ai_solution_chat_status_dict = ai_solution_chat_status_instance.to_dict()
# create an instance of AiSolutionChatStatus from a dict
ai_solution_chat_status_form_dict = ai_solution_chat_status.from_dict(ai_solution_chat_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


