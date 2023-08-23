# DeleteServiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **object** | Хеш, который совместно с кодом авторизации надо будет отправить для удаления. | 

## Example

```python
from openapi_client.models.delete_service_response import DeleteServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteServiceResponse from a JSON string
delete_service_response_instance = DeleteServiceResponse.from_json(json)
# print the JSON string representation of the object
print DeleteServiceResponse.to_json()

# convert the object into a dict
delete_service_response_dict = delete_service_response_instance.to_dict()
# create an instance of DeleteServiceResponse from a dict
delete_service_response_form_dict = delete_service_response.from_dict(delete_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


