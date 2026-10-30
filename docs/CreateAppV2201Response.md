# CreateAppV2201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppV2**](AppV2.md) |  | 
**response_id** | **object** | ID запроса, который можно указывать при обращении в службу технической поддержки, чтобы помочь определить проблему. | 

## Example

```python
from timeweb_cloud_api.models.create_app_v2201_response import CreateAppV2201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppV2201Response from a JSON string
create_app_v2201_response_instance = CreateAppV2201Response.from_json(json)
# print the JSON string representation of the object
print CreateAppV2201Response.to_json()

# convert the object into a dict
create_app_v2201_response_dict = create_app_v2201_response_instance.to_dict()
# create an instance of CreateAppV2201Response from a dict
create_app_v2201_response_form_dict = create_app_v2201_response.from_dict(create_app_v2201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


