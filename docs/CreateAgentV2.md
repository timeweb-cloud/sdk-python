# CreateAgentV2

Данные для создания AI агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название агента | 
**description** | **object** | Описание агента | [optional] 
**access_type** | **object** | Тип доступа: &#x60;public&#x60; — агент отвечает анонимным посетителям сайта через виджет; &#x60;private&#x60; — только по токену аккаунта. | 
**model_id** | **object** | ID основной модели агента | 
**settings** | [**AgentSettings**](AgentSettings.md) |  | 
**project_id** | **object** | ID проекта, в который нужно добавить агента. По умолчанию — проект по умолчанию. | [optional] 
**is_web_search_enabled** | **object** | Включить веб-поиск | [optional] 
**money_limit** | **object** | Дневной лимит расходов агента в валюте аккаунта. &#x60;0&#x60; или не передан — без лимита. Создаётся как лимит агента с периодом &#x60;day&#x60;; изменить его можно через лимиты агента. | [optional] 
**token_limit** | **object** | Устарело: дневной лимит агента в токенах. &#x60;0&#x60; или не передан — без лимита. Не учитывается, если передан &#x60;money_limit&#x60;. | [optional] 
**token_package_id** | **object** | Устарело и не учитывается: агент всегда создаётся с поресурсной оплатой. | [optional] 
**additional_model_ids** | **object** | ID дополнительных моделей агента (например, для генерации изображений). Список заменяет текущий целиком. | [optional] 
**additional_models** | **object** | Дополнительные модели вместе с настройками (для моделей генерации изображений — &#x60;width&#x60;/&#x60;height&#x60;). Если переданы и &#x60;additional_models&#x60;, и &#x60;additional_model_ids&#x60;, используется &#x60;additional_models&#x60;. | [optional] 
**skill_ids** | **object** | ID навыков, которые нужно подключить к агенту сразу после создания (текущие версии навыков). Неизвестные ID пропускаются; ошибка подключения навыков не отменяет создание агента. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_agent_v2 import CreateAgentV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentV2 from a JSON string
create_agent_v2_instance = CreateAgentV2.from_json(json)
# print the JSON string representation of the object
print CreateAgentV2.to_json()

# convert the object into a dict
create_agent_v2_dict = create_agent_v2_instance.to_dict()
# create an instance of CreateAgentV2 from a dict
create_agent_v2_form_dict = create_agent_v2.from_dict(create_agent_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


