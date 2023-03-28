from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import drive_item_source_application

class DriveItemSource(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new driveItemSource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Enumeration value that indicates the source application where the file was created.
        self._application: Optional[drive_item_source_application.DriveItemSourceApplication] = None
        # The external identifier for the drive item from the source.
        self._external_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    
    @property
    def application(self,) -> Optional[drive_item_source_application.DriveItemSourceApplication]:
        """
        Gets the application property value. Enumeration value that indicates the source application where the file was created.
        Returns: Optional[drive_item_source_application.DriveItemSourceApplication]
        """
        return self._application
    
    @application.setter
    def application(self,value: Optional[drive_item_source_application.DriveItemSourceApplication] = None) -> None:
        """
        Sets the application property value. Enumeration value that indicates the source application where the file was created.
        Args:
            value: Value to set for the application property.
        """
        self._application = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriveItemSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DriveItemSource()
    
    @property
    def external_id(self,) -> Optional[str]:
        """
        Gets the externalId property value. The external identifier for the drive item from the source.
        Returns: Optional[str]
        """
        return self._external_id
    
    @external_id.setter
    def external_id(self,value: Optional[str] = None) -> None:
        """
        Sets the externalId property value. The external identifier for the drive item from the source.
        Args:
            value: Value to set for the external_id property.
        """
        self._external_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import drive_item_source_application

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_enum_value(drive_item_source_application.DriveItemSourceApplication)),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("application", self.application)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

