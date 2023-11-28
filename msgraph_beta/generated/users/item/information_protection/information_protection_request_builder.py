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
    from ....models.information_protection import InformationProtection
    from ....models.o_data_errors.o_data_error import ODataError
    from .bitlocker.bitlocker_request_builder import BitlockerRequestBuilder
    from .data_loss_prevention_policies.data_loss_prevention_policies_request_builder import DataLossPreventionPoliciesRequestBuilder
    from .decrypt_buffer.decrypt_buffer_request_builder import DecryptBufferRequestBuilder
    from .encrypt_buffer.encrypt_buffer_request_builder import EncryptBufferRequestBuilder
    from .policy.policy_request_builder import PolicyRequestBuilder
    from .sensitivity_labels.sensitivity_labels_request_builder import SensitivityLabelsRequestBuilder
    from .sensitivity_policy_settings.sensitivity_policy_settings_request_builder import SensitivityPolicySettingsRequestBuilder
    from .sign_digest.sign_digest_request_builder import SignDigestRequestBuilder
    from .threat_assessment_requests.threat_assessment_requests_request_builder import ThreatAssessmentRequestsRequestBuilder
    from .verify_signature.verify_signature_request_builder import VerifySignatureRequestBuilder

class InformationProtectionRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the informationProtection property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InformationProtectionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/informationProtection{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[InformationProtectionRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property informationProtection for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
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
    
    async def get(self,request_configuration: Optional[InformationProtectionRequestBuilderGetRequestConfiguration] = None) -> Optional[InformationProtection]:
        """
        Get informationProtection from users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InformationProtection]
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
        from ....models.information_protection import InformationProtection

        return await self.request_adapter.send_async(request_info, InformationProtection, error_mapping)
    
    async def patch(self,body: Optional[InformationProtection] = None, request_configuration: Optional[InformationProtectionRequestBuilderPatchRequestConfiguration] = None) -> Optional[InformationProtection]:
        """
        Update the navigation property informationProtection in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InformationProtection]
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
        from ....models.information_protection import InformationProtection

        return await self.request_adapter.send_async(request_info, InformationProtection, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[InformationProtectionRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property informationProtection for users
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[InformationProtectionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get informationProtection from users
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
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[InformationProtection] = None, request_configuration: Optional[InformationProtectionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property informationProtection in users
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
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> InformationProtectionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InformationProtectionRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return InformationProtectionRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bitlocker(self) -> BitlockerRequestBuilder:
        """
        Provides operations to manage the bitlocker property of the microsoft.graph.informationProtection entity.
        """
        from .bitlocker.bitlocker_request_builder import BitlockerRequestBuilder

        return BitlockerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_loss_prevention_policies(self) -> DataLossPreventionPoliciesRequestBuilder:
        """
        Provides operations to manage the dataLossPreventionPolicies property of the microsoft.graph.informationProtection entity.
        """
        from .data_loss_prevention_policies.data_loss_prevention_policies_request_builder import DataLossPreventionPoliciesRequestBuilder

        return DataLossPreventionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decrypt_buffer(self) -> DecryptBufferRequestBuilder:
        """
        Provides operations to call the decryptBuffer method.
        """
        from .decrypt_buffer.decrypt_buffer_request_builder import DecryptBufferRequestBuilder

        return DecryptBufferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def encrypt_buffer(self) -> EncryptBufferRequestBuilder:
        """
        Provides operations to call the encryptBuffer method.
        """
        from .encrypt_buffer.encrypt_buffer_request_builder import EncryptBufferRequestBuilder

        return EncryptBufferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy(self) -> PolicyRequestBuilder:
        """
        Provides operations to manage the policy property of the microsoft.graph.informationProtection entity.
        """
        from .policy.policy_request_builder import PolicyRequestBuilder

        return PolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_labels(self) -> SensitivityLabelsRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.informationProtection entity.
        """
        from .sensitivity_labels.sensitivity_labels_request_builder import SensitivityLabelsRequestBuilder

        return SensitivityLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_policy_settings(self) -> SensitivityPolicySettingsRequestBuilder:
        """
        Provides operations to manage the sensitivityPolicySettings property of the microsoft.graph.informationProtection entity.
        """
        from .sensitivity_policy_settings.sensitivity_policy_settings_request_builder import SensitivityPolicySettingsRequestBuilder

        return SensitivityPolicySettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_digest(self) -> SignDigestRequestBuilder:
        """
        Provides operations to call the signDigest method.
        """
        from .sign_digest.sign_digest_request_builder import SignDigestRequestBuilder

        return SignDigestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_assessment_requests(self) -> ThreatAssessmentRequestsRequestBuilder:
        """
        Provides operations to manage the threatAssessmentRequests property of the microsoft.graph.informationProtection entity.
        """
        from .threat_assessment_requests.threat_assessment_requests_request_builder import ThreatAssessmentRequestsRequestBuilder

        return ThreatAssessmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify_signature(self) -> VerifySignatureRequestBuilder:
        """
        Provides operations to call the verifySignature method.
        """
        from .verify_signature.verify_signature_request_builder import VerifySignatureRequestBuilder

        return VerifySignatureRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class InformationProtectionRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class InformationProtectionRequestBuilderGetQueryParameters():
        """
        Get informationProtection from users
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
    class InformationProtectionRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[InformationProtectionRequestBuilder.InformationProtectionRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class InformationProtectionRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

