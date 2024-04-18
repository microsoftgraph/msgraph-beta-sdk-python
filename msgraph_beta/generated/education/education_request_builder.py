from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.education_root import EducationRoot
    from ..models.o_data_errors.o_data_error import ODataError
    from .classes.classes_request_builder import ClassesRequestBuilder
    from .me.me_request_builder import MeRequestBuilder
    from .schools.schools_request_builder import SchoolsRequestBuilder
    from .synchronization_profiles.synchronization_profiles_request_builder import SynchronizationProfilesRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder

class EducationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the educationRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EducationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[EducationRoot]:
        """
        Get education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.education_root import EducationRoot

        return await self.request_adapter.send_async(request_info, EducationRoot, error_mapping)
    
    async def patch(self,body: Optional[EducationRoot] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[EducationRoot]:
        """
        Update education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EducationRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.education_root import EducationRoot

        return await self.request_adapter.send_async(request_info, EducationRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get education
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[EducationRoot] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update education
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> EducationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EducationRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return EducationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def classes(self) -> ClassesRequestBuilder:
        """
        Provides operations to manage the classes property of the microsoft.graph.educationRoot entity.
        """
        from .classes.classes_request_builder import ClassesRequestBuilder

        return ClassesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def me(self) -> MeRequestBuilder:
        """
        Provides operations to manage the me property of the microsoft.graph.educationRoot entity.
        """
        from .me.me_request_builder import MeRequestBuilder

        return MeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schools(self) -> SchoolsRequestBuilder:
        """
        Provides operations to manage the schools property of the microsoft.graph.educationRoot entity.
        """
        from .schools.schools_request_builder import SchoolsRequestBuilder

        return SchoolsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def synchronization_profiles(self) -> SynchronizationProfilesRequestBuilder:
        """
        Provides operations to manage the synchronizationProfiles property of the microsoft.graph.educationRoot entity.
        """
        from .synchronization_profiles.synchronization_profiles_request_builder import SynchronizationProfilesRequestBuilder

        return SynchronizationProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        Provides operations to manage the users property of the microsoft.graph.educationRoot entity.
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EducationRequestBuilderGetQueryParameters():
        """
        Get education
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

    

