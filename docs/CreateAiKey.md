# CreateAiKey

Параметры создания ключа AI Gateway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название ключа | 
**description** | **object** | Описание ключа | [optional] 
**project_id** | **object** | ID проекта, к которому привязать ключ | [optional] 
**expire** | **object** | Дата и время окончания действия ключа в формате ISO 8601. Поле обязательно: передайте &#x60;null&#x60;, чтобы ключ был бессрочным | 
**fallback_models** | **object** | Запасные модели в порядке приоритета, не больше двух и без повторов. Подходят только действующие текстовые модели каталога. Запасные модели применяются к любой модели, запрошенной этим ключом, и только в &#x60;/v1/chat/completions&#x60; и &#x60;/v1/responses&#x60;: если запрошенная модель не ответила, запрос по порядку повторяется на запасных. Запасная модель, совпадающая с запрошенной, пропускается. Резерв средств и проверка лимитов делаются по цене запрошенной модели, списание и учёт расхода — по цене ответившей: если запасная модель дороже, итоговое списание может превысить резерв и денежный лимит ключа. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_ai_key import CreateAiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAiKey from a JSON string
create_ai_key_instance = CreateAiKey.from_json(json)
# print the JSON string representation of the object
print CreateAiKey.to_json()

# convert the object into a dict
create_ai_key_dict = create_ai_key_instance.to_dict()
# create an instance of CreateAiKey from a dict
create_ai_key_form_dict = create_ai_key.from_dict(create_ai_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


