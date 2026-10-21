# UpdateAiKey

Изменяемые параметры ключа AI Gateway. Не переданные поля не меняются

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название ключа | [optional] 
**description** | **object** | Описание ключа. &#x60;null&#x60; — очистить описание | [optional] 
**fallback_models** | **object** | Запасные модели в порядке приоритета, не больше двух и без повторов. Переданный список заменяет текущий целиком; &#x60;null&#x60; или &#x60;[]&#x60; — убрать запасные модели; поле не передано — не меняются. Запасные модели применяются к любой модели, запрошенной этим ключом, и только в &#x60;/v1/chat/completions&#x60; и &#x60;/v1/responses&#x60;: если запрошенная модель не ответила, запрос по порядку повторяется на запасных. Запасная модель, совпадающая с запрошенной, пропускается. Резерв средств и проверка лимитов делаются по цене запрошенной модели, списание и учёт расхода — по цене ответившей: если запасная модель дороже, итоговое списание может превысить резерв и денежный лимит ключа. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_ai_key import UpdateAiKey

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAiKey from a JSON string
update_ai_key_instance = UpdateAiKey.from_json(json)
# print the JSON string representation of the object
print UpdateAiKey.to_json()

# convert the object into a dict
update_ai_key_dict = update_ai_key_instance.to_dict()
# create an instance of UpdateAiKey from a dict
update_ai_key_form_dict = update_ai_key.from_dict(update_ai_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


