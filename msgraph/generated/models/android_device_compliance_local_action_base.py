from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_compliance_local_action_lock_device, android_device_compliance_local_action_lock_device_with_passcode, entity

from . import entity

class AndroidDeviceComplianceLocalActionBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidDeviceComplianceLocalActionBase and sets the default values.
        """
        super().__init__()
        # Number of minutes to wait till a local action is enforced. Valid values 0 to 2147483647
        self._grace_period_in_minutes: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceComplianceLocalActionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceComplianceLocalActionBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidDeviceComplianceLocalActionLockDevice":
                from . import android_device_compliance_local_action_lock_device

                return android_device_compliance_local_action_lock_device.AndroidDeviceComplianceLocalActionLockDevice()
            if mapping_value == "#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode":
                from . import android_device_compliance_local_action_lock_device_with_passcode

                return android_device_compliance_local_action_lock_device_with_passcode.AndroidDeviceComplianceLocalActionLockDeviceWithPasscode()
        return AndroidDeviceComplianceLocalActionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_compliance_local_action_lock_device, android_device_compliance_local_action_lock_device_with_passcode, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "gracePeriodInMinutes": lambda n : setattr(self, 'grace_period_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grace_period_in_minutes(self,) -> Optional[int]:
        """
        Gets the gracePeriodInMinutes property value. Number of minutes to wait till a local action is enforced. Valid values 0 to 2147483647
        Returns: Optional[int]
        """
        return self._grace_period_in_minutes
    
    @grace_period_in_minutes.setter
    def grace_period_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the gracePeriodInMinutes property value. Number of minutes to wait till a local action is enforced. Valid values 0 to 2147483647
        Args:
            value: Value to set for the grace_period_in_minutes property.
        """
        self._grace_period_in_minutes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("gracePeriodInMinutes", self.grace_period_in_minutes)
    

