# DatabaseInstance

База данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра базы данных. Автоматически генерируется при создании. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**name** | **object** | Название базы данных. | 
**description** | **object** | Описание базы данных | 

## Example

```python
from openapi_client.models.database_instance import DatabaseInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInstance from a JSON string
database_instance_instance = DatabaseInstance.from_json(json)
# print the JSON string representation of the object
print DatabaseInstance.to_json()

# convert the object into a dict
database_instance_dict = database_instance_instance.to_dict()
# create an instance of DatabaseInstance from a dict
database_instance_form_dict = database_instance.from_dict(database_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


