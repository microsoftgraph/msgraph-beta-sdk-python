from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

run_state = lazy_import('msgraph.generated.models.run_state')

class ManagedDeviceSummarizedAppState(AdditionalDataHolder, Parsable):
    """
    Event representing a user's devices with failed or pending apps.
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
        Instantiates a new managedDeviceSummarizedAppState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # DeviceId of device represented by this object
        self._device_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the type of execution status of the device management script.
        self._summarized_app_state: Optional[run_state.RunState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceSummarizedAppState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceSummarizedAppState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceSummarizedAppState()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. DeviceId of device represented by this object
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. DeviceId of device represented by this object
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
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "summarized_app_state": lambda n : setattr(self, 'summarized_app_state', n.get_enum_value(run_state.RunState)),
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
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("summarizedAppState", self.summarized_app_state)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def summarized_app_state(self,) -> Optional[run_state.RunState]:
        """
        Gets the summarizedAppState property value. Indicates the type of execution status of the device management script.
        Returns: Optional[run_state.RunState]
        """
        return self._summarized_app_state
    
    @summarized_app_state.setter
    def summarized_app_state(self,value: Optional[run_state.RunState] = None) -> None:
        """
        Sets the summarizedAppState property value. Indicates the type of execution status of the device management script.
        Args:
            value: Value to set for the summarizedAppState property.
        """
        self._summarized_app_state = value
    

