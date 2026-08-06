# GetDatabaseS3Backups200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_database_s3_backups200_response import GetDatabaseS3Backups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabaseS3Backups200Response from a JSON string
get_database_s3_backups200_response_instance = GetDatabaseS3Backups200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabaseS3Backups200Response.to_json()

# convert the object into a dict
get_database_s3_backups200_response_dict = get_database_s3_backups200_response_instance.to_dict()
# create an instance of GetDatabaseS3Backups200Response from a dict
get_database_s3_backups200_response_form_dict = get_database_s3_backups200_response.from_dict(get_database_s3_backups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


