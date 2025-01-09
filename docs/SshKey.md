# SshKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID SSH-ключа. | 
**name** | **object** | Название SSH-ключа. | 
**body** | **object** | Тело SSH-ключа. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан SSH-ключ. | 
**used_by** | **object** | Список серверов, которые используют SSH-ключ. | 
**is_default** | **object** | Это логическое значение, которое показывает, будет ли выбираться SSH-ключ по умолчанию при создании сервера. | [optional] 

## Example

```python
from timeweb_cloud_api.models.ssh_key import SshKey

# TODO update the JSON string below
json = "{}"
# create an instance of SshKey from a JSON string
ssh_key_instance = SshKey.from_json(json)
# print the JSON string representation of the object
print SshKey.to_json()

# convert the object into a dict
ssh_key_dict = ssh_key_instance.to_dict()
# create an instance of SshKey from a dict
ssh_key_form_dict = ssh_key.from_dict(ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


