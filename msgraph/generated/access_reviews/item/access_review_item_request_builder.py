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

apply_decisions_request_builder = lazy_import('msgraph.generated.access_reviews.item.apply_decisions.apply_decisions_request_builder')
decisions_request_builder = lazy_import('msgraph.generated.access_reviews.item.decisions.decisions_request_builder')
access_review_decision_item_request_builder = lazy_import('msgraph.generated.access_reviews.item.decisions.item.access_review_decision_item_request_builder')
instances_request_builder = lazy_import('msgraph.generated.access_reviews.item.instances.instances_request_builder')
access_review_item_request_builder = lazy_import('msgraph.generated.access_reviews.item.instances.item.access_review_item_request_builder')
my_decisions_request_builder = lazy_import('msgraph.generated.access_reviews.item.my_decisions.my_decisions_request_builder')
access_review_decision_item_request_builder = lazy_import('msgraph.generated.access_reviews.item.my_decisions.item.access_review_decision_item_request_builder')
reset_decisions_request_builder = lazy_import('msgraph.generated.access_reviews.item.reset_decisions.reset_decisions_request_builder')
reviewers_request_builder = lazy_import('msgraph.generated.access_reviews.item.reviewers.reviewers_request_builder')
access_review_reviewer_item_request_builder = lazy_import('msgraph.generated.access_reviews.item.reviewers.item.access_review_reviewer_item_request_builder')
send_reminder_request_builder = lazy_import('msgraph.generated.access_reviews.item.send_reminder.send_reminder_request_builder')
stop_request_builder = lazy_import('msgraph.generated.access_reviews.item.stop.stop_request_builder')
access_review = lazy_import('msgraph.generated.models.access_review')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AccessReviewItemRequestBuilder():
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def apply_decisions(self) -> apply_decisions_request_builder.ApplyDecisionsRequestBuilder:
        """
        Provides operations to call the applyDecisions method.
        """
        return apply_decisions_request_builder.ApplyDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decisions(self) -> decisions_request_builder.DecisionsRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReview entity.
        """
        return decisions_request_builder.DecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def instances(self) -> instances_request_builder.InstancesRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.accessReview entity.
        """
        return instances_request_builder.InstancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def my_decisions(self) -> my_decisions_request_builder.MyDecisionsRequestBuilder:
        """
        Provides operations to manage the myDecisions property of the microsoft.graph.accessReview entity.
        """
        return my_decisions_request_builder.MyDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_decisions(self) -> reset_decisions_request_builder.ResetDecisionsRequestBuilder:
        """
        Provides operations to call the resetDecisions method.
        """
        return reset_decisions_request_builder.ResetDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reviewers(self) -> reviewers_request_builder.ReviewersRequestBuilder:
        """
        Provides operations to manage the reviewers property of the microsoft.graph.accessReview entity.
        """
        return reviewers_request_builder.ReviewersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_reminder(self) -> send_reminder_request_builder.SendReminderRequestBuilder:
        """
        Provides operations to call the sendReminder method.
        """
        return send_reminder_request_builder.SendReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> stop_request_builder.StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        return stop_request_builder.StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/accessReviews/{accessReview%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AccessReviewItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        In the Azure AD access reviews feature, delete an accessReview object.
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
    
    def create_get_request_information(self,request_configuration: Optional[AccessReviewItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        In the Azure AD access reviews feature, retrieve an accessReview object.   To retrieve the reviewers of the access review, use the list accessReview reviewers API. To retrieve the decisions of the access review, use the list accessReview decisions API, or the list my accessReview decisions API. If this is a recurring access review, no decisions will be associated with the recurring access review series. Instead, use the `instances` relationship of that series to retrieve an accessReview collection of the past, current, and future instances of the access review. Each past and current instance will have decisions.
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
    
    def create_patch_request_information(self,body: Optional[access_review.AccessReview] = None, request_configuration: Optional[AccessReviewItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        In the Azure AD access reviews feature, update an existing accessReview object to change one or more of its properties. This API is not intended to change the reviewers or decisions of a review.  To change the reviewers, use the addReviewer or removeReviewer APIs.  To stop an already-started one-time review, or an already-started instance of a recurring review, early, use the stop API. To apply the decisions to the target group or app access rights, use the apply API. 
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
    
    def decisions_by_id(self,id: str) -> access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReview entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewDecision%2Did"] = id
        return access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[AccessReviewItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        In the Azure AD access reviews feature, delete an accessReview object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessReviewItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[access_review.AccessReview]:
        """
        In the Azure AD access reviews feature, retrieve an accessReview object.   To retrieve the reviewers of the access review, use the list accessReview reviewers API. To retrieve the decisions of the access review, use the list accessReview decisions API, or the list my accessReview decisions API. If this is a recurring access review, no decisions will be associated with the recurring access review series. Instead, use the `instances` relationship of that series to retrieve an accessReview collection of the past, current, and future instances of the access review. Each past and current instance will have decisions.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[access_review.AccessReview]
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
        return await self.request_adapter.send_async(request_info, access_review.AccessReview, response_handler, error_mapping)
    
    def instances_by_id(self,id: str) -> AccessReviewItemRequestBuilder:
        """
        Provides operations to manage the instances property of the microsoft.graph.accessReview entity.
        Args:
            id: Unique identifier of the item
        Returns: AccessReviewItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReview%2Did1"] = id
        return AccessReviewItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def my_decisions_by_id(self,id: str) -> access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder:
        """
        Provides operations to manage the myDecisions property of the microsoft.graph.accessReview entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewDecision%2Did"] = id
        return access_review_decision_item_request_builder.AccessReviewDecisionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[access_review.AccessReview] = None, request_configuration: Optional[AccessReviewItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[access_review.AccessReview]:
        """
        In the Azure AD access reviews feature, update an existing accessReview object to change one or more of its properties. This API is not intended to change the reviewers or decisions of a review.  To change the reviewers, use the addReviewer or removeReviewer APIs.  To stop an already-started one-time review, or an already-started instance of a recurring review, early, use the stop API. To apply the decisions to the target group or app access rights, use the apply API. 
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[access_review.AccessReview]
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
        return await self.request_adapter.send_async(request_info, access_review.AccessReview, response_handler, error_mapping)
    
    def reviewers_by_id(self,id: str) -> access_review_reviewer_item_request_builder.AccessReviewReviewerItemRequestBuilder:
        """
        Provides operations to manage the reviewers property of the microsoft.graph.accessReview entity.
        Args:
            id: Unique identifier of the item
        Returns: access_review_reviewer_item_request_builder.AccessReviewReviewerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["accessReviewReviewer%2Did"] = id
        return access_review_reviewer_item_request_builder.AccessReviewReviewerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class AccessReviewItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AccessReviewItemRequestBuilderGetQueryParameters():
        """
        In the Azure AD access reviews feature, retrieve an accessReview object.   To retrieve the reviewers of the access review, use the list accessReview reviewers API. To retrieve the decisions of the access review, use the list accessReview decisions API, or the list my accessReview decisions API. If this is a recurring access review, no decisions will be associated with the recurring access review series. Instead, use the `instances` relationship of that series to retrieve an accessReview collection of the past, current, and future instances of the access review. Each past and current instance will have decisions.
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
    class AccessReviewItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AccessReviewItemRequestBuilder.AccessReviewItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AccessReviewItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

