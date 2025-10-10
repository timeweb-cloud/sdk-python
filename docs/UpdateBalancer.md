# UpdateBalancer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Удобочитаемое имя, установленное для балансировщика. Должно быть уникальным в рамках аккаунта | [optional] 
**algo** | **object** | Алгоритм переключений балансировщика. | [optional] 
**is_sticky** | **object** | Это логическое значение, которое показывает, сохраняется ли сессия. | [optional] 
**is_use_proxy** | **object** | Это логическое значение, которое показывает, выступает ли балансировщик в качестве прокси. | [optional] 
**is_ssl** | **object** | Это логическое значение, которое показывает, требуется ли перенаправление на SSL. | [optional] 
**is_keepalive** | **object** | Это логическое значение, которое показывает, выдает ли балансировщик сигнал о проверке жизнеспособности. | [optional] 
**proto** | **object** | Протокол. | [optional] 
**port** | **object** | Порт балансировщика. | [optional] 
**path** | **object** | Адрес балансировщика. | [optional] 
**inter** | **object** | Интервал проверки. | [optional] 
**timeout** | **object** | Таймаут ответа балансировщика. | [optional] 
**fall** | **object** | Порог количества ошибок. | [optional] 
**rise** | **object** | Порог количества успешных ответов. | [optional] 
**maxconn** | **object** | Максимальное количество соединений. | [optional] 
**connect_timeout** | **object** | Таймаут подключения. | [optional] 
**client_timeout** | **object** | Таймаут клиента. | [optional] 
**server_timeout** | **object** | Таймаут сервера. | [optional] 
**httprequest_timeout** | **object** | Таймаут HTTP запроса. | [optional] 
**comment** | **object** | Комментарий к балансировщику. | [optional] 
**certificates** | [**CreateBalancerCertificates**](CreateBalancerCertificates.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_balancer import UpdateBalancer

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateBalancer from a JSON string
update_balancer_instance = UpdateBalancer.from_json(json)
# print the JSON string representation of the object
print UpdateBalancer.to_json()

# convert the object into a dict
update_balancer_dict = update_balancer_instance.to_dict()
# create an instance of UpdateBalancer from a dict
update_balancer_form_dict = update_balancer.from_dict(update_balancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


