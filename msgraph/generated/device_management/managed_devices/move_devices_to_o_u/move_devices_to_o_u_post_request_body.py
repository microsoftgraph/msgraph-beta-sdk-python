from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class MoveDevicesToOUPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the moveDevicesToOU method.
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
        Instantiates a new moveDevicesToOUPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceIds property
        self._device_ids: Optional[List[Guid]] = None
        # The organizationalUnitPath property
        self._organizational_unit_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MoveDevicesToOUPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MoveDevicesToOUPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MoveDevicesToOUPostRequestBody()
    
    @property
    def device_ids(self,) -> Optional[List[Guid]]:
        """
        Gets the deviceIds property value. The deviceIds property
        Returns: Optional[List[Guid]]
        """
        return self._device_ids
    
    @device_ids.setter
    def device_ids(self,value: Optional[List[Guid]] = None) -> None:
        """
        Sets the deviceIds property value. The deviceIds property
        Args:
            value: Value to set for the deviceIds property.
        """
        self._device_ids = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_ids": lambda n : setattr(self, 'device_ids', n.get_collection_of_primitive_values(guid)),
            "organizational_unit_path": lambda n : setattr(self, 'organizational_unit_path', n.get_str_value()),
        }
        return fields
    
    @property
    def organizational_unit_path(self,) -> Optional[str]:
        """
        Gets the organizationalUnitPath property value. The organizationalUnitPath property
        Returns: Optional[str]
        """
        return self._organizational_unit_path
    
    @organizational_unit_path.setter
    def organizational_unit_path(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationalUnitPath property value. The organizationalUnitPath property
        Args:
            value: Value to set for the organizationalUnitPath property.
        """
        self._organizational_unit_path = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("deviceIds", self.device_ids)
        writer.write_str_value("organizationalUnitPath", self.organizational_unit_path)
        writer.write_additional_data_value(self.additional_data)
    

