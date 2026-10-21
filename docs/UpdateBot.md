# UpdateBot

Изменяемые параметры Telegram-бота. Передайте только те поля, которые нужно изменить

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **object** | Новый токен того же бота (например, после перевыпуска в @BotFather). Токен другого бота не принимается | [optional] 
**description** | **object** | Комментарий к боту | [optional] 
**whitelist_enabled** | **object** | Ограничить доступ к боту списком &#x60;whitelist_usernames&#x60; | [optional] 
**whitelist_usernames** | **object** | Username пользователей Telegram, которым разрешено писать боту. Можно с &#x60;@&#x60; и в любом регистре — они будут приведены к нижнему регистру без &#x60;@&#x60;, дубли удаляются. Действует, только если &#x60;whitelist_enabled&#x60; равен &#x60;true&#x60; и список не пуст. Переданный список полностью заменяет текущий | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_bot import UpdateBot

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBot from a JSON string
update_bot_instance = UpdateBot.from_json(json)
# print the JSON string representation of the object
print UpdateBot.to_json()

# convert the object into a dict
update_bot_dict = update_bot_instance.to_dict()
# create an instance of UpdateBot from a dict
update_bot_form_dict = update_bot.from_dict(update_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


