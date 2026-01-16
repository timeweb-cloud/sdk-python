# CreateDomainMailboxV2Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailbox** | **object** | Название почтового ящика | 
**password** | **object** | Пароль почтового ящика | 
**comment** | **object** | Комментарий почтового ящика | [optional] 
**owner_full_name** | **object** | ФИО владельца почтового ящика | [optional] 
**filter_status** | **object** | Статус фильтрации почты | [optional] 
**filter_action** | **object** | Что делать с письмами, которые попадают в спам. \\  Параметры: \\  &#x60;directory&#x60; - переместить в папку спам; \\  &#x60;label&#x60; - пометить письмо; \\  Если передан параметр &#x60;filter_status&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_domain_mailbox_v2_request import CreateDomainMailboxV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainMailboxV2Request from a JSON string
create_domain_mailbox_v2_request_instance = CreateDomainMailboxV2Request.from_json(json)
# print the JSON string representation of the object
print CreateDomainMailboxV2Request.to_json()

# convert the object into a dict
create_domain_mailbox_v2_request_dict = create_domain_mailbox_v2_request_instance.to_dict()
# create an instance of CreateDomainMailboxV2Request from a dict
create_domain_mailbox_v2_request_form_dict = create_domain_mailbox_v2_request.from_dict(create_domain_mailbox_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


