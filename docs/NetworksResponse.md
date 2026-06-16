# NetworksResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**router_networks** | **object** | Сети роутера | 
**meta** | [**ComponentsSchemasMeta**](ComponentsSchemasMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.networks_response import NetworksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NetworksResponse from a JSON string
networks_response_instance = NetworksResponse.from_json(json)
# print the JSON string representation of the object
print NetworksResponse.to_json()

# convert the object into a dict
networks_response_dict = networks_response_instance.to_dict()
# create an instance of NetworksResponse from a dict
networks_response_form_dict = networks_response.from_dict(networks_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


