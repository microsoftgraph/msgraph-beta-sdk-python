from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_scope_action_status = lazy_import('msgraph.generated.models.device_scope_action_status')

class DeviceScopeActionResult(AdditionalDataHolder, Parsable):
    """
    The result of the triggered device scope action.
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
        Instantiates a new deviceScopeActionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        self._device_scope_action: Optional[str] = None
        # The unique identifier of the device scope the action was triggered on.
        self._device_scope_id: Optional[str] = None
        # The message indicates the reason the device scope action failed to trigger.
        self._failed_message: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the status of the attempted device scope action
        self._status: Optional[device_scope_action_status.DeviceScopeActionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceScopeActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceScopeActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceScopeActionResult()
    
    @property
    def device_scope_action(self,) -> Optional[str]:
        """
        Gets the deviceScopeAction property value. Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        Returns: Optional[str]
        """
        return self._device_scope_action
    
    @device_scope_action.setter
    def device_scope_action(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceScopeAction property value. Trigger on the service to either START or STOP computing metrics data based on a device scope configuration.
        Args:
            value: Value to set for the deviceScopeAction property.
        """
        self._device_scope_action = value
    
    @property
    def device_scope_id(self,) -> Optional[str]:
        """
        Gets the deviceScopeId property value. The unique identifier of the device scope the action was triggered on.
        Returns: Optional[str]
        """
        return self._device_scope_id
    
    @device_scope_id.setter
    def device_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceScopeId property value. The unique identifier of the device scope the action was triggered on.
        Args:
            value: Value to set for the deviceScopeId property.
        """
        self._device_scope_id = value
    
    @property
    def failed_message(self,) -> Optional[str]:
        """
        Gets the failedMessage property value. The message indicates the reason the device scope action failed to trigger.
        Returns: Optional[str]
        """
        return self._failed_message
    
    @failed_message.setter
    def failed_message(self,value: Optional[str] = None) -> None:
        """
        Sets the failedMessage property value. The message indicates the reason the device scope action failed to trigger.
        Args:
            value: Value to set for the failedMessage property.
        """
        self._failed_message = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_scope_action": lambda n : setattr(self, 'device_scope_action', n.get_str_value()),
            "device_scope_id": lambda n : setattr(self, 'device_scope_id', n.get_str_value()),
            "failed_message": lambda n : setattr(self, 'failed_message', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(device_scope_action_status.DeviceScopeActionStatus)),
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
        writer.write_str_value("deviceScopeAction", self.device_scope_action)
        writer.write_str_value("deviceScopeId", self.device_scope_id)
        writer.write_str_value("failedMessage", self.failed_message)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[device_scope_action_status.DeviceScopeActionStatus]:
        """
        Gets the status property value. Indicates the status of the attempted device scope action
        Returns: Optional[device_scope_action_status.DeviceScopeActionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[device_scope_action_status.DeviceScopeActionStatus] = None) -> None:
        """
        Sets the status property value. Indicates the status of the attempted device scope action
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

