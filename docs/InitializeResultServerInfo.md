# InitializeResultServerInfo

Сведения о сервере

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя сервера: &#x60;timeweb-cloud-mcp&#x60; на &#x60;/api/v1/mcp&#x60;, &#x60;timeweb-cloud-mcp-search&#x60; на &#x60;/api/v1/mcp/search&#x60; | 
**version** | **object** | Версия сервера | 

## Example

```python
from timeweb_cloud_api.models.initialize_result_server_info import InitializeResultServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeResultServerInfo from a JSON string
initialize_result_server_info_instance = InitializeResultServerInfo.from_json(json)
# print the JSON string representation of the object
print InitializeResultServerInfo.to_json()

# convert the object into a dict
initialize_result_server_info_dict = initialize_result_server_info_instance.to_dict()
# create an instance of InitializeResultServerInfo from a dict
initialize_result_server_info_form_dict = initialize_result_server_info.from_dict(initialize_result_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


