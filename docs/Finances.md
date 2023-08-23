# Finances

Платежная информация

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **object** | Баланс аккаунта. | 
**currency** | **object** | Валюта, которая используется на аккаунте. | 
**discount_end_date_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда заканчивается скидка для аккаунта. | 
**discount_percent** | **object** | Процент скидки для аккаунта. | 
**hourly_cost** | **object** | Стоимость услуг на аккаунте в час. | 
**hourly_fee** | **object** | Абонентская плата в час (с учетом скидок). | 
**monthly_cost** | **object** | Стоимость услуг на аккаунте в месяц. | 
**monthly_fee** | **object** | Абонентская плата в месяц (с учетом скидок). | 
**total_paid** | **object** | Общая сумма платежей на аккаунте. | 
**hours_left** | **object** | Сколько часов работы услуг оплачено на аккаунте. | 
**autopay_card_info** | **object** | Информация о карте, используемой для автоплатежей. | 

## Example

```python
from openapi_client.models.finances import Finances

# TODO update the JSON string below
json = "{}"
# create an instance of Finances from a JSON string
finances_instance = Finances.from_json(json)
# print the JSON string representation of the object
print Finances.to_json()

# convert the object into a dict
finances_dict = finances_instance.to_dict()
# create an instance of Finances from a dict
finances_form_dict = finances.from_dict(finances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


