# CrispIntegration

Интеграция AI агента с Crisp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID интеграции | 
**account_id** | **object** | Логин аккаунта, которому принадлежит интеграция | 
**agent_id** | **object** | ID агента | 
**website_id** | **object** | Website ID сайта в Crisp | 
**webhook_secret** | **object** | Секрет вебхука — последний сегмент адреса вебхука, который нужно добавить в Crisp: &#x60;https://api.timeweb.cloud/api/v1/crisp/{website_id}/webhook/{webhook_secret}&#x60; | 
**status** | **object** | Статус интеграции: &#x60;pending&#x60; — ожидает подключения, &#x60;active&#x60; — работает, &#x60;error&#x60; — ошибка подключения | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего обновления | 

## Example

```python
from timeweb_cloud_api.models.crisp_integration import CrispIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of CrispIntegration from a JSON string
crisp_integration_instance = CrispIntegration.from_json(json)
# print the JSON string representation of the object
print CrispIntegration.to_json()

# convert the object into a dict
crisp_integration_dict = crisp_integration_instance.to_dict()
# create an instance of CrispIntegration from a dict
crisp_integration_form_dict = crisp_integration.from_dict(crisp_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


