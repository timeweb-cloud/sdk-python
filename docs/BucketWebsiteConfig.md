# BucketWebsiteConfig

Позволяет разместить статический веб-сайт используя файлы бакета

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **object** | Включено ли сайтовое хранилище. | [optional] 
**index_page** | **object** | Страница сайта. | [optional] 
**error_pages** | **object** | Страницы ошибок. | [optional] 

## Example

```python
from timeweb_cloud_api.models.bucket_website_config import BucketWebsiteConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BucketWebsiteConfig from a JSON string
bucket_website_config_instance = BucketWebsiteConfig.from_json(json)
# print the JSON string representation of the object
print BucketWebsiteConfig.to_json()

# convert the object into a dict
bucket_website_config_dict = bucket_website_config_instance.to_dict()
# create an instance of BucketWebsiteConfig from a dict
bucket_website_config_form_dict = bucket_website_config.from_dict(bucket_website_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


