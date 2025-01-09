# ProjectResource

Ресурс проекта

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого ресурса проекта. Автоматически генерируется при создании. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан ресурс. | 
**resource_id** | **object** | Идентификатор ресурса проекта (сервера, хранилища, кластера, балансировщика, базы данных или выделенного сервера). | 
**project** | [**Project**](Project.md) |  | 
**type** | **object** | Тип ресурса проекта | 

## Example

```python
from timeweb_cloud_api.models.project_resource import ProjectResource

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResource from a JSON string
project_resource_instance = ProjectResource.from_json(json)
# print the JSON string representation of the object
print ProjectResource.to_json()

# convert the object into a dict
project_resource_dict = project_resource_instance.to_dict()
# create an instance of ProjectResource from a dict
project_resource_form_dict = project_resource.from_dict(project_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


