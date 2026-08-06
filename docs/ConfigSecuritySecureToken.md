# ConfigSecuritySecureToken

Защита ссылок подписанным токеном. `null` — отключить защиту ссылок.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **object** | Секретный ключ, которым подписывается ссылка. | 
**restrict_by_ip** | **object** | Привязывать подписанную ссылку к IP-адресу пользователя. | 

## Example

```python
from timeweb_cloud_api.models.config_security_secure_token import ConfigSecuritySecureToken

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSecuritySecureToken from a JSON string
config_security_secure_token_instance = ConfigSecuritySecureToken.from_json(json)
# print the JSON string representation of the object
print ConfigSecuritySecureToken.to_json()

# convert the object into a dict
config_security_secure_token_dict = config_security_secure_token_instance.to_dict()
# create an instance of ConfigSecuritySecureToken from a dict
config_security_secure_token_form_dict = config_security_secure_token.from_dict(config_security_secure_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


