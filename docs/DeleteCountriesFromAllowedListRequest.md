# DeleteCountriesFromAllowedListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **object** | Список удаляемых из списка разрешенных стран. | 

## Example

```python
from timeweb_cloud_api.models.delete_countries_from_allowed_list_request import DeleteCountriesFromAllowedListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteCountriesFromAllowedListRequest from a JSON string
delete_countries_from_allowed_list_request_instance = DeleteCountriesFromAllowedListRequest.from_json(json)
# print the JSON string representation of the object
print DeleteCountriesFromAllowedListRequest.to_json()

# convert the object into a dict
delete_countries_from_allowed_list_request_dict = delete_countries_from_allowed_list_request_instance.to_dict()
# create an instance of DeleteCountriesFromAllowedListRequest from a dict
delete_countries_from_allowed_list_request_form_dict = delete_countries_from_allowed_list_request.from_dict(delete_countries_from_allowed_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


