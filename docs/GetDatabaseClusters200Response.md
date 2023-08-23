# GetDatabaseClusters200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**dbs** | **object** |  | 

## Example

```python
from openapi_client.models.get_database_clusters200_response import GetDatabaseClusters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabaseClusters200Response from a JSON string
get_database_clusters200_response_instance = GetDatabaseClusters200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabaseClusters200Response.to_json()

# convert the object into a dict
get_database_clusters200_response_dict = get_database_clusters200_response_instance.to_dict()
# create an instance of GetDatabaseClusters200Response from a dict
get_database_clusters200_response_form_dict = get_database_clusters200_response.from_dict(get_database_clusters200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


