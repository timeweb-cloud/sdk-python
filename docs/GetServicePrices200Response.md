# GetServicePrices200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services_costs** | **object** | Список сервисов с информацией о стоимости | 
**meta** | [**GetServicePrices200ResponseMeta**](GetServicePrices200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_service_prices200_response import GetServicePrices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServicePrices200Response from a JSON string
get_service_prices200_response_instance = GetServicePrices200Response.from_json(json)
# print the JSON string representation of the object
print GetServicePrices200Response.to_json()

# convert the object into a dict
get_service_prices200_response_dict = get_service_prices200_response_instance.to_dict()
# create an instance of GetServicePrices200Response from a dict
get_service_prices200_response_form_dict = get_service_prices200_response.from_dict(get_service_prices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


