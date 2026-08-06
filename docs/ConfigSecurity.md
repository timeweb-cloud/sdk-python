# ConfigSecurity

Настройки безопасности

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redirect** | **object** | Перенаправлять запросы с HTTP на HTTPS. | [optional] 
**certificate_id** | **object** | ID SSL-сертификата, который используется для доменов ресурса. &#x60;null&#x60; — отвязать сертификат. | [optional] 
**secure_token** | [**ConfigSecuritySecureToken**](ConfigSecuritySecureToken.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_security import ConfigSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigSecurity from a JSON string
config_security_instance = ConfigSecurity.from_json(json)
# print the JSON string representation of the object
print ConfigSecurity.to_json()

# convert the object into a dict
config_security_dict = config_security_instance.to_dict()
# create an instance of ConfigSecurity from a dict
config_security_form_dict = config_security.from_dict(config_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


