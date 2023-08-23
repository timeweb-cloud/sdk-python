# GetTLD200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**top_level_domain** | [**TopLevelDomain**](TopLevelDomain.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_tld200_response import GetTLD200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetTLD200Response from a JSON string
get_tld200_response_instance = GetTLD200Response.from_json(json)
# print the JSON string representation of the object
print GetTLD200Response.to_json()

# convert the object into a dict
get_tld200_response_dict = get_tld200_response_instance.to_dict()
# create an instance of GetTLD200Response from a dict
get_tld200_response_form_dict = get_tld200_response.from_dict(get_tld200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


