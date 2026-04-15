# AddonsConfigResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**meta** | [**SchemasMeta**](SchemasMeta.md) |  | 
**k8s_addons** | **object** | Массив конфигураций дополнений k8s | 

## Example

```python
from timeweb_cloud_api.models.addons_config_response import AddonsConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsConfigResponse from a JSON string
addons_config_response_instance = AddonsConfigResponse.from_json(json)
# print the JSON string representation of the object
print AddonsConfigResponse.to_json()

# convert the object into a dict
addons_config_response_dict = addons_config_response_instance.to_dict()
# create an instance of AddonsConfigResponse from a dict
addons_config_response_form_dict = addons_config_response.from_dict(addons_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


