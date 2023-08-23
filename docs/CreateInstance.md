# CreateInstance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название инстанса базы данных | 
**description** | **object** | Описанеие инстанса базы данных | [optional] 

## Example

```python
from openapi_client.models.create_instance import CreateInstance

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstance from a JSON string
create_instance_instance = CreateInstance.from_json(json)
# print the JSON string representation of the object
print CreateInstance.to_json()

# convert the object into a dict
create_instance_dict = create_instance_instance.to_dict()
# create an instance of CreateInstance from a dict
create_instance_form_dict = create_instance.from_dict(create_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


