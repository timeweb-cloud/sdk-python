# DbParametersByType

Имена параметров конфигурации, доступных для каждого типа кластера базы данных. Ключ объекта — тип кластера (значение поля `type` при создании кластера), значение — массив имён параметров, которые можно передать в `config_parameters` для кластера этого типа. Наборы параметров различаются между версиями одной СУБД. Значения параметров этот метод не возвращает — рекомендуемые значения можно получить в `GET /api/v1/dbs/default-parameters`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mysql5** | **object** | Параметры, доступные для кластеров типа &#x60;mysql5&#x60;. | 
**mysql** | **object** | Параметры, доступные для кластеров типа &#x60;mysql&#x60;. | 
**mysql8_4** | **object** | Параметры, доступные для кластеров типа &#x60;mysql8_4&#x60;. | 
**postgres** | **object** | Параметры, доступные для кластеров типа &#x60;postgres&#x60; (PostgreSQL 13). | 
**postgres14** | **object** | Параметры, доступные для кластеров типа &#x60;postgres14&#x60;. | 
**postgres15** | **object** | Параметры, доступные для кластеров типа &#x60;postgres15&#x60;. | 
**postgres16** | **object** | Параметры, доступные для кластеров типа &#x60;postgres16&#x60;. | 
**postgres17** | **object** | Параметры, доступные для кластеров типа &#x60;postgres17&#x60;. | 
**postgres18** | **object** | Параметры, доступные для кластеров типа &#x60;postgres18&#x60;. Набор отличается от предыдущих версий PostgreSQL — например, добавлены &#x60;io_method&#x60; и &#x60;io_workers&#x60;. | 
**redis** | **object** | Параметры, доступные для кластеров типа &#x60;redis&#x60;. | 
**redis7** | **object** | Параметры, доступные для кластеров типа &#x60;redis7&#x60;. | 
**redis8_1** | **object** | Параметры, доступные для кластеров типа &#x60;redis8_1&#x60;. | 
**valkey** | **object** | Параметры, доступные для кластеров типа &#x60;valkey&#x60;. | 
**valkey7** | **object** | Параметры, доступные для кластеров типа &#x60;valkey7&#x60;. | 
**valkey8_1** | **object** | Параметры, доступные для кластеров типа &#x60;valkey8_1&#x60;. | 
**valkey9_1** | **object** | Параметры, доступные для кластеров типа &#x60;valkey9_1&#x60;. | 
**mongodb4** | **object** | Для кластеров типа &#x60;mongodb4&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**mongodb** | **object** | Для кластеров типа &#x60;mongodb&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**mongodb6** | **object** | Для кластеров типа &#x60;mongodb6&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**mongodb7** | **object** | Для кластеров типа &#x60;mongodb7&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**mongodb8_0** | **object** | Для кластеров типа &#x60;mongodb8_0&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**opensearch** | **object** | Для кластеров типа &#x60;opensearch&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**opensearch2_19** | **object** | Для кластеров типа &#x60;opensearch2_19&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**clickhouse** | **object** | Для кластеров типа &#x60;clickhouse&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**clickhouse24** | **object** | Для кластеров типа &#x60;clickhouse24&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**clickhouse25** | **object** | Для кластеров типа &#x60;clickhouse25&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**kafka** | **object** | Для кластеров типа &#x60;kafka&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**rabbitmq** | **object** | Для кластеров типа &#x60;rabbitmq&#x60; настраиваемых параметров нет — всегда пустой массив. | 
**rabbitmq4_0** | **object** | Для кластеров типа &#x60;rabbitmq4_0&#x60; настраиваемых параметров нет — всегда пустой массив. | 

## Example

```python
from timeweb_cloud_api.models.db_parameters_by_type import DbParametersByType

# TODO update the JSON string below
json = "{}"
# create an instance of DbParametersByType from a JSON string
db_parameters_by_type_instance = DbParametersByType.from_json(json)
# print the JSON string representation of the object
print DbParametersByType.to_json()

# convert the object into a dict
db_parameters_by_type_dict = db_parameters_by_type_instance.to_dict()
# create an instance of DbParametersByType from a dict
db_parameters_by_type_form_dict = db_parameters_by_type.from_dict(db_parameters_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


