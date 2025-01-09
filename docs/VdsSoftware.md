# VdsSoftware

ПО из маркетплейса.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ПО из маркетплейса. | [optional] 
**name** | **object** | Название ПО из маркетплейса. | [optional] 

## Example

```python
from timeweb_cloud_api.models.vds_software import VdsSoftware

# TODO update the JSON string below
json = "{}"
# create an instance of VdsSoftware from a JSON string
vds_software_instance = VdsSoftware.from_json(json)
# print the JSON string representation of the object
print VdsSoftware.to_json()

# convert the object into a dict
vds_software_dict = vds_software_instance.to_dict()
# create an instance of VdsSoftware from a dict
vds_software_form_dict = vds_software.from_dict(vds_software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


