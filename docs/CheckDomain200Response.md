# CheckDomain200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_domain_available** | **object** | Это логическое значение, которое показывает, доступен ли домен для регистрации. | 

## Example

```python
from timeweb_cloud_api.models.check_domain200_response import CheckDomain200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDomain200Response from a JSON string
check_domain200_response_instance = CheckDomain200Response.from_json(json)
# print the JSON string representation of the object
print CheckDomain200Response.to_json()

# convert the object into a dict
check_domain200_response_dict = check_domain200_response_instance.to_dict()
# create an instance of CheckDomain200Response from a dict
check_domain200_response_form_dict = check_domain200_response.from_dict(check_domain200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


