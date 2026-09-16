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
    from .....models.share_point_migration_task import SharePointMigrationTask
    from .....models.share_point_migration_task_collection_response import SharePointMigrationTaskCollectionResponse
    from .count.count_request_builder import CountRequestBuilder
    from .get_by_source_group_mail_nickname_with_source_group_mail_nickname.get_by_source_group_mail_nickname_with_source_group_mail_nickname_request_builder import GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder
    from .get_by_source_site_url_with_source_site_url.get_by_source_site_url_with_source_site_url_request_builder import GetBySourceSiteUrlWithSourceSiteUrlRequestBuilder
    from .get_by_source_user_principal_name_with_source_principal_name.get_by_source_user_principal_name_with_source_principal_name_request_builder import GetBySourceUserPrincipalNameWithSourcePrincipalNameRequestBuilder
    from .item.share_point_migration_task_item_request_builder import SharePointMigrationTaskItemRequestBuilder

class CrossOrganizationMigrationTasksRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the crossOrganizationMigrationTasks property of the microsoft.graph.sharePointMigrationsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CrossOrganizationMigrationTasksRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/sharePoint/migrations/crossOrganizationMigrationTasks{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_share_point_migration_task_id(self,share_point_migration_task_id: str) -> SharePointMigrationTaskItemRequestBuilder:
        """
        Provides operations to manage the crossOrganizationMigrationTasks property of the microsoft.graph.sharePointMigrationsRoot entity.
        param share_point_migration_task_id: The unique identifier of sharePointMigrationTask
        Returns: SharePointMigrationTaskItemRequestBuilder
        """
        if share_point_migration_task_id is None:
            raise TypeError("share_point_migration_task_id cannot be null.")
        from .item.share_point_migration_task_item_request_builder import SharePointMigrationTaskItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sharePointMigrationTask%2Did"] = share_point_migration_task_id
        return SharePointMigrationTaskItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CrossOrganizationMigrationTasksRequestBuilderGetQueryParameters]] = None) -> Optional[SharePointMigrationTaskCollectionResponse]:
        """
        Get a sharePointMigrationTask that was previously created, using the task ID. The returned sharePointMigrationTask object includes the source and target site URLs, migration status, optional timestamps (startedDateTime and finishedDateTime), and error details about issues during processing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharePointMigrationTaskCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.share_point_migration_task_collection_response import SharePointMigrationTaskCollectionResponse

        return await self.request_adapter.send_async(request_info, SharePointMigrationTaskCollectionResponse, error_mapping)
    
    def get_by_source_group_mail_nickname_with_source_group_mail_nickname(self,source_group_mail_nickname: str) -> GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder:
        """
        Provides operations to call the getBySourceGroupMailNickname method.
        param source_group_mail_nickname: Usage: sourceGroupMailNickname='{sourceGroupMailNickname}'
        Returns: GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder
        """
        if source_group_mail_nickname is None:
            raise TypeError("source_group_mail_nickname cannot be null.")
        from .get_by_source_group_mail_nickname_with_source_group_mail_nickname.get_by_source_group_mail_nickname_with_source_group_mail_nickname_request_builder import GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder

        return GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder(self.request_adapter, self.path_parameters, source_group_mail_nickname)
    
    def get_by_source_site_url_with_source_site_url(self,source_site_url: str) -> GetBySourceSiteUrlWithSourceSiteUrlRequestBuilder:
        """
        Provides operations to call the getBySourceSiteUrl method.
        param source_site_url: Usage: sourceSiteUrl='{sourceSiteUrl}'
        Returns: GetBySourceSiteUrlWithSourceSiteUrlRequestBuilder
        """
        if source_site_url is None:
            raise TypeError("source_site_url cannot be null.")
        from .get_by_source_site_url_with_source_site_url.get_by_source_site_url_with_source_site_url_request_builder import GetBySourceSiteUrlWithSourceSiteUrlRequestBuilder

        return GetBySourceSiteUrlWithSourceSiteUrlRequestBuilder(self.request_adapter, self.path_parameters, source_site_url)
    
    def get_by_source_user_principal_name_with_source_principal_name(self,source_principal_name: str) -> GetBySourceUserPrincipalNameWithSourcePrincipalNameRequestBuilder:
        """
        Provides operations to call the getBySourceUserPrincipalName method.
        param source_principal_name: Usage: sourcePrincipalName='{sourcePrincipalName}'
        Returns: GetBySourceUserPrincipalNameWithSourcePrincipalNameRequestBuilder
        """
        if source_principal_name is None:
            raise TypeError("source_principal_name cannot be null.")
        from .get_by_source_user_principal_name_with_source_principal_name.get_by_source_user_principal_name_with_source_principal_name_request_builder import GetBySourceUserPrincipalNameWithSourcePrincipalNameRequestBuilder

        return GetBySourceUserPrincipalNameWithSourcePrincipalNameRequestBuilder(self.request_adapter, self.path_parameters, source_principal_name)
    
    async def post(self,body: SharePointMigrationTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SharePointMigrationTask]:
        """
        Create or update a sharePointMigrationTask to migrate a resource from the source organization to the target organization, using the sharePointMigrationTaskParameters. The resource can be a user, a group, or a site. When an existing sharePointMigrationTask is retrieved, it might contain not only the specifics of the source and target organizations and resources, but also the status of the migration and errors encountered during the migration operation. The API calls occur on the source site and only add list items to the my site root web, for example, contoso-my.sharepoint.com. Then, it triggers a multi-geo site move job in the backend to enqueue and orchestrate several tenant workflow jobs, such as backup, restore, and cleanup, supported by TJ infrastructure. The OData type of sharePointResourceMigrationParameters differentiates user migration from site migration, rather than using different subpaths. For a user's OneDrive migration, specify sharePointUserMigrationParameters. If this migration task is a regular SharePoint site migration, specify sharePointSiteMigrationParameters. If this migration task is a group-connected site migration, specify sharePointGroupMigrationParameters.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharePointMigrationTask]
        Find more info here: https://learn.microsoft.com/graph/api/sharepointmigrationtask-update?view=graph-rest-beta
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.share_point_migration_task import SharePointMigrationTask

        return await self.request_adapter.send_async(request_info, SharePointMigrationTask, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CrossOrganizationMigrationTasksRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a sharePointMigrationTask that was previously created, using the task ID. The returned sharePointMigrationTask object includes the source and target site URLs, migration status, optional timestamps (startedDateTime and finishedDateTime), and error details about issues during processing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: SharePointMigrationTask, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create or update a sharePointMigrationTask to migrate a resource from the source organization to the target organization, using the sharePointMigrationTaskParameters. The resource can be a user, a group, or a site. When an existing sharePointMigrationTask is retrieved, it might contain not only the specifics of the source and target organizations and resources, but also the status of the migration and errors encountered during the migration operation. The API calls occur on the source site and only add list items to the my site root web, for example, contoso-my.sharepoint.com. Then, it triggers a multi-geo site move job in the backend to enqueue and orchestrate several tenant workflow jobs, such as backup, restore, and cleanup, supported by TJ infrastructure. The OData type of sharePointResourceMigrationParameters differentiates user migration from site migration, rather than using different subpaths. For a user's OneDrive migration, specify sharePointUserMigrationParameters. If this migration task is a regular SharePoint site migration, specify sharePointSiteMigrationParameters. If this migration task is a group-connected site migration, specify sharePointGroupMigrationParameters.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CrossOrganizationMigrationTasksRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CrossOrganizationMigrationTasksRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CrossOrganizationMigrationTasksRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class CrossOrganizationMigrationTasksRequestBuilderGetQueryParameters():
        """
        Get a sharePointMigrationTask that was previously created, using the task ID. The returned sharePointMigrationTask object includes the source and target site URLs, migration status, optional timestamps (startedDateTime and finishedDateTime), and error details about issues during processing.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class CrossOrganizationMigrationTasksRequestBuilderGetRequestConfiguration(RequestConfiguration[CrossOrganizationMigrationTasksRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CrossOrganizationMigrationTasksRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

