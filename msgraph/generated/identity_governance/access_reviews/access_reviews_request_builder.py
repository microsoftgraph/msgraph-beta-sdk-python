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
    from ...models import access_review_set
    from ...models.o_data_errors import o_data_error
    from .decisions import decisions_request_builder
    from .decisions.item import access_review_instance_decision_item_item_request_builder
    from .definitions import definitions_request_builder
    from .definitions.item import access_review_schedule_definition_item_request_builder
    from .history_definitions import history_definitions_request_builder
    from .history_definitions.item import access_review_history_definition_item_request_builder
    from .policy import policy_request_builder

class AccessReviewsRequestBuilder():
    """
    Provides operations to manage the accessReviews property of the microsoft.graph.identityGovernance entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/accessReviews{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def decisions_by_id(self,id: str) -> access_review_instance_decision_item_item_request_builder.AccessReviewInstanceDecisionItemItemRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReviewSet entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_instance_decision_item_item_request_builder.AccessReviewInstanceDecisionItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .decisions.item import access_review_instance_decision_item_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewInstanceDecisionItem%2Did"] = id
        return access_review_instance_decision_item_item_request_builder.AccessReviewInstanceDecisionItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def definitions_by_id(self,id: str) -> access_review_schedule_definition_item_request_builder.AccessReviewScheduleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the definitions property of the microsoft.graph.accessReviewSet entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_schedule_definition_item_request_builder.AccessReviewScheduleDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .definitions.item import access_review_schedule_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewScheduleDefinition%2Did"] = id
        return access_review_schedule_definition_item_request_builder.AccessReviewScheduleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[AccessReviewsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property accessReviews for identityGovernance
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
    
    async def get(self,request_configuration: Optional[AccessReviewsRequestBuilderGetRequestConfiguration] = None) -> Optional[access_review_set.AccessReviewSet]:
        """
        Get accessReviews from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_review_set.AccessReviewSet]
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
        from ...models import access_review_set

        return await self.request_adapter.send_async(request_info, access_review_set.AccessReviewSet, error_mapping)
    
    def history_definitions_by_id(self,id: str) -> access_review_history_definition_item_request_builder.AccessReviewHistoryDefinitionItemRequestBuilder:
        """
        Provides operations to manage the historyDefinitions property of the microsoft.graph.accessReviewSet entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_history_definition_item_request_builder.AccessReviewHistoryDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .history_definitions.item import access_review_history_definition_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewHistoryDefinition%2Did"] = id
        return access_review_history_definition_item_request_builder.AccessReviewHistoryDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[access_review_set.AccessReviewSet] = None, request_configuration: Optional[AccessReviewsRequestBuilderPatchRequestConfiguration] = None) -> Optional[access_review_set.AccessReviewSet]:
        """
        Update the navigation property accessReviews in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_review_set.AccessReviewSet]
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
        from ...models import access_review_set

        return await self.request_adapter.send_async(request_info, access_review_set.AccessReviewSet, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessReviewsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property accessReviews for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessReviewsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get accessReviews from identityGovernance
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
    
    def to_patch_request_information(self,body: Optional[access_review_set.AccessReviewSet] = None, request_configuration: Optional[AccessReviewsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property accessReviews in identityGovernance
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
    def decisions(self) -> decisions_request_builder.DecisionsRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReviewSet entity.
        """
        from .decisions import decisions_request_builder

        return decisions_request_builder.DecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definitions(self) -> definitions_request_builder.DefinitionsRequestBuilder:
        """
        Provides operations to manage the definitions property of the microsoft.graph.accessReviewSet entity.
        """
        from .definitions import definitions_request_builder

        return definitions_request_builder.DefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history_definitions(self) -> history_definitions_request_builder.HistoryDefinitionsRequestBuilder:
        """
        Provides operations to manage the historyDefinitions property of the microsoft.graph.accessReviewSet entity.
        """
        from .history_definitions import history_definitions_request_builder

        return history_definitions_request_builder.HistoryDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy(self) -> policy_request_builder.PolicyRequestBuilder:
        """
        Provides operations to manage the policy property of the microsoft.graph.accessReviewSet entity.
        """
        from .policy import policy_request_builder

        return policy_request_builder.PolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AccessReviewsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessReviewsRequestBuilderGetQueryParameters():
        """
        Get accessReviews from identityGovernance
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
    class AccessReviewsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessReviewsRequestBuilder.AccessReviewsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessReviewsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

