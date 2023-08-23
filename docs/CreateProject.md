# CreateProject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Удобочитаемое имя проекта. Максимальная длина — 255 символов. | 
**description** | **object** | Описание проекта. Максимальная длина — 255 символов. | [optional] 
**avatar_id** | **object** | Идентификатор аватара пользователя. Описание методов работы с аватарами появится позднее. | [optional] 

## Example

```python
from openapi_client.models.create_project import CreateProject

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProject from a JSON string
create_project_instance = CreateProject.from_json(json)
# print the JSON string representation of the object
print CreateProject.to_json()

# convert the object into a dict
create_project_dict = create_project_instance.to_dict()
# create an instance of CreateProject from a dict
create_project_form_dict = create_project.from_dict(create_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


