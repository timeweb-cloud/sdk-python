# AddonsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**meta** | [**SchemasMeta**](SchemasMeta.md) |  | 
**addons** | **object** | Массив дополнений k8s | 

## Example

```python
from timeweb_cloud_api.models.addons_response import AddonsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddonsResponse from a JSON string
addons_response_instance = AddonsResponse.from_json(json)
# print the JSON string representation of the object
print AddonsResponse.to_json()

# convert the object into a dict
addons_response_dict = addons_response_instance.to_dict()
# create an instance of AddonsResponse from a dict
addons_response_form_dict = addons_response.from_dict(addons_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


