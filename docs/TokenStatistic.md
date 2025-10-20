# TokenStatistic

Точка статистики использования токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **object** | Время точки статистики | 
**ingoing_tokens** | **object** | Количество входящих токенов (промпты) | 
**outgoing_tokens** | **object** | Количество исходящих токенов (ответы) | 

## Example

```python
from timeweb_cloud_api.models.token_statistic import TokenStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of TokenStatistic from a JSON string
token_statistic_instance = TokenStatistic.from_json(json)
# print the JSON string representation of the object
print TokenStatistic.to_json()

# convert the object into a dict
token_statistic_dict = token_statistic_instance.to_dict()
# create an instance of TokenStatistic from a dict
token_statistic_form_dict = token_statistic.from_dict(token_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


