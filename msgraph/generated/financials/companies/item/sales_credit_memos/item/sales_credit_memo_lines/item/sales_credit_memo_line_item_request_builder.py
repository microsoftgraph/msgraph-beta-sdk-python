from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import sales_credit_memo_line
    from ........models.o_data_errors import o_data_error
    from .account import account_request_builder
    from .item import item_request_builder

class SalesCreditMemoLineItemRequestBuilder():
    """
    Provides operations to manage the salesCreditMemoLines property of the microsoft.graph.salesCreditMemo entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SalesCreditMemoLineItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/financials/companies/{company%2Did}/salesCreditMemos/{salesCreditMemo%2Did}/salesCreditMemoLines/{salesCreditMemoLine%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[SalesCreditMemoLineItemRequestBuilderGetRequestConfiguration] = None) -> Optional[sales_credit_memo_line.SalesCreditMemoLine]:
        """
        Get salesCreditMemoLines from financials
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[sales_credit_memo_line.SalesCreditMemoLine]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import sales_credit_memo_line

        return await self.request_adapter.send_async(request_info, sales_credit_memo_line.SalesCreditMemoLine, error_mapping)
    
    async def patch(self,body: Optional[sales_credit_memo_line.SalesCreditMemoLine] = None, request_configuration: Optional[SalesCreditMemoLineItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[sales_credit_memo_line.SalesCreditMemoLine]:
        """
        Update the navigation property salesCreditMemoLines in financials
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[sales_credit_memo_line.SalesCreditMemoLine]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models import sales_credit_memo_line

        return await self.request_adapter.send_async(request_info, sales_credit_memo_line.SalesCreditMemoLine, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SalesCreditMemoLineItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get salesCreditMemoLines from financials
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
    
    def to_patch_request_information(self,body: Optional[sales_credit_memo_line.SalesCreditMemoLine] = None, request_configuration: Optional[SalesCreditMemoLineItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property salesCreditMemoLines in financials
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def account(self) -> account_request_builder.AccountRequestBuilder:
        """
        Provides operations to manage the account property of the microsoft.graph.salesCreditMemoLine entity.
        """
        from .account import account_request_builder

        return account_request_builder.AccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def item(self) -> item_request_builder.ItemRequestBuilder:
        """
        Provides operations to manage the item property of the microsoft.graph.salesCreditMemoLine entity.
        """
        from .item import item_request_builder

        return item_request_builder.ItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SalesCreditMemoLineItemRequestBuilderGetQueryParameters():
        """
        Get salesCreditMemoLines from financials
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SalesCreditMemoLineItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SalesCreditMemoLineItemRequestBuilder.SalesCreditMemoLineItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SalesCreditMemoLineItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

