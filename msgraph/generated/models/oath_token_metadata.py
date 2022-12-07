from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_value = lazy_import('msgraph.generated.models.key_value')

class OathTokenMetadata(AdditionalDataHolder, Parsable):
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
        Instantiates a new oathTokenMetadata and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The enabled property
        self._enabled: Optional[bool] = None
        # The manufacturer property
        self._manufacturer: Optional[str] = None
        # The manufacturerProperties property
        self._manufacturer_properties: Optional[List[key_value.KeyValue]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The serialNumber property
        self._serial_number: Optional[str] = None
        # The tokenType property
        self._token_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OathTokenMetadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OathTokenMetadata
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OathTokenMetadata()
    
    @property
    def enabled(self,) -> Optional[bool]:
        """
        Gets the enabled property value. The enabled property
        Returns: Optional[bool]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the enabled property value. The enabled property
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "manufacturer_properties": lambda n : setattr(self, 'manufacturer_properties', n.get_collection_of_object_values(key_value.KeyValue)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "token_type": lambda n : setattr(self, 'token_type', n.get_str_value()),
        }
        return fields
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The manufacturer property
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer property
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def manufacturer_properties(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the manufacturerProperties property value. The manufacturerProperties property
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._manufacturer_properties
    
    @manufacturer_properties.setter
    def manufacturer_properties(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the manufacturerProperties property value. The manufacturerProperties property
        Args:
            value: Value to set for the manufacturerProperties property.
        """
        self._manufacturer_properties = value
    
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_collection_of_object_values("manufacturerProperties", self.manufacturer_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("tokenType", self.token_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. The serialNumber property
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. The serialNumber property
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def token_type(self,) -> Optional[str]:
        """
        Gets the tokenType property value. The tokenType property
        Returns: Optional[str]
        """
        return self._token_type
    
    @token_type.setter
    def token_type(self,value: Optional[str] = None) -> None:
        """
        Sets the tokenType property value. The tokenType property
        Args:
            value: Value to set for the tokenType property.
        """
        self._token_type = value
    

