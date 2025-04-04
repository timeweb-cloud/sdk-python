# ServersStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя статистики. | [optional] 
**list** | **object** |  | [optional] 
**meta** | [**ServersStatisticsMeta**](ServersStatisticsMeta.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.servers_statistics import ServersStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ServersStatistics from a JSON string
servers_statistics_instance = ServersStatistics.from_json(json)
# print the JSON string representation of the object
print ServersStatistics.to_json()

# convert the object into a dict
servers_statistics_dict = servers_statistics_instance.to_dict()
# create an instance of ServersStatistics from a dict
servers_statistics_form_dict = servers_statistics.from_dict(servers_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


