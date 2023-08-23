# Resources


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | **object** | Количество нод | [optional] 
**cores** | [**Resource**](Resource.md) |  | [optional] 
**memory** | [**Resource**](Resource.md) |  | [optional] 
**pods** | [**Resource**](Resource.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.resources import Resources

# TODO update the JSON string below
json = "{}"
# create an instance of Resources from a JSON string
resources_instance = Resources.from_json(json)
# print the JSON string representation of the object
print Resources.to_json()

# convert the object into a dict
resources_dict = resources_instance.to_dict()
# create an instance of Resources from a dict
resources_form_dict = resources.from_dict(resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


