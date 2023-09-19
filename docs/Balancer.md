# Balancer

Балансировщик

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра балансировщика. Автоматически генерируется при создании. | 
**algo** | **object** | Алгоритм переключений балансировщика. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был создан балансировщик. | 
**fall** | **object** | Порог количества ошибок. | 
**inter** | **object** | Интервал проверки. | 
**ip** | **object** | IP-адрес сетевого интерфейса IPv4. | 
**local_ip** | **object** | Локальный IP-адрес сетевого интерфейса IPv4. | 
**is_keepalive** | **object** | Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности. | 
**name** | **object** | Удобочитаемое имя, установленное для балансировщика. | 
**path** | **object** | Адрес балансировщика. | 
**port** | **object** | Порт балансировщика. | 
**proto** | **object** | Протокол. | 
**rise** | **object** | Порог количества успешных ответов. | 
**preset_id** | **object** | Идентификатор тарифа. | 
**is_ssl** | **object** | Это логическое значение, которое показывает, требуется ли перенаправление на SSL. | 
**status** | **object** | Статус балансировщика. | 
**is_sticky** | **object** | Это логическое значение, которое показывает, сохраняется ли сессия. | 
**timeout** | **object** | Таймаут ответа балансировщика. | 
**is_use_proxy** | **object** | Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси. | 
**rules** | **object** |  | 
**ips** | **object** | Список IP-адресов, привязанных к балансировщику | 
**location** | **object** | Географическое расположение балансировщика | 

## Example

```python
from timeweb_cloud_api.models.balancer import Balancer

# TODO update the JSON string below
json = "{}"
# create an instance of Balancer from a JSON string
balancer_instance = Balancer.from_json(json)
# print the JSON string representation of the object
print Balancer.to_json()

# convert the object into a dict
balancer_dict = balancer_instance.to_dict()
# create an instance of Balancer from a dict
balancer_form_dict = balancer.from_dict(balancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


