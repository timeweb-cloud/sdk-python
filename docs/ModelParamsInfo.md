# ModelParamsInfo

Информация о доступных параметрах модели с их ограничениями

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temperature** | [**ModelParamsInfoTemperature**](ModelParamsInfoTemperature.md) |  | [optional] 
**max_tokens** | [**ModelParamsInfoMaxTokens**](ModelParamsInfoMaxTokens.md) |  | [optional] 
**reasoning_effort** | [**ModelParamsInfoReasoningEffort**](ModelParamsInfoReasoningEffort.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.model_params_info import ModelParamsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModelParamsInfo from a JSON string
model_params_info_instance = ModelParamsInfo.from_json(json)
# print the JSON string representation of the object
print ModelParamsInfo.to_json()

# convert the object into a dict
model_params_info_dict = model_params_info_instance.to_dict()
# create an instance of ModelParamsInfo from a dict
model_params_info_form_dict = model_params_info.from_dict(model_params_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


