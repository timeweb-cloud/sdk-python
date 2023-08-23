# NodeOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор ноды | 
**created_at** | **object** | Дата и время создания ноды в формате ISO8601 | 
**type** | **object** | Тип ноды | 
**group_id** | **object** | Идентификатор группы нод | 
**status** | **object** | Статус | 
**preset_id** | **object** | Идентификатор тарифа ноды | 
**cpu** | **object** | Количество ядер | 
**ram** | **object** | Количество памяти | 
**disk** | **object** | Количество пространства | 
**network** | **object** | Пропускная способность сети | 

## Example

```python
from timeweb_cloud_api.models.node_out import NodeOut

# TODO update the JSON string below
json = "{}"
# create an instance of NodeOut from a JSON string
node_out_instance = NodeOut.from_json(json)
# print the JSON string representation of the object
print NodeOut.to_json()

# convert the object into a dict
node_out_dict = node_out_instance.to_dict()
# create an instance of NodeOut from a dict
node_out_form_dict = node_out.from_dict(node_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


