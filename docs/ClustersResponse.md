# ClustersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**clusters** | **object** | Массив объектов Кластер | 

## Example

```python
from timeweb_cloud_api.models.clusters_response import ClustersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClustersResponse from a JSON string
clusters_response_instance = ClustersResponse.from_json(json)
# print the JSON string representation of the object
print ClustersResponse.to_json()

# convert the object into a dict
clusters_response_dict = clusters_response_instance.to_dict()
# create an instance of ClustersResponse from a dict
clusters_response_form_dict = clusters_response.from_dict(clusters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


