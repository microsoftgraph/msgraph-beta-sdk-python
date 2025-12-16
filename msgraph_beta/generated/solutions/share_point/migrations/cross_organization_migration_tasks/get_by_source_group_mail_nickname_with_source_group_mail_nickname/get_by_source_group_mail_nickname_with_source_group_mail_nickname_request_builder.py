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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.share_point_migration_task import SharePointMigrationTask

class GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getBySourceGroupMailNickname method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], source_group_mail_nickname: Optional[str] = None) -> None:
        """
        Instantiates a new GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        param source_group_mail_nickname: Usage: sourceGroupMailNickname='{sourceGroupMailNickname}'
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['sourceGroupMailNickname'] = source_group_mail_nickname
        super().__init__(request_adapter, "{+baseurl}/solutions/sharePoint/migrations/crossOrganizationMigrationTasks/getBySourceGroupMailNickname(sourceGroupMailNickname='{sourceGroupMailNickname}')", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SharePointMigrationTask]:
        """
        Get a sharePointMigrationTask that was previously created for a group, using the source group mail nickname. The returned sharePointMigrationTask object includes the source and target site URLs, migration status, optional timestamps (startedDateTime and finishedDateTime), and error details about issues during processing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SharePointMigrationTask]
        Find more info here: https://learn.microsoft.com/graph/api/sharepointmigrationtask-getbysourcegroupmailnickname?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.share_point_migration_task import SharePointMigrationTask

        return await self.request_adapter.send_async(request_info, SharePointMigrationTask, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get a sharePointMigrationTask that was previously created for a group, using the source group mail nickname. The returned sharePointMigrationTask object includes the source and target site URLs, migration status, optional timestamps (startedDateTime and finishedDateTime), and error details about issues during processing.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class GetBySourceGroupMailNicknameWithSourceGroupMailNicknameRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

