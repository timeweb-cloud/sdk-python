# NetworkDriversResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**network_drivers** | **object** | Массив сетевых драйверов k8s | 

## Example

```python
from openapi_client.models.network_drivers_response import NetworkDriversResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDriversResponse from a JSON string
network_drivers_response_instance = NetworkDriversResponse.from_json(json)
# print the JSON string representation of the object
print NetworkDriversResponse.to_json()

# convert the object into a dict
network_drivers_response_dict = network_drivers_response_instance.to_dict()
# create an instance of NetworkDriversResponse from a dict
network_drivers_response_form_dict = network_drivers_response.from_dict(network_drivers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


