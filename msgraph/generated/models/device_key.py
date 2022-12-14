from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceKey(AdditionalDataHolder, Parsable):
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
        Instantiates a new deviceKey and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceId property
        self._device_id: Optional[Guid] = None
        # The keyMaterial property
        self._key_material: Optional[bytes] = None
        # The keyType property
        self._key_type: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceKey
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceKey()
    
    @property
    def device_id(self,) -> Optional[Guid]:
        """
        Gets the deviceId property value. The deviceId property
        Returns: Optional[Guid]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the deviceId property value. The deviceId property
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_id": lambda n : setattr(self, 'device_id', n.get_object_value(Guid)),
            "key_material": lambda n : setattr(self, 'key_material', n.get_bytes_value()),
            "key_type": lambda n : setattr(self, 'key_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def key_material(self,) -> Optional[bytes]:
        """
        Gets the keyMaterial property value. The keyMaterial property
        Returns: Optional[bytes]
        """
        return self._key_material
    
    @key_material.setter
    def key_material(self,value: Optional[bytes] = None) -> None:
        """
        Sets the keyMaterial property value. The keyMaterial property
        Args:
            value: Value to set for the keyMaterial property.
        """
        self._key_material = value
    
    @property
    def key_type(self,) -> Optional[str]:
        """
        Gets the keyType property value. The keyType property
        Returns: Optional[str]
        """
        return self._key_type
    
    @key_type.setter
    def key_type(self,value: Optional[str] = None) -> None:
        """
        Sets the keyType property value. The keyType property
        Args:
            value: Value to set for the keyType property.
        """
        self._key_type = value
    
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
        writer.write_object_value("deviceId", self.device_id)
        writer.write_object_value("keyMaterial", self.key_material)
        writer.write_str_value("keyType", self.key_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

