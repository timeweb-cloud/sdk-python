# GetDomains200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**domains** | **object** |  | 

## Example

```python
from openapi_client.models.get_domains200_response import GetDomains200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomains200Response from a JSON string
get_domains200_response_instance = GetDomains200Response.from_json(json)
# print the JSON string representation of the object
print GetDomains200Response.to_json()

# convert the object into a dict
get_domains200_response_dict = get_domains200_response_instance.to_dict()
# create an instance of GetDomains200Response from a dict
get_domains200_response_form_dict = get_domains200_response.from_dict(get_domains200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


