from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..models.audit_log_root import AuditLogRoot
    from ..models.o_data_errors.o_data_error import ODataError
    from .audit_activity_types.audit_activity_types_request_builder import AuditActivityTypesRequestBuilder
    from .custom_security_attribute_audits.custom_security_attribute_audits_request_builder import CustomSecurityAttributeAuditsRequestBuilder
    from .directory_audits.directory_audits_request_builder import DirectoryAuditsRequestBuilder
    from .directory_provisioning.directory_provisioning_request_builder import DirectoryProvisioningRequestBuilder
    from .get_summarized_m_s_i_sign_ins_with_aggregation_window.get_summarized_m_s_i_sign_ins_with_aggregation_window_request_builder import GetSummarizedMSISignInsWithAggregationWindowRequestBuilder
    from .get_summarized_non_interactive_sign_ins_with_aggregation_window.get_summarized_non_interactive_sign_ins_with_aggregation_window_request_builder import GetSummarizedNonInteractiveSignInsWithAggregationWindowRequestBuilder
    from .get_summarized_service_principal_sign_ins_with_aggregation_window.get_summarized_service_principal_sign_ins_with_aggregation_window_request_builder import GetSummarizedServicePrincipalSignInsWithAggregationWindowRequestBuilder
    from .provisioning.provisioning_request_builder import ProvisioningRequestBuilder
    from .sign_ins.sign_ins_request_builder import SignInsRequestBuilder
    from .sign_in_events_app_summary.sign_in_events_app_summary_request_builder import SignInEventsAppSummaryRequestBuilder
    from .sign_in_events_summary.sign_in_events_summary_request_builder import SignInEventsSummaryRequestBuilder
    from .sign_ups.sign_ups_request_builder import SignUpsRequestBuilder

class AuditLogsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the auditLogRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AuditLogsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/auditLogs{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AuditLogsRequestBuilderGetQueryParameters]] = None) -> Optional[AuditLogRoot]:
        """
        Get auditLogs
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuditLogRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.audit_log_root import AuditLogRoot

        return await self.request_adapter.send_async(request_info, AuditLogRoot, error_mapping)
    
    def get_summarized_m_s_i_sign_ins_with_aggregation_window(self,aggregation_window: str) -> GetSummarizedMSISignInsWithAggregationWindowRequestBuilder:
        """
        Provides operations to call the getSummarizedMSISignIns method.
        param aggregation_window: Usage: aggregationWindow='{aggregationWindow}'
        Returns: GetSummarizedMSISignInsWithAggregationWindowRequestBuilder
        """
        if aggregation_window is None:
            raise TypeError("aggregation_window cannot be null.")
        from .get_summarized_m_s_i_sign_ins_with_aggregation_window.get_summarized_m_s_i_sign_ins_with_aggregation_window_request_builder import GetSummarizedMSISignInsWithAggregationWindowRequestBuilder

        return GetSummarizedMSISignInsWithAggregationWindowRequestBuilder(self.request_adapter, self.path_parameters, aggregation_window)
    
    def get_summarized_non_interactive_sign_ins_with_aggregation_window(self,aggregation_window: str) -> GetSummarizedNonInteractiveSignInsWithAggregationWindowRequestBuilder:
        """
        Provides operations to call the getSummarizedNonInteractiveSignIns method.
        param aggregation_window: Usage: aggregationWindow='{aggregationWindow}'
        Returns: GetSummarizedNonInteractiveSignInsWithAggregationWindowRequestBuilder
        """
        if aggregation_window is None:
            raise TypeError("aggregation_window cannot be null.")
        from .get_summarized_non_interactive_sign_ins_with_aggregation_window.get_summarized_non_interactive_sign_ins_with_aggregation_window_request_builder import GetSummarizedNonInteractiveSignInsWithAggregationWindowRequestBuilder

        return GetSummarizedNonInteractiveSignInsWithAggregationWindowRequestBuilder(self.request_adapter, self.path_parameters, aggregation_window)
    
    def get_summarized_service_principal_sign_ins_with_aggregation_window(self,aggregation_window: str) -> GetSummarizedServicePrincipalSignInsWithAggregationWindowRequestBuilder:
        """
        Provides operations to call the getSummarizedServicePrincipalSignIns method.
        param aggregation_window: Usage: aggregationWindow='{aggregationWindow}'
        Returns: GetSummarizedServicePrincipalSignInsWithAggregationWindowRequestBuilder
        """
        if aggregation_window is None:
            raise TypeError("aggregation_window cannot be null.")
        from .get_summarized_service_principal_sign_ins_with_aggregation_window.get_summarized_service_principal_sign_ins_with_aggregation_window_request_builder import GetSummarizedServicePrincipalSignInsWithAggregationWindowRequestBuilder

        return GetSummarizedServicePrincipalSignInsWithAggregationWindowRequestBuilder(self.request_adapter, self.path_parameters, aggregation_window)
    
    async def patch(self,body: AuditLogRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AuditLogRoot]:
        """
        Update auditLogs
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuditLogRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.audit_log_root import AuditLogRoot

        return await self.request_adapter.send_async(request_info, AuditLogRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AuditLogsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get auditLogs
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: AuditLogRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update auditLogs
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
    
    def with_url(self,raw_url: str) -> AuditLogsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AuditLogsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AuditLogsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def audit_activity_types(self) -> AuditActivityTypesRequestBuilder:
        """
        Provides operations to manage the auditActivityTypes property of the microsoft.graph.auditLogRoot entity.
        """
        from .audit_activity_types.audit_activity_types_request_builder import AuditActivityTypesRequestBuilder

        return AuditActivityTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_security_attribute_audits(self) -> CustomSecurityAttributeAuditsRequestBuilder:
        """
        Provides operations to manage the customSecurityAttributeAudits property of the microsoft.graph.auditLogRoot entity.
        """
        from .custom_security_attribute_audits.custom_security_attribute_audits_request_builder import CustomSecurityAttributeAuditsRequestBuilder

        return CustomSecurityAttributeAuditsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_audits(self) -> DirectoryAuditsRequestBuilder:
        """
        Provides operations to manage the directoryAudits property of the microsoft.graph.auditLogRoot entity.
        """
        from .directory_audits.directory_audits_request_builder import DirectoryAuditsRequestBuilder

        return DirectoryAuditsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def directory_provisioning(self) -> DirectoryProvisioningRequestBuilder:
        """
        Provides operations to manage the directoryProvisioning property of the microsoft.graph.auditLogRoot entity.
        """
        from .directory_provisioning.directory_provisioning_request_builder import DirectoryProvisioningRequestBuilder

        return DirectoryProvisioningRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def provisioning(self) -> ProvisioningRequestBuilder:
        """
        Provides operations to manage the provisioning property of the microsoft.graph.auditLogRoot entity.
        """
        from .provisioning.provisioning_request_builder import ProvisioningRequestBuilder

        return ProvisioningRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_in_events_app_summary(self) -> SignInEventsAppSummaryRequestBuilder:
        """
        Provides operations to manage the signInEventsAppSummary property of the microsoft.graph.auditLogRoot entity.
        """
        from .sign_in_events_app_summary.sign_in_events_app_summary_request_builder import SignInEventsAppSummaryRequestBuilder

        return SignInEventsAppSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_in_events_summary(self) -> SignInEventsSummaryRequestBuilder:
        """
        Provides operations to manage the signInEventsSummary property of the microsoft.graph.auditLogRoot entity.
        """
        from .sign_in_events_summary.sign_in_events_summary_request_builder import SignInEventsSummaryRequestBuilder

        return SignInEventsSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_ins(self) -> SignInsRequestBuilder:
        """
        Provides operations to manage the signIns property of the microsoft.graph.auditLogRoot entity.
        """
        from .sign_ins.sign_ins_request_builder import SignInsRequestBuilder

        return SignInsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_ups(self) -> SignUpsRequestBuilder:
        """
        Provides operations to manage the signUps property of the microsoft.graph.auditLogRoot entity.
        """
        from .sign_ups.sign_ups_request_builder import SignUpsRequestBuilder

        return SignUpsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuditLogsRequestBuilderGetQueryParameters():
        """
        Get auditLogs
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class AuditLogsRequestBuilderGetRequestConfiguration(RequestConfiguration[AuditLogsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuditLogsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

