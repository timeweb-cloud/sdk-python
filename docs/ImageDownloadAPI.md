# ImageDownloadAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор ссылки | 
**created_at** | **object** | Дата и время создания ссылки | 
**image** | **object** | Идентификатор образа | 
**type** | [**URLType**](URLType.md) |  | 
**url** | **object** | Ссылка на скачивание | [optional] 
**status** | [**UrlStatus**](UrlStatus.md) |  | 
**progress** | **object** | Прогресс загрузки образа | 

## Example

```python
from timeweb_cloud_api.models.image_download_api import ImageDownloadAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDownloadAPI from a JSON string
image_download_api_instance = ImageDownloadAPI.from_json(json)
# print the JSON string representation of the object
print ImageDownloadAPI.to_json()

# convert the object into a dict
image_download_api_dict = image_download_api_instance.to_dict()
# create an instance of ImageDownloadAPI from a dict
image_download_api_form_dict = image_download_api.from_dict(image_download_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


