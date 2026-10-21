# ConnectTelegram

Параметры подключения Telegram-бота

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_token** | **object** | Токен бота, выданный @BotFather, в формате &#x60;&lt;id бота&gt;:&lt;секрет&gt;&#x60;, например &#x60;123456789:AAH...&#x60; | 

## Example

```python
from timeweb_cloud_api.models.connect_telegram import ConnectTelegram

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectTelegram from a JSON string
connect_telegram_instance = ConnectTelegram.from_json(json)
# print the JSON string representation of the object
print ConnectTelegram.to_json()

# convert the object into a dict
connect_telegram_dict = connect_telegram_instance.to_dict()
# create an instance of ConnectTelegram from a dict
connect_telegram_form_dict = connect_telegram.from_dict(connect_telegram_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


