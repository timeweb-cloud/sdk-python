# RefreshApiKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expire** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда истекает токен. | [optional] 

## Example

```python
from timeweb_cloud_api.models.refresh_api_key import RefreshApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshApiKey from a JSON string
refresh_api_key_instance = RefreshApiKey.from_json(json)
# print the JSON string representation of the object
print RefreshApiKey.to_json()

# convert the object into a dict
refresh_api_key_dict = refresh_api_key_instance.to_dict()
# create an instance of RefreshApiKey from a dict
refresh_api_key_form_dict = refresh_api_key.from_dict(refresh_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


