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

bitlocker_request_builder = lazy_import('msgraph.generated.me.information_protection.bitlocker.bitlocker_request_builder')
data_loss_prevention_policies_request_builder = lazy_import('msgraph.generated.me.information_protection.data_loss_prevention_policies.data_loss_prevention_policies_request_builder')
data_loss_prevention_policy_item_request_builder = lazy_import('msgraph.generated.me.information_protection.data_loss_prevention_policies.item.data_loss_prevention_policy_item_request_builder')
decrypt_buffer_request_builder = lazy_import('msgraph.generated.me.information_protection.decrypt_buffer.decrypt_buffer_request_builder')
encrypt_buffer_request_builder = lazy_import('msgraph.generated.me.information_protection.encrypt_buffer.encrypt_buffer_request_builder')
policy_request_builder = lazy_import('msgraph.generated.me.information_protection.policy.policy_request_builder')
sensitivity_labels_request_builder = lazy_import('msgraph.generated.me.information_protection.sensitivity_labels.sensitivity_labels_request_builder')
sensitivity_label_item_request_builder = lazy_import('msgraph.generated.me.information_protection.sensitivity_labels.item.sensitivity_label_item_request_builder')
sensitivity_policy_settings_request_builder = lazy_import('msgraph.generated.me.information_protection.sensitivity_policy_settings.sensitivity_policy_settings_request_builder')
sign_digest_request_builder = lazy_import('msgraph.generated.me.information_protection.sign_digest.sign_digest_request_builder')
threat_assessment_requests_request_builder = lazy_import('msgraph.generated.me.information_protection.threat_assessment_requests.threat_assessment_requests_request_builder')
threat_assessment_request_item_request_builder = lazy_import('msgraph.generated.me.information_protection.threat_assessment_requests.item.threat_assessment_request_item_request_builder')
verify_signature_request_builder = lazy_import('msgraph.generated.me.information_protection.verify_signature.verify_signature_request_builder')
information_protection = lazy_import('msgraph.generated.models.information_protection')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class InformationProtectionRequestBuilder():
    """
    Provides operations to manage the informationProtection property of the microsoft.graph.user entity.
    """
    @property
    def bitlocker(self) -> bitlocker_request_builder.BitlockerRequestBuilder:
        """
        Provides operations to manage the bitlocker property of the microsoft.graph.informationProtection entity.
        """
        return bitlocker_request_builder.BitlockerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_loss_prevention_policies(self) -> data_loss_prevention_policies_request_builder.DataLossPreventionPoliciesRequestBuilder:
        """
        Provides operations to manage the dataLossPreventionPolicies property of the microsoft.graph.informationProtection entity.
        """
        return data_loss_prevention_policies_request_builder.DataLossPreventionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decrypt_buffer(self) -> decrypt_buffer_request_builder.DecryptBufferRequestBuilder:
        """
        Provides operations to call the decryptBuffer method.
        """
        return decrypt_buffer_request_builder.DecryptBufferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def encrypt_buffer(self) -> encrypt_buffer_request_builder.EncryptBufferRequestBuilder:
        """
        Provides operations to call the encryptBuffer method.
        """
        return encrypt_buffer_request_builder.EncryptBufferRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policy(self) -> policy_request_builder.PolicyRequestBuilder:
        """
        Provides operations to manage the policy property of the microsoft.graph.informationProtection entity.
        """
        return policy_request_builder.PolicyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_labels(self) -> sensitivity_labels_request_builder.SensitivityLabelsRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.informationProtection entity.
        """
        return sensitivity_labels_request_builder.SensitivityLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sensitivity_policy_settings(self) -> sensitivity_policy_settings_request_builder.SensitivityPolicySettingsRequestBuilder:
        """
        Provides operations to manage the sensitivityPolicySettings property of the microsoft.graph.informationProtection entity.
        """
        return sensitivity_policy_settings_request_builder.SensitivityPolicySettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sign_digest(self) -> sign_digest_request_builder.SignDigestRequestBuilder:
        """
        Provides operations to call the signDigest method.
        """
        return sign_digest_request_builder.SignDigestRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def threat_assessment_requests(self) -> threat_assessment_requests_request_builder.ThreatAssessmentRequestsRequestBuilder:
        """
        Provides operations to manage the threatAssessmentRequests property of the microsoft.graph.informationProtection entity.
        """
        return threat_assessment_requests_request_builder.ThreatAssessmentRequestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify_signature(self) -> verify_signature_request_builder.VerifySignatureRequestBuilder:
        """
        Provides operations to call the verifySignature method.
        """
        return verify_signature_request_builder.VerifySignatureRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InformationProtectionRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/informationProtection{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[InformationProtectionRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property informationProtection for me
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
    
    def create_get_request_information(self,request_configuration: Optional[InformationProtectionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get informationProtection from me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[information_protection.InformationProtection] = None, request_configuration: Optional[InformationProtectionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property informationProtection in me
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def data_loss_prevention_policies_by_id(self,id: str) -> data_loss_prevention_policy_item_request_builder.DataLossPreventionPolicyItemRequestBuilder:
        """
        Provides operations to manage the dataLossPreventionPolicies property of the microsoft.graph.informationProtection entity.
        Args:
            id: Unique identifier of the item
        Returns: data_loss_prevention_policy_item_request_builder.DataLossPreventionPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["dataLossPreventionPolicy%2Did"] = id
        return data_loss_prevention_policy_item_request_builder.DataLossPreventionPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[InformationProtectionRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property informationProtection for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    async def get(self,request_configuration: Optional[InformationProtectionRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[information_protection.InformationProtection]:
        """
        Get informationProtection from me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[information_protection.InformationProtection]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, information_protection.InformationProtection, response_handler, error_mapping)
    
    async def patch(self,body: Optional[information_protection.InformationProtection] = None, request_configuration: Optional[InformationProtectionRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[information_protection.InformationProtection]:
        """
        Update the navigation property informationProtection in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[information_protection.InformationProtection]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, information_protection.InformationProtection, response_handler, error_mapping)
    
    def sensitivity_labels_by_id(self,id: str) -> sensitivity_label_item_request_builder.SensitivityLabelItemRequestBuilder:
        """
        Provides operations to manage the sensitivityLabels property of the microsoft.graph.informationProtection entity.
        Args:
            id: Unique identifier of the item
        Returns: sensitivity_label_item_request_builder.SensitivityLabelItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sensitivityLabel%2Did"] = id
        return sensitivity_label_item_request_builder.SensitivityLabelItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def threat_assessment_requests_by_id(self,id: str) -> threat_assessment_request_item_request_builder.ThreatAssessmentRequestItemRequestBuilder:
        """
        Provides operations to manage the threatAssessmentRequests property of the microsoft.graph.informationProtection entity.
        Args:
            id: Unique identifier of the item
        Returns: threat_assessment_request_item_request_builder.ThreatAssessmentRequestItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["threatAssessmentRequest%2Did"] = id
        return threat_assessment_request_item_request_builder.ThreatAssessmentRequestItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class InformationProtectionRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class InformationProtectionRequestBuilderGetQueryParameters():
        """
        Get informationProtection from me
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class InformationProtectionRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[InformationProtectionRequestBuilder.InformationProtectionRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class InformationProtectionRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

