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
from warnings import warn

if TYPE_CHECKING:
    from .....models.cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan
    from .....models.o_data_errors.o_data_error import ODataError

class CloudPcSharedUseServicePlanItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sharedUseServicePlans property of the microsoft.graph.virtualEndpoint entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CloudPcSharedUseServicePlanItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/sharedUseServicePlans/{cloudPcSharedUseServicePlan%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CloudPcSharedUseServicePlanItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property sharedUseServicePlans for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CloudPcSharedUseServicePlanItemRequestBuilderGetRequestConfiguration] = None) -> Optional[CloudPcSharedUseServicePlan]:
        """
        Read the properties and relationships of a cloudPcSharedUseServicePlan object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPcSharedUseServicePlan]
        Find more info here: https://learn.microsoft.com/graph/api/cloudpcshareduseserviceplan-get?view=graph-rest-1.0
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan

        return await self.request_adapter.send_async(request_info, CloudPcSharedUseServicePlan, error_mapping)
    
    async def patch(self,body: Optional[CloudPcSharedUseServicePlan] = None, request_configuration: Optional[CloudPcSharedUseServicePlanItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[CloudPcSharedUseServicePlan]:
        """
        Update the navigation property sharedUseServicePlans in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPcSharedUseServicePlan]
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_pc_shared_use_service_plan import CloudPcSharedUseServicePlan

        return await self.request_adapter.send_async(request_info, CloudPcSharedUseServicePlan, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CloudPcSharedUseServicePlanItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property sharedUseServicePlans for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/deviceManagement/virtualEndpoint/sharedUseServicePlans/{cloudPcSharedUseServicePlan%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CloudPcSharedUseServicePlanItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a cloudPcSharedUseServicePlan object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[CloudPcSharedUseServicePlan] = None, request_configuration: Optional[CloudPcSharedUseServicePlanItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sharedUseServicePlans in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/deviceManagement/virtualEndpoint/sharedUseServicePlans/{cloudPcSharedUseServicePlan%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CloudPcSharedUseServicePlanItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudPcSharedUseServicePlanItemRequestBuilder
        """
        warn("The sharedUseServicePlans property is deprecated and will not be supported starting Oct 8, 2023. This property will not be included as part of the API response. as of 2023-03/sharedUseServicePlans", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CloudPcSharedUseServicePlanItemRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPcSharedUseServicePlanItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CloudPcSharedUseServicePlanItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a cloudPcSharedUseServicePlan object.
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
    class CloudPcSharedUseServicePlanItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CloudPcSharedUseServicePlanItemRequestBuilder.CloudPcSharedUseServicePlanItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPcSharedUseServicePlanItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

