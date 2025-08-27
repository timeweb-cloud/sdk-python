# Bucket

Хранилище S3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра хранилища. Автоматически генерируется при создании. | 
**name** | **object** | Удобочитаемое имя, установленное для хранилища. | 
**description** | **object** | Комментарий к хранилищу. | [optional] 
**disk_stats** | [**BucketDiskStats**](BucketDiskStats.md) |  | 
**type** | **object** | Тип хранилища. | 
**preset_id** | **object** | ID тарифа хранилища. | 
**configurator_id** | **object** | ID конфигуратора хранилища. | 
**avatar_link** | **object** | Ссылка на аватар хранилища. | 
**status** | **object** | Статус хранилища. | 
**object_amount** | **object** | Количество файлов в хранилище. | 
**location** | **object** | Регион хранилища. | 
**hostname** | **object** | Адрес хранилища для подключения. | 
**access_key** | **object** | Ключ доступа от хранилища. | 
**secret_key** | **object** | Секретный ключ доступа от хранилища. | 
**moved_in_quarantine_at** | **object** | Дата перемещения в карантин. | 
**storage_class** | **object** | Класс хранилища. | 
**project_id** | **object** | ID проекта. | 
**rate_id** | **object** | ID тарифа. | 
**website_config** | [**BucketWebsiteConfig**](BucketWebsiteConfig.md) |  | 

## Example

```python
from timeweb_cloud_api.models.bucket import Bucket

# TODO update the JSON string below
json = "{}"
# create an instance of Bucket from a JSON string
bucket_instance = Bucket.from_json(json)
# print the JSON string representation of the object
print Bucket.to_json()

# convert the object into a dict
bucket_dict = bucket_instance.to_dict()
# create an instance of Bucket from a dict
bucket_form_dict = bucket.from_dict(bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


