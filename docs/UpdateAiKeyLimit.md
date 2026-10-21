# UpdateAiKeyLimit

Изменяемые значения лимита. Нужно передать `limit` или `money_limit`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **object** | Лимит в токенах за период. Не передан — не меняется. &#x60;0&#x60; — запросы запрещены | [optional] 
**money_limit** | **object** | Лимит в деньгах за период, в валюте аккаунта, не больше 8 знаков после точки. Приоритетнее &#x60;limit&#x60;. Не передан — не меняется; &#x60;null&#x60; — снять денежный лимит (только вместе с &#x60;limit&#x60;); &#x60;0&#x60; — запросы запрещены | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_ai_key_limit import UpdateAiKeyLimit

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAiKeyLimit from a JSON string
update_ai_key_limit_instance = UpdateAiKeyLimit.from_json(json)
# print the JSON string representation of the object
print UpdateAiKeyLimit.to_json()

# convert the object into a dict
update_ai_key_limit_dict = update_ai_key_limit_instance.to_dict()
# create an instance of UpdateAiKeyLimit from a dict
update_ai_key_limit_form_dict = update_ai_key_limit.from_dict(update_ai_key_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


