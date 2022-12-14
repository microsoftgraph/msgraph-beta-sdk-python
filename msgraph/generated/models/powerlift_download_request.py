from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PowerliftDownloadRequest(AdditionalDataHolder, Parsable):
    """
    Request used to download app diagnostic files.
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
        Instantiates a new powerliftDownloadRequest and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The list of files to download
        self._files: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique id for the request
        self._powerlift_id: Optional[Guid] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PowerliftDownloadRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PowerliftDownloadRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PowerliftDownloadRequest()
    
    @property
    def files(self,) -> Optional[List[str]]:
        """
        Gets the files property value. The list of files to download
        Returns: Optional[List[str]]
        """
        return self._files
    
    @files.setter
    def files(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the files property value. The list of files to download
        Args:
            value: Value to set for the files property.
        """
        self._files = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "files": lambda n : setattr(self, 'files', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "powerlift_id": lambda n : setattr(self, 'powerlift_id', n.get_object_value(Guid)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def powerlift_id(self,) -> Optional[Guid]:
        """
        Gets the powerliftId property value. The unique id for the request
        Returns: Optional[Guid]
        """
        return self._powerlift_id
    
    @powerlift_id.setter
    def powerlift_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the powerliftId property value. The unique id for the request
        Args:
            value: Value to set for the powerliftId property.
        """
        self._powerlift_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("files", self.files)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("powerliftId", self.powerlift_id)
        writer.write_additional_data_value(self.additional_data)
    

