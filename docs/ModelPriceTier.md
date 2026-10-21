# ModelPriceTier

Ступень цены по размеру входного контекста. Действует, когда входной контекст запроса строго больше `above_context_tokens`; при этом по ступени тарифицируются и входные, и выходные токены запроса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**above_context_tokens** | **object** | Порог входного контекста в токенах | 
**cost_in** | **object** | Цена 1 входного токена в рублях | 
**cost_out** | **object** | Цена 1 выходного токена в рублях | 

## Example

```python
from timeweb_cloud_api.models.model_price_tier import ModelPriceTier

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPriceTier from a JSON string
model_price_tier_instance = ModelPriceTier.from_json(json)
# print the JSON string representation of the object
print ModelPriceTier.to_json()

# convert the object into a dict
model_price_tier_dict = model_price_tier_instance.to_dict()
# create an instance of ModelPriceTier from a dict
model_price_tier_form_dict = model_price_tier.from_dict(model_price_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


