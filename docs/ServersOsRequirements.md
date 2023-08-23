# ServersOsRequirements

Требования к облачному серверу для установки операционной системы.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_min** | **object** | Минимальной значение процессора. | [optional] 
**disk_min** | **object** | Минимальное значение диска. | [optional] 
**ram_min** | **object** | Минимальное значение оперативной памяти. | [optional] 
**bandwidth_min** | **object** | Минимальное значение пропускной способности. | [optional] 

## Example

```python
from openapi_client.models.servers_os_requirements import ServersOsRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of ServersOsRequirements from a JSON string
servers_os_requirements_instance = ServersOsRequirements.from_json(json)
# print the JSON string representation of the object
print ServersOsRequirements.to_json()

# convert the object into a dict
servers_os_requirements_dict = servers_os_requirements_instance.to_dict()
# create an instance of ServersOsRequirements from a dict
servers_os_requirements_form_dict = servers_os_requirements.from_dict(servers_os_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


