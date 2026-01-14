# ModelParamsInfoTemperature

Параметр температуры

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** |  | [optional] 
**min** | **object** |  | [optional] 
**max** | **object** |  | [optional] 
**default** | **object** |  | [optional] 
**description** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.model_params_info_temperature import ModelParamsInfoTemperature

# TODO update the JSON string below
json = "{}"
# create an instance of ModelParamsInfoTemperature from a JSON string
model_params_info_temperature_instance = ModelParamsInfoTemperature.from_json(json)
# print the JSON string representation of the object
print ModelParamsInfoTemperature.to_json()

# convert the object into a dict
model_params_info_temperature_dict = model_params_info_temperature_instance.to_dict()
# create an instance of ModelParamsInfoTemperature from a dict
model_params_info_temperature_form_dict = model_params_info_temperature.from_dict(model_params_info_temperature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


