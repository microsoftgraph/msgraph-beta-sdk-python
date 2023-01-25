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

apply_hold_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.noncustodial_data_sources.item.apply_hold.apply_hold_request_builder')
data_source_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.noncustodial_data_sources.item.data_source.data_source_request_builder')
release_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.noncustodial_data_sources.item.release.release_request_builder')
remove_hold_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.noncustodial_data_sources.item.remove_hold.remove_hold_request_builder')
update_index_request_builder = lazy_import('msgraph.generated.compliance.ediscovery.cases.item.noncustodial_data_sources.item.update_index.update_index_request_builder')
noncustodial_data_source = lazy_import('msgraph.generated.models.ediscovery.noncustodial_data_source')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class NoncustodialDataSourceItemRequestBuilder():
    """
    Provides operations to manage the noncustodialDataSources property of the microsoft.graph.ediscovery.case entity.
    """
    @property
    def apply_hold(self) -> apply_hold_request_builder.ApplyHoldRequestBuilder:
        """
        Provides operations to call the applyHold method.
        """
        return apply_hold_request_builder.ApplyHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_source(self) -> data_source_request_builder.DataSourceRequestBuilder:
        """
        Provides operations to manage the dataSource property of the microsoft.graph.ediscovery.noncustodialDataSource entity.
        """
        return data_source_request_builder.DataSourceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def release(self) -> release_request_builder.ReleaseRequestBuilder:
        """
        Provides operations to call the release method.
        """
        return release_request_builder.ReleaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_hold(self) -> remove_hold_request_builder.RemoveHoldRequestBuilder:
        """
        Provides operations to call the removeHold method.
        """
        return remove_hold_request_builder.RemoveHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_index(self) -> update_index_request_builder.UpdateIndexRequestBuilder:
        """
        Provides operations to call the updateIndex method.
        """
        return update_index_request_builder.UpdateIndexRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new NoncustodialDataSourceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/compliance/ediscovery/cases/{case%2Did}/noncustodialDataSources/{noncustodialDataSource%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property noncustodialDataSources for compliance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[noncustodial_data_source.NoncustodialDataSource]:
        """
        Returns a list of case noncustodialDataSource objects for this case.  Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[noncustodial_data_source.NoncustodialDataSource]
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
        return await self.request_adapter.send_async(request_info, noncustodial_data_source.NoncustodialDataSource, error_mapping)
    
    async def patch(self,body: Optional[noncustodial_data_source.NoncustodialDataSource] = None, request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[noncustodial_data_source.NoncustodialDataSource]:
        """
        Update the navigation property noncustodialDataSources in compliance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[noncustodial_data_source.NoncustodialDataSource]
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
        return await self.request_adapter.send_async(request_info, noncustodial_data_source.NoncustodialDataSource, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property noncustodialDataSources for compliance
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
    
    def to_get_request_information(self,request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of case noncustodialDataSource objects for this case.  Nullable.
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
    
    def to_patch_request_information(self,body: Optional[noncustodial_data_source.NoncustodialDataSource] = None, request_configuration: Optional[NoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property noncustodialDataSources in compliance
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
    class NoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class NoncustodialDataSourceItemRequestBuilderGetQueryParameters():
        """
        Returns a list of case noncustodialDataSource objects for this case.  Nullable.
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
    class NoncustodialDataSourceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[NoncustodialDataSourceItemRequestBuilder.NoncustodialDataSourceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class NoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

