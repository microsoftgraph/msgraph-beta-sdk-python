from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.schema_extension import SchemaExtension

class SchemaExtensionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of schemaExtension entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SchemaExtensionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/schemaExtensions/{schemaExtension%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete the definition of a schema extension. In app-only scenarios, only the app that created the schema extension (owner app) can delete the schema extension definition, and only when the extension is in the InDevelopment state. In delegated scenarios, the owner of the owner app can delete the schema extension definition, and only when the extension is in the InDevelopment state.  Deleting a schema extension definition before deleting the data associated with the extension in the target resources makes the data inaccessible. To recover the data, you can recreate the schema extension definition with the same configuration, but only if you used the verified domain for the schema extension id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/schemaextension-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[SchemaExtension]:
        """
        Get the properties of the specified schemaExtension definition.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SchemaExtension]
        Find more info here: https://learn.microsoft.com/graph/api/schemaextension-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.schema_extension import SchemaExtension

        return await self.request_adapter.send_async(request_info, SchemaExtension, error_mapping)
    
    async def patch(self,body: Optional[SchemaExtension] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[SchemaExtension]:
        """
        Update properties in the definition of the specified schemaExtension. Additive updates to the extension can only be made when the extension is in the InDevelopment or Available status. This means custom properties or target resource types cannot be removed from the definition, but new custom properties can be added and the description of the extension changed. The update applies to all the resources that are included in the targetTypes property of the extension. These resources are among the supporting resource types. For delegated flows, the signed-in user can update a schema extension as long as the owner property of the extension is set to the appId of an application the signed-in user owns. That application can be the one that initially created the extension, or some other application owned by the signed-in user.  This criteria for the owner property allows a signed-in user to make updates through other applications they don't own, such as Microsoft Graph Explorer. When using Graph Explorer to update a schemaExtension resource, include the owner property in the PATCH request body.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SchemaExtension]
        Find more info here: https://learn.microsoft.com/graph/api/schemaextension-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.schema_extension import SchemaExtension

        return await self.request_adapter.send_async(request_info, SchemaExtension, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete the definition of a schema extension. In app-only scenarios, only the app that created the schema extension (owner app) can delete the schema extension definition, and only when the extension is in the InDevelopment state. In delegated scenarios, the owner of the owner app can delete the schema extension definition, and only when the extension is in the InDevelopment state.  Deleting a schema extension definition before deleting the data associated with the extension in the target resources makes the data inaccessible. To recover the data, you can recreate the schema extension definition with the same configuration, but only if you used the verified domain for the schema extension id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties of the specified schemaExtension definition.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[SchemaExtension] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update properties in the definition of the specified schemaExtension. Additive updates to the extension can only be made when the extension is in the InDevelopment or Available status. This means custom properties or target resource types cannot be removed from the definition, but new custom properties can be added and the description of the extension changed. The update applies to all the resources that are included in the targetTypes property of the extension. These resources are among the supporting resource types. For delegated flows, the signed-in user can update a schema extension as long as the owner property of the extension is set to the appId of an application the signed-in user owns. That application can be the one that initially created the extension, or some other application owned by the signed-in user.  This criteria for the owner property allows a signed-in user to make updates through other applications they don't own, such as Microsoft Graph Explorer. When using Graph Explorer to update a schemaExtension resource, include the owner property in the PATCH request body.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> SchemaExtensionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SchemaExtensionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return SchemaExtensionItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SchemaExtensionItemRequestBuilderGetQueryParameters():
        """
        Get the properties of the specified schemaExtension definition.
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

    

