# ConfigParameters

Параметры базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql** | [**ConfigParametersMysql**](ConfigParametersMysql.md) |  | [optional] 
**postgres** | [**ConfigParametersPostgres**](ConfigParametersPostgres.md) |  | [optional] 
**valkey** | [**ConfigParametersValkey**](ConfigParametersValkey.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_parameters import ConfigParameters

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigParameters from a JSON string
config_parameters_instance = ConfigParameters.from_json(json)
# print the JSON string representation of the object
print ConfigParameters.to_json()

# convert the object into a dict
config_parameters_dict = config_parameters_instance.to_dict()
# create an instance of ConfigParameters from a dict
config_parameters_form_dict = config_parameters.from_dict(config_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


