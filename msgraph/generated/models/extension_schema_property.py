from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ExtensionSchemaProperty(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new extensionSchemaProperty and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the strongly typed property defined as part of a schema extension.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type of the property that is defined as part of a schema extension.  Allowed values are Binary, Boolean, DateTime, Integer or String. See the table below for more details.
        self._type: Optional[str] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExtensionSchemaProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExtensionSchemaProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExtensionSchemaProperty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the strongly typed property defined as part of a schema extension.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the strongly typed property defined as part of a schema extension.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type of the property that is defined as part of a schema extension.  Allowed values are Binary, Boolean, DateTime, Integer or String. See the table below for more details.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type of the property that is defined as part of a schema extension.  Allowed values are Binary, Boolean, DateTime, Integer or String. See the table below for more details.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

