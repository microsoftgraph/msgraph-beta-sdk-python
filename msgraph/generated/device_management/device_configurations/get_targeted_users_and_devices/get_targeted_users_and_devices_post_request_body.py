from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class GetTargetedUsersAndDevicesPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new getTargetedUsersAndDevicesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The deviceConfigurationIds property
        self._device_configuration_ids: Optional[List[str]] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GetTargetedUsersAndDevicesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GetTargetedUsersAndDevicesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GetTargetedUsersAndDevicesPostRequestBody()
    
    @property
    def device_configuration_ids(self,) -> Optional[List[str]]:
        """
        Gets the deviceConfigurationIds property value. The deviceConfigurationIds property
        Returns: Optional[List[str]]
        """
        return self._device_configuration_ids
    
    @device_configuration_ids.setter
    def device_configuration_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the deviceConfigurationIds property value. The deviceConfigurationIds property
        Args:
            value: Value to set for the device_configuration_ids property.
        """
        self._device_configuration_ids = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deviceConfigurationIds": lambda n : setattr(self, 'device_configuration_ids', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("deviceConfigurationIds", self.device_configuration_ids)
        writer.write_additional_data_value(self.additional_data)
    

