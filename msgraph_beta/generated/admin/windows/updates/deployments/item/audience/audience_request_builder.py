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
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.windows_updates.deployment_audience import DeploymentAudience
    from .applicable_content.applicable_content_request_builder import ApplicableContentRequestBuilder
    from .exclusions.exclusions_request_builder import ExclusionsRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder
    from .microsoft_graph_windows_updates_update_audience.microsoft_graph_windows_updates_update_audience_request_builder import MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder
    from .microsoft_graph_windows_updates_update_audience_by_id.microsoft_graph_windows_updates_update_audience_by_id_request_builder import MicrosoftGraphWindowsUpdatesUpdateAudienceByIdRequestBuilder

class AudienceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the audience property of the microsoft.graph.windowsUpdates.deployment entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AudienceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/windows/updates/deployments/{deployment%2Did}/audience{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property audience for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AudienceRequestBuilderGetQueryParameters]] = None) -> Optional[DeploymentAudience]:
        """
        Specifies the audience to which content is deployed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeploymentAudience]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.windows_updates.deployment_audience import DeploymentAudience

        return await self.request_adapter.send_async(request_info, DeploymentAudience, error_mapping)
    
    async def patch(self,body: DeploymentAudience, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeploymentAudience]:
        """
        Update the navigation property audience in admin
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeploymentAudience]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.windows_updates.deployment_audience import DeploymentAudience

        return await self.request_adapter.send_async(request_info, DeploymentAudience, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property audience for admin
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AudienceRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Specifies the audience to which content is deployed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeploymentAudience, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property audience in admin
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
    
    def with_url(self,raw_url: str) -> AudienceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AudienceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AudienceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def applicable_content(self) -> ApplicableContentRequestBuilder:
        """
        Provides operations to manage the applicableContent property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        from .applicable_content.applicable_content_request_builder import ApplicableContentRequestBuilder

        return ApplicableContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exclusions(self) -> ExclusionsRequestBuilder:
        """
        Provides operations to manage the exclusions property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        from .exclusions.exclusions_request_builder import ExclusionsRequestBuilder

        return ExclusionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.windowsUpdates.deploymentAudience entity.
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_windows_updates_update_audience(self) -> MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder:
        """
        Provides operations to call the updateAudience method.
        """
        from .microsoft_graph_windows_updates_update_audience.microsoft_graph_windows_updates_update_audience_request_builder import MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder

        return MicrosoftGraphWindowsUpdatesUpdateAudienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_windows_updates_update_audience_by_id(self) -> MicrosoftGraphWindowsUpdatesUpdateAudienceByIdRequestBuilder:
        """
        Provides operations to call the updateAudienceById method.
        """
        from .microsoft_graph_windows_updates_update_audience_by_id.microsoft_graph_windows_updates_update_audience_by_id_request_builder import MicrosoftGraphWindowsUpdatesUpdateAudienceByIdRequestBuilder

        return MicrosoftGraphWindowsUpdatesUpdateAudienceByIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AudienceRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AudienceRequestBuilderGetQueryParameters():
        """
        Specifies the audience to which content is deployed.
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
    class AudienceRequestBuilderGetRequestConfiguration(RequestConfiguration[AudienceRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AudienceRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

