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

assign_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.assign.assign_request_builder')
assignments_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.assignments.assignments_request_builder')
mobile_app_assignment_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.assignments.item.mobile_app_assignment_item_request_builder')
categories_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.categories.categories_request_builder')
mobile_app_category_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.categories.item.mobile_app_category_item_request_builder')
device_statuses_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.device_statuses.device_statuses_request_builder')
mobile_app_install_status_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.device_statuses.item.mobile_app_install_status_item_request_builder')
get_related_app_states_with_user_principal_name_with_device_id_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.get_related_app_states_with_user_principal_name_with_device_id.get_related_app_states_with_user_principal_name_with_device_id_request_builder')
install_summary_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.install_summary.install_summary_request_builder')
managed_mobile_lob_app_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.managed_mobile_lob_app.managed_mobile_lob_app_request_builder')
mobile_lob_app_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.mobile_lob_app.mobile_lob_app_request_builder')
relationships_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.relationships.relationships_request_builder')
mobile_app_relationship_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.relationships.item.mobile_app_relationship_item_request_builder')
update_relationships_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.update_relationships.update_relationships_request_builder')
user_statuses_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.user_statuses.user_statuses_request_builder')
user_app_install_status_item_request_builder = lazy_import('msgraph.generated.device_app_management.mobile_apps.item.user_statuses.item.user_app_install_status_item_request_builder')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class MobileAppItemRequestBuilder():
    """
    Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
    """
    @property
    def assign(self) -> assign_request_builder.AssignRequestBuilder:
        """
        Provides operations to call the assign method.
        """
        return assign_request_builder.AssignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assignments(self) -> assignments_request_builder.AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.mobileApp entity.
        """
        return assignments_request_builder.AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> categories_request_builder.CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.mobileApp entity.
        """
        return categories_request_builder.CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_statuses(self) -> device_statuses_request_builder.DeviceStatusesRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.mobileApp entity.
        """
        return device_statuses_request_builder.DeviceStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def install_summary(self) -> install_summary_request_builder.InstallSummaryRequestBuilder:
        """
        Provides operations to manage the installSummary property of the microsoft.graph.mobileApp entity.
        """
        return install_summary_request_builder.InstallSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_mobile_lob_app(self) -> managed_mobile_lob_app_request_builder.ManagedMobileLobAppRequestBuilder:
        """
        Casts the previous resource to managedMobileLobApp.
        """
        return managed_mobile_lob_app_request_builder.ManagedMobileLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_lob_app(self) -> mobile_lob_app_request_builder.MobileLobAppRequestBuilder:
        """
        Casts the previous resource to mobileLobApp.
        """
        return mobile_lob_app_request_builder.MobileLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relationships(self) -> relationships_request_builder.RelationshipsRequestBuilder:
        """
        Provides operations to manage the relationships property of the microsoft.graph.mobileApp entity.
        """
        return relationships_request_builder.RelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def update_relationships(self) -> update_relationships_request_builder.UpdateRelationshipsRequestBuilder:
        """
        Provides operations to call the updateRelationships method.
        """
        return update_relationships_request_builder.UpdateRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_statuses(self) -> user_statuses_request_builder.UserStatusesRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.mobileApp entity.
        """
        return user_statuses_request_builder.UserStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def assignments_by_id(self,id: str) -> mobile_app_assignment_item_request_builder.MobileAppAssignmentItemRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.mobileApp entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_assignment_item_request_builder.MobileAppAssignmentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppAssignment%2Did"] = id
        return mobile_app_assignment_item_request_builder.MobileAppAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def categories_by_id(self,id: str) -> mobile_app_category_item_request_builder.MobileAppCategoryItemRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.mobileApp entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_category_item_request_builder.MobileAppCategoryItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppCategory%2Did"] = id
        return mobile_app_category_item_request_builder.MobileAppCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MobileAppItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[MobileAppItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property mobileApps for deviceAppManagement
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
    
    def device_statuses_by_id(self,id: str) -> mobile_app_install_status_item_request_builder.MobileAppInstallStatusItemRequestBuilder:
        """
        Provides operations to manage the deviceStatuses property of the microsoft.graph.mobileApp entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_install_status_item_request_builder.MobileAppInstallStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppInstallStatus%2Did"] = id
        return mobile_app_install_status_item_request_builder.MobileAppInstallStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[MobileAppItemRequestBuilderGetRequestConfiguration] = None) -> Optional[mobile_app.MobileApp]:
        """
        The mobile apps.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mobile_app.MobileApp]
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
        return await self.request_adapter.send_async(request_info, mobile_app.MobileApp, error_mapping)
    
    def get_related_app_states_with_user_principal_name_with_device_id(self,device_id: Optional[str] = None, user_principal_name: Optional[str] = None) -> get_related_app_states_with_user_principal_name_with_device_id_request_builder.GetRelatedAppStatesWithUserPrincipalNameWithDeviceIdRequestBuilder:
        """
        Provides operations to call the getRelatedAppStates method.
        Args:
            deviceId: Usage: deviceId='{deviceId}'
            userPrincipalName: Usage: userPrincipalName='{userPrincipalName}'
        Returns: get_related_app_states_with_user_principal_name_with_device_id_request_builder.GetRelatedAppStatesWithUserPrincipalNameWithDeviceIdRequestBuilder
        """
        if device_id is None:
            raise Exception("device_id cannot be undefined")
        if user_principal_name is None:
            raise Exception("user_principal_name cannot be undefined")
        return get_related_app_states_with_user_principal_name_with_device_id_request_builder.GetRelatedAppStatesWithUserPrincipalNameWithDeviceIdRequestBuilder(self.request_adapter, self.path_parameters, deviceId, userPrincipalName)
    
    async def patch(self,body: Optional[mobile_app.MobileApp] = None, request_configuration: Optional[MobileAppItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[mobile_app.MobileApp]:
        """
        Update the navigation property mobileApps in deviceAppManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[mobile_app.MobileApp]
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
        return await self.request_adapter.send_async(request_info, mobile_app.MobileApp, error_mapping)
    
    def relationships_by_id(self,id: str) -> mobile_app_relationship_item_request_builder.MobileAppRelationshipItemRequestBuilder:
        """
        Provides operations to manage the relationships property of the microsoft.graph.mobileApp entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_app_relationship_item_request_builder.MobileAppRelationshipItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileAppRelationship%2Did"] = id
        return mobile_app_relationship_item_request_builder.MobileAppRelationshipItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[MobileAppItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property mobileApps for deviceAppManagement
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
    
    def to_get_request_information(self,request_configuration: Optional[MobileAppItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The mobile apps.
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
    
    def to_patch_request_information(self,body: Optional[mobile_app.MobileApp] = None, request_configuration: Optional[MobileAppItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property mobileApps in deviceAppManagement
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
    
    def user_statuses_by_id(self,id: str) -> user_app_install_status_item_request_builder.UserAppInstallStatusItemRequestBuilder:
        """
        Provides operations to manage the userStatuses property of the microsoft.graph.mobileApp entity.
        Args:
            id: Unique identifier of the item
        Returns: user_app_install_status_item_request_builder.UserAppInstallStatusItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userAppInstallStatus%2Did"] = id
        return user_app_install_status_item_request_builder.UserAppInstallStatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class MobileAppItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class MobileAppItemRequestBuilderGetQueryParameters():
        """
        The mobile apps.
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
    class MobileAppItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MobileAppItemRequestBuilder.MobileAppItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MobileAppItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

