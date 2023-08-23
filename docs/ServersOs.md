# ServersOs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор операционной системы. | [optional] 
**family** | **object** | Семейство операционной системы. | [optional] 
**name** | **object** | Название операционной системы. | [optional] 
**version** | **object** | Версия операционной системы. | [optional] 
**version_codename** | **object** | Кодовое имя версии операционной системы. | [optional] 
**description** | **object** | Описание операционной системы. | [optional] 
**requirements** | [**ServersOsRequirements**](ServersOsRequirements.md) |  | [optional] 

## Example

```python
from openapi_client.models.servers_os import ServersOs

# TODO update the JSON string below
json = "{}"
# create an instance of ServersOs from a JSON string
servers_os_instance = ServersOs.from_json(json)
# print the JSON string representation of the object
print ServersOs.to_json()

# convert the object into a dict
servers_os_dict = servers_os_instance.to_dict()
# create an instance of ServersOs from a dict
servers_os_form_dict = servers_os.from_dict(servers_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


