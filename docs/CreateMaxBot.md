# CreateMaxBot

Параметры подключения бота MAX

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **object** | ID агента, который будет отвечать от имени бота | 
**token** | **object** | Токен бота, выданный @MasterBot в MAX | 
**description** | **object** | Комментарий к боту | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_max_bot import CreateMaxBot

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMaxBot from a JSON string
create_max_bot_instance = CreateMaxBot.from_json(json)
# print the JSON string representation of the object
print CreateMaxBot.to_json()

# convert the object into a dict
create_max_bot_dict = create_max_bot_instance.to_dict()
# create an instance of CreateMaxBot from a dict
create_max_bot_form_dict = create_max_bot.from_dict(create_max_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


