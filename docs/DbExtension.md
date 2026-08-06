# DbExtension

Расширение базы данных. Для кластеров PostgreSQL доступны расширения PostgreSQL, для кластеров RabbitMQ — плагины RabbitMQ. Если расширение не подходит типу кластера, вернется ошибка `invalid_extension`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from timeweb_cloud_api.models.db_extension import DbExtension

# TODO update the JSON string below
json = "{}"
# create an instance of DbExtension from a JSON string
db_extension_instance = DbExtension.from_json(json)
# print the JSON string representation of the object
print DbExtension.to_json()

# convert the object into a dict
db_extension_dict = db_extension_instance.to_dict()
# create an instance of DbExtension from a dict
db_extension_form_dict = db_extension.from_dict(db_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


