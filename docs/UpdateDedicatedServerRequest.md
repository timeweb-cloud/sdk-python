# UpdateDedicatedServerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Удобочитаемое имя выделенного сервера. Максимальная длина — 255 символов, имя должно быть уникальным. | [optional] 
**comment** | **object** | Комментарий к выделенному серверу. Максимальная длина — 255 символов. | [optional] 

## Example

```python
from openapi_client.models.update_dedicated_server_request import UpdateDedicatedServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDedicatedServerRequest from a JSON string
update_dedicated_server_request_instance = UpdateDedicatedServerRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDedicatedServerRequest.to_json()

# convert the object into a dict
update_dedicated_server_request_dict = update_dedicated_server_request_instance.to_dict()
# create an instance of UpdateDedicatedServerRequest from a dict
update_dedicated_server_request_form_dict = update_dedicated_server_request.from_dict(update_dedicated_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


