# DomainNameServer

Name-сервер

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_delegation_allowed** | **object** | Это логическое значение, которое показывает включена ли услуга разрешено ли делегирование домена. | 
**items** | **object** | Список name-серверов | 
**task_status** | **object** | Статус добавления name-сервера. | 

## Example

```python
from openapi_client.models.domain_name_server import DomainNameServer

# TODO update the JSON string below
json = "{}"
# create an instance of DomainNameServer from a JSON string
domain_name_server_instance = DomainNameServer.from_json(json)
# print the JSON string representation of the object
print DomainNameServer.to_json()

# convert the object into a dict
domain_name_server_dict = domain_name_server_instance.to_dict()
# create an instance of DomainNameServer from a dict
domain_name_server_form_dict = domain_name_server.from_dict(domain_name_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


