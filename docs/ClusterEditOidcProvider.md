# ClusterEditOidcProvider

OIDC-провайдер

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название создаваемого подключения. Используется только для идентификации и не влияет на остальные параметры | 
**issuer_url** | **object** | Адрес OIDC-провайдера, используемый для аутентификации пользователей, запрашивающих доступ к кластеру | 
**client_id** | **object** | Идентификатор сервиса, выданный OIDC-провайдером, от имени которого осуществляется запрос к ресурсам | 
**username_claim** | **object** | Поле в JSON Web Token (JWT), используемое для идентификации пользователя | [optional] 
**groups_claim** | **object** | Поле в JSON Web Token (JWT), содержащее названии группы, к которой принадлежит пользователь | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_edit_oidc_provider import ClusterEditOidcProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEditOidcProvider from a JSON string
cluster_edit_oidc_provider_instance = ClusterEditOidcProvider.from_json(json)
# print the JSON string representation of the object
print ClusterEditOidcProvider.to_json()

# convert the object into a dict
cluster_edit_oidc_provider_dict = cluster_edit_oidc_provider_instance.to_dict()
# create an instance of ClusterEditOidcProvider from a dict
cluster_edit_oidc_provider_form_dict = cluster_edit_oidc_provider.from_dict(cluster_edit_oidc_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


