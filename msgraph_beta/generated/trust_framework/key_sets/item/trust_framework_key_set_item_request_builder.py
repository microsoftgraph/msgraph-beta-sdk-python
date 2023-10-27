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
    from ....models.trust_framework_key_set import TrustFrameworkKeySet
    from .generate_key.generate_key_request_builder import GenerateKeyRequestBuilder
    from .get_active_key.get_active_key_request_builder import GetActiveKeyRequestBuilder
    from .upload_certificate.upload_certificate_request_builder import UploadCertificateRequestBuilder
    from .upload_pkcs12.upload_pkcs12_request_builder import UploadPkcs12RequestBuilder
    from .upload_secret.upload_secret_request_builder import UploadSecretRequestBuilder

class TrustFrameworkKeySetItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the keySets property of the microsoft.graph.trustFramework entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TrustFrameworkKeySetItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/trustFramework/keySets/{trustFrameworkKeySet%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[TrustFrameworkKeySetItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a trustFrameworkKeySet. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkeyset-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[TrustFrameworkKeySetItemRequestBuilderGetRequestConfiguration] = None) -> Optional[TrustFrameworkKeySet]:
        """
        Retrieve the properties and associations for a Trustframeworkkeyset. This API is available in the following national cloud deployments.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TrustFrameworkKeySet]
        Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkeyset-get?view=graph-rest-1.0
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
        from ....models.trust_framework_key_set import TrustFrameworkKeySet

        return await self.request_adapter.send_async(request_info, TrustFrameworkKeySet, error_mapping)
    
    async def patch(self,body: Optional[TrustFrameworkKeySet] = None, request_configuration: Optional[TrustFrameworkKeySetItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[TrustFrameworkKeySet]:
        """
        Update the properties of a trustFrameworkKeyset. This operation will replace the content of an existing keyset. Specifying the ID in the request payload is optional.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TrustFrameworkKeySet]
        Find more info here: https://learn.microsoft.com/graph/api/trustframeworkkeyset-update?view=graph-rest-1.0
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
        from ....models.trust_framework_key_set import TrustFrameworkKeySet

        return await self.request_adapter.send_async(request_info, TrustFrameworkKeySet, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[TrustFrameworkKeySetItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a trustFrameworkKeySet. This API is available in the following national cloud deployments.
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
    
    def to_get_request_information(self,request_configuration: Optional[TrustFrameworkKeySetItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and associations for a Trustframeworkkeyset. This API is available in the following national cloud deployments.
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
    
    def to_patch_request_information(self,body: Optional[TrustFrameworkKeySet] = None, request_configuration: Optional[TrustFrameworkKeySetItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a trustFrameworkKeyset. This operation will replace the content of an existing keyset. Specifying the ID in the request payload is optional.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> TrustFrameworkKeySetItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TrustFrameworkKeySetItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return TrustFrameworkKeySetItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def generate_key(self) -> GenerateKeyRequestBuilder:
        """
        Provides operations to call the generateKey method.
        """
        from .generate_key.generate_key_request_builder import GenerateKeyRequestBuilder

        return GenerateKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_active_key(self) -> GetActiveKeyRequestBuilder:
        """
        Provides operations to call the getActiveKey method.
        """
        from .get_active_key.get_active_key_request_builder import GetActiveKeyRequestBuilder

        return GetActiveKeyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_certificate(self) -> UploadCertificateRequestBuilder:
        """
        Provides operations to call the uploadCertificate method.
        """
        from .upload_certificate.upload_certificate_request_builder import UploadCertificateRequestBuilder

        return UploadCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_pkcs12(self) -> UploadPkcs12RequestBuilder:
        """
        Provides operations to call the uploadPkcs12 method.
        """
        from .upload_pkcs12.upload_pkcs12_request_builder import UploadPkcs12RequestBuilder

        return UploadPkcs12RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload_secret(self) -> UploadSecretRequestBuilder:
        """
        Provides operations to call the uploadSecret method.
        """
        from .upload_secret.upload_secret_request_builder import UploadSecretRequestBuilder

        return UploadSecretRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TrustFrameworkKeySetItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class TrustFrameworkKeySetItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and associations for a Trustframeworkkeyset. This API is available in the following national cloud deployments.
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
    class TrustFrameworkKeySetItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[TrustFrameworkKeySetItemRequestBuilder.TrustFrameworkKeySetItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class TrustFrameworkKeySetItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

