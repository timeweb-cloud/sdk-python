# AiSolutionTelegramBot

Telegram-бот решения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_key** | **object** | ID бота в решении: &#x60;b&lt;ID бота в Telegram&gt;&#x60; | 
**bot_username** | **object** | Имя пользователя бота без &#x60;@&#x60;. &#x60;null&#x60;, если Telegram его не вернул | 
**state** | **object** | Состояние бота: &#x60;pending_pairing&#x60; — бот подключён, но владелец ещё не подтверждён (ожидается код подтверждения); &#x60;connected&#x60; — владелец подтверждён, агент отвечает в этом боте | 

## Example

```python
from timeweb_cloud_api.models.ai_solution_telegram_bot import AiSolutionTelegramBot

# TODO update the JSON string below
json = "{}"
# create an instance of AiSolutionTelegramBot from a JSON string
ai_solution_telegram_bot_instance = AiSolutionTelegramBot.from_json(json)
# print the JSON string representation of the object
print AiSolutionTelegramBot.to_json()

# convert the object into a dict
ai_solution_telegram_bot_dict = ai_solution_telegram_bot_instance.to_dict()
# create an instance of AiSolutionTelegramBot from a dict
ai_solution_telegram_bot_form_dict = ai_solution_telegram_bot.from_dict(ai_solution_telegram_bot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


