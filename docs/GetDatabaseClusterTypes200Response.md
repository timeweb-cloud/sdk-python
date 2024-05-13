# GetDatabaseClusterTypes200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**types** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_database_cluster_types200_response import GetDatabaseClusterTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabaseClusterTypes200Response from a JSON string
get_database_cluster_types200_response_instance = GetDatabaseClusterTypes200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabaseClusterTypes200Response.to_json()

# convert the object into a dict
get_database_cluster_types200_response_dict = get_database_cluster_types200_response_instance.to_dict()
# create an instance of GetDatabaseClusterTypes200Response from a dict
get_database_cluster_types200_response_form_dict = get_database_cluster_types200_response.from_dict(get_database_cluster_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


