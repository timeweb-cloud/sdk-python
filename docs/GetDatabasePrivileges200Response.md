# GetDatabasePrivileges200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**privileges** | **object** | Список привилегий, доступных для кластера базы данных | 

## Example

```python
from timeweb_cloud_api.models.get_database_privileges200_response import GetDatabasePrivileges200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasePrivileges200Response from a JSON string
get_database_privileges200_response_instance = GetDatabasePrivileges200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabasePrivileges200Response.to_json()

# convert the object into a dict
get_database_privileges200_response_dict = get_database_privileges200_response_instance.to_dict()
# create an instance of GetDatabasePrivileges200Response from a dict
get_database_privileges200_response_form_dict = get_database_privileges200_response.from_dict(get_database_privileges200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


