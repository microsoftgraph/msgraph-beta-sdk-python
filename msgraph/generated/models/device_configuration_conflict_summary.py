from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
setting_source = lazy_import('msgraph.generated.models.setting_source')

class DeviceConfigurationConflictSummary(entity.Entity):
    """
    Conflict summary for a set of device configuration policies.
    """
    @property
    def conflicting_device_configurations(self,) -> Optional[List[setting_source.SettingSource]]:
        """
        Gets the conflictingDeviceConfigurations property value. The set of policies in conflict with the given setting
        Returns: Optional[List[setting_source.SettingSource]]
        """
        return self._conflicting_device_configurations
    
    @conflicting_device_configurations.setter
    def conflicting_device_configurations(self,value: Optional[List[setting_source.SettingSource]] = None) -> None:
        """
        Sets the conflictingDeviceConfigurations property value. The set of policies in conflict with the given setting
        Args:
            value: Value to set for the conflictingDeviceConfigurations property.
        """
        self._conflicting_device_configurations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfigurationConflictSummary and sets the default values.
        """
        super().__init__()
        # The set of policies in conflict with the given setting
        self._conflicting_device_configurations: Optional[List[setting_source.SettingSource]] = None
        # The set of settings in conflict with the given policies
        self._contributing_settings: Optional[List[str]] = None
        # The count of checkins impacted by the conflicting policies and settings
        self._device_checkins_impacted: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def contributing_settings(self,) -> Optional[List[str]]:
        """
        Gets the contributingSettings property value. The set of settings in conflict with the given policies
        Returns: Optional[List[str]]
        """
        return self._contributing_settings
    
    @contributing_settings.setter
    def contributing_settings(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contributingSettings property value. The set of settings in conflict with the given policies
        Args:
            value: Value to set for the contributingSettings property.
        """
        self._contributing_settings = value
    
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
    
    @property
    def device_checkins_impacted(self,) -> Optional[int]:
        """
        Gets the deviceCheckinsImpacted property value. The count of checkins impacted by the conflicting policies and settings
        Returns: Optional[int]
        """
        return self._device_checkins_impacted
    
    @device_checkins_impacted.setter
    def device_checkins_impacted(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceCheckinsImpacted property value. The count of checkins impacted by the conflicting policies and settings
        Args:
            value: Value to set for the deviceCheckinsImpacted property.
        """
        self._device_checkins_impacted = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conflicting_device_configurations": lambda n : setattr(self, 'conflicting_device_configurations', n.get_collection_of_object_values(setting_source.SettingSource)),
            "contributing_settings": lambda n : setattr(self, 'contributing_settings', n.get_collection_of_primitive_values(str)),
            "device_checkins_impacted": lambda n : setattr(self, 'device_checkins_impacted', n.get_int_value()),
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
    

