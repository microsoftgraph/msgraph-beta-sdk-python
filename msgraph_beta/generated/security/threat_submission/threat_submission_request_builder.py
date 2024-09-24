from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.security.threat_submission_root import ThreatSubmissionRoot
    from .email_threats.email_threats_request_builder import EmailThreatsRequestBuilder
    from .email_threat_submission_policies.email_threat_submission_policies_request_builder import EmailThreatSubmissionPoliciesRequestBuilder
    from .file_threats.file_threats_request_builder import FileThreatsRequestBuilder
    from .url_threats.url_threats_request_builder import UrlThreatsRequestBuilder

class ThreatSubmissionRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the threatSubmission property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ThreatSubmissionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/threatSubmission{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property threatSubmission for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ThreatSubmissionRequestBuilderGetQueryParameters]] = None) -> Optional[ThreatSubmissionRoot]:
        """
        A threat submission sent to Microsoft; for example, a suspicious email threat, URL threat, or file threat.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThreatSubmissionRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.threat_submission_root import ThreatSubmissionRoot

        return await self.request_adapter.send_async(request_info, ThreatSubmissionRoot, error_mapping)
    
    async def patch(self,body: ThreatSubmissionRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ThreatSubmissionRoot]:
        """
        Update the navigation property threatSubmission in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThreatSubmissionRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.threat_submission_root import ThreatSubmissionRoot

        return await self.request_adapter.send_async(request_info, ThreatSubmissionRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property threatSubmission for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ThreatSubmissionRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        A threat submission sent to Microsoft; for example, a suspicious email threat, URL threat, or file threat.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ThreatSubmissionRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property threatSubmission in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ThreatSubmissionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ThreatSubmissionRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ThreatSubmissionRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def email_threat_submission_policies(self) -> EmailThreatSubmissionPoliciesRequestBuilder:
        """
        Provides operations to manage the emailThreatSubmissionPolicies property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        from .email_threat_submission_policies.email_threat_submission_policies_request_builder import EmailThreatSubmissionPoliciesRequestBuilder

        return EmailThreatSubmissionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_threats(self) -> EmailThreatsRequestBuilder:
        """
        Provides operations to manage the emailThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        from .email_threats.email_threats_request_builder import EmailThreatsRequestBuilder

        return EmailThreatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file_threats(self) -> FileThreatsRequestBuilder:
        """
        Provides operations to manage the fileThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        from .file_threats.file_threats_request_builder import FileThreatsRequestBuilder

        return FileThreatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def url_threats(self) -> UrlThreatsRequestBuilder:
        """
        Provides operations to manage the urlThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        from .url_threats.url_threats_request_builder import UrlThreatsRequestBuilder

        return UrlThreatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ThreatSubmissionRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ThreatSubmissionRequestBuilderGetQueryParameters():
        """
        A threat submission sent to Microsoft; for example, a suspicious email threat, URL threat, or file threat.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
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
    class ThreatSubmissionRequestBuilderGetRequestConfiguration(RequestConfiguration[ThreatSubmissionRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ThreatSubmissionRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

