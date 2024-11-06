# apivideo.AnalyticsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregated_metrics**](AnalyticsApi.md#get_aggregated_metrics) | **GET** /data/metrics/{metric}/{aggregation} | Retrieve aggregated metrics
[**get_metrics_breakdown**](AnalyticsApi.md#get_metrics_breakdown) | **GET** /data/buckets/{metric}/{breakdown} | Retrieve metrics in a breakdown of dimensions
[**get_metrics_over_time**](AnalyticsApi.md#get_metrics_over_time) | **GET** /data/timeseries/{metric} | Retrieve metrics over time


# **get_aggregated_metrics**
> AnalyticsAggregatedMetricsResponse get_aggregated_metrics(metric, aggregation)

Retrieve aggregated metrics

Retrieve time-based and countable metrics like average watch time or the number of impressions over a certain period of time.

### Example

```python
import apivideo
from apivideo.api import analytics_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.unrecognized_request_url import UnrecognizedRequestUrl
from apivideo.model.filter_by2 import FilterBy2
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from apivideo.model.analytics_aggregated_metrics_response import AnalyticsAggregatedMetricsResponse
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    metric = "play" # str | Use this path parameter to select a metric that you want analytics for.  - `play` is the number of times your content has been played. You can use the aggregations `count`, `rate`, and `total` with the `play` metric. - `start` is the number of times playback was started. You can use the aggregation `count` with this metric. - `end` is the number of times playback has ended with the content watch until the end. You can use the aggregation `count` with this metric. - `impression` is the number of times your content has been loaded and was ready for playback. You can use the aggregation `count` with this metric. - `impression-time` is the time in milliseconds that your content was loading for until the first video frame is displayed. You can use the aggregations `average` and `sum` with this metric. - `watch-time` is the cumulative time in seconds that the user has spent watching your content. You can use the aggregations `average` and `sum` with this metric. - `ccv`: is the number of concurrent viewers, or users watching at the same time. - `view`: the total number of viewers until this point in time. 
    aggregation = "count" # str | Use this path parameter to define a way of collecting data for the metric that you want analytics for.  - `count` returns the overall number of events for the `play` metric. - `rate` returns the ratio that calculates the number of plays your content receives divided by its impressions. This aggregation can be used only with the `play` metric. - `total` calculates the total number of events for the `play` metric.  - `average` calculates an average value for the selected metric. - `sum` adds up the total value of the select metric. - `peak` shows the highest value of the `ccv` metric in the timeframe of your request. You can use this aggregation only with the `ccv` metric. - `live` shows the highest value of the `ccv` metric from the last 20 seconds. You can use this aggregation only with the `ccv` metric. 
    _from = dateutil_parser('2024-02-05T00:00:00+01:00') # datetime | Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for `from`, the default assigned value is 1 day ago, based on the `to` parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: `2024-02-05T00:00:00+01:00` - The API ignores this parameter when you call `/data/metrics/play/total`.  (optional)
    to = dateutil_parser('2024-02-06T00:00:00+01:00') # datetime | Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for `to`, the default assigned value is `now`. - The API ignores this parameter when you call `/data/metrics/play/total`. - The value for `to` is a non-inclusive value: the API returns data **before** the date-time that you set.  (optional)
    unique = True # bool | Use this query parameter to control how viewer data is counted:  - `true` means that a single user watching multiple times counts as 1 unique viewer - `false` means that all views count, even if from the same user.  The API accepts this parameter only when you use the `ccv` or `view` metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer's `user-agent` and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times.  (optional)
    view_duration = "5s" # str | Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter with the `view` metric. - The accepted values are `3s`, `5s`, `10s`, and `30s`.  - If you do not set this parameter, the API defaults to `5s`.  (optional)
    filter_by = {
        media_id=["vi4blUQJFrYWbaG44NChkH27"],
        media_type="video",
        continent=["EU"],
        country=["FR"],
        device_type=["computer"],
        operating_system=["windows"],
        browser=["firefox"],
        tag="Cool videos",
        referrer=["https%3A%2F%2Fmy-awesome-videos.com"],
    } # FilterBy2 | Use this parameter to filter the API's response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for `filterBy`, the API returns the full dataset for your project. - The API only accepts the `mediaId` and `mediaType` filters when you call `/data/metrics/play/total` or `/data/buckets/play-total/media-id`.  These are the available breakdown dimensions:  - `mediaId`: Returns analytics based on the unique identifiers of a video or a live stream. - `mediaType`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `EU`. Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `FR`. - `deviceType`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `tag`: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - `referrer`: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve aggregated metrics
        api_response = api_instance.get_aggregated_metrics(metric, aggregation)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_aggregated_metrics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve aggregated metrics
        api_response = api_instance.get_aggregated_metrics(metric, aggregation, _from=_from, to=to, unique=unique, view_duration=view_duration, filter_by=filter_by)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_aggregated_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| Use this path parameter to select a metric that you want analytics for.  - &#x60;play&#x60; is the number of times your content has been played. You can use the aggregations &#x60;count&#x60;, &#x60;rate&#x60;, and &#x60;total&#x60; with the &#x60;play&#x60; metric. - &#x60;start&#x60; is the number of times playback was started. You can use the aggregation &#x60;count&#x60; with this metric. - &#x60;end&#x60; is the number of times playback has ended with the content watch until the end. You can use the aggregation &#x60;count&#x60; with this metric. - &#x60;impression&#x60; is the number of times your content has been loaded and was ready for playback. You can use the aggregation &#x60;count&#x60; with this metric. - &#x60;impression-time&#x60; is the time in milliseconds that your content was loading for until the first video frame is displayed. You can use the aggregations &#x60;average&#x60; and &#x60;sum&#x60; with this metric. - &#x60;watch-time&#x60; is the cumulative time in seconds that the user has spent watching your content. You can use the aggregations &#x60;average&#x60; and &#x60;sum&#x60; with this metric. - &#x60;ccv&#x60;: is the number of concurrent viewers, or users watching at the same time. - &#x60;view&#x60;: the total number of viewers until this point in time.  |
 **aggregation** | **str**| Use this path parameter to define a way of collecting data for the metric that you want analytics for.  - &#x60;count&#x60; returns the overall number of events for the &#x60;play&#x60; metric. - &#x60;rate&#x60; returns the ratio that calculates the number of plays your content receives divided by its impressions. This aggregation can be used only with the &#x60;play&#x60; metric. - &#x60;total&#x60; calculates the total number of events for the &#x60;play&#x60; metric.  - &#x60;average&#x60; calculates an average value for the selected metric. - &#x60;sum&#x60; adds up the total value of the select metric. - &#x60;peak&#x60; shows the highest value of the &#x60;ccv&#x60; metric in the timeframe of your request. You can use this aggregation only with the &#x60;ccv&#x60; metric. - &#x60;live&#x60; shows the highest value of the &#x60;ccv&#x60; metric from the last 20 seconds. You can use this aggregation only with the &#x60;ccv&#x60; metric.  |
 **_from** | **datetime**| Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for &#x60;from&#x60;, the default assigned value is 1 day ago, based on the &#x60;to&#x60; parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: &#x60;2024-02-05T00:00:00+01:00&#x60; - The API ignores this parameter when you call &#x60;/data/metrics/play/total&#x60;.  | [optional]
 **to** | **datetime**| Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for &#x60;to&#x60;, the default assigned value is &#x60;now&#x60;. - The API ignores this parameter when you call &#x60;/data/metrics/play/total&#x60;. - The value for &#x60;to&#x60; is a non-inclusive value: the API returns data **before** the date-time that you set.  | [optional]
 **unique** | **bool**| Use this query parameter to control how viewer data is counted:  - &#x60;true&#x60; means that a single user watching multiple times counts as 1 unique viewer - &#x60;false&#x60; means that all views count, even if from the same user.  The API accepts this parameter only when you use the &#x60;ccv&#x60; or &#x60;view&#x60; metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer&#39;s &#x60;user-agent&#x60; and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times.  | [optional]
 **view_duration** | **str**| Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter with the &#x60;view&#x60; metric. - The accepted values are &#x60;3s&#x60;, &#x60;5s&#x60;, &#x60;10s&#x60;, and &#x60;30s&#x60;.  - If you do not set this parameter, the API defaults to &#x60;5s&#x60;.  | [optional]
 **filter_by** | **FilterBy2**| Use this parameter to filter the API&#39;s response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for &#x60;filterBy&#x60;, the API returns the full dataset for your project. - The API only accepts the &#x60;mediaId&#x60; and &#x60;mediaType&#x60; filters when you call &#x60;/data/metrics/play/total&#x60; or &#x60;/data/buckets/play-total/media-id&#x60;.  These are the available breakdown dimensions:  - &#x60;mediaId&#x60;: Returns analytics based on the unique identifiers of a video or a live stream. - &#x60;mediaType&#x60;: Returns analytics based on the type of content. Possible values: &#x60;video&#x60; and &#x60;live-stream&#x60;.  - &#x60;continent&#x60;: Returns analytics based on the viewers&#39; continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example &#x60;EU&#x60;. Possible values are: &#x60;AS&#x60;, &#x60;AF&#x60;, &#x60;NA&#x60;, &#x60;SA&#x60;, &#x60;AN&#x60;, &#x60;EU&#x60;, &#x60;AZ&#x60;.  - &#x60;country&#x60;: Returns analytics based on the viewers&#39; country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example &#x60;FR&#x60;. - &#x60;deviceType&#x60;: Returns analytics based on the type of device used by the viewers. Response values can include: &#x60;computer&#x60;, &#x60;phone&#x60;, &#x60;tablet&#x60;, &#x60;tv&#x60;, &#x60;console&#x60;, &#x60;wearable&#x60;, &#x60;unknown&#x60;. - &#x60;operatingSystem&#x60;: Returns analytics based on the operating system used by the viewers. Response values can include &#x60;windows&#x60;, &#x60;mac osx&#x60;, &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;linux&#x60;. - &#x60;browser&#x60;: Returns analytics based on the browser used by the viewers. Response values can include &#x60;chrome&#x60;, &#x60;firefox&#x60;, &#x60;edge&#x60;, &#x60;opera&#x60;. - &#x60;tag&#x60;: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - &#x60;referrer&#x60;: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available.  | [optional]

### Return type

[**AnalyticsAggregatedMetricsResponse**](AnalyticsAggregatedMetricsResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad request error |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Unrecognized request URL |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_breakdown**
> AnalyticsMetricsBreakdownResponse get_metrics_breakdown(metric, breakdown)

Retrieve metrics in a breakdown of dimensions

Retrieve detailed analytics play-rate and number of impressions segmented by dimensions like country or device type.

### Example

```python
import apivideo
from apivideo.api import analytics_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.unrecognized_request_url import UnrecognizedRequestUrl
from apivideo.model.filter_by2 import FilterBy2
from apivideo.model.analytics_metrics_breakdown_response import AnalyticsMetricsBreakdownResponse
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    metric = "play" # str | Use this path parameter to select a metric that you want analytics for.  - `play` is the number of times your content has been played. - `play-rate` is the ratio that calculates the number of plays your content receives divided by its impressions. - `play-total` is the total number of times a specific content has been played. You can only use the `media-id` breakdown with this metric. - `start` is the number of times playback was started. - `end` is the number of times playback has ended with the content watch until the end. - `impression` is the number of times your content has been loaded and was ready for playback. - `ccv-peak` is the highest number of concurrent viewers in the timeframe of your request. - `ccv-average` is the average number of concurrent viewers in the timeframe of your request. - `view` is the total number of viewers until this point in time. 
    breakdown = "media-id" # str | Use this path parameter to define a dimension for segmenting analytics data. You must use `kebab-case` for path parameters.  These are the available dimensions:  - `media-id`: Returns analytics based on the unique identifiers of a video or a live stream. - `media-type`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `device-type`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operating-system`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `referrer`: Returns the URL where the view originates from, for example a website where the video is embedded. View events from Android and iOS return empty strings as the value for `referrer`. 
    _from = dateutil_parser('2024-02-05T00:00:00+01:00') # datetime | Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for `from`, the default assigned value is 1 day ago, based on the `to` parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: `2024-02-05T00:00:00+01:00`  (optional)
    to = dateutil_parser('2024-02-06T00:00:00+01:00') # datetime | Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for `to`, the default assigned value is `now`. - The value for `to` is a non-inclusive value: the API returns data **before** the date-time that you set.  (optional)
    sort_by = "metricValue" # str | Use this parameter to choose which field the API will use to sort the analytics data.  These are the available fields to sort by:  - `metricValue`: Sorts the results based on the **metric** you selected in your request. - `dimensionValue`: Sorts the results based on the **dimension** you selected in your request.  (optional)
    sort_order = "asc" # str | Use this parameter to define the sort order of results.  These are the available sort orders:  - `asc`: Sorts the results in ascending order: `A to Z` and `0 to 9`. - `desc`: Sorts the results in descending order: `Z to A` and `9 to 0`.  (optional)
    unique = True # bool | Use this query parameter to control how viewer data is counted:  - `true` means that a single user watching multiple times counts as 1 unique viewer - `false` means that all views count, even if from the same user.  The API accepts this parameter only when you use the `ccv-peak`, `ccv-average`, or `view` metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer's `user-agent` and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times.  (optional)
    view_duration = "3s" # str | Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter together with the `view` metric. - The accepted values are `3s`, `5s`, `10s`, and `30s`.  - If you do not set this parameter, the API defaults to `5s`.  (optional)
    filter_by = {
        media_id=["vi4blUQJFrYWbaG44NChkH27"],
        media_type="video",
        continent=["EU"],
        country=["FR"],
        device_type=["computer"],
        operating_system=["windows"],
        browser=["firefox"],
        tag="Cool videos",
        referrer=["https%3A%2F%2Fmy-awesome-videos.com"],
    } # FilterBy2 | Use this parameter to filter the API's response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for `filterBy`, the API returns the full dataset for your project. - The API only accepts the `mediaId` and `mediaType` filters when you call `/data/metrics/play/total` or `/data/buckets/play-total/media-id`.  These are the available breakdown dimensions:  - `mediaId`: Returns analytics based on the unique identifiers of a video or a live stream. - `mediaType`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `EU`. Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `FR`. - `deviceType`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `tag`: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - `referrer`: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available.  (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Retrieve metrics in a breakdown of dimensions
        api_response = api_instance.get_metrics_breakdown(metric, breakdown)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_metrics_breakdown: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve metrics in a breakdown of dimensions
        api_response = api_instance.get_metrics_breakdown(metric, breakdown, _from=_from, to=to, sort_by=sort_by, sort_order=sort_order, unique=unique, view_duration=view_duration, filter_by=filter_by, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_metrics_breakdown: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| Use this path parameter to select a metric that you want analytics for.  - &#x60;play&#x60; is the number of times your content has been played. - &#x60;play-rate&#x60; is the ratio that calculates the number of plays your content receives divided by its impressions. - &#x60;play-total&#x60; is the total number of times a specific content has been played. You can only use the &#x60;media-id&#x60; breakdown with this metric. - &#x60;start&#x60; is the number of times playback was started. - &#x60;end&#x60; is the number of times playback has ended with the content watch until the end. - &#x60;impression&#x60; is the number of times your content has been loaded and was ready for playback. - &#x60;ccv-peak&#x60; is the highest number of concurrent viewers in the timeframe of your request. - &#x60;ccv-average&#x60; is the average number of concurrent viewers in the timeframe of your request. - &#x60;view&#x60; is the total number of viewers until this point in time.  |
 **breakdown** | **str**| Use this path parameter to define a dimension for segmenting analytics data. You must use &#x60;kebab-case&#x60; for path parameters.  These are the available dimensions:  - &#x60;media-id&#x60;: Returns analytics based on the unique identifiers of a video or a live stream. - &#x60;media-type&#x60;: Returns analytics based on the type of content. Possible values: &#x60;video&#x60; and &#x60;live-stream&#x60;.  - &#x60;continent&#x60;: Returns analytics based on the viewers&#39; continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). Possible values are: &#x60;AS&#x60;, &#x60;AF&#x60;, &#x60;NA&#x60;, &#x60;SA&#x60;, &#x60;AN&#x60;, &#x60;EU&#x60;, &#x60;AZ&#x60;.  - &#x60;country&#x60;: Returns analytics based on the viewers&#39; country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - &#x60;device-type&#x60;: Returns analytics based on the type of device used by the viewers. Response values can include: &#x60;computer&#x60;, &#x60;phone&#x60;, &#x60;tablet&#x60;, &#x60;tv&#x60;, &#x60;console&#x60;, &#x60;wearable&#x60;, &#x60;unknown&#x60;. - &#x60;operating-system&#x60;: Returns analytics based on the operating system used by the viewers. Response values can include &#x60;windows&#x60;, &#x60;mac osx&#x60;, &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;linux&#x60;. - &#x60;browser&#x60;: Returns analytics based on the browser used by the viewers. Response values can include &#x60;chrome&#x60;, &#x60;firefox&#x60;, &#x60;edge&#x60;, &#x60;opera&#x60;. - &#x60;referrer&#x60;: Returns the URL where the view originates from, for example a website where the video is embedded. View events from Android and iOS return empty strings as the value for &#x60;referrer&#x60;.  |
 **_from** | **datetime**| Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for &#x60;from&#x60;, the default assigned value is 1 day ago, based on the &#x60;to&#x60; parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: &#x60;2024-02-05T00:00:00+01:00&#x60;  | [optional]
 **to** | **datetime**| Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for &#x60;to&#x60;, the default assigned value is &#x60;now&#x60;. - The value for &#x60;to&#x60; is a non-inclusive value: the API returns data **before** the date-time that you set.  | [optional]
 **sort_by** | **str**| Use this parameter to choose which field the API will use to sort the analytics data.  These are the available fields to sort by:  - &#x60;metricValue&#x60;: Sorts the results based on the **metric** you selected in your request. - &#x60;dimensionValue&#x60;: Sorts the results based on the **dimension** you selected in your request.  | [optional]
 **sort_order** | **str**| Use this parameter to define the sort order of results.  These are the available sort orders:  - &#x60;asc&#x60;: Sorts the results in ascending order: &#x60;A to Z&#x60; and &#x60;0 to 9&#x60;. - &#x60;desc&#x60;: Sorts the results in descending order: &#x60;Z to A&#x60; and &#x60;9 to 0&#x60;.  | [optional]
 **unique** | **bool**| Use this query parameter to control how viewer data is counted:  - &#x60;true&#x60; means that a single user watching multiple times counts as 1 unique viewer - &#x60;false&#x60; means that all views count, even if from the same user.  The API accepts this parameter only when you use the &#x60;ccv-peak&#x60;, &#x60;ccv-average&#x60;, or &#x60;view&#x60; metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer&#39;s &#x60;user-agent&#x60; and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times.  | [optional]
 **view_duration** | **str**| Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter together with the &#x60;view&#x60; metric. - The accepted values are &#x60;3s&#x60;, &#x60;5s&#x60;, &#x60;10s&#x60;, and &#x60;30s&#x60;.  - If you do not set this parameter, the API defaults to &#x60;5s&#x60;.  | [optional]
 **filter_by** | **FilterBy2**| Use this parameter to filter the API&#39;s response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for &#x60;filterBy&#x60;, the API returns the full dataset for your project. - The API only accepts the &#x60;mediaId&#x60; and &#x60;mediaType&#x60; filters when you call &#x60;/data/metrics/play/total&#x60; or &#x60;/data/buckets/play-total/media-id&#x60;.  These are the available breakdown dimensions:  - &#x60;mediaId&#x60;: Returns analytics based on the unique identifiers of a video or a live stream. - &#x60;mediaType&#x60;: Returns analytics based on the type of content. Possible values: &#x60;video&#x60; and &#x60;live-stream&#x60;.  - &#x60;continent&#x60;: Returns analytics based on the viewers&#39; continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example &#x60;EU&#x60;. Possible values are: &#x60;AS&#x60;, &#x60;AF&#x60;, &#x60;NA&#x60;, &#x60;SA&#x60;, &#x60;AN&#x60;, &#x60;EU&#x60;, &#x60;AZ&#x60;.  - &#x60;country&#x60;: Returns analytics based on the viewers&#39; country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example &#x60;FR&#x60;. - &#x60;deviceType&#x60;: Returns analytics based on the type of device used by the viewers. Response values can include: &#x60;computer&#x60;, &#x60;phone&#x60;, &#x60;tablet&#x60;, &#x60;tv&#x60;, &#x60;console&#x60;, &#x60;wearable&#x60;, &#x60;unknown&#x60;. - &#x60;operatingSystem&#x60;: Returns analytics based on the operating system used by the viewers. Response values can include &#x60;windows&#x60;, &#x60;mac osx&#x60;, &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;linux&#x60;. - &#x60;browser&#x60;: Returns analytics based on the browser used by the viewers. Response values can include &#x60;chrome&#x60;, &#x60;firefox&#x60;, &#x60;edge&#x60;, &#x60;opera&#x60;. - &#x60;tag&#x60;: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - &#x60;referrer&#x60;: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available.  | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**AnalyticsMetricsBreakdownResponse**](AnalyticsMetricsBreakdownResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad request error |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Unrecognized request URL |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics_over_time**
> AnalyticsMetricsOverTimeResponse get_metrics_over_time(metric)

Retrieve metrics over time

Retrieve countable metrics like the number of plays or impressions, grouped by the time at which they occurred

### Example

```python
import apivideo
from apivideo.api import analytics_api
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.unrecognized_request_url import UnrecognizedRequestUrl
from apivideo.model.analytics_metrics_over_time_response import AnalyticsMetricsOverTimeResponse
from apivideo.model.filter_by2 import FilterBy2
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from pprint import pprint

# Enter a context with an instance of the API client
with apivideo.AuthenticatedApiClient(__API_KEY__) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)
    metric = "play" # str | Use this path parameter to select a metric that you want analytics for.  - `play` is the number of times your content has been played. - `play-rate` is the ratio that calculates the number of plays your content receives divided by its impressions. - `start` is the number of times playback was started. - `end` is the number of times playback has ended with the content watch until the end. - `impression` is the number of times your content has been loaded and was ready for playback. - `ccv-peak` is the highest number of concurrent viewers in the timeframe of your request. - `ccv-average` is the average number of concurrent viewers in the timeframe of your request. - `view` is the total number of viewers.  
    _from = dateutil_parser('2024-02-05T00:00:00+01:00') # datetime | Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for `from`, the default assigned value is 1 day ago, based on the `to` parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: `2024-02-05T00:00:00+01:00`  (optional)
    to = dateutil_parser('2024-02-06T00:00:00+01:00') # datetime | Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for `to`, the default assigned value is `now`. - The value for `to` is a non-inclusive value: the API returns data **before** the date-time that you set.  (optional)
    interval = "hour" # str | Use this query parameter to define the granularity of the data. Possible values: `minute`, `hour`, `day`.  - If you do not set a value for `interval`, and the period you set using the `from` and `to` parameters is less than or equals to 2 days, then the default assigned value is `hour`. Otherwise the API sets it to `day`. - When you set `minute` as interval, the timeframe you define with the `from` and `to` parameters must be less than 60 minutes.  (optional)
    sort_by = "metricValue" # str | Use this parameter to choose which field the API will use to sort the analytics data.  These are the available fields to sort by:  - `metricValue`: Sorts the results based on the **metric** you selected in your request. - `emittedAt`: Sorts the results based on the **timestamp** of the event in ATOM date-time format.  (optional)
    sort_order = "asc" # str | Use this parameter to define the sort order of results.  These are the available sort orders:  - `asc`: Sorts the results in ascending order: `A to Z` and `0 to 9`. - `desc`: Sorts the results in descending order: `Z to A` and `9 to 0`.  (optional)
    unique = True # bool | Use this query parameter to control how viewer data is counted:  - `true` means that a single user watching multiple times counts as 1 unique viewer - `false` means that all views count, even if from the same user.  The API accepts this parameter only when you use the `ccv-peak`, `ccv-average`, or `view` metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer's `user-agent` and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times.  (optional)
    view_duration = "3s" # str | Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter together with the `view` metric. - The accepted values are `3s`, `5s`, `10s`, and `30s`.  - If you do not set this parameter, the API defaults to `5s`.  (optional)
    filter_by = {
        media_id=["vi4blUQJFrYWbaG44NChkH27"],
        media_type="video",
        continent=["EU"],
        country=["FR"],
        device_type=["computer"],
        operating_system=["windows"],
        browser=["firefox"],
        tag="Cool videos",
        referrer=["https%3A%2F%2Fmy-awesome-videos.com"],
    } # FilterBy2 | Use this parameter to filter the API's response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for `filterBy`, the API returns the full dataset for your project. - The API only accepts the `mediaId` and `mediaType` filters when you call `/data/metrics/play/total` or `/data/buckets/play-total/media-id`.  These are the available breakdown dimensions:  - `mediaId`: Returns analytics based on the unique identifiers of a video or a live stream. - `mediaType`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `EU`. Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `FR`. - `deviceType`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `tag`: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - `referrer`: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available.  (optional)
    current_page = 2 # int | Choose the number of search results to return per page. Minimum value: 1 (optional) if omitted the server will use the default value of 1
    page_size = 30 # int | Results per page. Allowed values 1-100, default is 25. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Retrieve metrics over time
        api_response = api_instance.get_metrics_over_time(metric)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_metrics_over_time: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve metrics over time
        api_response = api_instance.get_metrics_over_time(metric, _from=_from, to=to, interval=interval, sort_by=sort_by, sort_order=sort_order, unique=unique, view_duration=view_duration, filter_by=filter_by, current_page=current_page, page_size=page_size)
        pprint(api_response)
    except apivideo.ApiException as e:
        print("Exception when calling AnalyticsApi->get_metrics_over_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **metric** | **str**| Use this path parameter to select a metric that you want analytics for.  - &#x60;play&#x60; is the number of times your content has been played. - &#x60;play-rate&#x60; is the ratio that calculates the number of plays your content receives divided by its impressions. - &#x60;start&#x60; is the number of times playback was started. - &#x60;end&#x60; is the number of times playback has ended with the content watch until the end. - &#x60;impression&#x60; is the number of times your content has been loaded and was ready for playback. - &#x60;ccv-peak&#x60; is the highest number of concurrent viewers in the timeframe of your request. - &#x60;ccv-average&#x60; is the average number of concurrent viewers in the timeframe of your request. - &#x60;view&#x60; is the total number of viewers.   |
 **_from** | **datetime**| Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for &#x60;from&#x60;, the default assigned value is 1 day ago, based on the &#x60;to&#x60; parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: &#x60;2024-02-05T00:00:00+01:00&#x60;  | [optional]
 **to** | **datetime**| Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for &#x60;to&#x60;, the default assigned value is &#x60;now&#x60;. - The value for &#x60;to&#x60; is a non-inclusive value: the API returns data **before** the date-time that you set.  | [optional]
 **interval** | **str**| Use this query parameter to define the granularity of the data. Possible values: &#x60;minute&#x60;, &#x60;hour&#x60;, &#x60;day&#x60;.  - If you do not set a value for &#x60;interval&#x60;, and the period you set using the &#x60;from&#x60; and &#x60;to&#x60; parameters is less than or equals to 2 days, then the default assigned value is &#x60;hour&#x60;. Otherwise the API sets it to &#x60;day&#x60;. - When you set &#x60;minute&#x60; as interval, the timeframe you define with the &#x60;from&#x60; and &#x60;to&#x60; parameters must be less than 60 minutes.  | [optional]
 **sort_by** | **str**| Use this parameter to choose which field the API will use to sort the analytics data.  These are the available fields to sort by:  - &#x60;metricValue&#x60;: Sorts the results based on the **metric** you selected in your request. - &#x60;emittedAt&#x60;: Sorts the results based on the **timestamp** of the event in ATOM date-time format.  | [optional]
 **sort_order** | **str**| Use this parameter to define the sort order of results.  These are the available sort orders:  - &#x60;asc&#x60;: Sorts the results in ascending order: &#x60;A to Z&#x60; and &#x60;0 to 9&#x60;. - &#x60;desc&#x60;: Sorts the results in descending order: &#x60;Z to A&#x60; and &#x60;9 to 0&#x60;.  | [optional]
 **unique** | **bool**| Use this query parameter to control how viewer data is counted:  - &#x60;true&#x60; means that a single user watching multiple times counts as 1 unique viewer - &#x60;false&#x60; means that all views count, even if from the same user.  The API accepts this parameter only when you use the &#x60;ccv-peak&#x60;, &#x60;ccv-average&#x60;, or &#x60;view&#x60; metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer&#39;s &#x60;user-agent&#x60; and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times.  | [optional]
 **view_duration** | **str**| Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter together with the &#x60;view&#x60; metric. - The accepted values are &#x60;3s&#x60;, &#x60;5s&#x60;, &#x60;10s&#x60;, and &#x60;30s&#x60;.  - If you do not set this parameter, the API defaults to &#x60;5s&#x60;.  | [optional]
 **filter_by** | **FilterBy2**| Use this parameter to filter the API&#39;s response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for &#x60;filterBy&#x60;, the API returns the full dataset for your project. - The API only accepts the &#x60;mediaId&#x60; and &#x60;mediaType&#x60; filters when you call &#x60;/data/metrics/play/total&#x60; or &#x60;/data/buckets/play-total/media-id&#x60;.  These are the available breakdown dimensions:  - &#x60;mediaId&#x60;: Returns analytics based on the unique identifiers of a video or a live stream. - &#x60;mediaType&#x60;: Returns analytics based on the type of content. Possible values: &#x60;video&#x60; and &#x60;live-stream&#x60;.  - &#x60;continent&#x60;: Returns analytics based on the viewers&#39; continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example &#x60;EU&#x60;. Possible values are: &#x60;AS&#x60;, &#x60;AF&#x60;, &#x60;NA&#x60;, &#x60;SA&#x60;, &#x60;AN&#x60;, &#x60;EU&#x60;, &#x60;AZ&#x60;.  - &#x60;country&#x60;: Returns analytics based on the viewers&#39; country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example &#x60;FR&#x60;. - &#x60;deviceType&#x60;: Returns analytics based on the type of device used by the viewers. Response values can include: &#x60;computer&#x60;, &#x60;phone&#x60;, &#x60;tablet&#x60;, &#x60;tv&#x60;, &#x60;console&#x60;, &#x60;wearable&#x60;, &#x60;unknown&#x60;. - &#x60;operatingSystem&#x60;: Returns analytics based on the operating system used by the viewers. Response values can include &#x60;windows&#x60;, &#x60;mac osx&#x60;, &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;linux&#x60;. - &#x60;browser&#x60;: Returns analytics based on the browser used by the viewers. Response values can include &#x60;chrome&#x60;, &#x60;firefox&#x60;, &#x60;edge&#x60;, &#x60;opera&#x60;. - &#x60;tag&#x60;: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - &#x60;referrer&#x60;: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available.  | [optional]
 **current_page** | **int**| Choose the number of search results to return per page. Minimum value: 1 | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Results per page. Allowed values 1-100, default is 25. | [optional] if omitted the server will use the default value of 25

### Return type

[**AnalyticsMetricsOverTimeResponse**](AnalyticsMetricsOverTimeResponse.md)


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**400** | Bad request error |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**404** | Unrecognized request URL |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |
**429** | Too Many Requests |  * X-RateLimit-Limit - The request limit per minute. <br>  * X-RateLimit-Remaining - The number of available requests left for the current time window. <br>  * X-RateLimit-Retry-After - The number of seconds left until the current rate limit window resets. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

