# CreateVpc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя сети. | 
**subnet_v4** | **object** | Маска подсети. | 
**location** | **object** | Локация сети. | 
**description** | **object** | Описание. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_vpc import CreateVpc

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVpc from a JSON string
create_vpc_instance = CreateVpc.from_json(json)
# print the JSON string representation of the object
print CreateVpc.to_json()

# convert the object into a dict
create_vpc_dict = create_vpc_instance.to_dict()
# create an instance of CreateVpc from a dict
create_vpc_form_dict = create_vpc.from_dict(create_vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


