from __future__ import annotations
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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.password_validation_information import PasswordValidationInformation
    from .validate_password_post_request_body import ValidatePasswordPostRequestBody

class ValidatePasswordRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the validatePassword method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ValidatePasswordRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/validatePassword", path_parameters)
    
    async def post(self,body: Optional[ValidatePasswordPostRequestBody] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[PasswordValidationInformation]:
        """
        Check a user's password against the organization's password validation policy and report whether the password is valid. Use this action to provide real-time feedback on password strength while the user types their password.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PasswordValidationInformation]
        Find more info here: https://learn.microsoft.com/graph/api/user-validatepassword?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.password_validation_information import PasswordValidationInformation

        return await self.request_adapter.send_async(request_info, PasswordValidationInformation, error_mapping)
    
    def to_post_request_information(self,body: Optional[ValidatePasswordPostRequestBody] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Check a user's password against the organization's password validation policy and report whether the password is valid. Use this action to provide real-time feedback on password strength while the user types their password.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ValidatePasswordRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ValidatePasswordRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ValidatePasswordRequestBuilder(self.request_adapter, raw_url)
    

