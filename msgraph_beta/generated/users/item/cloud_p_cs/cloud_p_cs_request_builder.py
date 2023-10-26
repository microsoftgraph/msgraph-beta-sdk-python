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
    from ....models.cloud_p_c import CloudPC
    from ....models.cloud_p_c_collection_response import CloudPCCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .bulk_resize.bulk_resize_request_builder import BulkResizeRequestBuilder
    from .count.count_request_builder import CountRequestBuilder
    from .get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id.get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id_request_builder import GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder
    from .item.cloud_p_c_item_request_builder import CloudPCItemRequestBuilder
    from .validate_bulk_resize.validate_bulk_resize_request_builder import ValidateBulkResizeRequestBuilder

class CloudPCsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CloudPCsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/cloudPCs{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_cloud_p_c_id(self,cloud_p_c_id: str) -> CloudPCItemRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
        param cloud_p_c_id: The unique identifier of cloudPC
        Returns: CloudPCItemRequestBuilder
        """
        if not cloud_p_c_id:
            raise TypeError("cloud_p_c_id cannot be null.")
        from .item.cloud_p_c_item_request_builder import CloudPCItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["cloudPC%2Did"] = cloud_p_c_id
        return CloudPCItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[CloudPCsRequestBuilderGetRequestConfiguration] = None) -> Optional[CloudPCCollectionResponse]:
        """
        List the cloudPC devices that are attributed to the signed-in user.  This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPCCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/user-list-cloudpcs?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cloud_p_c_collection_response import CloudPCCollectionResponse

        return await self.request_adapter.send_async(request_info, CloudPCCollectionResponse, error_mapping)
    
    def get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id(self,group_id: Optional[str] = None, service_plan_id: Optional[str] = None) -> GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder:
        """
        Provides operations to call the getProvisionedCloudPCs method.
        param group_id: Usage: groupId='{groupId}'
        param service_plan_id: Usage: servicePlanId='{servicePlanId}'
        Returns: GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder
        """
        if not group_id:
            raise TypeError("group_id cannot be null.")
        if not service_plan_id:
            raise TypeError("service_plan_id cannot be null.")
        from .get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id.get_provisioned_cloud_p_cs_with_group_id_with_service_plan_id_request_builder import GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder

        return GetProvisionedCloudPCsWithGroupIdWithServicePlanIdRequestBuilder(self.request_adapter, self.path_parameters, group_id, service_plan_id)
    
    async def post(self,body: Optional[CloudPC] = None, request_configuration: Optional[CloudPCsRequestBuilderPostRequestConfiguration] = None) -> Optional[CloudPC]:
        """
        Create new navigation property to cloudPCs for users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[CloudPCsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List the cloudPC devices that are attributed to the signed-in user.  This API is available in the following national cloud deployments.
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
    
    def to_post_request_information(self,body: Optional[CloudPC] = None, request_configuration: Optional[CloudPCsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to cloudPCs for users
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CloudPCsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudPCsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CloudPCsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulk_resize(self) -> BulkResizeRequestBuilder:
        """
        Provides operations to call the bulkResize method.
        """
        from .bulk_resize.bulk_resize_request_builder import BulkResizeRequestBuilder

        return BulkResizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_bulk_resize(self) -> ValidateBulkResizeRequestBuilder:
        """
        Provides operations to call the validateBulkResize method.
        """
        from .validate_bulk_resize.validate_bulk_resize_request_builder import ValidateBulkResizeRequestBuilder

        return ValidateBulkResizeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CloudPCsRequestBuilderGetQueryParameters():
        """
        List the cloudPC devices that are attributed to the signed-in user.  This API is available in the following national cloud deployments.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CloudPCsRequestBuilder.CloudPCsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

