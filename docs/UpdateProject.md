# UpdateProject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Удобочитаемое имя проекта. Максимальная длина — 255 символов. | [optional] 
**description** | **object** | Описание проекта. Максимальная длина — 255 символов. | [optional] 
**avatar_id** | **object** | Идентификатор аватара пользователя. Описание методов работы с аватарами появится позднее. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_project import UpdateProject

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProject from a JSON string
update_project_instance = UpdateProject.from_json(json)
# print the JSON string representation of the object
print UpdateProject.to_json()

# convert the object into a dict
update_project_dict = update_project_instance.to_dict()
# create an instance of UpdateProject from a dict
update_project_form_dict = update_project.from_dict(update_project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


