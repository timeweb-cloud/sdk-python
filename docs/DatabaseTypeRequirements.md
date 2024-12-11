# DatabaseTypeRequirements

Требования к кластеру базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_min** | **object** | Минимальное количество CPU. | [optional] 
**ram_min** | **object** | Минимальный объем оперативной памяти. | [optional] 
**disk_min** | **object** | Минимальный объем дискового пространства. | [optional] 

## Example

```python
from timeweb_cloud_api.models.database_type_requirements import DatabaseTypeRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseTypeRequirements from a JSON string
database_type_requirements_instance = DatabaseTypeRequirements.from_json(json)
# print the JSON string representation of the object
print DatabaseTypeRequirements.to_json()

# convert the object into a dict
database_type_requirements_dict = database_type_requirements_instance.to_dict()
# create an instance of DatabaseTypeRequirements from a dict
database_type_requirements_form_dict = database_type_requirements.from_dict(database_type_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


