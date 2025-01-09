# Repository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID репозитория. | 
**name** | **object** | Имя репозитория. | 
**full_name** | **object** | Полное имя репозитория. | 
**url** | **object** | Ссылка на репозиторий. | 
**is_private** | **object** | Является ли репозиторий приватным. | 
**is_allowed_webhook** | **object** | Доступно ли создание вебхука для функции автодеплойя. | 

## Example

```python
from timeweb_cloud_api.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print Repository.to_json()

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_form_dict = repository.from_dict(repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


