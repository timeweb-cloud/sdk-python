# InitializeParamsClientInfo

Сведения о клиенте

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название клиента | 
**version** | **object** | Версия клиента | 

## Example

```python
from timeweb_cloud_api.models.initialize_params_client_info import InitializeParamsClientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeParamsClientInfo from a JSON string
initialize_params_client_info_instance = InitializeParamsClientInfo.from_json(json)
# print the JSON string representation of the object
print InitializeParamsClientInfo.to_json()

# convert the object into a dict
initialize_params_client_info_dict = initialize_params_client_info_instance.to_dict()
# create an instance of InitializeParamsClientInfo from a dict
initialize_params_client_info_form_dict = initialize_params_client_info.from_dict(initialize_params_client_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


