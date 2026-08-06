# ConfigRobots

Настройки robots.txt для доменов ресурса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Режим отдачи &#x60;robots.txt&#x60;. - &#x60;deny&#x60; — CDN отдает &#x60;robots.txt&#x60;, запрещающий индексацию; - &#x60;cached&#x60; — &#x60;robots.txt&#x60; берется с источника контента; - &#x60;custom&#x60; — CDN отдает содержимое из поля &#x60;content&#x60;. | 
**content** | **object** | Содержимое &#x60;robots.txt&#x60;. Обязательно и учитывается только при &#x60;type&#x60; &#x3D; &#x60;custom&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_robots import ConfigRobots

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigRobots from a JSON string
config_robots_instance = ConfigRobots.from_json(json)
# print the JSON string representation of the object
print ConfigRobots.to_json()

# convert the object into a dict
config_robots_dict = config_robots_instance.to_dict()
# create an instance of ConfigRobots from a dict
config_robots_form_dict = config_robots.from_dict(config_robots_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


