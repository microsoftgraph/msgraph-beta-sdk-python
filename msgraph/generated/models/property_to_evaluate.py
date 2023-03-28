from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class PropertyToEvaluate(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new propertyToEvaluate and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Provides the property name.
        self._property_name: Optional[str] = None
        # Provides the property value.
        self._property_value: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PropertyToEvaluate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PropertyToEvaluate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PropertyToEvaluate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propertyName": lambda n : setattr(self, 'property_name', n.get_str_value()),
            "propertyValue": lambda n : setattr(self, 'property_value', n.get_str_value()),
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
    
    @property
    def property_name(self,) -> Optional[str]:
        """
        Gets the propertyName property value. Provides the property name.
        Returns: Optional[str]
        """
        return self._property_name
    
    @property_name.setter
    def property_name(self,value: Optional[str] = None) -> None:
        """
        Sets the propertyName property value. Provides the property name.
        Args:
            value: Value to set for the property_name property.
        """
        self._property_name = value
    
    @property
    def property_value(self,) -> Optional[str]:
        """
        Gets the propertyValue property value. Provides the property value.
        Returns: Optional[str]
        """
        return self._property_value
    
    @property_value.setter
    def property_value(self,value: Optional[str] = None) -> None:
        """
        Sets the propertyValue property value. Provides the property value.
        Args:
            value: Value to set for the property_value property.
        """
        self._property_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("propertyName", self.property_name)
        writer.write_str_value("propertyValue", self.property_value)
        writer.write_additional_data_value(self.additional_data)
    

