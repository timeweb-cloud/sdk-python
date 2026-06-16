# RouterStatisticsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**statistics** | **object** | Статистика | 

## Example

```python
from timeweb_cloud_api.models.router_statistics_response import RouterStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouterStatisticsResponse from a JSON string
router_statistics_response_instance = RouterStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print RouterStatisticsResponse.to_json()

# convert the object into a dict
router_statistics_response_dict = router_statistics_response_instance.to_dict()
# create an instance of RouterStatisticsResponse from a dict
router_statistics_response_form_dict = router_statistics_response.from_dict(router_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


