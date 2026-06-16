# RouterStatistic


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя метрики | 
**list** | **object** | Значения метрики | 
**meta** | [**RouterStatisticMeta**](RouterStatisticMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.router_statistic import RouterStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of RouterStatistic from a JSON string
router_statistic_instance = RouterStatistic.from_json(json)
# print the JSON string representation of the object
print RouterStatistic.to_json()

# convert the object into a dict
router_statistic_dict = router_statistic_instance.to_dict()
# create an instance of RouterStatistic from a dict
router_statistic_form_dict = router_statistic.from_dict(router_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


