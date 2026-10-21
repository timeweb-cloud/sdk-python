# AiKey

Ключ AI Gateway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ключа (UUID) | 
**account_id** | **object** | Логин аккаунта | 
**name** | **object** | Название ключа | 
**description** | **object** | Описание ключа | 
**entity_type** | **object** | Тип ключа: &#x60;aikey&#x60; — ключ, созданный пользователем (в том числе ключ AI-решения), &#x60;k8s&#x60; — ключ, выпущенный платформой для кластера Kubernetes | 
**entity_id** | **object** | ID ресурса, для которого платформа выпустила ключ (например, кластера Kubernetes). &#x60;null&#x60; — у ключей, созданных пользователем | 
**project_id** | **object** | ID проекта, к которому привязан ключ | 
**expires_at** | **object** | Дата и время окончания действия ключа. &#x60;null&#x60; — ключ бессрочный | 
**is_readonly** | **object** | Ключ управляется платформой (выпущен для AI-решения или кластера Kubernetes): изменить, перевыпустить и удалить его нельзя — такие запросы вернут 403 | 
**fallback_models** | **object** | Запасные модели в порядке приоритета. &#x60;[]&#x60; — не настроены, &#x60;null&#x60; — настройки временно не удалось прочитать (повторите запрос позже). Запасные модели применяются к любой модели, запрошенной этим ключом, и только в &#x60;/v1/chat/completions&#x60; и &#x60;/v1/responses&#x60;: если запрошенная модель не ответила, запрос по порядку повторяется на запасных. Запасная модель, совпадающая с запрошенной, пропускается. Резерв средств и проверка лимитов делаются по цене запрошенной модели, списание и учёт расхода — по цене ответившей: если запасная модель дороже, итоговое списание может превысить резерв и денежный лимит ключа. | 
**created_at** | **object** | Дата и время создания ключа | 
**updated_at** | **object** | Дата и время изменения ключа | 

## Example

```python
from timeweb_cloud_api.models.ai_key import AiKey

# TODO update the JSON string below
json = "{}"
# create an instance of AiKey from a JSON string
ai_key_instance = AiKey.from_json(json)
# print the JSON string representation of the object
print AiKey.to_json()

# convert the object into a dict
ai_key_dict = ai_key_instance.to_dict()
# create an instance of AiKey from a dict
ai_key_form_dict = ai_key.from_dict(ai_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


