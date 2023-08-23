# CreateDomainMailboxRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox** | **object** | Название почтового ящика | 
**password** | **object** | Пароль почтового ящика | 
**comment** | **object** | Комментарий почтового ящика | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_domain_mailbox_request import CreateDomainMailboxRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainMailboxRequest from a JSON string
create_domain_mailbox_request_instance = CreateDomainMailboxRequest.from_json(json)
# print the JSON string representation of the object
print CreateDomainMailboxRequest.to_json()

# convert the object into a dict
create_domain_mailbox_request_dict = create_domain_mailbox_request_instance.to_dict()
# create an instance of CreateDomainMailboxRequest from a dict
create_domain_mailbox_request_form_dict = create_domain_mailbox_request.from_dict(create_domain_mailbox_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


