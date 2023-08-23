# Status

Статус аккаунта

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_blocked** | **object** | Это логическое значение, которое показывает, заблокирован ли аккаунт. | 
**is_permanent_blocked** | **object** | Это логическое значение, которое показывает, заблокирован ли аккаунт навсегда. | 
**is_send_bill_letters** | **object** | Это логическое значение, которое показывает, требуется ли отправлять счета на почту. | 
**company_info** | [**StatusCompanyInfo**](StatusCompanyInfo.md) |  | 
**last_password_changed_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда последний раз изменялся пароль. | 
**ym_client_id** | **object** | Идентификатор аккаунта для яндекс метрики. | 

## Example

```python
from timeweb_cloud_api.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print Status.to_json()

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_form_dict = status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


