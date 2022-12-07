from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

generate_apple_push_notification_certificate_signing_request_response = lazy_import('msgraph.generated.device_management.apple_push_notification_certificate.generate_apple_push_notification_certificate_signing_request.generate_apple_push_notification_certificate_signing_request_response')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class GenerateApplePushNotificationCertificateSigningRequestRequestBuilder():
    """
    Provides operations to call the generateApplePushNotificationCertificateSigningRequest method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GenerateApplePushNotificationCertificateSigningRequestRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/applePushNotificationCertificate/microsoft.graph.generateApplePushNotificationCertificateSigningRequest"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_post_request_information(self,request_configuration: Optional[GenerateApplePushNotificationCertificateSigningRequestRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Download Apple push notification certificate signing request
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    async def post(self,request_configuration: Optional[GenerateApplePushNotificationCertificateSigningRequestRequestBuilderPostRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[generate_apple_push_notification_certificate_signing_request_response.GenerateApplePushNotificationCertificateSigningRequestResponse]:
        """
        Download Apple push notification certificate signing request
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[generate_apple_push_notification_certificate_signing_request_response.GenerateApplePushNotificationCertificateSigningRequestResponse]
        """
        request_info = self.create_post_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, generate_apple_push_notification_certificate_signing_request_response.GenerateApplePushNotificationCertificateSigningRequestResponse, response_handler, error_mapping)
    
    @dataclass
    class GenerateApplePushNotificationCertificateSigningRequestRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

