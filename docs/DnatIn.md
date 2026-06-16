# DnatIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **object** | Протокол | 
**local** | [**DnatInLocal**](DnatInLocal.md) |  | 
**public** | [**DnatInPublic**](DnatInPublic.md) |  | 

## Example

```python
from timeweb_cloud_api.models.dnat_in import DnatIn

# TODO update the JSON string below
json = "{}"
# create an instance of DnatIn from a JSON string
dnat_in_instance = DnatIn.from_json(json)
# print the JSON string representation of the object
print DnatIn.to_json()

# convert the object into a dict
dnat_in_dict = dnat_in_instance.to_dict()
# create an instance of DnatIn from a dict
dnat_in_form_dict = dnat_in.from_dict(dnat_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


