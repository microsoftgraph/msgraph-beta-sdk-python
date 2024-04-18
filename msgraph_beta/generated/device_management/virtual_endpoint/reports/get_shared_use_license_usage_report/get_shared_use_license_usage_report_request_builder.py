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
from warnings import warn

if TYPE_CHECKING:
    from .....models.o_data_errors.o_data_error import ODataError
    from .get_shared_use_license_usage_report_post_request_body import GetSharedUseLicenseUsageReportPostRequestBody

class GetSharedUseLicenseUsageReportRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getSharedUseLicenseUsageReport method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GetSharedUseLicenseUsageReportRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/reports/getSharedUseLicenseUsageReport", path_parameters)
    
    async def post(self,body: Optional[GetSharedUseLicenseUsageReportPostRequestBody] = None, request_configuration: Optional[RequestConfiguration] = None) -> bytes:
        """
        Get a usage report on shared-use licenses, such as servicePlanId, licenseCount, and claimedLicenseCount, for real-time, 7 days, or 28 days trend.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        Find more info here: https://learn.microsoft.com/graph/api/cloudpcreports-getshareduselicenseusagereport?view=graph-rest-1.0
        """
        warn("The getSharedUseLicenseUsageReport API is deprecated and will stop returning on Oct 17, 2023. Please use getFrontlineReport instead. as of 2023-05/getSharedUseLicenseUsageReport", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_post_request_information(self,body: Optional[GetSharedUseLicenseUsageReportPostRequestBody] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get a usage report on shared-use licenses, such as servicePlanId, licenseCount, and claimedLicenseCount, for real-time, 7 days, or 28 days trend.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("The getSharedUseLicenseUsageReport API is deprecated and will stop returning on Oct 17, 2023. Please use getFrontlineReport instead. as of 2023-05/getSharedUseLicenseUsageReport", DeprecationWarning)
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/octet-stream, application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> GetSharedUseLicenseUsageReportRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetSharedUseLicenseUsageReportRequestBuilder
        """
        warn("The getSharedUseLicenseUsageReport API is deprecated and will stop returning on Oct 17, 2023. Please use getFrontlineReport instead. as of 2023-05/getSharedUseLicenseUsageReport", DeprecationWarning)
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GetSharedUseLicenseUsageReportRequestBuilder(self.request_adapter, raw_url)
    

