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
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.security.hunting_query_results import HuntingQueryResults

class MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getRunHuntingQuery method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], query: Optional[str] = None) -> None:
        """
        Instantiates a new MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param query: Usage: query='{query}'
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['query'] = query
        super().__init__(request_adapter, "{+baseurl}/security/microsoft.graph.security.getRunHuntingQuery(query='{query}',timespan='@timespan',workspaceId=@workspaceId){?timespan*,workspaceId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilderGetQueryParameters]] = None) -> Optional[HuntingQueryResults]:
        """
        Query a specified set of event, activity, or entity data supported by Microsoft Defender XDR to proactively look for specific threats in your environment, by using a GET request. This function is the GET-based companion to the runHuntingQuery action. It accepts a query in Kusto Query Language (KQL) as a URL parameter, executes it against the advanced hunting schema, and returns the same huntingQueryResults shape as the POST action. Use this function in scenarios that can't issue authenticated POST requests, such as Power BI dashboards that authenticate through Web.Contents. Find out more about hunting for threats across devices, emails, apps, and identities. Learn about KQL. For information on using advanced hunting in the Microsoft Defender portal, see Proactively hunt for threats with advanced hunting in Microsoft Defender XDR.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[HuntingQueryResults]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.hunting_query_results import HuntingQueryResults

        return await self.request_adapter.send_async(request_info, HuntingQueryResults, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Query a specified set of event, activity, or entity data supported by Microsoft Defender XDR to proactively look for specific threats in your environment, by using a GET request. This function is the GET-based companion to the runHuntingQuery action. It accepts a query in Kusto Query Language (KQL) as a URL parameter, executes it against the advanced hunting schema, and returns the same huntingQueryResults shape as the POST action. Use this function in scenarios that can't issue authenticated POST requests, such as Power BI dashboards that authenticate through Web.Contents. Find out more about hunting for threats across devices, emails, apps, and identities. Learn about KQL. For information on using advanced hunting in the Microsoft Defender portal, see Proactively hunt for threats with advanced hunting in Microsoft Defender XDR.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilderGetQueryParameters():
        """
        Query a specified set of event, activity, or entity data supported by Microsoft Defender XDR to proactively look for specific threats in your environment, by using a GET request. This function is the GET-based companion to the runHuntingQuery action. It accepts a query in Kusto Query Language (KQL) as a URL parameter, executes it against the advanced hunting schema, and returns the same huntingQueryResults shape as the POST action. Use this function in scenarios that can't issue authenticated POST requests, such as Power BI dashboards that authenticate through Web.Contents. Find out more about hunting for threats across devices, emails, apps, and identities. Learn about KQL. For information on using advanced hunting in the Microsoft Defender portal, see Proactively hunt for threats with advanced hunting in Microsoft Defender XDR.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "workspace_id":
                return "workspaceId"
            if original_name == "timespan":
                return "timespan"
            return original_name
        
        # Usage: timespan='@timespan'
        timespan: Optional[str] = None

        # Usage: workspaceId=@workspaceId
        workspace_id: Optional[UUID] = None

    
    @dataclass
    class MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilderGetRequestConfiguration(RequestConfiguration[MicrosoftGraphSecurityGetRunHuntingQueryWithQuerytimespanTimespanWithWorkspaceIdRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

