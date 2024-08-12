# AddGitlab

Добавление аккаунта gitlab

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **object** | Тип провайдера. | 
**provider_token** | **object** | Токен доступа. &lt;br&gt; Для Gitlab необходимо использовать персональный токен доступа. Инструкции по созданию можно найти в &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html#create-a-personal-access-token&#39;&gt;документации GitLab&lt;/a&gt;. &lt;br&gt; Установите следующие разрешения: &#x60;api&#x60; | 

## Example

```python
from timeweb_cloud_api.models.add_gitlab import AddGitlab

# TODO update the JSON string below
json = "{}"
# create an instance of AddGitlab from a JSON string
add_gitlab_instance = AddGitlab.from_json(json)
# print the JSON string representation of the object
print AddGitlab.to_json()

# convert the object into a dict
add_gitlab_dict = add_gitlab_instance.to_dict()
# create an instance of AddGitlab from a dict
add_gitlab_form_dict = add_gitlab.from_dict(add_gitlab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


