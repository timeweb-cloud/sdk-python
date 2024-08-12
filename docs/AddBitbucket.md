# AddBitbucket

Добавление аккаунта Bitbucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | **object** | Тип провайдера. | 
**provider_token** | **object** | Токен доступа. &lt;br&gt; Для Bitbucket необходимо использовать &#39;App password&#39;. Инструкции по созданию можно найти в &lt;a target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/&#39;&gt;документации Bitbucket&lt;/a&gt;. &lt;br&gt; Установите следующие разрешения: &#x60;Account: Read&#x60;, &#x60;Projects: Read&#x60;, &#x60;Repositories: Read&#x60;, &#x60;Webhooks: Read and write&#x60; | 
**login** | **object** | Логин пользователя Bitbucket. | 

## Example

```python
from timeweb_cloud_api.models.add_bitbucket import AddBitbucket

# TODO update the JSON string below
json = "{}"
# create an instance of AddBitbucket from a JSON string
add_bitbucket_instance = AddBitbucket.from_json(json)
# print the JSON string representation of the object
print AddBitbucket.to_json()

# convert the object into a dict
add_bitbucket_dict = add_bitbucket_instance.to_dict()
# create an instance of AddBitbucket from a dict
add_bitbucket_form_dict = add_bitbucket.from_dict(add_bitbucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


