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
    from ....models.education_synchronization_profile import EducationSynchronizationProfile
    from ....models.o_data_errors.o_data_error import ODataError
    from .errors.errors_request_builder import ErrorsRequestBuilder
    from .pause.pause_request_builder import PauseRequestBuilder
    from .profile_status.profile_status_request_builder import ProfileStatusRequestBuilder
    from .reset.reset_request_builder import ResetRequestBuilder
    from .resume.resume_request_builder import ResumeRequestBuilder
    from .start.start_request_builder import StartRequestBuilder
    from .upload_url.upload_url_request_builder import UploadUrlRequestBuilder

class EducationSynchronizationProfileItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the synchronizationProfiles property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationSynchronizationProfileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/synchronizationProfiles/{educationSynchronizationProfile%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a school data synchronization profile in the tenant based on the identifier. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/educationsynchronizationprofile-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderGetRequestConfiguration] = None) -> Optional[EducationSynchronizationProfile]:
        """
        Retrieve a school data synchronization profile in the tenant based on the identifier. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSynchronizationProfile]
        Find more info here: https://learn.microsoft.com/graph/api/educationsynchronizationprofile-get?view=graph-rest-1.0
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
        from ....models.education_synchronization_profile import EducationSynchronizationProfile

        return await self.request_adapter.send_async(request_info, EducationSynchronizationProfile, error_mapping)
    
    async def patch(self,body: Optional[EducationSynchronizationProfile] = None, request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[EducationSynchronizationProfile]:
        """
        Update the navigation property synchronizationProfiles in education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationSynchronizationProfile]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.education_synchronization_profile import EducationSynchronizationProfile

        return await self.request_adapter.send_async(request_info, EducationSynchronizationProfile, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a school data synchronization profile in the tenant based on the identifier. This API is available in the following national cloud deployments.
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
        request_info.headers.try_add("Accept", "application/json, application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a school data synchronization profile in the tenant based on the identifier. This API is available in the following national cloud deployments.
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
    
    def to_patch_request_information(self,body: Optional[EducationSynchronizationProfile] = None, request_configuration: Optional[EducationSynchronizationProfileItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property synchronizationProfiles in education
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
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> EducationSynchronizationProfileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationSynchronizationProfileItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EducationSynchronizationProfileItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def errors(self) -> ErrorsRequestBuilder:
        """
        Provides operations to manage the errors property of the microsoft.graph.educationSynchronizationProfile entity.
        """
        from .errors.errors_request_builder import ErrorsRequestBuilder

        return ErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pause(self) -> PauseRequestBuilder:
        """
        Provides operations to call the pause method.
        """
        from .pause.pause_request_builder import PauseRequestBuilder

        return PauseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profile_status(self) -> ProfileStatusRequestBuilder:
        """
        Provides operations to manage the profileStatus property of the microsoft.graph.educationSynchronizationProfile entity.
        """
        from .profile_status.profile_status_request_builder import ProfileStatusRequestBuilder

        return ProfileStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset(self) -> ResetRequestBuilder:
        """
        Provides operations to call the reset method.
        """
        from .reset.reset_request_builder import ResetRequestBuilder

        return ResetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resume(self) -> ResumeRequestBuilder:
        """
        Provides operations to call the resume method.
        """
        from .resume.resume_request_builder import ResumeRequestBuilder

        return ResumeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> StartRequestBuilder:
        """
        Provides operations to call the start method.
        """
        from .start.start_request_builder import StartRequestBuilder

        return StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_url(self) -> UploadUrlRequestBuilder:
        """
        Provides operations to call the uploadUrl method.
        """
        from .upload_url.upload_url_request_builder import UploadUrlRequestBuilder

        return UploadUrlRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EducationSynchronizationProfileItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class EducationSynchronizationProfileItemRequestBuilderGetQueryParameters():
        """
        Retrieve a school data synchronization profile in the tenant based on the identifier. This API is available in the following national cloud deployments.
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
    class EducationSynchronizationProfileItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[EducationSynchronizationProfileItemRequestBuilder.EducationSynchronizationProfileItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class EducationSynchronizationProfileItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

