# CreateAgent

Данные для создания AI агента (устаревший метод API v1)

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
**token_package_id** | **object** | ID пакета токенов. Обязателен для совместимости, но не учитывается: агент всегда создаётся с поресурсной оплатой. | 

## Example

```python
from timeweb_cloud_api.models.create_agent import CreateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgent from a JSON string
create_agent_instance = CreateAgent.from_json(json)
# print the JSON string representation of the object
print CreateAgent.to_json()

# convert the object into a dict
create_agent_dict = create_agent_instance.to_dict()
# create an instance of CreateAgent from a dict
create_agent_form_dict = create_agent.from_dict(create_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


