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
    from .....models.unified_role_definition import UnifiedRoleDefinition
    from .assigned_principals_with_transitivedirectory_scope_type_directory_scope_type_directory_scope_id_directory_scope_id.assigned_principals_with_transitivedirectory_scope_type_directory_scope_type_directory_scope_id_directory_scope_id_request_builder import AssignedPrincipalsWithTransitivedirectoryScopeTypeDirectoryScopeTypeDirectoryScopeIdDirectoryScopeIdRequestBuilder
    from .inherits_permissions_from.inherits_permissions_from_request_builder import InheritsPermissionsFromRequestBuilder

class UnifiedRoleDefinitionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the roleDefinitions property of the microsoft.graph.rbacApplication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UnifiedRoleDefinitionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/roleManagement/directory/roleDefinitions/{unifiedRoleDefinition%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a unifiedRoleDefinition object for an RBAC provider. You cannot delete built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license. The following RBAC providers are currently supported:- Cloud PC- device management (Intune)- Defender (Microsoft Defender XDR Unified RBAC)- directory (Microsoft Entra ID) 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/unifiedroledefinition-delete?view=graph-rest-beta
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[UnifiedRoleDefinitionItemRequestBuilderGetQueryParameters]] = None) -> Optional[UnifiedRoleDefinition]:
        """
        Get the properties and relationships of a unifiedRoleDefinition object of an RBAC provider.  The following RBAC providers are currently supported:- Cloud PC - device management (Intune)- Defender (Microsoft Defender XDR Unified RBAC)- directory (Microsoft Entra directory roles)- entitlement management (Microsoft Entra entitlement management)- Exchange Online (Except China operated by 21Vianet)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleDefinition]
        Find more info here: https://learn.microsoft.com/graph/api/unifiedroledefinition-get?view=graph-rest-beta
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_definition import UnifiedRoleDefinition

        return await self.request_adapter.send_async(request_info, UnifiedRoleDefinition, error_mapping)
    
    async def patch(self,body: UnifiedRoleDefinition, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[UnifiedRoleDefinition]:
        """
        Update the properties of a unifiedRoleDefinition object for an RBAC provider. You cannot update built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license. The following RBAC providers are currently supported:- Cloud PC- device management (Intune)- directory (Microsoft Entra ID) 
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[UnifiedRoleDefinition]
        Find more info here: https://learn.microsoft.com/graph/api/unifiedroledefinition-update?view=graph-rest-beta
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.unified_role_definition import UnifiedRoleDefinition

        return await self.request_adapter.send_async(request_info, UnifiedRoleDefinition, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a unifiedRoleDefinition object for an RBAC provider. You cannot delete built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license. The following RBAC providers are currently supported:- Cloud PC- device management (Intune)- Defender (Microsoft Defender XDR Unified RBAC)- directory (Microsoft Entra ID) 
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[UnifiedRoleDefinitionItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the properties and relationships of a unifiedRoleDefinition object of an RBAC provider.  The following RBAC providers are currently supported:- Cloud PC - device management (Intune)- Defender (Microsoft Defender XDR Unified RBAC)- directory (Microsoft Entra directory roles)- entitlement management (Microsoft Entra entitlement management)- Exchange Online (Except China operated by 21Vianet)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: UnifiedRoleDefinition, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a unifiedRoleDefinition object for an RBAC provider. You cannot update built-in roles. This feature requires a Microsoft Entra ID P1 or P2 license. The following RBAC providers are currently supported:- Cloud PC- device management (Intune)- directory (Microsoft Entra ID) 
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> UnifiedRoleDefinitionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UnifiedRoleDefinitionItemRequestBuilder
        """
        warn("This version is being deprecated and is scheduled for removal on 2025-12-01.Please migrate to the latest version before the removal date. as of 2025-01/PrivatePreview:microsoft.applicationAuthorization on 2025-01-01 and will be removed 2025-12-01", DeprecationWarning)
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UnifiedRoleDefinitionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assigned_principals_with_transitivedirectory_scope_type_directory_scope_type_directory_scope_id_directory_scope_id(self) -> AssignedPrincipalsWithTransitivedirectoryScopeTypeDirectoryScopeTypeDirectoryScopeIdDirectoryScopeIdRequestBuilder:
        """
        Provides operations to call the assignedPrincipals method.
        """
        from .assigned_principals_with_transitivedirectory_scope_type_directory_scope_type_directory_scope_id_directory_scope_id.assigned_principals_with_transitivedirectory_scope_type_directory_scope_type_directory_scope_id_directory_scope_id_request_builder import AssignedPrincipalsWithTransitivedirectoryScopeTypeDirectoryScopeTypeDirectoryScopeIdDirectoryScopeIdRequestBuilder

        return AssignedPrincipalsWithTransitivedirectoryScopeTypeDirectoryScopeTypeDirectoryScopeIdDirectoryScopeIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inherits_permissions_from(self) -> InheritsPermissionsFromRequestBuilder:
        """
        Provides operations to manage the inheritsPermissionsFrom property of the microsoft.graph.unifiedRoleDefinition entity.
        """
        from .inherits_permissions_from.inherits_permissions_from_request_builder import InheritsPermissionsFromRequestBuilder

        return InheritsPermissionsFromRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UnifiedRoleDefinitionItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UnifiedRoleDefinitionItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a unifiedRoleDefinition object of an RBAC provider.  The following RBAC providers are currently supported:- Cloud PC - device management (Intune)- Defender (Microsoft Defender XDR Unified RBAC)- directory (Microsoft Entra directory roles)- entitlement management (Microsoft Entra entitlement management)- Exchange Online (Except China operated by 21Vianet)
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class UnifiedRoleDefinitionItemRequestBuilderGetRequestConfiguration(RequestConfiguration[UnifiedRoleDefinitionItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UnifiedRoleDefinitionItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

