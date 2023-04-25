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
    from ..models import data_classification_service
    from ..models.o_data_errors import o_data_error
    from .classify_exact_matches import classify_exact_matches_request_builder
    from .classify_file import classify_file_request_builder
    from .classify_file_jobs import classify_file_jobs_request_builder
    from .classify_text_jobs import classify_text_jobs_request_builder
    from .evaluate_dlp_policies_jobs import evaluate_dlp_policies_jobs_request_builder
    from .evaluate_label_jobs import evaluate_label_jobs_request_builder
    from .exact_match_data_stores import exact_match_data_stores_request_builder
    from .exact_match_upload_agents import exact_match_upload_agents_request_builder
    from .jobs import jobs_request_builder
    from .sensitive_types import sensitive_types_request_builder
    from .sensitivity_labels import sensitivity_labels_request_builder

class DataClassificationRequestBuilder():
    """
    Provides operations to manage the dataClassificationService singleton.
    """
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
    
    async def get(self,request_configuration: Optional[DataClassificationRequestBuilderGetRequestConfiguration] = None) -> Optional[data_classification_service.DataClassificationService]:
        """
        Get dataClassification
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[data_classification_service.DataClassificationService]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import data_classification_service

        return await self.request_adapter.send_async(request_info, data_classification_service.DataClassificationService, error_mapping)
    
    async def patch(self,body: Optional[data_classification_service.DataClassificationService] = None, request_configuration: Optional[DataClassificationRequestBuilderPatchRequestConfiguration] = None) -> Optional[data_classification_service.DataClassificationService]:
        """
        Update dataClassification
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[data_classification_service.DataClassificationService]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import data_classification_service

        return await self.request_adapter.send_async(request_info, data_classification_service.DataClassificationService, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DataClassificationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[data_classification_service.DataClassificationService] = None, request_configuration: Optional[DataClassificationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def classify_exact_matches(self) -> classify_exact_matches_request_builder.ClassifyExactMatchesRequestBuilder:
        """
        Provides operations to call the classifyExactMatches method.
        """
        from .classify_exact_matches import classify_exact_matches_request_builder

        return classify_exact_matches_request_builder.ClassifyExactMatchesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_file(self) -> classify_file_request_builder.ClassifyFileRequestBuilder:
        """
        Provides operations to call the classifyFile method.
        """
        from .classify_file import classify_file_request_builder

        return classify_file_request_builder.ClassifyFileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_file_jobs(self) -> classify_file_jobs_request_builder.ClassifyFileJobsRequestBuilder:
        """
        Provides operations to manage the classifyFileJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .classify_file_jobs import classify_file_jobs_request_builder

        return classify_file_jobs_request_builder.ClassifyFileJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def classify_text_jobs(self) -> classify_text_jobs_request_builder.ClassifyTextJobsRequestBuilder:
        """
        Provides operations to manage the classifyTextJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .classify_text_jobs import classify_text_jobs_request_builder

        return classify_text_jobs_request_builder.ClassifyTextJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_dlp_policies_jobs(self) -> evaluate_dlp_policies_jobs_request_builder.EvaluateDlpPoliciesJobsRequestBuilder:
        """
        Provides operations to manage the evaluateDlpPoliciesJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .evaluate_dlp_policies_jobs import evaluate_dlp_policies_jobs_request_builder

        return evaluate_dlp_policies_jobs_request_builder.EvaluateDlpPoliciesJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def evaluate_label_jobs(self) -> evaluate_label_jobs_request_builder.EvaluateLabelJobsRequestBuilder:
        """
        Provides operations to manage the evaluateLabelJobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .evaluate_label_jobs import evaluate_label_jobs_request_builder

        return evaluate_label_jobs_request_builder.EvaluateLabelJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact_match_data_stores(self) -> exact_match_data_stores_request_builder.ExactMatchDataStoresRequestBuilder:
        """
        Provides operations to manage the exactMatchDataStores property of the microsoft.graph.dataClassificationService entity.
        """
        from .exact_match_data_stores import exact_match_data_stores_request_builder

        return exact_match_data_stores_request_builder.ExactMatchDataStoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exact_match_upload_agents(self) -> exact_match_upload_agents_request_builder.ExactMatchUploadAgentsRequestBuilder:
        """
        Provides operations to manage the exactMatchUploadAgents property of the microsoft.graph.dataClassificationService entity.
        """
        from .exact_match_upload_agents import exact_match_upload_agents_request_builder

        return exact_match_upload_agents_request_builder.ExactMatchUploadAgentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> jobs_request_builder.JobsRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.dataClassificationService entity.
        """
        from .jobs import jobs_request_builder

        return jobs_request_builder.JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitive_types(self) -> sensitive_types_request_builder.SensitiveTypesRequestBuilder:
        """
        Provides operations to manage the sensitiveTypes property of the microsoft.graph.dataClassificationService entity.
        """
        from .sensitive_types import sensitive_types_request_builder

        return sensitive_types_request_builder.SensitiveTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_labels(self) -> sensitivity_labels_request_builder.SensitivityLabelsRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.dataClassificationService entity.
        """
        from .sensitivity_labels import sensitivity_labels_request_builder

        return sensitivity_labels_request_builder.SensitivityLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DataClassificationRequestBuilderGetQueryParameters():
        """
        Get dataClassification
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
    class DataClassificationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

