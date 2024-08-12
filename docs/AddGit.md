# AddGit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **object** | Тип провайдера. | 
**url** | **object** | Внешний url адрес репозитория. | 
**login** | **object** | Логин провайдера. Используется при добавлении приватных репозиториев | [optional] 
**password** | **object** | Пароль или токен провайдера. Обязателен при добавлении приватных репозиториев. Подробнее в нашей &lt;a href&#x3D;&#39;https://timeweb.cloud/docs/apps/connecting-repositories#podkluchenie-repozitoriya-po-ssylke&#39;&gt;документации&lt;/a&gt;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.add_git import AddGit

# TODO update the JSON string below
json = "{}"
# create an instance of AddGit from a JSON string
add_git_instance = AddGit.from_json(json)
# print the JSON string representation of the object
print AddGit.to_json()

# convert the object into a dict
add_git_dict = add_git_instance.to_dict()
# create an instance of AddGit from a dict
add_git_form_dict = add_git.from_dict(add_git_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


