from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class ChromeOSDeviceProperty(AdditionalDataHolder, Parsable):
    """
    Represents a property of the ChromeOS device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new chromeOSDeviceProperty and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of the property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Whether this property is updatable
        self._updatable: Optional[bool] = None
        # Value of the property
        self._value: Optional[str] = None
        # Type of the value
        self._value_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChromeOSDeviceProperty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChromeOSDeviceProperty
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChromeOSDeviceProperty()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updatable": lambda n : setattr(self, 'updatable', n.get_bool_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
            "valueType": lambda n : setattr(self, 'value_type', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the property
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
        writer.write_bool_value("updatable", self.updatable)
        writer.write_str_value("value", self.value)
        writer.write_str_value("valueType", self.value_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def updatable(self,) -> Optional[bool]:
        """
        Gets the updatable property value. Whether this property is updatable
        Returns: Optional[bool]
        """
        return self._updatable
    
    @updatable.setter
    def updatable(self,value: Optional[bool] = None) -> None:
        """
        Sets the updatable property value. Whether this property is updatable
        Args:
            value: Value to set for the updatable property.
        """
        self._updatable = value
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. Value of the property
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. Value of the property
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    
    @property
    def value_type(self,) -> Optional[str]:
        """
        Gets the valueType property value. Type of the value
        Returns: Optional[str]
        """
        return self._value_type
    
    @value_type.setter
    def value_type(self,value: Optional[str] = None) -> None:
        """
        Sets the valueType property value. Type of the value
        Args:
            value: Value to set for the value_type property.
        """
        self._value_type = value
    

