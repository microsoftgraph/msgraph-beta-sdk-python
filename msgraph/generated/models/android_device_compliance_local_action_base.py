from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_device_compliance_local_action_lock_device, android_device_compliance_local_action_lock_device_with_passcode, entity

from . import entity

@dataclass
class AndroidDeviceComplianceLocalActionBase(entity.Entity):
    # Number of minutes to wait till a local action is enforced. Valid values 0 to 2147483647
    grace_period_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidDeviceComplianceLocalActionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidDeviceComplianceLocalActionBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceComplianceLocalActionLockDevice".casefold():
            from . import android_device_compliance_local_action_lock_device

            return android_device_compliance_local_action_lock_device.AndroidDeviceComplianceLocalActionLockDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidDeviceComplianceLocalActionLockDeviceWithPasscode".casefold():
            from . import android_device_compliance_local_action_lock_device_with_passcode

            return android_device_compliance_local_action_lock_device_with_passcode.AndroidDeviceComplianceLocalActionLockDeviceWithPasscode()
        return AndroidDeviceComplianceLocalActionBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_device_compliance_local_action_lock_device, android_device_compliance_local_action_lock_device_with_passcode, entity

        from . import android_device_compliance_local_action_lock_device, android_device_compliance_local_action_lock_device_with_passcode, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "gracePeriodInMinutes": lambda n : setattr(self, 'grace_period_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("gracePeriodInMinutes", self.grace_period_in_minutes)
    

