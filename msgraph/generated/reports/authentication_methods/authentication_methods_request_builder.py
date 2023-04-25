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
    from ...models import authentication_methods_root
    from ...models.o_data_errors import o_data_error
    from .user_registration_details import user_registration_details_request_builder
    from .users_registered_by_feature import users_registered_by_feature_request_builder
    from .users_registered_by_feature_with_included_user_types_with_included_user_roles import users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder
    from .users_registered_by_method import users_registered_by_method_request_builder
    from .users_registered_by_method_with_included_user_types_with_included_user_roles import users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder

class AuthenticationMethodsRequestBuilder():
    """
    Provides operations to manage the authenticationMethods property of the microsoft.graph.reportRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuthenticationMethodsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/reports/authenticationMethods{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property authenticationMethods for reports
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
    
    async def get(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderGetRequestConfiguration] = None) -> Optional[authentication_methods_root.AuthenticationMethodsRoot]:
        """
        Container for navigation properties for Azure AD authentication methods resources.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[authentication_methods_root.AuthenticationMethodsRoot]
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
        from ...models import authentication_methods_root

        return await self.request_adapter.send_async(request_info, authentication_methods_root.AuthenticationMethodsRoot, error_mapping)
    
    async def patch(self,body: Optional[authentication_methods_root.AuthenticationMethodsRoot] = None, request_configuration: Optional[AuthenticationMethodsRequestBuilderPatchRequestConfiguration] = None) -> Optional[authentication_methods_root.AuthenticationMethodsRoot]:
        """
        Update the navigation property authenticationMethods in reports
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[authentication_methods_root.AuthenticationMethodsRoot]
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
        from ...models import authentication_methods_root

        return await self.request_adapter.send_async(request_info, authentication_methods_root.AuthenticationMethodsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property authenticationMethods for reports
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
    
    def to_get_request_information(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Container for navigation properties for Azure AD authentication methods resources.
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
    
    def to_patch_request_information(self,body: Optional[authentication_methods_root.AuthenticationMethodsRoot] = None, request_configuration: Optional[AuthenticationMethodsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property authenticationMethods in reports
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
    
    def users_registered_by_feature_with_included_user_types_with_included_user_roles(self,included_user_roles: Optional[str] = None, included_user_types: Optional[str] = None) -> users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder.UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder:
        """
        Provides operations to call the usersRegisteredByFeature method.
        Args:
            includedUserRoles: Usage: includedUserRoles='{includedUserRoles}'
            includedUserTypes: Usage: includedUserTypes='{includedUserTypes}'
        Returns: users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder.UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
        """
        if included_user_roles is None:
            raise Exception("included_user_roles cannot be undefined")
        if included_user_types is None:
            raise Exception("included_user_types cannot be undefined")
        from .users_registered_by_feature_with_included_user_types_with_included_user_roles import users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder

        return users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder.UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder(self.request_adapter, self.path_parameters, included_user_roles, included_user_types)
    
    def users_registered_by_method_with_included_user_types_with_included_user_roles(self,included_user_roles: Optional[str] = None, included_user_types: Optional[str] = None) -> users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder.UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder:
        """
        Provides operations to call the usersRegisteredByMethod method.
        Args:
            includedUserRoles: Usage: includedUserRoles='{includedUserRoles}'
            includedUserTypes: Usage: includedUserTypes='{includedUserTypes}'
        Returns: users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder.UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
        """
        if included_user_roles is None:
            raise Exception("included_user_roles cannot be undefined")
        if included_user_types is None:
            raise Exception("included_user_types cannot be undefined")
        from .users_registered_by_method_with_included_user_types_with_included_user_roles import users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder

        return users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder.UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder(self.request_adapter, self.path_parameters, included_user_roles, included_user_types)
    
    @property
    def user_registration_details(self) -> user_registration_details_request_builder.UserRegistrationDetailsRequestBuilder:
        """
        Provides operations to manage the userRegistrationDetails property of the microsoft.graph.authenticationMethodsRoot entity.
        """
        from .user_registration_details import user_registration_details_request_builder

        return user_registration_details_request_builder.UserRegistrationDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users_registered_by_feature(self) -> users_registered_by_feature_request_builder.UsersRegisteredByFeatureRequestBuilder:
        """
        Provides operations to call the usersRegisteredByFeature method.
        """
        from .users_registered_by_feature import users_registered_by_feature_request_builder

        return users_registered_by_feature_request_builder.UsersRegisteredByFeatureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users_registered_by_method(self) -> users_registered_by_method_request_builder.UsersRegisteredByMethodRequestBuilder:
        """
        Provides operations to call the usersRegisteredByMethod method.
        """
        from .users_registered_by_method import users_registered_by_method_request_builder

        return users_registered_by_method_request_builder.UsersRegisteredByMethodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationMethodsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AuthenticationMethodsRequestBuilderGetQueryParameters():
        """
        Container for navigation properties for Azure AD authentication methods resources.
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
    class AuthenticationMethodsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AuthenticationMethodsRequestBuilder.AuthenticationMethodsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AuthenticationMethodsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

