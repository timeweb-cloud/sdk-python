# UpdateAgent

Данные для обновления AI агента. Передавайте только изменяемые поля.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название агента | [optional] 
**description** | **object** | Описание агента | [optional] 
**access_type** | **object** | Тип доступа | [optional] 
**status** | **object** | Статус агента: &#x60;suspended&#x60; — приостановить, &#x60;active&#x60; — возобновить. Статус заблокированного или удалённого агента изменить нельзя. | [optional] 
**settings** | [**AgentSettings**](AgentSettings.md) |  | [optional] 
**project_id** | **object** | Не используется: перенести агента в другой проект можно методами проектов. | [optional] 
**additional_model_ids** | **object** | ID дополнительных моделей агента (например, для генерации изображений). Список заменяет текущий целиком. | [optional] 
**additional_models** | **object** | Дополнительные модели вместе с настройками (для моделей генерации изображений — &#x60;width&#x60;/&#x60;height&#x60;). Если переданы и &#x60;additional_models&#x60;, и &#x60;additional_model_ids&#x60;, используется &#x60;additional_models&#x60;. | [optional] 
**is_web_search_enabled** | **object** | Включить или выключить веб-поиск | [optional] 
**ai_gateway_key_id** | **object** | ID ключа AI Gateway, к которому нужно привязать агента. Привязка доступна, только если в ответе агента &#x60;ai_gateway_key_id&#x60; равен &#x60;null&#x60; (агент без баз знаний, инструментов и интеграций, созданный до 9 октября 2026 года), и делается один раз. При первой привязке на аккаунт однократно начисляется временная скидка 10% на запросы через ключи AI Gateway. | [optional] 
**token_package_id** | **object** | Новый пакет токенов. Только для агентов с пакетом токенов (устаревшая схема оплаты): пакет должен относиться к модели агента и быть не меньше текущего, его стоимость сразу списывается с баланса. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_agent import UpdateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgent from a JSON string
update_agent_instance = UpdateAgent.from_json(json)
# print the JSON string representation of the object
print UpdateAgent.to_json()

# convert the object into a dict
update_agent_dict = update_agent_instance.to_dict()
# create an instance of UpdateAgent from a dict
update_agent_form_dict = update_agent.from_dict(update_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


