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

background_image_request_builder = lazy_import('msgraph.generated.branding.background_image.background_image_request_builder')
banner_logo_request_builder = lazy_import('msgraph.generated.branding.banner_logo.banner_logo_request_builder')
custom_c_s_s_request_builder = lazy_import('msgraph.generated.branding.custom_c_s_s.custom_c_s_s_request_builder')
favicon_request_builder = lazy_import('msgraph.generated.branding.favicon.favicon_request_builder')
header_logo_request_builder = lazy_import('msgraph.generated.branding.header_logo.header_logo_request_builder')
localizations_request_builder = lazy_import('msgraph.generated.branding.localizations.localizations_request_builder')
organizational_branding_localization_item_request_builder = lazy_import('msgraph.generated.branding.localizations.item.organizational_branding_localization_item_request_builder')
square_logo_request_builder = lazy_import('msgraph.generated.branding.square_logo.square_logo_request_builder')
square_logo_dark_request_builder = lazy_import('msgraph.generated.branding.square_logo_dark.square_logo_dark_request_builder')
organizational_branding = lazy_import('msgraph.generated.models.organizational_branding')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class BrandingRequestBuilder():
    """
    Provides operations to manage the organizationalBranding singleton.
    """
    @property
    def background_image(self) -> background_image_request_builder.BackgroundImageRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return background_image_request_builder.BackgroundImageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def banner_logo(self) -> banner_logo_request_builder.BannerLogoRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return banner_logo_request_builder.BannerLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_c_s_s(self) -> custom_c_s_s_request_builder.CustomCSSRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return custom_c_s_s_request_builder.CustomCSSRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favicon(self) -> favicon_request_builder.FaviconRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return favicon_request_builder.FaviconRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def header_logo(self) -> header_logo_request_builder.HeaderLogoRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return header_logo_request_builder.HeaderLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def localizations(self) -> localizations_request_builder.LocalizationsRequestBuilder:
        """
        Provides operations to manage the localizations property of the microsoft.graph.organizationalBranding entity.
        """
        return localizations_request_builder.LocalizationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def square_logo(self) -> square_logo_request_builder.SquareLogoRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return square_logo_request_builder.SquareLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def square_logo_dark(self) -> square_logo_dark_request_builder.SquareLogoDarkRequestBuilder:
        """
        Provides operations to manage the media for the organizationalBranding entity.
        """
        return square_logo_dark_request_builder.SquareLogoDarkRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new BrandingRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/branding{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[BrandingRequestBuilderGetRequestConfiguration] = None) -> Optional[organizational_branding.OrganizationalBranding]:
        """
        Get branding
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organizational_branding.OrganizationalBranding]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, organizational_branding.OrganizationalBranding, error_mapping)
    
    def localizations_by_id(self,id: str) -> organizational_branding_localization_item_request_builder.OrganizationalBrandingLocalizationItemRequestBuilder:
        """
        Provides operations to manage the localizations property of the microsoft.graph.organizationalBranding entity.
        Args:
            id: Unique identifier of the item
        Returns: organizational_branding_localization_item_request_builder.OrganizationalBrandingLocalizationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["organizationalBrandingLocalization%2Did"] = id
        return organizational_branding_localization_item_request_builder.OrganizationalBrandingLocalizationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[organizational_branding.OrganizationalBranding] = None, request_configuration: Optional[BrandingRequestBuilderPatchRequestConfiguration] = None) -> Optional[organizational_branding.OrganizationalBranding]:
        """
        Update branding
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[organizational_branding.OrganizationalBranding]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, organizational_branding.OrganizationalBranding, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[BrandingRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get branding
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
    
    def to_patch_request_information(self,body: Optional[organizational_branding.OrganizationalBranding] = None, request_configuration: Optional[BrandingRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update branding
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
    
    @dataclass
    class BrandingRequestBuilderGetQueryParameters():
        """
        Get branding
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
    class BrandingRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[BrandingRequestBuilder.BrandingRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class BrandingRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

