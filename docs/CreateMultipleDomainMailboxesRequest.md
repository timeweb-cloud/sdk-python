# CreateMultipleDomainMailboxesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailboxes** | **object** | Массив объектов с данными почтовых ящиков | 

## Example

```python
from timeweb_cloud_api.models.create_multiple_domain_mailboxes_request import CreateMultipleDomainMailboxesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMultipleDomainMailboxesRequest from a JSON string
create_multiple_domain_mailboxes_request_instance = CreateMultipleDomainMailboxesRequest.from_json(json)
# print the JSON string representation of the object
print CreateMultipleDomainMailboxesRequest.to_json()

# convert the object into a dict
create_multiple_domain_mailboxes_request_dict = create_multiple_domain_mailboxes_request_instance.to_dict()
# create an instance of CreateMultipleDomainMailboxesRequest from a dict
create_multiple_domain_mailboxes_request_form_dict = create_multiple_domain_mailboxes_request.from_dict(create_multiple_domain_mailboxes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


