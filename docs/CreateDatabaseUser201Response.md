# CreateDatabaseUser201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | [**DatabaseAdmin**](DatabaseAdmin.md) |  | 

## Example

```python
from openapi_client.models.create_database_user201_response import CreateDatabaseUser201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabaseUser201Response from a JSON string
create_database_user201_response_instance = CreateDatabaseUser201Response.from_json(json)
# print the JSON string representation of the object
print CreateDatabaseUser201Response.to_json()

# convert the object into a dict
create_database_user201_response_dict = create_database_user201_response_instance.to_dict()
# create an instance of CreateDatabaseUser201Response from a dict
create_database_user201_response_form_dict = create_database_user201_response.from_dict(create_database_user201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


