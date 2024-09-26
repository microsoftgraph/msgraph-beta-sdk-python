from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .......models.content_model import ContentModel
    from .......models.o_data_errors.o_data_error import ODataError
    from .add_to_drive.add_to_drive_request_builder import AddToDriveRequestBuilder
    from .get_applied_drives.get_applied_drives_request_builder import GetAppliedDrivesRequestBuilder
    from .remove_from_drive.remove_from_drive_request_builder import RemoveFromDriveRequestBuilder

class GetByNameWithModelNameRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the getByName method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]], model_name: Optional[str] = None) -> None:
        """
        Instantiates a new GetByNameWithModelNameRequestBuilder and sets the default values.
        param model_name: Usage: modelName='{modelName}'
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['modelName'] = model_name
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/contentModels/getByName(modelName='{modelName}')", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ContentModel]:
        """
        Read the properties and relationships of a contentModel object by its model name. The name should be the full model filename, including the file extension; for example, exampleModel.classifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ContentModel]
        Find more info here: https://learn.microsoft.com/graph/api/contentmodel-getbyname?view=graph-rest-beta
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.content_model import ContentModel

        return await self.request_adapter.send_async(request_info, ContentModel, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a contentModel object by its model name. The name should be the full model filename, including the file extension; for example, exampleModel.classifier.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> GetByNameWithModelNameRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GetByNameWithModelNameRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GetByNameWithModelNameRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def add_to_drive(self) -> AddToDriveRequestBuilder:
        """
        Provides operations to call the addToDrive method.
        """
        from .add_to_drive.add_to_drive_request_builder import AddToDriveRequestBuilder

        return AddToDriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_applied_drives(self) -> GetAppliedDrivesRequestBuilder:
        """
        Provides operations to call the getAppliedDrives method.
        """
        from .get_applied_drives.get_applied_drives_request_builder import GetAppliedDrivesRequestBuilder

        return GetAppliedDrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_from_drive(self) -> RemoveFromDriveRequestBuilder:
        """
        Provides operations to call the removeFromDrive method.
        """
        from .remove_from_drive.remove_from_drive_request_builder import RemoveFromDriveRequestBuilder

        return RemoveFromDriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GetByNameWithModelNameRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

