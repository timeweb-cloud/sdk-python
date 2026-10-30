# AppV2Provider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID провайдера Git. Для готового Docker-образа — пустая строка. | 
**type** | **object** | Тип провайдера исходного кода или образа. | 

## Example

```python
from timeweb_cloud_api.models.app_v2_provider import AppV2Provider

# TODO update the JSON string below
json = "{}"
# create an instance of AppV2Provider from a JSON string
app_v2_provider_instance = AppV2Provider.from_json(json)
# print the JSON string representation of the object
print AppV2Provider.to_json()

# convert the object into a dict
app_v2_provider_dict = app_v2_provider_instance.to_dict()
# create an instance of AppV2Provider from a dict
app_v2_provider_form_dict = app_v2_provider.from_dict(app_v2_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


