from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

powerlift_download_request = lazy_import('msgraph.generated.models.powerlift_download_request')

class DownloadAppDiagnosticsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the downloadAppDiagnostics method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new downloadAppDiagnosticsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The request property
        self._request: Optional[powerlift_download_request.PowerliftDownloadRequest] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DownloadAppDiagnosticsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DownloadAppDiagnosticsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DownloadAppDiagnosticsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "request": lambda n : setattr(self, 'request', n.get_object_value(powerlift_download_request.PowerliftDownloadRequest)),
        }
        return fields
    
    @property
    def request(self,) -> Optional[powerlift_download_request.PowerliftDownloadRequest]:
        """
        Gets the request property value. The request property
        Returns: Optional[powerlift_download_request.PowerliftDownloadRequest]
        """
        return self._request
    
    @request.setter
    def request(self,value: Optional[powerlift_download_request.PowerliftDownloadRequest] = None) -> None:
        """
        Sets the request property value. The request property
        Args:
            value: Value to set for the request property.
        """
        self._request = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("request", self.request)
        writer.write_additional_data_value(self.additional_data)
    

