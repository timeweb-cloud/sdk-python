# CreatePayment

Данные для создания платежа

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **object** | Сумма оплаты | 
**payment_type** | [**PaymentType**](PaymentType.md) |  | 
**is_bind_card** | **object** | Привязать карту | [optional] 
**return_url** | **object** | URL для перенаправления после успешной оплаты | [optional] 
**fail_url** | **object** | URL для перенаправления после неудачной оплаты | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_payment import CreatePayment

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePayment from a JSON string
create_payment_instance = CreatePayment.from_json(json)
# print the JSON string representation of the object
print CreatePayment.to_json()

# convert the object into a dict
create_payment_dict = create_payment_instance.to_dict()
# create an instance of CreatePayment from a dict
create_payment_form_dict = create_payment.from_dict(create_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


