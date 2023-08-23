# ImageOutAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор образа | 
**status** | [**ImageStatus**](ImageStatus.md) |  | 
**created_at** | **object** | Дата и время создания | 
**deleted_at** | **object** | Дата и время удаления | 
**size** | **object** | Размер в мегабайтах | 
**name** | **object** | Имя образа | 
**description** | **object** | Описание образа | 
**disk_id** | **object** | Идентификатор связанного с образом диска | 
**location** | **object** | Локация, в которой создан образ | [optional] 
**os** | [**OS**](OS.md) |  | 
**progress** | **object** | Процент создания образа | 
**is_custom** | **object** | Признак указывающий на то является ли образ кастомным | 

## Example

```python
from timeweb_cloud_api.models.image_out_api import ImageOutAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOutAPI from a JSON string
image_out_api_instance = ImageOutAPI.from_json(json)
# print the JSON string representation of the object
print ImageOutAPI.to_json()

# convert the object into a dict
image_out_api_dict = image_out_api_instance.to_dict()
# create an instance of ImageOutAPI from a dict
image_out_api_form_dict = image_out_api.from_dict(image_out_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


