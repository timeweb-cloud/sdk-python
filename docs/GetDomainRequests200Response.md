# GetDomainRequests200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**requests** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_domain_requests200_response import GetDomainRequests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainRequests200Response from a JSON string
get_domain_requests200_response_instance = GetDomainRequests200Response.from_json(json)
# print the JSON string representation of the object
print GetDomainRequests200Response.to_json()

# convert the object into a dict
get_domain_requests200_response_dict = get_domain_requests200_response_instance.to_dict()
# create an instance of GetDomainRequests200Response from a dict
get_domain_requests200_response_form_dict = get_domain_requests200_response.from_dict(get_domain_requests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


