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

access_review_instance = lazy_import('msgraph.generated.models.access_review_instance')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
accept_recommendations_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.accept_recommendations.accept_recommendations_request_builder')
apply_decisions_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.apply_decisions.apply_decisions_request_builder')
batch_record_decisions_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.batch_record_decisions.batch_record_decisions_request_builder')
contacted_reviewers_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.contacted_reviewers.contacted_reviewers_request_builder')
access_review_reviewer_item_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.contacted_reviewers.item.access_review_reviewer_item_request_builder')
decisions_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.decisions.decisions_request_builder')
access_review_instance_decision_item_item_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.decisions.item.access_review_instance_decision_item_item_request_builder')
definition_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.definition.definition_request_builder')
reset_decisions_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.reset_decisions.reset_decisions_request_builder')
send_reminder_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.send_reminder.send_reminder_request_builder')
stages_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.stages.stages_request_builder')
access_review_stage_item_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.stages.item.access_review_stage_item_request_builder')
stop_request_builder = lazy_import('msgraph.generated.users.item.pending_access_review_instances.item.stop.stop_request_builder')

class AccessReviewInstanceItemRequestBuilder():
    """
    Provides operations to manage the pendingAccessReviewInstances property of the microsoft.graph.user entity.
    """
    @property
    def accept_recommendations(self) -> accept_recommendations_request_builder.AcceptRecommendationsRequestBuilder:
        """
        Provides operations to call the acceptRecommendations method.
        """
        return accept_recommendations_request_builder.AcceptRecommendationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_decisions(self) -> apply_decisions_request_builder.ApplyDecisionsRequestBuilder:
        """
        Provides operations to call the applyDecisions method.
        """
        return apply_decisions_request_builder.ApplyDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def batch_record_decisions(self) -> batch_record_decisions_request_builder.BatchRecordDecisionsRequestBuilder:
        """
        Provides operations to call the batchRecordDecisions method.
        """
        return batch_record_decisions_request_builder.BatchRecordDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacted_reviewers(self) -> contacted_reviewers_request_builder.ContactedReviewersRequestBuilder:
        """
        Provides operations to manage the contactedReviewers property of the microsoft.graph.accessReviewInstance entity.
        """
        return contacted_reviewers_request_builder.ContactedReviewersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decisions(self) -> decisions_request_builder.DecisionsRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReviewInstance entity.
        """
        return decisions_request_builder.DecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def definition(self) -> definition_request_builder.DefinitionRequestBuilder:
        """
        Provides operations to manage the definition property of the microsoft.graph.accessReviewInstance entity.
        """
        return definition_request_builder.DefinitionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_decisions(self) -> reset_decisions_request_builder.ResetDecisionsRequestBuilder:
        """
        Provides operations to call the resetDecisions method.
        """
        return reset_decisions_request_builder.ResetDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_reminder(self) -> send_reminder_request_builder.SendReminderRequestBuilder:
        """
        Provides operations to call the sendReminder method.
        """
        return send_reminder_request_builder.SendReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stages(self) -> stages_request_builder.StagesRequestBuilder:
        """
        Provides operations to manage the stages property of the microsoft.graph.accessReviewInstance entity.
        """
        return stages_request_builder.StagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> stop_request_builder.StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        return stop_request_builder.StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewInstanceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/pendingAccessReviewInstances/{accessReviewInstance%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def contacted_reviewers_by_id(self,id: str) -> access_review_reviewer_item_request_builder.AccessReviewReviewerItemRequestBuilder:
        """
        Provides operations to manage the contactedReviewers property of the microsoft.graph.accessReviewInstance entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_reviewer_item_request_builder.AccessReviewReviewerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewReviewer%2Did"] = id
        return access_review_reviewer_item_request_builder.AccessReviewReviewerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def decisions_by_id(self,id: str) -> access_review_instance_decision_item_item_request_builder.AccessReviewInstanceDecisionItemItemRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReviewInstance entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_instance_decision_item_item_request_builder.AccessReviewInstanceDecisionItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewInstanceDecisionItem%2Did"] = id
        return access_review_instance_decision_item_item_request_builder.AccessReviewInstanceDecisionItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property pendingAccessReviewInstances for users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[access_review_instance.AccessReviewInstance]:
        """
        Navigation property to get list of access reviews pending approval by reviewer.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_review_instance.AccessReviewInstance]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, access_review_instance.AccessReviewInstance, error_mapping)
    
    async def patch(self,body: Optional[access_review_instance.AccessReviewInstance] = None, request_configuration: Optional[AccessReviewInstanceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[access_review_instance.AccessReviewInstance]:
        """
        Update the navigation property pendingAccessReviewInstances in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[access_review_instance.AccessReviewInstance]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, access_review_instance.AccessReviewInstance, error_mapping)
    
    def stages_by_id(self,id: str) -> access_review_stage_item_request_builder.AccessReviewStageItemRequestBuilder:
        """
        Provides operations to manage the stages property of the microsoft.graph.accessReviewInstance entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_stage_item_request_builder.AccessReviewStageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewStage%2Did"] = id
        return access_review_stage_item_request_builder.AccessReviewStageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property pendingAccessReviewInstances for users
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Navigation property to get list of access reviews pending approval by reviewer.
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
    
    def to_patch_request_information(self,body: Optional[access_review_instance.AccessReviewInstance] = None, request_configuration: Optional[AccessReviewInstanceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property pendingAccessReviewInstances in users
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
    
    @dataclass
    class AccessReviewInstanceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessReviewInstanceItemRequestBuilderGetQueryParameters():
        """
        Navigation property to get list of access reviews pending approval by reviewer.
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
    class AccessReviewInstanceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessReviewInstanceItemRequestBuilder.AccessReviewInstanceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessReviewInstanceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

