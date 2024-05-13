# timeweb_cloud_api.LocationsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_locations**](LocationsApi.md#get_locations) | **GET** /api/v2/locations | Получение списка локаций


# **get_locations**
> GetLocations200Response get_locations()

Получение списка локаций

Чтобы получить список локаций, отправьте GET-запрос на `/api/v2/locations`.   Тело ответа будет представлять собой объект JSON с ключом `locations`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_locations200_response import GetLocations200Response
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
    api_instance = timeweb_cloud_api.LocationsApi(api_client)

    try:
        # Получение списка локаций
        api_response = api_instance.get_locations()
        print("The response of LocationsApi->get_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLocations200Response**](GetLocations200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;locations&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

