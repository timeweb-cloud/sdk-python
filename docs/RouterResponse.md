# RouterResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**router** | [**RouterOut**](RouterOut.md) |  | 

## Example

```python
from timeweb_cloud_api.models.router_response import RouterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouterResponse from a JSON string
router_response_instance = RouterResponse.from_json(json)
# print the JSON string representation of the object
print RouterResponse.to_json()

# convert the object into a dict
router_response_dict = router_response_instance.to_dict()
# create an instance of RouterResponse from a dict
router_response_form_dict = router_response.from_dict(router_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


