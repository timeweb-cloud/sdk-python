# ImageDownload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ссылки. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана ссылка. | 
**image** | **object** | ID образа. | 
**type** | [**URLType**](URLType.md) |  | 
**url** | **object** | Ссылка на скачивание. | [optional] 
**status** | [**UrlStatus**](UrlStatus.md) |  | 
**progress** | **object** | Прогресс загрузки образа. | 

## Example

```python
from timeweb_cloud_api.models.image_download import ImageDownload

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDownload from a JSON string
image_download_instance = ImageDownload.from_json(json)
# print the JSON string representation of the object
print ImageDownload.to_json()

# convert the object into a dict
image_download_dict = image_download_instance.to_dict()
# create an instance of ImageDownload from a dict
image_download_form_dict = image_download.from_dict(image_download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


