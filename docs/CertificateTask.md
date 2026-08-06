# CertificateTask

Задача на выпуск сертификата Let's Encrypt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID задачи на выпуск сертификата. | 
**status** | **object** | Статус выпуска сертификата. - &#x60;in_progress&#x60; — сертификат выпускается; - &#x60;success&#x60; — сертификат выпущен и привязан к ресурсу; - &#x60;failed&#x60; — выпустить сертификат не удалось. | 
**domains** | **object** | Доменные имена, для которых выпускается сертификат. | 
**resource_id** | **object** | ID CDN-ресурса, для которого выпускается сертификат. | 

## Example

```python
from timeweb_cloud_api.models.certificate_task import CertificateTask

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateTask from a JSON string
certificate_task_instance = CertificateTask.from_json(json)
# print the JSON string representation of the object
print CertificateTask.to_json()

# convert the object into a dict
certificate_task_dict = certificate_task_instance.to_dict()
# create an instance of CertificateTask from a dict
certificate_task_form_dict = certificate_task.from_dict(certificate_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


