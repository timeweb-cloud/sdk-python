# ResourcesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**resources** | [**Resources**](Resources.md) |  | 

## Example

```python
from timeweb_cloud_api.models.resources_response import ResourcesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesResponse from a JSON string
resources_response_instance = ResourcesResponse.from_json(json)
# print the JSON string representation of the object
print ResourcesResponse.to_json()

# convert the object into a dict
resources_response_dict = resources_response_instance.to_dict()
# create an instance of ResourcesResponse from a dict
resources_response_form_dict = resources_response.from_dict(resources_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


