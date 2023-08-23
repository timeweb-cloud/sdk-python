# BucketDiskStats

Статистика использования диска хранилища.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Размер (в Кб) диска хранилища. | 
**used** | **object** | Размер (в Кб) использованного пространства диска хранилища. | 

## Example

```python
from openapi_client.models.bucket_disk_stats import BucketDiskStats

# TODO update the JSON string below
json = "{}"
# create an instance of BucketDiskStats from a JSON string
bucket_disk_stats_instance = BucketDiskStats.from_json(json)
# print the JSON string representation of the object
print BucketDiskStats.to_json()

# convert the object into a dict
bucket_disk_stats_dict = bucket_disk_stats_instance.to_dict()
# create an instance of BucketDiskStats from a dict
bucket_disk_stats_form_dict = bucket_disk_stats.from_dict(bucket_disk_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


