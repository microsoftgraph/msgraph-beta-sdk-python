from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.ediscovery.custodian import Custodian
    from .......models.o_data_errors.o_data_error import ODataError
    from .last_index_operation.last_index_operation_request_builder import LastIndexOperationRequestBuilder
    from .microsoft_graph_ediscovery_activate.microsoft_graph_ediscovery_activate_request_builder import MicrosoftGraphEdiscoveryActivateRequestBuilder
    from .microsoft_graph_ediscovery_apply_hold.microsoft_graph_ediscovery_apply_hold_request_builder import MicrosoftGraphEdiscoveryApplyHoldRequestBuilder
    from .microsoft_graph_ediscovery_release.microsoft_graph_ediscovery_release_request_builder import MicrosoftGraphEdiscoveryReleaseRequestBuilder
    from .microsoft_graph_ediscovery_remove_hold.microsoft_graph_ediscovery_remove_hold_request_builder import MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder
    from .microsoft_graph_ediscovery_update_index.microsoft_graph_ediscovery_update_index_request_builder import MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder
    from .site_sources.site_sources_request_builder import SiteSourcesRequestBuilder
    from .unified_group_sources.unified_group_sources_request_builder import UnifiedGroupSourcesRequestBuilder
    from .user_sources.user_sources_request_builder import UserSourcesRequestBuilder

class CustodianItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the custodians property of the microsoft.graph.ediscovery.case entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CustodianItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/custodians/{custodian%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CustodianItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property custodians for compliance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CustodianItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Custodian]:
        """
        Read the properties and relationships of a custodian object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Custodian]
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery.custodian import Custodian

        return await self.request_adapter.send_async(request_info, Custodian, error_mapping)
    
    async def patch(self,body: Optional[Custodian] = None, request_configuration: Optional[CustodianItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Custodian]:
        """
        Update the properties of a custodian object. This API is available in the following national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Custodian]
        Find more info here: https://learn.microsoft.com/graph/api/ediscovery-custodian-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.ediscovery.custodian import Custodian

        return await self.request_adapter.send_async(request_info, Custodian, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CustodianItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property custodians for compliance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CustodianItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a custodian object. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json;q=1")
        return request_info
    
    def to_patch_request_information(self,body: Optional[Custodian] = None, request_configuration: Optional[CustodianItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a custodian object. This API is available in the following national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CustodianItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CustodianItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CustodianItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def last_index_operation(self) -> LastIndexOperationRequestBuilder:
        """
        Provides operations to manage the lastIndexOperation property of the microsoft.graph.ediscovery.dataSourceContainer entity.
        """
        from .last_index_operation.last_index_operation_request_builder import LastIndexOperationRequestBuilder

        return LastIndexOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_activate(self) -> MicrosoftGraphEdiscoveryActivateRequestBuilder:
        """
        Provides operations to call the activate method.
        """
        from .microsoft_graph_ediscovery_activate.microsoft_graph_ediscovery_activate_request_builder import MicrosoftGraphEdiscoveryActivateRequestBuilder

        return MicrosoftGraphEdiscoveryActivateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_apply_hold(self) -> MicrosoftGraphEdiscoveryApplyHoldRequestBuilder:
        """
        Provides operations to call the applyHold method.
        """
        from .microsoft_graph_ediscovery_apply_hold.microsoft_graph_ediscovery_apply_hold_request_builder import MicrosoftGraphEdiscoveryApplyHoldRequestBuilder

        return MicrosoftGraphEdiscoveryApplyHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_release(self) -> MicrosoftGraphEdiscoveryReleaseRequestBuilder:
        """
        Provides operations to call the release method.
        """
        from .microsoft_graph_ediscovery_release.microsoft_graph_ediscovery_release_request_builder import MicrosoftGraphEdiscoveryReleaseRequestBuilder

        return MicrosoftGraphEdiscoveryReleaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_remove_hold(self) -> MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder:
        """
        Provides operations to call the removeHold method.
        """
        from .microsoft_graph_ediscovery_remove_hold.microsoft_graph_ediscovery_remove_hold_request_builder import MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder

        return MicrosoftGraphEdiscoveryRemoveHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_ediscovery_update_index(self) -> MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder:
        """
        Provides operations to call the updateIndex method.
        """
        from .microsoft_graph_ediscovery_update_index.microsoft_graph_ediscovery_update_index_request_builder import MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder

        return MicrosoftGraphEdiscoveryUpdateIndexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site_sources(self) -> SiteSourcesRequestBuilder:
        """
        Provides operations to manage the siteSources property of the microsoft.graph.ediscovery.custodian entity.
        """
        from .site_sources.site_sources_request_builder import SiteSourcesRequestBuilder

        return SiteSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unified_group_sources(self) -> UnifiedGroupSourcesRequestBuilder:
        """
        Provides operations to manage the unifiedGroupSources property of the microsoft.graph.ediscovery.custodian entity.
        """
        from .unified_group_sources.unified_group_sources_request_builder import UnifiedGroupSourcesRequestBuilder

        return UnifiedGroupSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_sources(self) -> UserSourcesRequestBuilder:
        """
        Provides operations to manage the userSources property of the microsoft.graph.ediscovery.custodian entity.
        """
        from .user_sources.user_sources_request_builder import UserSourcesRequestBuilder

        return UserSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CustodianItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CustodianItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a custodian object. This API is available in the following national cloud deployments.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CustodianItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CustodianItemRequestBuilder.CustodianItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CustodianItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

