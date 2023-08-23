# CreateDatabaseBackup201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | [**Backup**](Backup.md) |  | 

## Example

```python
from openapi_client.models.create_database_backup201_response import CreateDatabaseBackup201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabaseBackup201Response from a JSON string
create_database_backup201_response_instance = CreateDatabaseBackup201Response.from_json(json)
# print the JSON string representation of the object
print CreateDatabaseBackup201Response.to_json()

# convert the object into a dict
create_database_backup201_response_dict = create_database_backup201_response_instance.to_dict()
# create an instance of CreateDatabaseBackup201Response from a dict
create_database_backup201_response_form_dict = create_database_backup201_response.from_dict(create_database_backup201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


