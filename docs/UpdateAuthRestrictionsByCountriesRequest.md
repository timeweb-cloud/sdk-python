# UpdateAuthRestrictionsByCountriesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Это логическое значение, которое показывает, включены ли ограничения по IP-адресу. | 

## Example

```python
from timeweb_cloud_api.models.update_auth_restrictions_by_countries_request import UpdateAuthRestrictionsByCountriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAuthRestrictionsByCountriesRequest from a JSON string
update_auth_restrictions_by_countries_request_instance = UpdateAuthRestrictionsByCountriesRequest.from_json(json)
# print the JSON string representation of the object
print UpdateAuthRestrictionsByCountriesRequest.to_json()

# convert the object into a dict
update_auth_restrictions_by_countries_request_dict = update_auth_restrictions_by_countries_request_instance.to_dict()
# create an instance of UpdateAuthRestrictionsByCountriesRequest from a dict
update_auth_restrictions_by_countries_request_form_dict = update_auth_restrictions_by_countries_request.from_dict(update_auth_restrictions_by_countries_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


