# GetServerStatistics200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **object** |  | 
**network_traffic** | **object** |  | 
**disk** | **object** | Статистика основного диска | 
**ram** | **object** |  | 

## Example

```python
from openapi_client.models.get_server_statistics200_response import GetServerStatistics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerStatistics200Response from a JSON string
get_server_statistics200_response_instance = GetServerStatistics200Response.from_json(json)
# print the JSON string representation of the object
print GetServerStatistics200Response.to_json()

# convert the object into a dict
get_server_statistics200_response_dict = get_server_statistics200_response_instance.to_dict()
# create an instance of GetServerStatistics200Response from a dict
get_server_statistics200_response_form_dict = get_server_statistics200_response.from_dict(get_server_statistics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


