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

classify_exact_matches_request_builder = lazy_import('msgraph.generated.data_classification.classify_exact_matches.classify_exact_matches_request_builder')
classify_file_request_builder = lazy_import('msgraph.generated.data_classification.classify_file.classify_file_request_builder')
classify_file_jobs_request_builder = lazy_import('msgraph.generated.data_classification.classify_file_jobs.classify_file_jobs_request_builder')
job_response_base_item_request_builder = lazy_import('msgraph.generated.data_classification.classify_file_jobs.item.job_response_base_item_request_builder')
classify_text_jobs_request_builder = lazy_import('msgraph.generated.data_classification.classify_text_jobs.classify_text_jobs_request_builder')
job_response_base_item_request_builder = lazy_import('msgraph.generated.data_classification.classify_text_jobs.item.job_response_base_item_request_builder')
evaluate_dlp_policies_jobs_request_builder = lazy_import('msgraph.generated.data_classification.evaluate_dlp_policies_jobs.evaluate_dlp_policies_jobs_request_builder')
job_response_base_item_request_builder = lazy_import('msgraph.generated.data_classification.evaluate_dlp_policies_jobs.item.job_response_base_item_request_builder')
evaluate_label_jobs_request_builder = lazy_import('msgraph.generated.data_classification.evaluate_label_jobs.evaluate_label_jobs_request_builder')
job_response_base_item_request_builder = lazy_import('msgraph.generated.data_classification.evaluate_label_jobs.item.job_response_base_item_request_builder')
exact_match_data_stores_request_builder = lazy_import('msgraph.generated.data_classification.exact_match_data_stores.exact_match_data_stores_request_builder')
exact_match_data_store_item_request_builder = lazy_import('msgraph.generated.data_classification.exact_match_data_stores.item.exact_match_data_store_item_request_builder')
exact_match_upload_agents_request_builder = lazy_import('msgraph.generated.data_classification.exact_match_upload_agents.exact_match_upload_agents_request_builder')
exact_match_upload_agent_item_request_builder = lazy_import('msgraph.generated.data_classification.exact_match_upload_agents.item.exact_match_upload_agent_item_request_builder')
jobs_request_builder = lazy_import('msgraph.generated.data_classification.jobs.jobs_request_builder')
job_response_base_item_request_builder = lazy_import('msgraph.generated.data_classification.jobs.item.job_response_base_item_request_builder')
sensitive_types_request_builder = lazy_import('msgraph.generated.data_classification.sensitive_types.sensitive_types_request_builder')
sensitive_type_item_request_builder = lazy_import('msgraph.generated.data_classification.sensitive_types.item.sensitive_type_item_request_builder')
sensitivity_labels_request_builder = lazy_import('msgraph.generated.data_classification.sensitivity_labels.sensitivity_labels_request_builder')
sensitivity_label_item_request_builder = lazy_import('msgraph.generated.data_classification.sensitivity_labels.item.sensitivity_label_item_request_builder')
data_classification_service = lazy_import('msgraph.generated.models.data_classification_service')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DataClassificationRequestBuilder():
    """
    Provides operations to manage the dataClassificationService singleton.
    """
    @property
    def classify_exact_matches(self) -> classify_exact_matches_request_builder.ClassifyExactMatchesRequestBuilder:
        """
        Provides operations to call the classifyExactMatches method.
        """
        return classify_exact_matches_request_builder.ClassifyExactMatchesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_file(self) -> classify_file_request_builder.ClassifyFileRequestBuilder:
        """
        Provides operations to call the classifyFile method.
        """
        return classify_file_request_builder.ClassifyFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_file_jobs(self) -> classify_file_jobs_request_builder.ClassifyFileJobsRequestBuilder:
        """
        Provides operations to manage the classifyFileJobs property of the microsoft.graph.dataClassificationService entity.
        """
        return classify_file_jobs_request_builder.ClassifyFileJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_text_jobs(self) -> classify_text_jobs_request_builder.ClassifyTextJobsRequestBuilder:
        """
        Provides operations to manage the classifyTextJobs property of the microsoft.graph.dataClassificationService entity.
        """
        return classify_text_jobs_request_builder.ClassifyTextJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_dlp_policies_jobs(self) -> evaluate_dlp_policies_jobs_request_builder.EvaluateDlpPoliciesJobsRequestBuilder:
        """
        Provides operations to manage the evaluateDlpPoliciesJobs property of the microsoft.graph.dataClassificationService entity.
        """
        return evaluate_dlp_policies_jobs_request_builder.EvaluateDlpPoliciesJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_label_jobs(self) -> evaluate_label_jobs_request_builder.EvaluateLabelJobsRequestBuilder:
        """
        Provides operations to manage the evaluateLabelJobs property of the microsoft.graph.dataClassificationService entity.
        """
        return evaluate_label_jobs_request_builder.EvaluateLabelJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact_match_data_stores(self) -> exact_match_data_stores_request_builder.ExactMatchDataStoresRequestBuilder:
        """
        Provides operations to manage the exactMatchDataStores property of the microsoft.graph.dataClassificationService entity.
        """
        return exact_match_data_stores_request_builder.ExactMatchDataStoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact_match_upload_agents(self) -> exact_match_upload_agents_request_builder.ExactMatchUploadAgentsRequestBuilder:
        """
        Provides operations to manage the exactMatchUploadAgents property of the microsoft.graph.dataClassificationService entity.
        """
        return exact_match_upload_agents_request_builder.ExactMatchUploadAgentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> jobs_request_builder.JobsRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.dataClassificationService entity.
        """
        return jobs_request_builder.JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitive_types(self) -> sensitive_types_request_builder.SensitiveTypesRequestBuilder:
        """
        Provides operations to manage the sensitiveTypes property of the microsoft.graph.dataClassificationService entity.
        """
        return sensitive_types_request_builder.SensitiveTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_labels(self) -> sensitivity_labels_request_builder.SensitivityLabelsRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.dataClassificationService entity.
        """
        return sensitivity_labels_request_builder.SensitivityLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def classify_file_jobs_by_id(self,id: str) -> job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder:
        """
        Provides operations to manage the classifyFileJobs property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["jobResponseBase%2Did"] = id
        return job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def classify_text_jobs_by_id(self,id: str) -> job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder:
        """
        Provides operations to manage the classifyTextJobs property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["jobResponseBase%2Did"] = id
        return job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DataClassificationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/dataClassification{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[DataClassificationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get dataClassification
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
    
    def create_patch_request_information(self,body: Optional[data_classification_service.DataClassificationService] = None, request_configuration: Optional[DataClassificationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update dataClassification
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
    
    def evaluate_dlp_policies_jobs_by_id(self,id: str) -> job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder:
        """
        Provides operations to manage the evaluateDlpPoliciesJobs property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["jobResponseBase%2Did"] = id
        return job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def evaluate_label_jobs_by_id(self,id: str) -> job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder:
        """
        Provides operations to manage the evaluateLabelJobs property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["jobResponseBase%2Did"] = id
        return job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def exact_match_data_stores_by_id(self,id: str) -> exact_match_data_store_item_request_builder.ExactMatchDataStoreItemRequestBuilder:
        """
        Provides operations to manage the exactMatchDataStores property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: exact_match_data_store_item_request_builder.ExactMatchDataStoreItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["exactMatchDataStore%2Did"] = id
        return exact_match_data_store_item_request_builder.ExactMatchDataStoreItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def exact_match_upload_agents_by_id(self,id: str) -> exact_match_upload_agent_item_request_builder.ExactMatchUploadAgentItemRequestBuilder:
        """
        Provides operations to manage the exactMatchUploadAgents property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: exact_match_upload_agent_item_request_builder.ExactMatchUploadAgentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["exactMatchUploadAgent%2Did"] = id
        return exact_match_upload_agent_item_request_builder.ExactMatchUploadAgentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DataClassificationRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[data_classification_service.DataClassificationService]:
        """
        Get dataClassification
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[data_classification_service.DataClassificationService]
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
        return await self.request_adapter.send_async(request_info, data_classification_service.DataClassificationService, response_handler, error_mapping)
    
    def jobs_by_id(self,id: str) -> job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["jobResponseBase%2Did"] = id
        return job_response_base_item_request_builder.JobResponseBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[data_classification_service.DataClassificationService] = None, request_configuration: Optional[DataClassificationRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[data_classification_service.DataClassificationService]:
        """
        Update dataClassification
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[data_classification_service.DataClassificationService]
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
        return await self.request_adapter.send_async(request_info, data_classification_service.DataClassificationService, response_handler, error_mapping)
    
    def sensitive_types_by_id(self,id: str) -> sensitive_type_item_request_builder.SensitiveTypeItemRequestBuilder:
        """
        Provides operations to manage the sensitiveTypes property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: sensitive_type_item_request_builder.SensitiveTypeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sensitiveType%2Did"] = id
        return sensitive_type_item_request_builder.SensitiveTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sensitivity_labels_by_id(self,id: str) -> sensitivity_label_item_request_builder.SensitivityLabelItemRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.dataClassificationService entity.
        Args:
            id: Unique identifier of the item
        Returns: sensitivity_label_item_request_builder.SensitivityLabelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sensitivityLabel%2Did"] = id
        return sensitivity_label_item_request_builder.SensitivityLabelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DataClassificationRequestBuilderGetQueryParameters():
        """
        Get dataClassification
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
    class DataClassificationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DataClassificationRequestBuilder.DataClassificationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DataClassificationRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

