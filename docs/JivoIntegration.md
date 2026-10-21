# JivoIntegration

Интеграция AI агента с Jivo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID интеграции | 
**account_id** | **object** | Логин аккаунта, которому принадлежит интеграция | 
**agent_id** | **object** | ID агента | 
**access_id** | **object** | Access ID агента. Это токен бота для Jivo и последний сегмент адреса, на который Jivo отправляет события | 
**status** | **object** | Статус интеграции: &#x60;pending&#x60; — ожидает подключения, &#x60;active&#x60; — работает, &#x60;error&#x60; — ошибка подключения | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего обновления | 

## Example

```python
from timeweb_cloud_api.models.jivo_integration import JivoIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of JivoIntegration from a JSON string
jivo_integration_instance = JivoIntegration.from_json(json)
# print the JSON string representation of the object
print JivoIntegration.to_json()

# convert the object into a dict
jivo_integration_dict = jivo_integration_instance.to_dict()
# create an instance of JivoIntegration from a dict
jivo_integration_form_dict = jivo_integration.from_dict(jivo_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


