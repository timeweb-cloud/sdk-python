# Invoice

Оплата заявки на продление/регистрацию домена при помощи платежной системы

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**money_source** | **object** | Тип создаваемой заявки. | 
**person_id** | **object** | ID администратора, на которого зарегистрирован домен. | [optional] 
**payment_type** | **object** | Тип платежной системы. | 
**payer_id** | **object** | Идентификационный номер плательщика | 

## Example

```python
from timeweb_cloud_api.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print Invoice.to_json()

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_form_dict = invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


