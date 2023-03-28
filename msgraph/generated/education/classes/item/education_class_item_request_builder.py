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
    from ....models import education_class
    from ....models.o_data_errors import o_data_error
    from .assignment_categories import assignment_categories_request_builder
    from .assignment_categories.item import education_category_item_request_builder
    from .assignment_defaults import assignment_defaults_request_builder
    from .assignments import assignments_request_builder
    from .assignments.item import education_assignment_item_request_builder
    from .assignment_settings import assignment_settings_request_builder
    from .group import group_request_builder
    from .members import members_request_builder
    from .members.item import education_user_item_request_builder
    from .schools import schools_request_builder
    from .schools.item import education_school_item_request_builder
    from .teachers import teachers_request_builder
    from .teachers.item import education_user_item_request_builder

class EducationClassItemRequestBuilder():
    """
    Provides operations to manage the classes property of the microsoft.graph.educationRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EducationClassItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/education/classes/{educationClass%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def assignment_categories_by_id(self,id: str) -> education_category_item_request_builder.EducationCategoryItemRequestBuilder:
        """
        Provides operations to manage the assignmentCategories property of the microsoft.graph.educationClass entity.
        Args:
            id: Unique identifier of the item
        Returns: education_category_item_request_builder.EducationCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignment_categories.item import education_category_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationCategory%2Did"] = id
        return education_category_item_request_builder.EducationCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def assignments_by_id(self,id: str) -> education_assignment_item_request_builder.EducationAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.educationClass entity.
        Args:
            id: Unique identifier of the item
        Returns: education_assignment_item_request_builder.EducationAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .assignments.item import education_assignment_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationAssignment%2Did"] = id
        return education_assignment_item_request_builder.EducationAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[EducationClassItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property classes for education
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
    
    async def get(self,request_configuration: Optional[EducationClassItemRequestBuilderGetRequestConfiguration] = None) -> Optional[education_class.EducationClass]:
        """
        Get classes from education
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[education_class.EducationClass]
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
        from ....models import education_class

        return await self.request_adapter.send_async(request_info, education_class.EducationClass, error_mapping)
    
    def members_by_id(self,id: str) -> education_user_item_request_builder.EducationUserItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.education.classes.item.members.item collection
        Args:
            id: Unique identifier of the item
        Returns: education_user_item_request_builder.EducationUserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .members.item import education_user_item_request_builder
        from .teachers.item import education_user_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationUser%2Did"] = id
        return education_user_item_request_builder.EducationUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[education_class.EducationClass] = None, request_configuration: Optional[EducationClassItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[education_class.EducationClass]:
        """
        Update the navigation property classes in education
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[education_class.EducationClass]
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
        from ....models import education_class

        return await self.request_adapter.send_async(request_info, education_class.EducationClass, error_mapping)
    
    def schools_by_id(self,id: str) -> education_school_item_request_builder.EducationSchoolItemRequestBuilder:
        """
        Provides operations to manage the schools property of the microsoft.graph.educationClass entity.
        Args:
            id: Unique identifier of the item
        Returns: education_school_item_request_builder.EducationSchoolItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .schools.item import education_school_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationSchool%2Did"] = id
        return education_school_item_request_builder.EducationSchoolItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def teachers_by_id(self,id: str) -> education_user_item_request_builder.EducationUserItemRequestBuilder:
        """
        Gets an item from the msgraph.generated.education.classes.item.teachers.item collection
        Args:
            id: Unique identifier of the item
        Returns: education_user_item_request_builder.EducationUserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .members.item import education_user_item_request_builder
        from .teachers.item import education_user_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["educationUser%2Did"] = id
        return education_user_item_request_builder.EducationUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[EducationClassItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property classes for education
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
    
    def to_get_request_information(self,request_configuration: Optional[EducationClassItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get classes from education
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
    
    def to_patch_request_information(self,body: Optional[education_class.EducationClass] = None, request_configuration: Optional[EducationClassItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property classes in education
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
    def assignment_categories(self) -> assignment_categories_request_builder.AssignmentCategoriesRequestBuilder:
        """
        Provides operations to manage the assignmentCategories property of the microsoft.graph.educationClass entity.
        """
        from .assignment_categories import assignment_categories_request_builder

        return assignment_categories_request_builder.AssignmentCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_defaults(self) -> assignment_defaults_request_builder.AssignmentDefaultsRequestBuilder:
        """
        Provides operations to manage the assignmentDefaults property of the microsoft.graph.educationClass entity.
        """
        from .assignment_defaults import assignment_defaults_request_builder

        return assignment_defaults_request_builder.AssignmentDefaultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.educationClass entity.
        """
        from .assignments import assignments_request_builder

        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignment_settings(self) -> assignment_settings_request_builder.AssignmentSettingsRequestBuilder:
        """
        Provides operations to manage the assignmentSettings property of the microsoft.graph.educationClass entity.
        """
        from .assignment_settings import assignment_settings_request_builder

        return assignment_settings_request_builder.AssignmentSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def group(self) -> group_request_builder.GroupRequestBuilder:
        """
        Provides operations to manage the group property of the microsoft.graph.educationClass entity.
        """
        from .group import group_request_builder

        return group_request_builder.GroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> members_request_builder.MembersRequestBuilder:
        """
        Provides operations to manage the members property of the microsoft.graph.educationClass entity.
        """
        from .members import members_request_builder

        return members_request_builder.MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def schools(self) -> schools_request_builder.SchoolsRequestBuilder:
        """
        Provides operations to manage the schools property of the microsoft.graph.educationClass entity.
        """
        from .schools import schools_request_builder

        return schools_request_builder.SchoolsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teachers(self) -> teachers_request_builder.TeachersRequestBuilder:
        """
        Provides operations to manage the teachers property of the microsoft.graph.educationClass entity.
        """
        from .teachers import teachers_request_builder

        return teachers_request_builder.TeachersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EducationClassItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EducationClassItemRequestBuilderGetQueryParameters():
        """
        Get classes from education
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
    class EducationClassItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EducationClassItemRequestBuilder.EducationClassItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EducationClassItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

