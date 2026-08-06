# UpdateDatabaseCluster200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | [**DatabaseCluster**](DatabaseCluster.md) |  | 
**warning** | **object** | Предупреждение о частично примененных изменениях. Появляется, если в &#x60;config_parameters&#x60; были переданы значения, не прошедшие валидацию: такие параметры отбрасываются, остальные изменения применяются. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_database_cluster200_response import UpdateDatabaseCluster200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDatabaseCluster200Response from a JSON string
update_database_cluster200_response_instance = UpdateDatabaseCluster200Response.from_json(json)
# print the JSON string representation of the object
print UpdateDatabaseCluster200Response.to_json()

# convert the object into a dict
update_database_cluster200_response_dict = update_database_cluster200_response_instance.to_dict()
# create an instance of UpdateDatabaseCluster200Response from a dict
update_database_cluster200_response_form_dict = update_database_cluster200_response.from_dict(update_database_cluster200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


