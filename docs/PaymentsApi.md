# timeweb_cloud_api.PaymentsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_finances**](PaymentsApi.md#get_finances) | **GET** /api/v1/account/finances | Получение платежной информации
[**get_service_prices**](PaymentsApi.md#get_service_prices) | **GET** /api/v1/account/services/cost | Получение стоимости сервисов


# **get_finances**
> GetFinances200Response get_finances()

Получение платежной информации

Чтобы получить платежную информацию, отправьте GET-запрос на `/api/v1/account/finances`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_finances200_response import GetFinances200Response
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.PaymentsApi(api_client)

    try:
        # Получение платежной информации
        api_response = api_instance.get_finances()
        print("The response of PaymentsApi->get_finances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_finances: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFinances200Response**](GetFinances200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;finances&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_prices**
> GetServicePrices200Response get_service_prices()

Получение стоимости сервисов

Чтобы получить информацию о стоимости всех активных сервисов аккаунта, отправьте GET-запрос на `/api/v1/account/services/cost`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_service_prices200_response import GetServicePrices200Response
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.PaymentsApi(api_client)

    try:
        # Получение стоимости сервисов
        api_response = api_instance.get_service_prices()
        print("The response of PaymentsApi->get_service_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentsApi->get_service_prices: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetServicePrices200Response**](GetServicePrices200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON с ключом &#x60;services_costs&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

