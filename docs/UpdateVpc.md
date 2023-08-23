# UpdateVpc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя сети. | [optional] 
**description** | **object** | Описание. | [optional] 

## Example

```python
from openapi_client.models.update_vpc import UpdateVpc

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVpc from a JSON string
update_vpc_instance = UpdateVpc.from_json(json)
# print the JSON string representation of the object
print UpdateVpc.to_json()

# convert the object into a dict
update_vpc_dict = update_vpc_instance.to_dict()
# create an instance of UpdateVpc from a dict
update_vpc_form_dict = update_vpc.from_dict(update_vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


