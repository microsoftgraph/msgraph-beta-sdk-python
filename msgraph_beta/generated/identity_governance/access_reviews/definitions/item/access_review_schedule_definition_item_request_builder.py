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
    from .....models.access_review_schedule_definition import AccessReviewScheduleDefinition
    from .....models.o_data_errors.o_data_error import ODataError
    from .instances.instances_request_builder import InstancesRequestBuilder
    from .stop.stop_request_builder import StopRequestBuilder

class AccessReviewScheduleDefinitionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the definitions property of the microsoft.graph.accessReviewSet entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewScheduleDefinitionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/definitions/{accessReviewScheduleDefinition%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AccessReviewScheduleDefinitionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete an accessReviewScheduleDefinition object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/accessreviewscheduledefinition-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessReviewScheduleDefinitionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessReviewScheduleDefinition]:
        """
        Retrieve an accessReviewScheduleDefinition object by ID. This returns all properties of the scheduled access review series except for the associated accessReviewInstances. Each accessReviewScheduleDefinition has at least one instance. An instance represents a review for a specific resource (such as a particular group's members), during one occurrence (for example, March 2021) of a recurring review. To retrieve the instances of the access review series, use the list accessReviewInstance API.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewScheduleDefinition]
        Find more info here: https://learn.microsoft.com/graph/api/accessreviewscheduledefinition-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_review_schedule_definition import AccessReviewScheduleDefinition

        return await self.request_adapter.send_async(request_info, AccessReviewScheduleDefinition, error_mapping)
    
    async def put(self,body: Optional[AccessReviewScheduleDefinition] = None, request_configuration: Optional[AccessReviewScheduleDefinitionItemRequestBuilderPutRequestConfiguration] = None) -> Optional[AccessReviewScheduleDefinition]:
        """
        Update the navigation property definitions in identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewScheduleDefinition]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.access_review_schedule_definition import AccessReviewScheduleDefinition

        return await self.request_adapter.send_async(request_info, AccessReviewScheduleDefinition, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessReviewScheduleDefinitionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete an accessReviewScheduleDefinition object.
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[AccessReviewScheduleDefinitionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve an accessReviewScheduleDefinition object by ID. This returns all properties of the scheduled access review series except for the associated accessReviewInstances. Each accessReviewScheduleDefinition has at least one instance. An instance represents a review for a specific resource (such as a particular group's members), during one occurrence (for example, March 2021) of a recurring review. To retrieve the instances of the access review series, use the list accessReviewInstance API.
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: Optional[AccessReviewScheduleDefinition] = None, request_configuration: Optional[AccessReviewScheduleDefinitionItemRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property definitions in identityGovernance
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
        request_info.http_method = Method.PUT
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessReviewScheduleDefinitionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessReviewScheduleDefinitionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AccessReviewScheduleDefinitionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def instances(self) -> InstancesRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.accessReviewScheduleDefinition entity.
        """
        from .instances.instances_request_builder import InstancesRequestBuilder

        return InstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        from .stop.stop_request_builder import StopRequestBuilder

        return StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessReviewScheduleDefinitionItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AccessReviewScheduleDefinitionItemRequestBuilderGetQueryParameters():
        """
        Retrieve an accessReviewScheduleDefinition object by ID. This returns all properties of the scheduled access review series except for the associated accessReviewInstances. Each accessReviewScheduleDefinition has at least one instance. An instance represents a review for a specific resource (such as a particular group's members), during one occurrence (for example, March 2021) of a recurring review. To retrieve the instances of the access review series, use the list accessReviewInstance API.
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
    class AccessReviewScheduleDefinitionItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessReviewScheduleDefinitionItemRequestBuilder.AccessReviewScheduleDefinitionItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessReviewScheduleDefinitionItemRequestBuilderPutRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

