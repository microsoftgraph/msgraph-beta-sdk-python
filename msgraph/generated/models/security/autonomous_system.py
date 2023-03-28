from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class AutonomousSystem(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new autonomousSystem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the autonomous system.
        self._name: Optional[str] = None
        # The autonomous system number, assigned by IANA.
        self._number: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The name of the autonomous system organization.
        self._organization: Optional[str] = None
        # A displayable value for these autonomous system details.
        self._value: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AutonomousSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AutonomousSystem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AutonomousSystem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the autonomous system.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the autonomous system.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def number(self,) -> Optional[int]:
        """
        Gets the number property value. The autonomous system number, assigned by IANA.
        Returns: Optional[int]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[int] = None) -> None:
        """
        Sets the number property value. The autonomous system number, assigned by IANA.
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
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
    def organization(self,) -> Optional[str]:
        """
        Gets the organization property value. The name of the autonomous system organization.
        Returns: Optional[str]
        """
        return self._organization
    
    @organization.setter
    def organization(self,value: Optional[str] = None) -> None:
        """
        Sets the organization property value. The name of the autonomous system organization.
        Args:
            value: Value to set for the organization property.
        """
        self._organization = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("name", self.name)
        writer.write_int_value("number", self.number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. A displayable value for these autonomous system details.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. A displayable value for these autonomous system details.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

