# UpdateMailQuotaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **object** | Общее количество места на почте (в Мб). | 

## Example

```python
from timeweb_cloud_api.models.update_mail_quota_request import UpdateMailQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailQuotaRequest from a JSON string
update_mail_quota_request_instance = UpdateMailQuotaRequest.from_json(json)
# print the JSON string representation of the object
print UpdateMailQuotaRequest.to_json()

# convert the object into a dict
update_mail_quota_request_dict = update_mail_quota_request_instance.to_dict()
# create an instance of UpdateMailQuotaRequest from a dict
update_mail_quota_request_form_dict = update_mail_quota_request.from_dict(update_mail_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


