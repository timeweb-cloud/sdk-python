# ClusterOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID кластера | 
**name** | **object** | Название | 
**created_at** | **object** | Дата и время создания кластера в формате ISO8601 | 
**status** | **object** | Статус | 
**description** | **object** | Описание | 
**k8s_version** | **object** | Версия Kubernetes | 
**network_driver** | **object** | Используемый сетевой драйвер | 
**ingress** | **object** | Логическое значение, показывающее, включен ли Ingress | 
**preset_id** | **object** | ID тарифа мастер-ноды | 
**cpu** | **object** | Общее количество ядер | [optional] 
**ram** | **object** | Общее количество памяти | [optional] 
**disk** | **object** | Общее дисковое пространство | [optional] 
**availability_zone** | **object** | Зона доступности | [optional] 
**project_id** | **object** | ID проекта | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_out import ClusterOut

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOut from a JSON string
cluster_out_instance = ClusterOut.from_json(json)
# print the JSON string representation of the object
print ClusterOut.to_json()

# convert the object into a dict
cluster_out_dict = cluster_out_instance.to_dict()
# create an instance of ClusterOut from a dict
cluster_out_form_dict = cluster_out.from_dict(cluster_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


