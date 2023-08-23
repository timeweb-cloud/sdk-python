# Project

Проект

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого проекта. Автоматически генерируется при создании. | 
**account_id** | **object** | Идентификатор пользователя. | 
**avatar_id** | **object** | Идентификатор аватара пользователя. Описание методов работы с аватарами появится позднее. | 
**description** | **object** | Описание проекта. | 
**name** | **object** | Удобочитаемое имя проекта. | 
**is_default** | **object** | Это логическое значение, которое показывает, выбран ли проект по умолчанию для создания новых сущностей. | 

## Example

```python
from timeweb_cloud_api.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print Project.to_json()

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_form_dict = project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


