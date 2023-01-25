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

printer = lazy_import('msgraph.generated.models.printer')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
connectors_request_builder = lazy_import('msgraph.generated.print.printers.item.connectors.connectors_request_builder')
print_connector_item_request_builder = lazy_import('msgraph.generated.print.printers.item.connectors.item.print_connector_item_request_builder')
get_capabilities_request_builder = lazy_import('msgraph.generated.print.printers.item.get_capabilities.get_capabilities_request_builder')
reset_defaults_request_builder = lazy_import('msgraph.generated.print.printers.item.reset_defaults.reset_defaults_request_builder')
restore_factory_defaults_request_builder = lazy_import('msgraph.generated.print.printers.item.restore_factory_defaults.restore_factory_defaults_request_builder')
share_request_builder = lazy_import('msgraph.generated.print.printers.item.share.share_request_builder')
shares_request_builder = lazy_import('msgraph.generated.print.printers.item.shares.shares_request_builder')
printer_share_item_request_builder = lazy_import('msgraph.generated.print.printers.item.shares.item.printer_share_item_request_builder')
task_triggers_request_builder = lazy_import('msgraph.generated.print.printers.item.task_triggers.task_triggers_request_builder')
print_task_trigger_item_request_builder = lazy_import('msgraph.generated.print.printers.item.task_triggers.item.print_task_trigger_item_request_builder')

class PrinterItemRequestBuilder():
    """
    Provides operations to manage the printers property of the microsoft.graph.print entity.
    """
    @property
    def connectors(self) -> connectors_request_builder.ConnectorsRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.printer entity.
        """
        return connectors_request_builder.ConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_defaults(self) -> reset_defaults_request_builder.ResetDefaultsRequestBuilder:
        """
        Provides operations to call the resetDefaults method.
        """
        return reset_defaults_request_builder.ResetDefaultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_factory_defaults(self) -> restore_factory_defaults_request_builder.RestoreFactoryDefaultsRequestBuilder:
        """
        Provides operations to call the restoreFactoryDefaults method.
        """
        return restore_factory_defaults_request_builder.RestoreFactoryDefaultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share(self) -> share_request_builder.ShareRequestBuilder:
        """
        Provides operations to manage the share property of the microsoft.graph.printer entity.
        """
        return share_request_builder.ShareRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shares(self) -> shares_request_builder.SharesRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.printer entity.
        """
        return shares_request_builder.SharesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def task_triggers(self) -> task_triggers_request_builder.TaskTriggersRequestBuilder:
        """
        Provides operations to manage the taskTriggers property of the microsoft.graph.printer entity.
        """
        return task_triggers_request_builder.TaskTriggersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def connectors_by_id(self,id: str) -> print_connector_item_request_builder.PrintConnectorItemRequestBuilder:
        """
        Provides operations to manage the connectors property of the microsoft.graph.printer entity.
        Args:
            id: Unique identifier of the item
        Returns: print_connector_item_request_builder.PrintConnectorItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printConnector%2Did"] = id
        return print_connector_item_request_builder.PrintConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrinterItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/print/printers/{printer%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[PrinterItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property printers for print
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
    
    async def get(self,request_configuration: Optional[PrinterItemRequestBuilderGetRequestConfiguration] = None) -> Optional[printer.Printer]:
        """
        The list of printers registered in the tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[printer.Printer]
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
        return await self.request_adapter.send_async(request_info, printer.Printer, error_mapping)
    
    def get_capabilities(self,) -> get_capabilities_request_builder.GetCapabilitiesRequestBuilder:
        """
        Provides operations to call the getCapabilities method.
        Returns: get_capabilities_request_builder.GetCapabilitiesRequestBuilder
        """
        return get_capabilities_request_builder.GetCapabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def patch(self,body: Optional[printer.Printer] = None, request_configuration: Optional[PrinterItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[printer.Printer]:
        """
        Update the navigation property printers in print
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[printer.Printer]
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
        return await self.request_adapter.send_async(request_info, printer.Printer, error_mapping)
    
    def shares_by_id(self,id: str) -> printer_share_item_request_builder.PrinterShareItemRequestBuilder:
        """
        Provides operations to manage the shares property of the microsoft.graph.printer entity.
        Args:
            id: Unique identifier of the item
        Returns: printer_share_item_request_builder.PrinterShareItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printerShare%2Did"] = id
        return printer_share_item_request_builder.PrinterShareItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def task_triggers_by_id(self,id: str) -> print_task_trigger_item_request_builder.PrintTaskTriggerItemRequestBuilder:
        """
        Provides operations to manage the taskTriggers property of the microsoft.graph.printer entity.
        Args:
            id: Unique identifier of the item
        Returns: print_task_trigger_item_request_builder.PrintTaskTriggerItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["printTaskTrigger%2Did"] = id
        return print_task_trigger_item_request_builder.PrintTaskTriggerItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[PrinterItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property printers for print
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
    
    def to_get_request_information(self,request_configuration: Optional[PrinterItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of printers registered in the tenant.
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
    
    def to_patch_request_information(self,body: Optional[printer.Printer] = None, request_configuration: Optional[PrinterItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property printers in print
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
    class PrinterItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class PrinterItemRequestBuilderGetQueryParameters():
        """
        The list of printers registered in the tenant.
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
    class PrinterItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PrinterItemRequestBuilder.PrinterItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PrinterItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

