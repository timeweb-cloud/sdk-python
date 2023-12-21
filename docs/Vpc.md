# Vpc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор сети. | 
**name** | **object** | Имя сети. | 
**subnet_v4** | **object** | Маска подсети. | 
**location** | **object** | Локация сети. | 
**created_at** | **object** | Дата создания сети. | 
**description** | **object** | Описание. | [optional] 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 

## Example

```python
from timeweb_cloud_api.models.vpc import Vpc

# TODO update the JSON string below
json = "{}"
# create an instance of Vpc from a JSON string
vpc_instance = Vpc.from_json(json)
# print the JSON string representation of the object
print Vpc.to_json()

# convert the object into a dict
vpc_dict = vpc_instance.to_dict()
# create an instance of Vpc from a dict
vpc_form_dict = vpc.from_dict(vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


