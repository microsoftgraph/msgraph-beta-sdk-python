from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .upload_url_get_response import UploadUrlGetResponse

class UploadUrlRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the uploadUrl method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UploadUrlRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/synchronizationProfiles/{educationSynchronizationProfile%2Did}/uploadUrl()", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UploadUrlGetResponse]:
        """
        Retrieve a shared access signature (SAS) for uploading source files to Azure blob storage for a specific school data synchronization profile in the tenant. The SAS token has a validity of one hour. The upload URL is provided only for the CSV data provider.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UploadUrlGetResponse]
        Find more info here: https://learn.microsoft.com/graph/api/educationsynchronizationprofile-uploadurl?view=graph-rest-beta
        """
        warn("The Education Sync Profile API is deprecated and will stop returning data on December 31, 2024. Please transition to the new IndustryData API. as of 2024-06/Deprecated:SynchronizationProfiles", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .upload_url_get_response import UploadUrlGetResponse

        return await self.request_adapter.send_async(request_info, UploadUrlGetResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Retrieve a shared access signature (SAS) for uploading source files to Azure blob storage for a specific school data synchronization profile in the tenant. The SAS token has a validity of one hour. The upload URL is provided only for the CSV data provider.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The Education Sync Profile API is deprecated and will stop returning data on December 31, 2024. Please transition to the new IndustryData API. as of 2024-06/Deprecated:SynchronizationProfiles", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> UploadUrlRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UploadUrlRequestBuilder
        """
        warn("The Education Sync Profile API is deprecated and will stop returning data on December 31, 2024. Please transition to the new IndustryData API. as of 2024-06/Deprecated:SynchronizationProfiles", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UploadUrlRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class UploadUrlRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

