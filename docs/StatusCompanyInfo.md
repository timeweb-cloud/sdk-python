# StatusCompanyInfo

Информация о компании.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID компании. | 
**name** | **object** | Название компании. | 

## Example

```python
from timeweb_cloud_api.models.status_company_info import StatusCompanyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StatusCompanyInfo from a JSON string
status_company_info_instance = StatusCompanyInfo.from_json(json)
# print the JSON string representation of the object
print StatusCompanyInfo.to_json()

# convert the object into a dict
status_company_info_dict = status_company_info_instance.to_dict()
# create an instance of StatusCompanyInfo from a dict
status_company_info_form_dict = status_company_info.from_dict(status_company_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


