# Clusterk8s

Кластер

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра кластера. Автоматически генерируется при создании. | 
**name** | **object** | Удобочитаемое имя, установленное для кластера. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан кластер. | 
**status** | **object** | Статус кластера. | 
**description** | **object** | Описание кластера. | 
**ha** | **object** | Описание появится позднее. | 
**k8s_version** | **object** | Версия k8s. | 
**network_driver** | **object** | Описание появится позднее. | 
**ingress** | **object** | Описание появится позднее. | 
**cpu** | **object** | Количество ядер процессора кластера. | 
**ram** | **object** | Количество (в Мб) оперативной памяти кластера. | 
**disk** | **object** | Размер (в Гб) диска кластера. | 
**preset_id** | **object** | Тип сервиса кластера. | 

## Example

```python
from timeweb_cloud_api.models.clusterk8s import Clusterk8s

# TODO update the JSON string below
json = "{}"
# create an instance of Clusterk8s from a JSON string
clusterk8s_instance = Clusterk8s.from_json(json)
# print the JSON string representation of the object
print Clusterk8s.to_json()

# convert the object into a dict
clusterk8s_dict = clusterk8s_instance.to_dict()
# create an instance of Clusterk8s from a dict
clusterk8s_form_dict = clusterk8s.from_dict(clusterk8s_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


