# GetCdnCertificateTasks200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_tasks** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_cdn_certificate_tasks200_response import GetCdnCertificateTasks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdnCertificateTasks200Response from a JSON string
get_cdn_certificate_tasks200_response_instance = GetCdnCertificateTasks200Response.from_json(json)
# print the JSON string representation of the object
print GetCdnCertificateTasks200Response.to_json()

# convert the object into a dict
get_cdn_certificate_tasks200_response_dict = get_cdn_certificate_tasks200_response_instance.to_dict()
# create an instance of GetCdnCertificateTasks200Response from a dict
get_cdn_certificate_tasks200_response_form_dict = get_cdn_certificate_tasks200_response.from_dict(get_cdn_certificate_tasks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


