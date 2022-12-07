from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UnsupportedDeviceConfigurationDetail(AdditionalDataHolder, Parsable):
    """
    A description of why an entity is unsupported.
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
        Instantiates a new unsupportedDeviceConfigurationDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A message explaining why an entity is unsupported.
        self._message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If message is related to a specific property in the original entity, then the name of that property.
        self._property_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnsupportedDeviceConfigurationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnsupportedDeviceConfigurationDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnsupportedDeviceConfigurationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "property_name": lambda n : setattr(self, 'property_name', n.get_str_value()),
        }
        return fields
    
    @property
    def message(self,) -> Optional[str]:
        """
        Gets the message property value. A message explaining why an entity is unsupported.
        Returns: Optional[str]
        """
        return self._message
    
    @message.setter
    def message(self,value: Optional[str] = None) -> None:
        """
        Sets the message property value. A message explaining why an entity is unsupported.
        Args:
            value: Value to set for the message property.
        """
        self._message = value
    
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
    def property_name(self,) -> Optional[str]:
        """
        Gets the propertyName property value. If message is related to a specific property in the original entity, then the name of that property.
        Returns: Optional[str]
        """
        return self._property_name
    
    @property_name.setter
    def property_name(self,value: Optional[str] = None) -> None:
        """
        Sets the propertyName property value. If message is related to a specific property in the original entity, then the name of that property.
        Args:
            value: Value to set for the propertyName property.
        """
        self._property_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("message", self.message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("propertyName", self.property_name)
        writer.write_additional_data_value(self.additional_data)
    

