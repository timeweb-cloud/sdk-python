# ApproveTelegramPairing

Параметры подтверждения владельца Telegram-бота

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **object** | Код подтверждения, который бот присылает в личные сообщения в ответ на первое сообщение. Только буквы и цифры, от 4 до 32 символов | 

## Example

```python
from timeweb_cloud_api.models.approve_telegram_pairing import ApproveTelegramPairing

# TODO update the JSON string below
json = "{}"
# create an instance of ApproveTelegramPairing from a JSON string
approve_telegram_pairing_instance = ApproveTelegramPairing.from_json(json)
# print the JSON string representation of the object
print ApproveTelegramPairing.to_json()

# convert the object into a dict
approve_telegram_pairing_dict = approve_telegram_pairing_instance.to_dict()
# create an instance of ApproveTelegramPairing from a dict
approve_telegram_pairing_form_dict = approve_telegram_pairing.from_dict(approve_telegram_pairing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


