# FloatingIp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор IP. | 
**ip** | **object** | IP-адрес | 
**is_ddos_guard** | **object** | Это логическое значение, которое показывает, включена ли защита от DDoS. | 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 
**resource_type** | **object** | Тип ресурса. | 
**resource_id** | **object** | Id ресурса. | 
**comment** | **object** | Комментарий | 
**ptr** | **object** | Запись имени узла. | 

## Example

```python
from timeweb_cloud_api.models.floating_ip import FloatingIp

# TODO update the JSON string below
json = "{}"
# create an instance of FloatingIp from a JSON string
floating_ip_instance = FloatingIp.from_json(json)
# print the JSON string representation of the object
print FloatingIp.to_json()

# convert the object into a dict
floating_ip_dict = floating_ip_instance.to_dict()
# create an instance of FloatingIp from a dict
floating_ip_form_dict = floating_ip.from_dict(floating_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


