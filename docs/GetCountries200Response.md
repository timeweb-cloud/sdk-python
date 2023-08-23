# GetCountries200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**countries** | **object** | Список стран, приходит в виде объекта, где ключ - код страны в формате Alpha-2 ISO 3166-1, а значение - название страны в удобочитаемом формате. | 

## Example

```python
from timeweb_cloud_api.models.get_countries200_response import GetCountries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCountries200Response from a JSON string
get_countries200_response_instance = GetCountries200Response.from_json(json)
# print the JSON string representation of the object
print GetCountries200Response.to_json()

# convert the object into a dict
get_countries200_response_dict = get_countries200_response_instance.to_dict()
# create an instance of GetCountries200Response from a dict
get_countries200_response_form_dict = get_countries200_response.from_dict(get_countries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


