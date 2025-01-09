# ServersSoftware


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ПО из маркетплейса. | [optional] 
**name** | **object** | Имя ПО из маркетплейса. | [optional] 
**os_ids** | **object** | Список id операционных систем, на которых доступна установка ПО. | [optional] 
**description** | **object** | Описание ПО из маркетплейса. | [optional] 
**installations** | **object** | Количество установок ПО. | [optional] 
**requirements** | [**ServersSoftwareRequirements**](ServersSoftwareRequirements.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.servers_software import ServersSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of ServersSoftware from a JSON string
servers_software_instance = ServersSoftware.from_json(json)
# print the JSON string representation of the object
print ServersSoftware.to_json()

# convert the object into a dict
servers_software_dict = servers_software_instance.to_dict()
# create an instance of ServersSoftware from a dict
servers_software_form_dict = servers_software.from_dict(servers_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


