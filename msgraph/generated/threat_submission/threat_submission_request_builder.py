from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
threat_submission_root = lazy_import('msgraph.generated.models.security.threat_submission_root')
email_threats_request_builder = lazy_import('msgraph.generated.threat_submission.email_threats.email_threats_request_builder')
email_threat_submission_item_request_builder = lazy_import('msgraph.generated.threat_submission.email_threats.item.email_threat_submission_item_request_builder')
email_threat_submission_policies_request_builder = lazy_import('msgraph.generated.threat_submission.email_threat_submission_policies.email_threat_submission_policies_request_builder')
email_threat_submission_policy_item_request_builder = lazy_import('msgraph.generated.threat_submission.email_threat_submission_policies.item.email_threat_submission_policy_item_request_builder')
file_threats_request_builder = lazy_import('msgraph.generated.threat_submission.file_threats.file_threats_request_builder')
file_threat_submission_item_request_builder = lazy_import('msgraph.generated.threat_submission.file_threats.item.file_threat_submission_item_request_builder')
url_threats_request_builder = lazy_import('msgraph.generated.threat_submission.url_threats.url_threats_request_builder')
url_threat_submission_item_request_builder = lazy_import('msgraph.generated.threat_submission.url_threats.item.url_threat_submission_item_request_builder')

class ThreatSubmissionRequestBuilder():
    """
    Provides operations to manage the threatSubmissionRoot singleton.
    """
    @property
    def email_threats(self) -> email_threats_request_builder.EmailThreatsRequestBuilder:
        """
        Provides operations to manage the emailThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        return email_threats_request_builder.EmailThreatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email_threat_submission_policies(self) -> email_threat_submission_policies_request_builder.EmailThreatSubmissionPoliciesRequestBuilder:
        """
        Provides operations to manage the emailThreatSubmissionPolicies property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        return email_threat_submission_policies_request_builder.EmailThreatSubmissionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file_threats(self) -> file_threats_request_builder.FileThreatsRequestBuilder:
        """
        Provides operations to manage the fileThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        return file_threats_request_builder.FileThreatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def url_threats(self) -> url_threats_request_builder.UrlThreatsRequestBuilder:
        """
        Provides operations to manage the urlThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        """
        return url_threats_request_builder.UrlThreatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ThreatSubmissionRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/threatSubmission{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[ThreatSubmissionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get threatSubmission
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[threat_submission_root.ThreatSubmissionRoot] = None, request_configuration: Optional[ThreatSubmissionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update threatSubmission
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def email_threats_by_id(self,id: str) -> email_threat_submission_item_request_builder.EmailThreatSubmissionItemRequestBuilder:
        """
        Provides operations to manage the emailThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: email_threat_submission_item_request_builder.EmailThreatSubmissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["emailThreatSubmission%2Did"] = id
        return email_threat_submission_item_request_builder.EmailThreatSubmissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def email_threat_submission_policies_by_id(self,id: str) -> email_threat_submission_policy_item_request_builder.EmailThreatSubmissionPolicyItemRequestBuilder:
        """
        Provides operations to manage the emailThreatSubmissionPolicies property of the microsoft.graph.security.threatSubmissionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: email_threat_submission_policy_item_request_builder.EmailThreatSubmissionPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["emailThreatSubmissionPolicy%2Did"] = id
        return email_threat_submission_policy_item_request_builder.EmailThreatSubmissionPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def file_threats_by_id(self,id: str) -> file_threat_submission_item_request_builder.FileThreatSubmissionItemRequestBuilder:
        """
        Provides operations to manage the fileThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: file_threat_submission_item_request_builder.FileThreatSubmissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileThreatSubmission%2Did"] = id
        return file_threat_submission_item_request_builder.FileThreatSubmissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ThreatSubmissionRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[threat_submission_root.ThreatSubmissionRoot]:
        """
        Get threatSubmission
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[threat_submission_root.ThreatSubmissionRoot]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, threat_submission_root.ThreatSubmissionRoot, response_handler, error_mapping)
    
    async def patch(self,body: Optional[threat_submission_root.ThreatSubmissionRoot] = None, request_configuration: Optional[ThreatSubmissionRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[threat_submission_root.ThreatSubmissionRoot]:
        """
        Update threatSubmission
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[threat_submission_root.ThreatSubmissionRoot]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, threat_submission_root.ThreatSubmissionRoot, response_handler, error_mapping)
    
    def url_threats_by_id(self,id: str) -> url_threat_submission_item_request_builder.UrlThreatSubmissionItemRequestBuilder:
        """
        Provides operations to manage the urlThreats property of the microsoft.graph.security.threatSubmissionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: url_threat_submission_item_request_builder.UrlThreatSubmissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["urlThreatSubmission%2Did"] = id
        return url_threat_submission_item_request_builder.UrlThreatSubmissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ThreatSubmissionRequestBuilderGetQueryParameters():
        """
        Get threatSubmission
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class ThreatSubmissionRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ThreatSubmissionRequestBuilder.ThreatSubmissionRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ThreatSubmissionRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

