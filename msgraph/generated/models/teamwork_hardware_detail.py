from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamworkHardwareDetail(AdditionalDataHolder, Parsable):
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
        Instantiates a new teamworkHardwareDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # MAC address.
        self._mac_addresses: Optional[List[str]] = None
        # Device manufacturer.
        self._manufacturer: Optional[str] = None
        # Devie model.
        self._model: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Device serial number.
        self._serial_number: Optional[str] = None
        # The unique identifier for the device.
        self._unique_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkHardwareDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkHardwareDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkHardwareDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "mac_addresses": lambda n : setattr(self, 'mac_addresses', n.get_collection_of_primitive_values(str)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serial_number": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "unique_id": lambda n : setattr(self, 'unique_id', n.get_str_value()),
        }
        return fields
    
    @property
    def mac_addresses(self,) -> Optional[List[str]]:
        """
        Gets the macAddresses property value. MAC address.
        Returns: Optional[List[str]]
        """
        return self._mac_addresses
    
    @mac_addresses.setter
    def mac_addresses(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the macAddresses property value. MAC address.
        Args:
            value: Value to set for the macAddresses property.
        """
        self._mac_addresses = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Device manufacturer.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Device manufacturer.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Devie model.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Devie model.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
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
        writer.write_collection_of_primitive_values("macAddresses", self.mac_addresses)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("uniqueId", self.unique_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. Device serial number.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. Device serial number.
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    
    @property
    def unique_id(self,) -> Optional[str]:
        """
        Gets the uniqueId property value. The unique identifier for the device.
        Returns: Optional[str]
        """
        return self._unique_id
    
    @unique_id.setter
    def unique_id(self,value: Optional[str] = None) -> None:
        """
        Sets the uniqueId property value. The unique identifier for the device.
        Args:
            value: Value to set for the uniqueId property.
        """
        self._unique_id = value
    

