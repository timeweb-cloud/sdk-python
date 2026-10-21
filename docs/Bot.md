# Bot

Бот, подключенный к AI агенту (Telegram или MAX)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID бота в Timeweb Cloud | 
**account_id** | **object** | Логин аккаунта, которому принадлежит бот | 
**agent_id** | **object** | ID агента, который отвечает от имени бота | 
**username** | **object** | Username бота в мессенджере (без &#x60;@&#x60;) | 
**first_name** | **object** | Имя бота в мессенджере | 
**description** | **object** | Комментарий к боту. Пустая строка, если не задан | 
**status** | **object** | Статус подключения: &#x60;pending&#x60; — ожидает подключения, &#x60;active&#x60; — работает, &#x60;error&#x60; — ошибка подключения | 
**whitelist_enabled** | **object** | Включено ли ограничение доступа по списку username. У MAX-ботов всегда &#x60;false&#x60; | 
**whitelist_usernames** | **object** | Username пользователей, которым разрешено писать боту: в нижнем регистре, без &#x60;@&#x60;. У MAX-ботов всегда пустой | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего обновления | 

## Example

```python
from timeweb_cloud_api.models.bot import Bot

# TODO update the JSON string below
json = "{}"
# create an instance of Bot from a JSON string
bot_instance = Bot.from_json(json)
# print the JSON string representation of the object
print Bot.to_json()

# convert the object into a dict
bot_dict = bot_instance.to_dict()
# create an instance of Bot from a dict
bot_form_dict = bot.from_dict(bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


