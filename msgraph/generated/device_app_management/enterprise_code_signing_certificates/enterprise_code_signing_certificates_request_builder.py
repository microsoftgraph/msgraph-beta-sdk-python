from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
    from ...models.enterprise_code_signing_certificate_collection_response import EnterpriseCodeSigningCertificateCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.enterprise_code_signing_certificate_item_request_builder import EnterpriseCodeSigningCertificateItemRequestBuilder

class EnterpriseCodeSigningCertificatesRequestBuilder():
    """
    Provides operations to manage the enterpriseCodeSigningCertificates property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EnterpriseCodeSigningCertificatesRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/enterpriseCodeSigningCertificates{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_enterprise_code_signing_certificate_id(self,enterprise_code_signing_certificate_id: str) -> EnterpriseCodeSigningCertificateItemRequestBuilder:
        """
        Provides operations to manage the enterpriseCodeSigningCertificates property of the microsoft.graph.deviceAppManagement entity.
        Args:
            enterprise_code_signing_certificate_id: Unique identifier of the item
        Returns: EnterpriseCodeSigningCertificateItemRequestBuilder
        """
        if not enterprise_code_signing_certificate_id:
            raise TypeError("enterprise_code_signing_certificate_id cannot be null.")
        from .item.enterprise_code_signing_certificate_item_request_builder import EnterpriseCodeSigningCertificateItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["enterpriseCodeSigningCertificate%2Did"] = enterprise_code_signing_certificate_id
        return EnterpriseCodeSigningCertificateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[EnterpriseCodeSigningCertificatesRequestBuilderGetRequestConfiguration] = None) -> Optional[EnterpriseCodeSigningCertificateCollectionResponse]:
        """
        The Windows Enterprise Code Signing Certificate.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EnterpriseCodeSigningCertificateCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.enterprise_code_signing_certificate_collection_response import EnterpriseCodeSigningCertificateCollectionResponse

        return await self.request_adapter.send_async(request_info, EnterpriseCodeSigningCertificateCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[EnterpriseCodeSigningCertificate] = None, request_configuration: Optional[EnterpriseCodeSigningCertificatesRequestBuilderPostRequestConfiguration] = None) -> Optional[EnterpriseCodeSigningCertificate]:
        """
        Create new navigation property to enterpriseCodeSigningCertificates for deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EnterpriseCodeSigningCertificate]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate

        return await self.request_adapter.send_async(request_info, EnterpriseCodeSigningCertificate, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[EnterpriseCodeSigningCertificatesRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The Windows Enterprise Code Signing Certificate.
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
    
    def to_post_request_information(self,body: Optional[EnterpriseCodeSigningCertificate] = None, request_configuration: Optional[EnterpriseCodeSigningCertificatesRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to enterpriseCodeSigningCertificates for deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EnterpriseCodeSigningCertificatesRequestBuilderGetQueryParameters():
        """
        The Windows Enterprise Code Signing Certificate.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class EnterpriseCodeSigningCertificatesRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EnterpriseCodeSigningCertificatesRequestBuilder.EnterpriseCodeSigningCertificatesRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EnterpriseCodeSigningCertificatesRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

