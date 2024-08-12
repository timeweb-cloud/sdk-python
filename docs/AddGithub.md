# AddGithub

Добавление аккаунта GitHub

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **object** | Тип провайдера. | 
**provider_token** | **object** | Токен доступа. &lt;br&gt; Для GitHub необходимо использовать &#39;Fine-grained personal access token&#39;. Инструкции по созданию можно найти в &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://docs.GitHub.com/ru/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token&#39;&gt;документации GitHub&lt;/a&gt;. &lt;br&gt; Выберите репозитории, к которым хотите предоставить доступ, и установите следующие разрешения: &#x60;Webhooks: read and write&#x60;, &#x60;Contents: read-only&#x60;. | 

## Example

```python
from timeweb_cloud_api.models.add_github import AddGithub

# TODO update the JSON string below
json = "{}"
# create an instance of AddGithub from a JSON string
add_github_instance = AddGithub.from_json(json)
# print the JSON string representation of the object
print AddGithub.to_json()

# convert the object into a dict
add_github_dict = add_github_instance.to_dict()
# create an instance of AddGithub from a dict
add_github_form_dict = add_github.from_dict(add_github_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


