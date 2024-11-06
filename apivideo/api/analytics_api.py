"""
    api.video

    api.video is an API that encodes on the go to facilitate immediate playback, enhancing viewer streaming experiences across multiple devices and platforms. You can stream live or on-demand online videos within minutes.  # noqa: E501

    Contact: ecosystem@api.video
"""

import os  # noqa: F401
import re  # noqa: F401
import sys  # noqa: F401
from types import MethodType
from types import FunctionType

from apivideo.api_client import ApiClient
from apivideo.endpoint import EndPoint as _EndPoint, ChunkIO
from apivideo.model.video_id import VideoId
from apivideo.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from apivideo.exceptions import ApiTypeError, ApiValueError
from apivideo.model.analytics_aggregated_metrics_response import AnalyticsAggregatedMetricsResponse
from apivideo.model.analytics_metrics_breakdown_response import AnalyticsMetricsBreakdownResponse
from apivideo.model.analytics_metrics_over_time_response import AnalyticsMetricsOverTimeResponse
from apivideo.model.analytics_plays400_error import AnalyticsPlays400Error
from apivideo.model.filter_by2 import FilterBy2
from apivideo.model.too_many_requests import TooManyRequests
from apivideo.model.unrecognized_request_url import UnrecognizedRequestUrl


class AnalyticsApi(_EndPoint):

    def get_aggregated_metrics(
            self,
            metric,
            aggregation,
            **kwargs
        ):
            """Retrieve aggregated metrics  # noqa: E501

            Retrieve time-based and countable metrics like average watch time or the number of impressions over a certain period of time.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_aggregated_metrics(metric, aggregation, async_req=True)
            >>> result = thread.get()

            Args:
                metric (str): Use this path parameter to select a metric that you want analytics for.  - `play` is the number of times your content has been played. You can use the aggregations `count`, `rate`, and `total` with the `play` metric. - `start` is the number of times playback was started. You can use the aggregation `count` with this metric. - `end` is the number of times playback has ended with the content watch until the end. You can use the aggregation `count` with this metric. - `impression` is the number of times your content has been loaded and was ready for playback. You can use the aggregation `count` with this metric. - `impression-time` is the time in milliseconds that your content was loading for until the first video frame is displayed. You can use the aggregations `average` and `sum` with this metric. - `watch-time` is the cumulative time in seconds that the user has spent watching your content. You can use the aggregations `average` and `sum` with this metric. - `ccv`: is the number of concurrent viewers, or users watching at the same time. - `view`: the total number of viewers until this point in time. 
                aggregation (str): Use this path parameter to define a way of collecting data for the metric that you want analytics for.  - `count` returns the overall number of events for the `play` metric. - `rate` returns the ratio that calculates the number of plays your content receives divided by its impressions. This aggregation can be used only with the `play` metric. - `total` calculates the total number of events for the `play` metric.  - `average` calculates an average value for the selected metric. - `sum` adds up the total value of the select metric. - `peak` shows the highest value of the `ccv` metric in the timeframe of your request. You can use this aggregation only with the `ccv` metric. - `live` shows the highest value of the `ccv` metric from the last 20 seconds. You can use this aggregation only with the `ccv` metric. 

            Keyword Args:
                _from (datetime): Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for `from`, the default assigned value is 1 day ago, based on the `to` parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: `2024-02-05T00:00:00+01:00` - The API ignores this parameter when you call `/data/metrics/play/total`. . [optional]
                to (datetime): Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for `to`, the default assigned value is `now`. - The API ignores this parameter when you call `/data/metrics/play/total`. - The value for `to` is a non-inclusive value: the API returns data **before** the date-time that you set. . [optional]
                unique (bool): Use this query parameter to control how viewer data is counted:  - `true` means that a single user watching multiple times counts as 1 unique viewer - `false` means that all views count, even if from the same user.  The API accepts this parameter only when you use the `ccv` or `view` metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer's `user-agent` and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times. . [optional]
                view_duration (str): Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter with the `view` metric. - The accepted values are `3s`, `5s`, `10s`, and `30s`.  - If you do not set this parameter, the API defaults to `5s`. . [optional]
                filter_by (FilterBy2): Use this parameter to filter the API's response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for `filterBy`, the API returns the full dataset for your project. - The API only accepts the `mediaId` and `mediaType` filters when you call `/data/metrics/play/total` or `/data/buckets/play-total/media-id`.  These are the available breakdown dimensions:  - `mediaId`: Returns analytics based on the unique identifiers of a video or a live stream. - `mediaType`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `EU`. Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `FR`. - `deviceType`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `tag`: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - `referrer`: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available. . [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                async_req (bool): execute request asynchronously

            Returns:
                AnalyticsAggregatedMetricsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['metric'] = \
                metric
            kwargs['aggregation'] = \
                aggregation

            params_map = {
                'all': [
                    'metric',
                    'aggregation',
                    '_from',
                    'to',
                    'unique',
                    'view_duration',
                    'filter_by',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'metric',
                    'aggregation',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'metric',
                    'aggregation',
                    'view_duration',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('metric',): {

                    "PLAY": "play",
                    "START": "start",
                    "END": "end",
                    "IMPRESSION": "impression",
                    "IMPRESSION-TIME": "impression-time",
                    "WATCH-TIME": "watch-time",
                    "CCV": "ccv",
                    "VIEW": "view"
                },
                ('aggregation',): {

                    "COUNT": "count",
                    "RATE": "rate",
                    "TOTAL": "total",
                    "AVERAGE": "average",
                    "SUM": "sum",
                    "PEAK": "peak",
                    "LIVE": "live"
                },
                ('view_duration',): {

                    "3S": "3s",
                    "5S": "5s",
                    "10S": "10s",
                    "30S": "30s"
                },
            }
            openapi_types = {
                'metric':
                    (str,),
                'aggregation':
                    (str,),
                '_from':
                    (datetime,),
                'to':
                    (datetime,),
                'unique':
                    (bool,),
                'view_duration':
                    (str,),
                'filter_by':
                    (FilterBy2,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'metric': 'metric',
                'aggregation': 'aggregation',
                '_from': 'from',
                'to': 'to',
                'unique': 'unique',
                'view_duration': 'viewDuration',
                'filter_by': 'filterBy',
            }
            location_map = {
                'metric': 'path',
                'aggregation': 'path',
                '_from': 'query',
                'to': 'query',
                'unique': 'query',
                'view_duration': 'query',
                'filter_by': 'query',
            }
            collection_format_map = {
                'filter_by': 'deepObject',
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get_aggregated_metrics`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get_aggregated_metrics`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get_aggregated_metrics`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/data/metrics/{metric}/{aggregation}",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(AnalyticsAggregatedMetricsResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def get_metrics_breakdown(
            self,
            metric,
            breakdown,
            **kwargs
        ):
            """Retrieve metrics in a breakdown of dimensions  # noqa: E501

            Retrieve detailed analytics play-rate and number of impressions segmented by dimensions like country or device type.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_metrics_breakdown(metric, breakdown, async_req=True)
            >>> result = thread.get()

            Args:
                metric (str): Use this path parameter to select a metric that you want analytics for.  - `play` is the number of times your content has been played. - `play-rate` is the ratio that calculates the number of plays your content receives divided by its impressions. - `play-total` is the total number of times a specific content has been played. You can only use the `media-id` breakdown with this metric. - `start` is the number of times playback was started. - `end` is the number of times playback has ended with the content watch until the end. - `impression` is the number of times your content has been loaded and was ready for playback. - `ccv-peak` is the highest number of concurrent viewers in the timeframe of your request. - `ccv-average` is the average number of concurrent viewers in the timeframe of your request. - `view` is the total number of viewers until this point in time. 
                breakdown (str): Use this path parameter to define a dimension for segmenting analytics data. You must use `kebab-case` for path parameters.  These are the available dimensions:  - `media-id`: Returns analytics based on the unique identifiers of a video or a live stream. - `media-type`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). - `device-type`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operating-system`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `referrer`: Returns the URL where the view originates from, for example a website where the video is embedded. View events from Android and iOS return empty strings as the value for `referrer`. 

            Keyword Args:
                _from (datetime): Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for `from`, the default assigned value is 1 day ago, based on the `to` parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: `2024-02-05T00:00:00+01:00` . [optional]
                to (datetime): Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for `to`, the default assigned value is `now`. - The value for `to` is a non-inclusive value: the API returns data **before** the date-time that you set. . [optional]
                sort_by (str): Use this parameter to choose which field the API will use to sort the analytics data.  These are the available fields to sort by:  - `metricValue`: Sorts the results based on the **metric** you selected in your request. - `dimensionValue`: Sorts the results based on the **dimension** you selected in your request. . [optional]
                sort_order (str): Use this parameter to define the sort order of results.  These are the available sort orders:  - `asc`: Sorts the results in ascending order: `A to Z` and `0 to 9`. - `desc`: Sorts the results in descending order: `Z to A` and `9 to 0`. . [optional]
                unique (bool): Use this query parameter to control how viewer data is counted:  - `true` means that a single user watching multiple times counts as 1 unique viewer - `false` means that all views count, even if from the same user.  The API accepts this parameter only when you use the `ccv-peak`, `ccv-average`, or `view` metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer's `user-agent` and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times. . [optional]
                view_duration (str): Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter together with the `view` metric. - The accepted values are `3s`, `5s`, `10s`, and `30s`.  - If you do not set this parameter, the API defaults to `5s`. . [optional]
                filter_by (FilterBy2): Use this parameter to filter the API's response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for `filterBy`, the API returns the full dataset for your project. - The API only accepts the `mediaId` and `mediaType` filters when you call `/data/metrics/play/total` or `/data/buckets/play-total/media-id`.  These are the available breakdown dimensions:  - `mediaId`: Returns analytics based on the unique identifiers of a video or a live stream. - `mediaType`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `EU`. Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `FR`. - `deviceType`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `tag`: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - `referrer`: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available. . [optional]
                current_page (int): Choose the number of search results to return per page. Minimum value: 1. [optional] if omitted the server will use the default value of 1
                page_size (int): Results per page. Allowed values 1-100, default is 25.. [optional] if omitted the server will use the default value of 25
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                async_req (bool): execute request asynchronously

            Returns:
                AnalyticsMetricsBreakdownResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['metric'] = \
                metric
            kwargs['breakdown'] = \
                breakdown

            params_map = {
                'all': [
                    'metric',
                    'breakdown',
                    '_from',
                    'to',
                    'sort_by',
                    'sort_order',
                    'unique',
                    'view_duration',
                    'filter_by',
                    'current_page',
                    'page_size',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'metric',
                    'breakdown',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'metric',
                    'breakdown',
                    'sort_by',
                    'sort_order',
                    'view_duration',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('metric',): {

                    "PLAY": "play",
                    "PLAY-RATE": "play-rate",
                    "PLAY-TOTAL": "play-total",
                    "START": "start",
                    "END": "end",
                    "IMPRESSION": "impression",
                    "CCV-PEAK": "ccv-peak",
                    "CCV-AVERAGE": "ccv-average",
                    "VIEW": "view"
                },
                ('breakdown',): {

                    "MEDIA-ID": "media-id",
                    "MEDIA-TYPE": "media-type",
                    "CONTINENT": "continent",
                    "COUNTRY": "country",
                    "DEVICE-TYPE": "device-type",
                    "OPERATING-SYSTEM": "operating-system",
                    "BROWSER": "browser",
                    "REFERRER": "referrer"
                },
                ('sort_by',): {

                    "METRICVALUE": "metricValue",
                    "DIMENSIONVALUE": "dimensionValue"
                },
                ('sort_order',): {

                    "ASC": "asc",
                    "DESC": "desc"
                },
                ('view_duration',): {

                    "3S": "3s",
                    "5S": "5s",
                    "10S": "10s",
                    "30S": "30s"
                },
            }
            openapi_types = {
                'metric':
                    (str,),
                'breakdown':
                    (str,),
                '_from':
                    (datetime,),
                'to':
                    (datetime,),
                'sort_by':
                    (str,),
                'sort_order':
                    (str,),
                'unique':
                    (bool,),
                'view_duration':
                    (str,),
                'filter_by':
                    (FilterBy2,),
                'current_page':
                    (int,),
                'page_size':
                    (int,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'metric': 'metric',
                'breakdown': 'breakdown',
                '_from': 'from',
                'to': 'to',
                'sort_by': 'sortBy',
                'sort_order': 'sortOrder',
                'unique': 'unique',
                'view_duration': 'viewDuration',
                'filter_by': 'filterBy',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                'metric': 'path',
                'breakdown': 'path',
                '_from': 'query',
                'to': 'query',
                'sort_by': 'query',
                'sort_order': 'query',
                'unique': 'query',
                'view_duration': 'query',
                'filter_by': 'query',
                'current_page': 'query',
                'page_size': 'query',
            }
            collection_format_map = {
                'filter_by': 'deepObject',
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get_metrics_breakdown`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get_metrics_breakdown`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get_metrics_breakdown`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/data/buckets/{metric}/{breakdown}",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(AnalyticsMetricsBreakdownResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

    def get_metrics_over_time(
            self,
            metric,
            **kwargs
        ):
            """Retrieve metrics over time  # noqa: E501

            Retrieve countable metrics like the number of plays or impressions, grouped by the time at which they occurred  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_metrics_over_time(metric, async_req=True)
            >>> result = thread.get()

            Args:
                metric (str): Use this path parameter to select a metric that you want analytics for.  - `play` is the number of times your content has been played. - `play-rate` is the ratio that calculates the number of plays your content receives divided by its impressions. - `start` is the number of times playback was started. - `end` is the number of times playback has ended with the content watch until the end. - `impression` is the number of times your content has been loaded and was ready for playback. - `ccv-peak` is the highest number of concurrent viewers in the timeframe of your request. - `ccv-average` is the average number of concurrent viewers in the timeframe of your request. - `view` is the total number of viewers.  

            Keyword Args:
                _from (datetime): Use this query parameter to define the starting date-time of the period you want analytics for.  - If you do not set a value for `from`, the default assigned value is 1 day ago, based on the `to` parameter. - The maximum value is 30 days ago. - The value you provide should follow the ATOM date-time format: `2024-02-05T00:00:00+01:00` . [optional]
                to (datetime): Use this query parameter to define the ending date-time of the period you want analytics for.  - If you do not set a value for `to`, the default assigned value is `now`. - The value for `to` is a non-inclusive value: the API returns data **before** the date-time that you set. . [optional]
                interval (str): Use this query parameter to define the granularity of the data. Possible values: `minute`, `hour`, `day`.  - If you do not set a value for `interval`, and the period you set using the `from` and `to` parameters is less than or equals to 2 days, then the default assigned value is `hour`. Otherwise the API sets it to `day`. - When you set `minute` as interval, the timeframe you define with the `from` and `to` parameters must be less than 60 minutes. . [optional]
                sort_by (str): Use this parameter to choose which field the API will use to sort the analytics data.  These are the available fields to sort by:  - `metricValue`: Sorts the results based on the **metric** you selected in your request. - `emittedAt`: Sorts the results based on the **timestamp** of the event in ATOM date-time format. . [optional]
                sort_order (str): Use this parameter to define the sort order of results.  These are the available sort orders:  - `asc`: Sorts the results in ascending order: `A to Z` and `0 to 9`. - `desc`: Sorts the results in descending order: `Z to A` and `9 to 0`. . [optional]
                unique (bool): Use this query parameter to control how viewer data is counted:  - `true` means that a single user watching multiple times counts as 1 unique viewer - `false` means that all views count, even if from the same user.  The API accepts this parameter only when you use the `ccv-peak`, `ccv-average`, or `view` metric.            Viewers are unique for 1 day.  The API determines uniqueness based on a viewer's `user-agent` and IP address. This means that the API can filter viewers using multiple tabs to watch the same video multiple times, but cannot filter for viewers who use multiple browsers to watch the same content multiple times. . [optional]
                view_duration (str): Use this query parameter to define how many seconds a view has to last to be counted in analytics data.  - You can only use this parameter together with the `view` metric. - The accepted values are `3s`, `5s`, `10s`, and `30s`.  - If you do not set this parameter, the API defaults to `5s`. . [optional]
                filter_by (FilterBy2): Use this parameter to filter the API's response based on different data dimensions. You can serialize filters in your query to receive more detailed breakdowns of your analytics.  - If you do not set a value for `filterBy`, the API returns the full dataset for your project. - The API only accepts the `mediaId` and `mediaType` filters when you call `/data/metrics/play/total` or `/data/buckets/play-total/media-id`.  These are the available breakdown dimensions:  - `mediaId`: Returns analytics based on the unique identifiers of a video or a live stream. - `mediaType`: Returns analytics based on the type of content. Possible values: `video` and `live-stream`.  - `continent`: Returns analytics based on the viewers' continent. The list of supported continents names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `EU`. Possible values are: `AS`, `AF`, `NA`, `SA`, `AN`, `EU`, `AZ`.  - `country`: Returns analytics based on the viewers' country. The list of supported country names are based on the [GeoNames public database](https://www.geonames.org/countries/). You must use the ISO-3166 alpha2 format, for example `FR`. - `deviceType`: Returns analytics based on the type of device used by the viewers. Response values can include: `computer`, `phone`, `tablet`, `tv`, `console`, `wearable`, `unknown`. - `operatingSystem`: Returns analytics based on the operating system used by the viewers. Response values can include `windows`, `mac osx`, `android`, `ios`, `linux`. - `browser`: Returns analytics based on the browser used by the viewers. Response values can include `chrome`, `firefox`, `edge`, `opera`. - `tag`: Returns analytics for videos using this tag. This filter only accepts a single value and is case sensitive. Read more about tagging your videos [here](https://docs.api.video/vod/tags-metadata). - `referrer`: Filters data based on the URL where the view is originating from. Accepts an empty string as a value to filter view events where no referrer is available. . [optional]
                current_page (int): Choose the number of search results to return per page. Minimum value: 1. [optional] if omitted the server will use the default value of 1
                page_size (int): Results per page. Allowed values 1-100, default is 25.. [optional] if omitted the server will use the default value of 25
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                async_req (bool): execute request asynchronously

            Returns:
                AnalyticsMetricsOverTimeResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['metric'] = \
                metric

            params_map = {
                'all': [
                    'metric',
                    '_from',
                    'to',
                    'interval',
                    'sort_by',
                    'sort_order',
                    'unique',
                    'view_duration',
                    'filter_by',
                    'current_page',
                    'page_size',
                    'async_req',
                    '_preload_content',
                    '_request_timeout',
                    '_return_http_data_only'
                ],
                'required': [
                    'metric',
                ],
                'nullable': [
                    '_request_timeout'
                ],
                'enum': [
                    'metric',
                    'interval',
                    'sort_by',
                    'sort_order',
                    'view_duration',
                ],
                'validation': [
                ]
            }
            validations = {
            }
            allowed_values = {
                ('metric',): {

                    "PLAY": "play",
                    "PLAY-RATE": "play-rate",
                    "START": "start",
                    "END": "end",
                    "IMPRESSION": "impression",
                    "CCV-PEAK": "ccv-peak",
                    "CCV-AVERAGE": "ccv-average",
                    "VIEW": "view"
                },
                ('interval',): {

                    "MINUTE": "minute",
                    "HOUR": "hour",
                    "DAY": "day"
                },
                ('sort_by',): {

                    "METRICVALUE": "metricValue",
                    "EMITTEDAT": "emittedAt"
                },
                ('sort_order',): {

                    "ASC": "asc",
                    "DESC": "desc"
                },
                ('view_duration',): {

                    "3S": "3s",
                    "5S": "5s",
                    "10S": "10s",
                    "30S": "30s"
                },
            }
            openapi_types = {
                'metric':
                    (str,),
                '_from':
                    (datetime,),
                'to':
                    (datetime,),
                'interval':
                    (str,),
                'sort_by':
                    (str,),
                'sort_order':
                    (str,),
                'unique':
                    (bool,),
                'view_duration':
                    (str,),
                'filter_by':
                    (FilterBy2,),
                'current_page':
                    (int,),
                'page_size':
                    (int,),
                'async_req': (bool,),
                '_preload_content': (bool,),
                '_request_timeout': (none_type, int, (int,), [int]),
                '_return_http_data_only': (bool,)
            }
            attribute_map = {
                'metric': 'metric',
                '_from': 'from',
                'to': 'to',
                'interval': 'interval',
                'sort_by': 'sortBy',
                'sort_order': 'sortOrder',
                'unique': 'unique',
                'view_duration': 'viewDuration',
                'filter_by': 'filterBy',
                'current_page': 'currentPage',
                'page_size': 'pageSize',
            }
            location_map = {
                'metric': 'path',
                '_from': 'query',
                'to': 'query',
                'interval': 'query',
                'sort_by': 'query',
                'sort_order': 'query',
                'unique': 'query',
                'view_duration': 'query',
                'filter_by': 'query',
                'current_page': 'query',
                'page_size': 'query',
            }
            collection_format_map = {
                'filter_by': 'deepObject',
            }

            for key, value in kwargs.items():
                if key not in params_map['all']:
                    raise ApiTypeError(
                        "Got an unexpected parameter '%s'"
                        " to method `get_metrics_over_time`" %
                        (key, )
                    )
                if (key not in params_map['nullable'] and value is None):
                    raise ApiValueError(
                        "Value may not be None for non-nullable parameter `%s`"
                        " when calling `get_metrics_over_time`" %
                        (key, )
                    )

            for key in params_map['required']:
                if key not in kwargs.keys():
                    raise ApiValueError(
                        "Missing the required parameter `%s` when calling "
                        "`get_metrics_over_time`" % (key, )
                    )

            self._validate_inputs(kwargs, params_map, allowed_values, validations, openapi_types)
            params = self._gather_params(kwargs, location_map, attribute_map, openapi_types, collection_format_map)
            return self.api_client.call_api(
                "/data/timeseries/{metric}",
                "GET",
                params['path'],
                params['query'],
                params['header'],
                body=params['body'],
                post_params=params['form'],
                files=params['file'],
                response_type=(AnalyticsMetricsOverTimeResponse,),
                async_req=kwargs['async_req'],
                _return_http_data_only=kwargs['_return_http_data_only'],
                _preload_content=kwargs['_preload_content'],
                _request_timeout=kwargs['_request_timeout'],
                collection_formats=params['collection_format'])

