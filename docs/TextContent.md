# TextContent

Текстовый блок результата

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип блока | 
**text** | **object** | Результат инструмента — как правило, JSON, сериализованный в строку. Для изменяющих инструментов — объект подтверждения со статусом (см. «Подтверждение изменений» в описании раздела) | 

## Example

```python
from timeweb_cloud_api.models.text_content import TextContent

# TODO update the JSON string below
json = "{}"
# create an instance of TextContent from a JSON string
text_content_instance = TextContent.from_json(json)
# print the JSON string representation of the object
print TextContent.to_json()

# convert the object into a dict
text_content_dict = text_content_instance.to_dict()
# create an instance of TextContent from a dict
text_content_form_dict = text_content.from_dict(text_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


