# AddTokenPackage

Данные для добавления дополнительного пакета токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** | Количество пакетов для добавления (от 1 до 100) | [optional] 

## Example

```python
from timeweb_cloud_api.models.add_token_package import AddTokenPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AddTokenPackage from a JSON string
add_token_package_instance = AddTokenPackage.from_json(json)
# print the JSON string representation of the object
print AddTokenPackage.to_json()

# convert the object into a dict
add_token_package_dict = add_token_package_instance.to_dict()
# create an instance of AddTokenPackage from a dict
add_token_package_form_dict = add_token_package.from_dict(add_token_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


