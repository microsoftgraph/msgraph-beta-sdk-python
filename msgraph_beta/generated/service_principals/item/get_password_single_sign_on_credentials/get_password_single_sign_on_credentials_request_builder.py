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
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.password_single_sign_on_credential_set import PasswordSingleSignOnCredentialSet
    from .get_password_single_sign_on_credentials_post_request_body import GetPasswordSingleSignOnCredentialsPostRequestBody

class GetPasswordSingleSignOnCredentialsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getPasswordSingleSignOnCredentials method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GetPasswordSingleSignOnCredentialsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/getPasswordSingleSignOnCredentials", path_parameters)
    
    async def post(self,body: Optional[GetPasswordSingleSignOnCredentialsPostRequestBody] = None, request_configuration: Optional[GetPasswordSingleSignOnCredentialsRequestBuilderPostRequestConfiguration] = None) -> Optional[PasswordSingleSignOnCredentialSet]:
        """
        Get a list of single sign-on credentials using a password for a user or group. This API is available in the following national cloud deployments.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PasswordSingleSignOnCredentialSet]
        Find more info here: https://learn.microsoft.com/graph/api/serviceprincipal-getpasswordsinglesignoncredentials?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.password_single_sign_on_credential_set import PasswordSingleSignOnCredentialSet

        return await self.request_adapter.send_async(request_info, PasswordSingleSignOnCredentialSet, error_mapping)
    
    def to_post_request_information(self,body: Optional[GetPasswordSingleSignOnCredentialsPostRequestBody] = None, request_configuration: Optional[GetPasswordSingleSignOnCredentialsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Get a list of single sign-on credentials using a password for a user or group. This API is available in the following national cloud deployments.
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json;q=1")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GetPasswordSingleSignOnCredentialsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetPasswordSingleSignOnCredentialsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GetPasswordSingleSignOnCredentialsRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class GetPasswordSingleSignOnCredentialsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

