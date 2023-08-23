# AddCountriesToAllowedListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **object** | Список разрешенных стран | 

## Example

```python
from timeweb_cloud_api.models.add_countries_to_allowed_list_request import AddCountriesToAllowedListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddCountriesToAllowedListRequest from a JSON string
add_countries_to_allowed_list_request_instance = AddCountriesToAllowedListRequest.from_json(json)
# print the JSON string representation of the object
print AddCountriesToAllowedListRequest.to_json()

# convert the object into a dict
add_countries_to_allowed_list_request_dict = add_countries_to_allowed_list_request_instance.to_dict()
# create an instance of AddCountriesToAllowedListRequest from a dict
add_countries_to_allowed_list_request_form_dict = add_countries_to_allowed_list_request.from_dict(add_countries_to_allowed_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


