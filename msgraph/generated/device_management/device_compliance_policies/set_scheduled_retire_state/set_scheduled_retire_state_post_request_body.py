from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

scheduled_retire_state = lazy_import('msgraph.generated.models.scheduled_retire_state')

class SetScheduledRetireStatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the setScheduledRetireState method.
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
        Instantiates a new setScheduledRetireStatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The managedDeviceIds property
        self._managed_device_ids: Optional[List[str]] = None
        # The scopedToAllDevices property
        self._scoped_to_all_devices: Optional[bool] = None
        # Cancel or confirm scheduled retire 
        self._state: Optional[scheduled_retire_state.ScheduledRetireState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SetScheduledRetireStatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SetScheduledRetireStatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SetScheduledRetireStatePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "managed_device_ids": lambda n : setattr(self, 'managed_device_ids', n.get_collection_of_primitive_values(str)),
            "scoped_to_all_devices": lambda n : setattr(self, 'scoped_to_all_devices', n.get_bool_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(scheduled_retire_state.ScheduledRetireState)),
        }
        return fields
    
    @property
    def managed_device_ids(self,) -> Optional[List[str]]:
        """
        Gets the managedDeviceIds property value. The managedDeviceIds property
        Returns: Optional[List[str]]
        """
        return self._managed_device_ids
    
    @managed_device_ids.setter
    def managed_device_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the managedDeviceIds property value. The managedDeviceIds property
        Args:
            value: Value to set for the managedDeviceIds property.
        """
        self._managed_device_ids = value
    
    @property
    def scoped_to_all_devices(self,) -> Optional[bool]:
        """
        Gets the scopedToAllDevices property value. The scopedToAllDevices property
        Returns: Optional[bool]
        """
        return self._scoped_to_all_devices
    
    @scoped_to_all_devices.setter
    def scoped_to_all_devices(self,value: Optional[bool] = None) -> None:
        """
        Sets the scopedToAllDevices property value. The scopedToAllDevices property
        Args:
            value: Value to set for the scopedToAllDevices property.
        """
        self._scoped_to_all_devices = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("managedDeviceIds", self.managed_device_ids)
        writer.write_bool_value("scopedToAllDevices", self.scoped_to_all_devices)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[scheduled_retire_state.ScheduledRetireState]:
        """
        Gets the state property value. Cancel or confirm scheduled retire 
        Returns: Optional[scheduled_retire_state.ScheduledRetireState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[scheduled_retire_state.ScheduledRetireState] = None) -> None:
        """
        Sets the state property value. Cancel or confirm scheduled retire 
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

