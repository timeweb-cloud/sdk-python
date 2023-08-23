# AddCountries


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **object** | Страна. | 
**status** | **object** | Результат добавления страны. | 

## Example

```python
from timeweb_cloud_api.models.add_countries import AddCountries

# TODO update the JSON string below
json = "{}"
# create an instance of AddCountries from a JSON string
add_countries_instance = AddCountries.from_json(json)
# print the JSON string representation of the object
print AddCountries.to_json()

# convert the object into a dict
add_countries_dict = add_countries_instance.to_dict()
# create an instance of AddCountries from a dict
add_countries_form_dict = add_countries.from_dict(add_countries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


