# CreateBot

Параметры подключения Telegram-бота

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **object** | ID агента, который будет отвечать от имени бота | 
**token** | **object** | Токен бота, выданный @BotFather | 
**description** | **object** | Комментарий к боту | [optional] 
**whitelist_enabled** | **object** | Ограничить доступ к боту списком &#x60;whitelist_usernames&#x60; | [optional] 
**whitelist_usernames** | **object** | Username пользователей Telegram, которым разрешено писать боту. Можно с &#x60;@&#x60; и в любом регистре — они будут приведены к нижнему регистру без &#x60;@&#x60;, дубли удаляются. Действует, только если &#x60;whitelist_enabled&#x60; равен &#x60;true&#x60; и список не пуст | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_bot import CreateBot

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBot from a JSON string
create_bot_instance = CreateBot.from_json(json)
# print the JSON string representation of the object
print CreateBot.to_json()

# convert the object into a dict
create_bot_dict = create_bot_instance.to_dict()
# create an instance of CreateBot from a dict
create_bot_form_dict = create_bot.from_dict(create_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


