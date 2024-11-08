# apivideo.SummariesApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](SummariesApi.md#create) | **POST** /summaries | Generate video summary
[**update**](SummariesApi.md#update) | **PATCH** /summaries/{summaryId}/source | Update summary details
[**delete**](SummariesApi.md#delete) | **DELETE** /summaries/{summaryId} | Delete video summary
[**list**](SummariesApi.md#list) | **GET** /summaries | List summaries
[**get_summary_source**](SummariesApi.md#get_summary_source) | **GET** /summaries/{summaryId}/source | Get summary details


# **create**
> Summary create(summary_creation_payload)

Generate video summary

Generate an abstract and key takeaways for a video.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.conflict_error import ConflictError
from apivideo.model.summary_creation_payload import SummaryCreationPayload
from apivideo.model.summary import Summary
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_creation_payload = SummaryCreationPayload(
        video_id="vi4k0jvEUuaTdRAEjQ4Jfrgz",
        origin="auto",
        attributes=[
            "abstract",
        ],
    ) # SummaryCreationPayload | 

    # example passing only required values which don't have defaults set
    try:
        # Generate video summary
        api_response = api_instance.create(summary_creation_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_creation_payload** | [**SummaryCreationPayload**](SummaryCreationPayload.md)|  |

### Return type

[**Summary**](Summary.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**409** | Conflict |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SummarySource update(summary_id, summary_update_payload)

Update summary details

Update details for a summary.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.conflict_error import ConflictError
from apivideo.model.summary_source import SummarySource
from apivideo.model.summary_update_payload import SummaryUpdatePayload
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_id = "summary_1CGHWuXjhxmeH4WiZ51234" # str | The unique identifier of the summary source you want to update.
    summary_update_payload = SummaryUpdatePayload(
        abstract="In this lecture, we discuss how complicated quantum theory is, using the famous example of Schrödingers cat. We also discuss practical applications like quantum computing.",
        takeaways=["Quantum theory is complicated.","Schrödinger's cat is neither dead, nor alive.","Quantum computers are super cool."],
    ) # SummaryUpdatePayload | 

    # example passing only required values which don't have defaults set
    try:
        # Update summary details
        api_response = api_instance.update(summary_id, summary_update_payload)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_id** | **str**| The unique identifier of the summary source you want to update. |
 **summary_update_payload** | [**SummaryUpdatePayload**](SummaryUpdatePayload.md)|  |

### Return type

[**SummarySource**](SummarySource.md)


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**409** | Conflict |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(summary_id)

Delete video summary

Delete a summary tied to a video.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_id = "summary_1CGHWuXjhxmeH4WiZ51234" # str | The unique identifier of the summary you want to delete.

    # example passing only required values which don't have defaults set
    try:
        # Delete video summary
        api_instance.delete(summary_id)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_id** | **str**| The unique identifier of the summary you want to delete. |

### Return type

void (empty response body)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> SummariesListResponse list()

List summaries

List all summarries for your videos in a project.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.summaries_list_response import SummariesListResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    video_id = "vilkR8K3N7yrRcxcMt91234" # str | Use this parameter to filter for a summary that belongs to a specific video. (optional)
    origin = "auto" # str | Use this parameter to filter for summaries based on the way they were created: automatically or manually via the API. (optional)
    source_status = "auto" # str | Use this parameter to filter for summaries based on the current status of the summary source.  These are the available statuses:  `missing`: the input for a summary is not present. `waiting` : the input video is being processed and a summary will be generated. `failed`: a technical issue prevented summary generation. `completed`: the summary is generated. `unprocessable`: the API rules the source video to be unsuitable for summary generation. An example for this is an input video that has no audio.  (optional)
    sort_by = "createdAt" # str | Use this parameter to choose which field the API will use to sort the response data. The default is `value`.  These are the available fields to sort by:  - `createdAt`: Sorts the results based on date and timestamps when summaries were created. - `updatedAt`: Sorts the results based on date and timestamps when summaries were last updated. - `videoId`: Sorts the results based on video IDs.  (optional)
    sort_order = "asc" # str | Use this parameter to sort results. `asc` is ascending and sorts from A to Z. `desc` is descending and sorts from Z to A. (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List summaries
        api_response = api_instance.list(video_id=video_id, origin=origin, source_status=source_status, sort_by=sort_by, sort_order=sort_order, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| Use this parameter to filter for a summary that belongs to a specific video. | [optional]
 **origin** | **str**| Use this parameter to filter for summaries based on the way they were created: automatically or manually via the API. | [optional]
 **source_status** | **str**| Use this parameter to filter for summaries based on the current status of the summary source.  These are the available statuses:  &#x60;missing&#x60;: the input for a summary is not present. &#x60;waiting&#x60; : the input video is being processed and a summary will be generated. &#x60;failed&#x60;: a technical issue prevented summary generation. &#x60;completed&#x60;: the summary is generated. &#x60;unprocessable&#x60;: the API rules the source video to be unsuitable for summary generation. An example for this is an input video that has no audio.  | [optional]
 **sort_by** | **str**| Use this parameter to choose which field the API will use to sort the response data. The default is &#x60;value&#x60;.  These are the available fields to sort by:  - &#x60;createdAt&#x60;: Sorts the results based on date and timestamps when summaries were created. - &#x60;updatedAt&#x60;: Sorts the results based on date and timestamps when summaries were last updated. - &#x60;videoId&#x60;: Sorts the results based on video IDs.  | [optional]
 **sort_order** | **str**| Use this parameter to sort results. &#x60;asc&#x60; is ascending and sorts from A to Z. &#x60;desc&#x60; is descending and sorts from Z to A. | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**SummariesListResponse**](SummariesListResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_source**
> SummarySource get_summary_source(summary_id)

Get summary details

Get all details for a summary.

### Example

```python
import apivideo
from apivideo.api import summaries_api
from apivideo.model.summary_source import SummarySource
from apivideo.model.not_found import NotFound
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = summaries_api.SummariesApi(api_client)
    summary_id = "summary_1CGHWuXjhxmeH4WiZ51234" # str | The unique identifier of the summary source you want to retrieve.

    # example passing only required values which don't have defaults set
    try:
        # Get summary details
        api_response = api_instance.get_summary_source(summary_id)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling SummariesApi->get_summary_source: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summary_id** | **str**| The unique identifier of the summary source you want to retrieve. |

### Return type

[**SummarySource**](SummarySource.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Not Found |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

