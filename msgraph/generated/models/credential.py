from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Credential(AdditionalDataHolder, Parsable):
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
        Instantiates a new credential and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The name of the field for this credential. e.g, username or password or phoneNumber. This is defined by the application. Must match what is in the html field on singleSignOnSettings/password object.
        self._field_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type for this credential. Valid values: username, password, or other.
        self._type: Optional[str] = None
        # The value for this credential. e.g, mysuperhiddenpassword. Note the value for passwords is write-only, the value can never be read back.
        self._value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Credential:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Credential
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Credential()
    
    @property
    def field_id(self,) -> Optional[str]:
        """
        Gets the fieldId property value. The name of the field for this credential. e.g, username or password or phoneNumber. This is defined by the application. Must match what is in the html field on singleSignOnSettings/password object.
        Returns: Optional[str]
        """
        return self._field_id
    
    @field_id.setter
    def field_id(self,value: Optional[str] = None) -> None:
        """
        Sets the fieldId property value. The name of the field for this credential. e.g, username or password or phoneNumber. This is defined by the application. Must match what is in the html field on singleSignOnSettings/password object.
        Args:
            value: Value to set for the fieldId property.
        """
        self._field_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "field_id": lambda n : setattr(self, 'field_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("fieldId", self.field_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type for this credential. Valid values: username, password, or other.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type for this credential. Valid values: username, password, or other.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def value(self,) -> Optional[str]:
        """
        Gets the value property value. The value for this credential. e.g, mysuperhiddenpassword. Note the value for passwords is write-only, the value can never be read back.
        Returns: Optional[str]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[str] = None) -> None:
        """
        Sets the value property value. The value for this credential. e.g, mysuperhiddenpassword. Note the value for passwords is write-only, the value can never be read back.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

