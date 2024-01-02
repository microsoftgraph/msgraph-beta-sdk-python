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
    from ..models.data_classification_service import DataClassificationService
    from ..models.o_data_errors.o_data_error import ODataError
    from .classify_exact_matches.classify_exact_matches_request_builder import ClassifyExactMatchesRequestBuilder
    from .classify_file.classify_file_request_builder import ClassifyFileRequestBuilder
    from .classify_file_jobs.classify_file_jobs_request_builder import ClassifyFileJobsRequestBuilder
    from .classify_text_jobs.classify_text_jobs_request_builder import ClassifyTextJobsRequestBuilder
    from .evaluate_dlp_policies_jobs.evaluate_dlp_policies_jobs_request_builder import EvaluateDlpPoliciesJobsRequestBuilder
    from .evaluate_label_jobs.evaluate_label_jobs_request_builder import EvaluateLabelJobsRequestBuilder
    from .exact_match_data_stores.exact_match_data_stores_request_builder import ExactMatchDataStoresRequestBuilder
    from .exact_match_upload_agents.exact_match_upload_agents_request_builder import ExactMatchUploadAgentsRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .sensitive_types.sensitive_types_request_builder import SensitiveTypesRequestBuilder
    from .sensitivity_labels.sensitivity_labels_request_builder import SensitivityLabelsRequestBuilder

class DataClassificationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the dataClassificationService singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DataClassificationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/dataClassification{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[DataClassificationRequestBuilderGetRequestConfiguration] = None) -> Optional[DataClassificationService]:
        """
        Get dataClassification
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DataClassificationService]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.data_classification_service import DataClassificationService

        return await self.request_adapter.send_async(request_info, DataClassificationService, error_mapping)
    
    async def patch(self,body: Optional[DataClassificationService] = None, request_configuration: Optional[DataClassificationRequestBuilderPatchRequestConfiguration] = None) -> Optional[DataClassificationService]:
        """
        Update dataClassification
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DataClassificationService]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.data_classification_service import DataClassificationService

        return await self.request_adapter.send_async(request_info, DataClassificationService, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DataClassificationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get dataClassification
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
    
    def to_patch_request_information(self,body: Optional[DataClassificationService] = None, request_configuration: Optional[DataClassificationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update dataClassification
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
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> DataClassificationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DataClassificationRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DataClassificationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def classify_exact_matches(self) -> ClassifyExactMatchesRequestBuilder:
        """
        Provides operations to call the classifyExactMatches method.
        """
        from .classify_exact_matches.classify_exact_matches_request_builder import ClassifyExactMatchesRequestBuilder

        return ClassifyExactMatchesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_file(self) -> ClassifyFileRequestBuilder:
        """
        Provides operations to call the classifyFile method.
        """
        from .classify_file.classify_file_request_builder import ClassifyFileRequestBuilder

        return ClassifyFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_file_jobs(self) -> ClassifyFileJobsRequestBuilder:
        """
        Provides operations to manage the classifyFileJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .classify_file_jobs.classify_file_jobs_request_builder import ClassifyFileJobsRequestBuilder

        return ClassifyFileJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_text_jobs(self) -> ClassifyTextJobsRequestBuilder:
        """
        Provides operations to manage the classifyTextJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .classify_text_jobs.classify_text_jobs_request_builder import ClassifyTextJobsRequestBuilder

        return ClassifyTextJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_dlp_policies_jobs(self) -> EvaluateDlpPoliciesJobsRequestBuilder:
        """
        Provides operations to manage the evaluateDlpPoliciesJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .evaluate_dlp_policies_jobs.evaluate_dlp_policies_jobs_request_builder import EvaluateDlpPoliciesJobsRequestBuilder

        return EvaluateDlpPoliciesJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_label_jobs(self) -> EvaluateLabelJobsRequestBuilder:
        """
        Provides operations to manage the evaluateLabelJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .evaluate_label_jobs.evaluate_label_jobs_request_builder import EvaluateLabelJobsRequestBuilder

        return EvaluateLabelJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact_match_data_stores(self) -> ExactMatchDataStoresRequestBuilder:
        """
        Provides operations to manage the exactMatchDataStores property of the microsoft.graph.dataClassificationService entity.
        """
        from .exact_match_data_stores.exact_match_data_stores_request_builder import ExactMatchDataStoresRequestBuilder

        return ExactMatchDataStoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact_match_upload_agents(self) -> ExactMatchUploadAgentsRequestBuilder:
        """
        Provides operations to manage the exactMatchUploadAgents property of the microsoft.graph.dataClassificationService entity.
        """
        from .exact_match_upload_agents.exact_match_upload_agents_request_builder import ExactMatchUploadAgentsRequestBuilder

        return ExactMatchUploadAgentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitive_types(self) -> SensitiveTypesRequestBuilder:
        """
        Provides operations to manage the sensitiveTypes property of the microsoft.graph.dataClassificationService entity.
        """
        from .sensitive_types.sensitive_types_request_builder import SensitiveTypesRequestBuilder

        return SensitiveTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_labels(self) -> SensitivityLabelsRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.dataClassificationService entity.
        """
        from .sensitivity_labels.sensitivity_labels_request_builder import SensitivityLabelsRequestBuilder

        return SensitivityLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DataClassificationRequestBuilderGetQueryParameters():
        """
        Get dataClassification
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
    class DataClassificationRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DataClassificationRequestBuilder.DataClassificationRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DataClassificationRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

