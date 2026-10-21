# SyncAiKeyLimits

Полный набор лимитов ключа за один период

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **object** | Лимиты по моделям. &#x60;model_id&#x60; в списке не должны повторяться. Пустой список удаляет все лимиты периода | 
**limit_type** | **object** | Период лимита: &#x60;hour&#x60; — час, &#x60;day&#x60; — сутки, &#x60;week&#x60; — 7 дней, &#x60;month&#x60; — 30 дней | 
**entity_type** | **object** | Тип сущности. По умолчанию — тип ключа (лимиты на сам ключ) | [optional] 
**entity_id** | **object** | ID сущности. Для лимитов на сам ключ не нужен | [optional] 

## Example

```python
from timeweb_cloud_api.models.sync_ai_key_limits import SyncAiKeyLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SyncAiKeyLimits from a JSON string
sync_ai_key_limits_instance = SyncAiKeyLimits.from_json(json)
# print the JSON string representation of the object
print SyncAiKeyLimits.to_json()

# convert the object into a dict
sync_ai_key_limits_dict = sync_ai_key_limits_instance.to_dict()
# create an instance of SyncAiKeyLimits from a dict
sync_ai_key_limits_form_dict = sync_ai_key_limits.from_dict(sync_ai_key_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


