# Agent

AI агент

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID агента | 
**name** | **object** | Название агента | 
**description** | **object** | Описание агента | 
**project_id** | **object** | ID проекта, в котором находится агент | [optional] 
**model_id** | **object** | ID основной модели агента | 
**provider_id** | **object** | ID провайдера модели | 
**settings** | [**AgentSettings**](AgentSettings.md) |  | 
**status** | **object** | Статус агента: - &#x60;active&#x60; — работает; - &#x60;suspended&#x60; — приостановлен владельцем; - &#x60;blocked&#x60; — заблокирован (для агентов с пакетом токенов — закончились токены или подписка); - &#x60;deleted&#x60; — удалён. | 
**access_type** | **object** | Тип доступа: &#x60;public&#x60; — агент отвечает анонимным посетителям сайта через виджет; &#x60;private&#x60; — только по токену аккаунта. | 
**access_id** | **object** | Идентификатор доступа агента. Используется для вызова агента из своих приложений через OpenAI-совместимое API (см. https://agent.timeweb.cloud/docs) и для встраивания виджета. | 
**token_limit** | **object** | Устарело. Дневной лимит агента в токенах без привязки к модели, если он задан; &#x60;0&#x60; — такого лимита нет. Лимиты в деньгах, по моделям и за другие периоды здесь не отражаются — используйте лимиты агента (&#x60;/api/v1/cloud-ai/agents/{id}/entity-limits&#x60;). | 
**total_tokens** | **object** | Всего токенов в пакете. Только для агентов с пакетом токенов (устаревшая схема оплаты). | [optional] 
**used_tokens** | **object** | Использовано токенов пакета. Для агентов с поресурсной оплатой — &#x60;null&#x60;. | 
**remaining_tokens** | **object** | Осталось токенов в пакете. Только для агентов с пакетом токенов. | [optional] 
**token_package_id** | **object** | ID пакета токенов. Только для агентов с пакетом токенов; у агентов с поресурсной оплатой поле отсутствует. | [optional] 
**subscription_renewal_date** | **object** | Дата продления подписки на пакет токенов. Только для агентов с пакетом токенов. | [optional] 
**auto_buy_additional_tokens** | **object** | Включена ли автоматическая докупка пакетов токенов | 
**tools** | **object** | Инструменты, подключённые к агенту | 
**additional_model_ids** | **object** | ID дополнительных моделей агента | 
**additional_models** | **object** | Дополнительные модели агента с настройками | 
**is_web_search_enabled** | **object** | Включён ли веб-поиск | 
**ai_gateway_key_id** | **object** | ID ключа AI Gateway, к которому привязан агент. &#x60;null&#x60; — агента можно привязать к ключу (см. обновление агента); поле отсутствует — привязка недоступна. | [optional] 
**created_at** | **object** | Дата создания агента | 
**knowledge_bases_ids** | **object** | ID баз знаний, подключённых к агенту | 

## Example

```python
from timeweb_cloud_api.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print Agent.to_json()

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


