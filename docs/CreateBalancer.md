# CreateBalancer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Удобочитаемое имя, установленное для балансировщика. | 
**algo** | **object** | Алгоритм переключений балансировщика. | 
**is_sticky** | **object** | Это логическое значение, которое показывает, сохраняется ли сессия. | 
**is_use_proxy** | **object** | Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси. | 
**is_ssl** | **object** | Это логическое значение, которое показывает, требуется ли перенаправление на SSL. | 
**is_keepalive** | **object** | Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности. | 
**proto** | **object** | Протокол. | 
**port** | **object** | Порт балансировщика. | 
**path** | **object** | Адрес балансировщика. | 
**inter** | **object** | Интервал проверки. | 
**timeout** | **object** | Таймаут ответа балансировщика. | 
**fall** | **object** | Порог количества ошибок. | 
**rise** | **object** | Порог количества успешных ответов. | 
**preset_id** | **object** | Идентификатор тарифа. | 
**network** | [**Network**](Network.md) |  | [optional] 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_balancer import CreateBalancer

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBalancer from a JSON string
create_balancer_instance = CreateBalancer.from_json(json)
# print the JSON string representation of the object
print CreateBalancer.to_json()

# convert the object into a dict
create_balancer_dict = create_balancer_instance.to_dict()
# create an instance of CreateBalancer from a dict
create_balancer_form_dict = create_balancer.from_dict(create_balancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


