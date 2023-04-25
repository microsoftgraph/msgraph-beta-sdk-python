from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors import o_data_error
    from ...models.security import threat_intelligence
    from .article_indicators import article_indicators_request_builder
    from .articles import articles_request_builder
    from .host_components import host_components_request_builder
    from .host_cookies import host_cookies_request_builder
    from .hosts import hosts_request_builder
    from .host_trackers import host_trackers_request_builder
    from .intelligence_profile_indicators import intelligence_profile_indicators_request_builder
    from .intel_profiles import intel_profiles_request_builder
    from .passive_dns_records import passive_dns_records_request_builder
    from .vulnerabilities import vulnerabilities_request_builder

class ThreatIntelligenceRequestBuilder():
    """
    Provides operations to manage the threatIntelligence property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ThreatIntelligenceRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/threatIntelligence{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property threatIntelligence for security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderGetRequestConfiguration] = None) -> Optional[threat_intelligence.ThreatIntelligence]:
        """
        Get threatIntelligence from security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[threat_intelligence.ThreatIntelligence]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security import threat_intelligence

        return await self.request_adapter.send_async(request_info, threat_intelligence.ThreatIntelligence, error_mapping)
    
    async def patch(self,body: Optional[threat_intelligence.ThreatIntelligence] = None, request_configuration: Optional[ThreatIntelligenceRequestBuilderPatchRequestConfiguration] = None) -> Optional[threat_intelligence.ThreatIntelligence]:
        """
        Update the navigation property threatIntelligence in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[threat_intelligence.ThreatIntelligence]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security import threat_intelligence

        return await self.request_adapter.send_async(request_info, threat_intelligence.ThreatIntelligence, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property threatIntelligence for security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ThreatIntelligenceRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get threatIntelligence from security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[threat_intelligence.ThreatIntelligence] = None, request_configuration: Optional[ThreatIntelligenceRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property threatIntelligence in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def article_indicators(self) -> article_indicators_request_builder.ArticleIndicatorsRequestBuilder:
        """
        Provides operations to manage the articleIndicators property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .article_indicators import article_indicators_request_builder

        return article_indicators_request_builder.ArticleIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def articles(self) -> articles_request_builder.ArticlesRequestBuilder:
        """
        Provides operations to manage the articles property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .articles import articles_request_builder

        return articles_request_builder.ArticlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_components(self) -> host_components_request_builder.HostComponentsRequestBuilder:
        """
        Provides operations to manage the hostComponents property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_components import host_components_request_builder

        return host_components_request_builder.HostComponentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_cookies(self) -> host_cookies_request_builder.HostCookiesRequestBuilder:
        """
        Provides operations to manage the hostCookies property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_cookies import host_cookies_request_builder

        return host_cookies_request_builder.HostCookiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hosts(self) -> hosts_request_builder.HostsRequestBuilder:
        """
        Provides operations to manage the hosts property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .hosts import hosts_request_builder

        return hosts_request_builder.HostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_trackers(self) -> host_trackers_request_builder.HostTrackersRequestBuilder:
        """
        Provides operations to manage the hostTrackers property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_trackers import host_trackers_request_builder

        return host_trackers_request_builder.HostTrackersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intelligence_profile_indicators(self) -> intelligence_profile_indicators_request_builder.IntelligenceProfileIndicatorsRequestBuilder:
        """
        Provides operations to manage the intelligenceProfileIndicators property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .intelligence_profile_indicators import intelligence_profile_indicators_request_builder

        return intelligence_profile_indicators_request_builder.IntelligenceProfileIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intel_profiles(self) -> intel_profiles_request_builder.IntelProfilesRequestBuilder:
        """
        Provides operations to manage the intelProfiles property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .intel_profiles import intel_profiles_request_builder

        return intel_profiles_request_builder.IntelProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passive_dns_records(self) -> passive_dns_records_request_builder.PassiveDnsRecordsRequestBuilder:
        """
        Provides operations to manage the passiveDnsRecords property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .passive_dns_records import passive_dns_records_request_builder

        return passive_dns_records_request_builder.PassiveDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vulnerabilities(self) -> vulnerabilities_request_builder.VulnerabilitiesRequestBuilder:
        """
        Provides operations to manage the vulnerabilities property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .vulnerabilities import vulnerabilities_request_builder

        return vulnerabilities_request_builder.VulnerabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ThreatIntelligenceRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ThreatIntelligenceRequestBuilderGetQueryParameters():
        """
        Get threatIntelligence from security
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ThreatIntelligenceRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ThreatIntelligenceRequestBuilder.ThreatIntelligenceRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ThreatIntelligenceRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

