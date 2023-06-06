from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, setting_source

from . import entity

@dataclass
class DeviceConfigurationConflictSummary(entity.Entity):
    """
    Conflict summary for a set of device configuration policies.
    """
    # The set of policies in conflict with the given setting
    conflicting_device_configurations: Optional[List[setting_source.SettingSource]] = None
    # The set of settings in conflict with the given policies
    contributing_settings: Optional[List[str]] = None
    # The count of checkins impacted by the conflicting policies and settings
    device_checkins_impacted: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfigurationConflictSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfigurationConflictSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceConfigurationConflictSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, setting_source

        fields: Dict[str, Callable[[Any], None]] = {
            "conflictingDeviceConfigurations": lambda n : setattr(self, 'conflicting_device_configurations', n.get_collection_of_object_values(setting_source.SettingSource)),
            "contributingSettings": lambda n : setattr(self, 'contributing_settings', n.get_collection_of_primitive_values(str)),
            "deviceCheckinsImpacted": lambda n : setattr(self, 'device_checkins_impacted', n.get_int_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("conflictingDeviceConfigurations", self.conflicting_device_configurations)
        writer.write_collection_of_primitive_values("contributingSettings", self.contributing_settings)
        writer.write_int_value("deviceCheckinsImpacted", self.device_checkins_impacted)
    

