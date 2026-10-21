# ModelParamInfo

Настраиваемый параметр генерации

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип значения параметра | 
**description** | **object** | Описание параметра (на английском) | 
**min** | **object** | Минимальное значение, для &#x60;type: number&#x60; | [optional] 
**max** | **object** | Максимальное значение, для &#x60;type: number&#x60; | [optional] 
**enum** | **object** | Допустимые значения, для &#x60;type: enum&#x60; | [optional] 
**default** | **object** | Значение по умолчанию | 

## Example

```python
from timeweb_cloud_api.models.model_param_info import ModelParamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModelParamInfo from a JSON string
model_param_info_instance = ModelParamInfo.from_json(json)
# print the JSON string representation of the object
print ModelParamInfo.to_json()

# convert the object into a dict
model_param_info_dict = model_param_info_instance.to_dict()
# create an instance of ModelParamInfo from a dict
model_param_info_form_dict = model_param_info.from_dict(model_param_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


