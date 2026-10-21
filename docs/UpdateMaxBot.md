# UpdateMaxBot

Изменяемые параметры бота MAX. Передайте только те поля, которые нужно изменить

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **object** | Новый токен того же бота. Токен другого бота не принимается | [optional] 
**description** | **object** | Комментарий к боту | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_max_bot import UpdateMaxBot

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMaxBot from a JSON string
update_max_bot_instance = UpdateMaxBot.from_json(json)
# print the JSON string representation of the object
print UpdateMaxBot.to_json()

# convert the object into a dict
update_max_bot_dict = update_max_bot_instance.to_dict()
# create an instance of UpdateMaxBot from a dict
update_max_bot_form_dict = update_max_bot.from_dict(update_max_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


