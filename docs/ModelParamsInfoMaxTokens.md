# ModelParamsInfoMaxTokens

Максимальное количество токенов

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
from timeweb_cloud_api.models.model_params_info_max_tokens import ModelParamsInfoMaxTokens

# TODO update the JSON string below
json = "{}"
# create an instance of ModelParamsInfoMaxTokens from a JSON string
model_params_info_max_tokens_instance = ModelParamsInfoMaxTokens.from_json(json)
# print the JSON string representation of the object
print ModelParamsInfoMaxTokens.to_json()

# convert the object into a dict
model_params_info_max_tokens_dict = model_params_info_max_tokens_instance.to_dict()
# create an instance of ModelParamsInfoMaxTokens from a dict
model_params_info_max_tokens_form_dict = model_params_info_max_tokens.from_dict(model_params_info_max_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


