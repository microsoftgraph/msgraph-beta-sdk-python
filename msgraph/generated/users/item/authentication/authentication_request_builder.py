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
    from ....models import authentication
    from ....models.o_data_errors import o_data_error
    from .email_methods import email_methods_request_builder
    from .email_methods.item import email_authentication_method_item_request_builder
    from .fido2_methods import fido2_methods_request_builder
    from .fido2_methods.item import fido2_authentication_method_item_request_builder
    from .methods import methods_request_builder
    from .methods.item import authentication_method_item_request_builder
    from .microsoft_authenticator_methods import microsoft_authenticator_methods_request_builder
    from .microsoft_authenticator_methods.item import microsoft_authenticator_authentication_method_item_request_builder
    from .operations import operations_request_builder
    from .operations.item import long_running_operation_item_request_builder
    from .passwordless_microsoft_authenticator_methods import passwordless_microsoft_authenticator_methods_request_builder
    from .passwordless_microsoft_authenticator_methods.item import passwordless_microsoft_authenticator_authentication_method_item_request_builder
    from .password_methods import password_methods_request_builder
    from .password_methods.item import password_authentication_method_item_request_builder
    from .phone_methods import phone_methods_request_builder
    from .phone_methods.item import phone_authentication_method_item_request_builder
    from .software_oath_methods import software_oath_methods_request_builder
    from .software_oath_methods.item import software_oath_authentication_method_item_request_builder
    from .temporary_access_pass_methods import temporary_access_pass_methods_request_builder
    from .temporary_access_pass_methods.item import temporary_access_pass_authentication_method_item_request_builder
    from .windows_hello_for_business_methods import windows_hello_for_business_methods_request_builder
    from .windows_hello_for_business_methods.item import windows_hello_for_business_authentication_method_item_request_builder

class AuthenticationRequestBuilder():
    """
    Provides operations to manage the authentication property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuthenticationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/authentication{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AuthenticationRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property authentication for users
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
    
    def email_methods_by_id(self,id: str) -> email_authentication_method_item_request_builder.EmailAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the emailMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: email_authentication_method_item_request_builder.EmailAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .email_methods.item import email_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["emailAuthenticationMethod%2Did"] = id
        return email_authentication_method_item_request_builder.EmailAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def fido2_methods_by_id(self,id: str) -> fido2_authentication_method_item_request_builder.Fido2AuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the fido2Methods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: fido2_authentication_method_item_request_builder.Fido2AuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .fido2_methods.item import fido2_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fido2AuthenticationMethod%2Did"] = id
        return fido2_authentication_method_item_request_builder.Fido2AuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AuthenticationRequestBuilderGetRequestConfiguration] = None) -> Optional[authentication.Authentication]:
        """
        Get authentication from users
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[authentication.Authentication]
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
        from ....models import authentication

        return await self.request_adapter.send_async(request_info, authentication.Authentication, error_mapping)
    
    def methods_by_id(self,id: str) -> authentication_method_item_request_builder.AuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the methods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: authentication_method_item_request_builder.AuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .methods.item import authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationMethod%2Did"] = id
        return authentication_method_item_request_builder.AuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_authenticator_methods_by_id(self,id: str) -> microsoft_authenticator_authentication_method_item_request_builder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: microsoft_authenticator_authentication_method_item_request_builder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .microsoft_authenticator_methods.item import microsoft_authenticator_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["microsoftAuthenticatorAuthenticationMethod%2Did"] = id
        return microsoft_authenticator_authentication_method_item_request_builder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .operations.item import long_running_operation_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["longRunningOperation%2Did"] = id
        return long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def passwordless_microsoft_authenticator_methods_by_id(self,id: str) -> passwordless_microsoft_authenticator_authentication_method_item_request_builder.PasswordlessMicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the passwordlessMicrosoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: passwordless_microsoft_authenticator_authentication_method_item_request_builder.PasswordlessMicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .passwordless_microsoft_authenticator_methods.item import passwordless_microsoft_authenticator_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["passwordlessMicrosoftAuthenticatorAuthenticationMethod%2Did"] = id
        return passwordless_microsoft_authenticator_authentication_method_item_request_builder.PasswordlessMicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def password_methods_by_id(self,id: str) -> password_authentication_method_item_request_builder.PasswordAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the passwordMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: password_authentication_method_item_request_builder.PasswordAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .password_methods.item import password_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["passwordAuthenticationMethod%2Did"] = id
        return password_authentication_method_item_request_builder.PasswordAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[authentication.Authentication] = None, request_configuration: Optional[AuthenticationRequestBuilderPatchRequestConfiguration] = None) -> Optional[authentication.Authentication]:
        """
        Update the navigation property authentication in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[authentication.Authentication]
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
        from ....models import authentication

        return await self.request_adapter.send_async(request_info, authentication.Authentication, error_mapping)
    
    def phone_methods_by_id(self,id: str) -> phone_authentication_method_item_request_builder.PhoneAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: phone_authentication_method_item_request_builder.PhoneAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .phone_methods.item import phone_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["phoneAuthenticationMethod%2Did"] = id
        return phone_authentication_method_item_request_builder.PhoneAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def software_oath_methods_by_id(self,id: str) -> software_oath_authentication_method_item_request_builder.SoftwareOathAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the softwareOathMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: software_oath_authentication_method_item_request_builder.SoftwareOathAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .software_oath_methods.item import software_oath_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["softwareOathAuthenticationMethod%2Did"] = id
        return software_oath_authentication_method_item_request_builder.SoftwareOathAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def temporary_access_pass_methods_by_id(self,id: str) -> temporary_access_pass_authentication_method_item_request_builder.TemporaryAccessPassAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the temporaryAccessPassMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: temporary_access_pass_authentication_method_item_request_builder.TemporaryAccessPassAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .temporary_access_pass_methods.item import temporary_access_pass_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["temporaryAccessPassAuthenticationMethod%2Did"] = id
        return temporary_access_pass_authentication_method_item_request_builder.TemporaryAccessPassAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[AuthenticationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property authentication for users
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
    
    def to_get_request_information(self,request_configuration: Optional[AuthenticationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get authentication from users
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
    
    def to_patch_request_information(self,body: Optional[authentication.Authentication] = None, request_configuration: Optional[AuthenticationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property authentication in users
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
    
    def windows_hello_for_business_methods_by_id(self,id: str) -> windows_hello_for_business_authentication_method_item_request_builder.WindowsHelloForBusinessAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the windowsHelloForBusinessMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_hello_for_business_authentication_method_item_request_builder.WindowsHelloForBusinessAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .windows_hello_for_business_methods.item import windows_hello_for_business_authentication_method_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsHelloForBusinessAuthenticationMethod%2Did"] = id
        return windows_hello_for_business_authentication_method_item_request_builder.WindowsHelloForBusinessAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def email_methods(self) -> email_methods_request_builder.EmailMethodsRequestBuilder:
        """
        Provides operations to manage the emailMethods property of the microsoft.graph.authentication entity.
        """
        from .email_methods import email_methods_request_builder

        return email_methods_request_builder.EmailMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fido2_methods(self) -> fido2_methods_request_builder.Fido2MethodsRequestBuilder:
        """
        Provides operations to manage the fido2Methods property of the microsoft.graph.authentication entity.
        """
        from .fido2_methods import fido2_methods_request_builder

        return fido2_methods_request_builder.Fido2MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def methods(self) -> methods_request_builder.MethodsRequestBuilder:
        """
        Provides operations to manage the methods property of the microsoft.graph.authentication entity.
        """
        from .methods import methods_request_builder

        return methods_request_builder.MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_authenticator_methods(self) -> microsoft_authenticator_methods_request_builder.MicrosoftAuthenticatorMethodsRequestBuilder:
        """
        Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        """
        from .microsoft_authenticator_methods import microsoft_authenticator_methods_request_builder

        return microsoft_authenticator_methods_request_builder.MicrosoftAuthenticatorMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.authentication entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passwordless_microsoft_authenticator_methods(self) -> passwordless_microsoft_authenticator_methods_request_builder.PasswordlessMicrosoftAuthenticatorMethodsRequestBuilder:
        """
        Provides operations to manage the passwordlessMicrosoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        """
        from .passwordless_microsoft_authenticator_methods import passwordless_microsoft_authenticator_methods_request_builder

        return passwordless_microsoft_authenticator_methods_request_builder.PasswordlessMicrosoftAuthenticatorMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password_methods(self) -> password_methods_request_builder.PasswordMethodsRequestBuilder:
        """
        Provides operations to manage the passwordMethods property of the microsoft.graph.authentication entity.
        """
        from .password_methods import password_methods_request_builder

        return password_methods_request_builder.PasswordMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone_methods(self) -> phone_methods_request_builder.PhoneMethodsRequestBuilder:
        """
        Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
        """
        from .phone_methods import phone_methods_request_builder

        return phone_methods_request_builder.PhoneMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_oath_methods(self) -> software_oath_methods_request_builder.SoftwareOathMethodsRequestBuilder:
        """
        Provides operations to manage the softwareOathMethods property of the microsoft.graph.authentication entity.
        """
        from .software_oath_methods import software_oath_methods_request_builder

        return software_oath_methods_request_builder.SoftwareOathMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def temporary_access_pass_methods(self) -> temporary_access_pass_methods_request_builder.TemporaryAccessPassMethodsRequestBuilder:
        """
        Provides operations to manage the temporaryAccessPassMethods property of the microsoft.graph.authentication entity.
        """
        from .temporary_access_pass_methods import temporary_access_pass_methods_request_builder

        return temporary_access_pass_methods_request_builder.TemporaryAccessPassMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_hello_for_business_methods(self) -> windows_hello_for_business_methods_request_builder.WindowsHelloForBusinessMethodsRequestBuilder:
        """
        Provides operations to manage the windowsHelloForBusinessMethods property of the microsoft.graph.authentication entity.
        """
        from .windows_hello_for_business_methods import windows_hello_for_business_methods_request_builder

        return windows_hello_for_business_methods_request_builder.WindowsHelloForBusinessMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AuthenticationRequestBuilderGetQueryParameters():
        """
        Get authentication from users
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
    class AuthenticationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AuthenticationRequestBuilder.AuthenticationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AuthenticationRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

