# CreateDatabaseCluster201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | [**DatabaseCluster**](DatabaseCluster.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_database_cluster201_response import CreateDatabaseCluster201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabaseCluster201Response from a JSON string
create_database_cluster201_response_instance = CreateDatabaseCluster201Response.from_json(json)
# print the JSON string representation of the object
print CreateDatabaseCluster201Response.to_json()

# convert the object into a dict
create_database_cluster201_response_dict = create_database_cluster201_response_instance.to_dict()
# create an instance of CreateDatabaseCluster201Response from a dict
create_database_cluster201_response_form_dict = create_database_cluster201_response.from_dict(create_database_cluster201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


