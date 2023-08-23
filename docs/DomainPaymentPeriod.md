# DomainPaymentPeriod

Период оплаты (для доменов в зонах .ru и .рф только 1-3 года).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.domain_payment_period import DomainPaymentPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of DomainPaymentPeriod from a JSON string
domain_payment_period_instance = DomainPaymentPeriod.from_json(json)
# print the JSON string representation of the object
print DomainPaymentPeriod.to_json()

# convert the object into a dict
domain_payment_period_dict = domain_payment_period_instance.to_dict()
# create an instance of DomainPaymentPeriod from a dict
domain_payment_period_form_dict = domain_payment_period.from_dict(domain_payment_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


