# ToolPrice

Цена системного инструмента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID шаблона инструмента | 
**name** | **object** | Название инструмента | 
**cost** | **object** | Цена за единицу использования инструмента: в рублях для &#x60;locale&#x3D;ru&#x60;, в долларах США для &#x60;locale&#x3D;en&#x60; | 

## Example

```python
from timeweb_cloud_api.models.tool_price import ToolPrice

# TODO update the JSON string below
json = "{}"
# create an instance of ToolPrice from a JSON string
tool_price_instance = ToolPrice.from_json(json)
# print the JSON string representation of the object
print ToolPrice.to_json()

# convert the object into a dict
tool_price_dict = tool_price_instance.to_dict()
# create an instance of ToolPrice from a dict
tool_price_form_dict = tool_price.from_dict(tool_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


