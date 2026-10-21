# SendAiSolutionMessage

Сообщение агенту решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** | Текст сообщения, до 32 000 символов. Если не передать, агент сам отправит приветствие — так можно получить первую реплику чата | [optional] 
**conversation_id** | **object** | ID разговора. Если не передать, сообщение уйдёт в основной разговор решения (&#x60;solution-&lt;solution_id&gt;&#x60;). Чтобы начать отдельный разговор, передайте новый ID. Буквы, цифры и дефисы, до 64 символов | [optional] 

## Example

```python
from timeweb_cloud_api.models.send_ai_solution_message import SendAiSolutionMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SendAiSolutionMessage from a JSON string
send_ai_solution_message_instance = SendAiSolutionMessage.from_json(json)
# print the JSON string representation of the object
print SendAiSolutionMessage.to_json()

# convert the object into a dict
send_ai_solution_message_dict = send_ai_solution_message_instance.to_dict()
# create an instance of SendAiSolutionMessage from a dict
send_ai_solution_message_form_dict = send_ai_solution_message.from_dict(send_ai_solution_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


