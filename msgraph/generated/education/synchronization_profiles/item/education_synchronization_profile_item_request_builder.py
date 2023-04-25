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
    from ....models import education_synchronization_profile
    from ....models.o_data_errors import o_data_error
    from .errors import errors_request_builder
    from .pause import pause_request_builder
    from .profile_status import profile_status_request_builder
    from .reset import reset_request_builder
    from .resume import resume_request_builder
    from .start import start_request_builder
    from .upload_url import upload_url_request_builder

class EducationSynchronizationProfileItemRequestBuilder():
    """
    Provides operations to manage the synchronizationProfiles property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationSynchronizationProfileItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/education/synchronizationProfiles/{educationSynchronizationProfile%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property synchronizationProfiles for education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[education_synchronization_profile.EducationSynchronizationProfile]:
        """
        Get synchronizationProfiles from education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[education_synchronization_profile.EducationSynchronizationProfile]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import education_synchronization_profile

        return await self.request_adapter.send_async(request_info, education_synchronization_profile.EducationSynchronizationProfile, error_mapping)
    
    async def patch(self,body: Optional[education_synchronization_profile.EducationSynchronizationProfile] = None, request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[education_synchronization_profile.EducationSynchronizationProfile]:
        """
        Update the navigation property synchronizationProfiles in education
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[education_synchronization_profile.EducationSynchronizationProfile]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import education_synchronization_profile

        return await self.request_adapter.send_async(request_info, education_synchronization_profile.EducationSynchronizationProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property synchronizationProfiles for education
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
    
    def to_get_request_information(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get synchronizationProfiles from education
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
    
    def to_patch_request_information(self,body: Optional[education_synchronization_profile.EducationSynchronizationProfile] = None, request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property synchronizationProfiles in education
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
    def errors(self) -> errors_request_builder.ErrorsRequestBuilder:
        """
        Provides operations to manage the errors property of the microsoft.graph.educationSynchronizationProfile entity.
        """
        from .errors import errors_request_builder

        return errors_request_builder.ErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pause(self) -> pause_request_builder.PauseRequestBuilder:
        """
        Provides operations to call the pause method.
        """
        from .pause import pause_request_builder

        return pause_request_builder.PauseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profile_status(self) -> profile_status_request_builder.ProfileStatusRequestBuilder:
        """
        Provides operations to manage the profileStatus property of the microsoft.graph.educationSynchronizationProfile entity.
        """
        from .profile_status import profile_status_request_builder

        return profile_status_request_builder.ProfileStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset(self) -> reset_request_builder.ResetRequestBuilder:
        """
        Provides operations to call the reset method.
        """
        from .reset import reset_request_builder

        return reset_request_builder.ResetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resume(self) -> resume_request_builder.ResumeRequestBuilder:
        """
        Provides operations to call the resume method.
        """
        from .resume import resume_request_builder

        return resume_request_builder.ResumeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> start_request_builder.StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start import start_request_builder

        return start_request_builder.StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_url(self) -> upload_url_request_builder.UploadUrlRequestBuilder:
        """
        Provides operations to call the uploadUrl method.
        """
        from .upload_url import upload_url_request_builder

        return upload_url_request_builder.UploadUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EducationSynchronizationProfileItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EducationSynchronizationProfileItemRequestBuilderGetQueryParameters():
        """
        Get synchronizationProfiles from education
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
    class EducationSynchronizationProfileItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EducationSynchronizationProfileItemRequestBuilder.EducationSynchronizationProfileItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EducationSynchronizationProfileItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

