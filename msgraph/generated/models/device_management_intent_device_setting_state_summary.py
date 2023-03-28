from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class DeviceManagementIntentDeviceSettingStateSummary(entity.Entity):
    """
    Entity that represents device setting state summary for an intent
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementIntentDeviceSettingStateSummary and sets the default values.
        """
        super().__init__()
        # Number of compliant devices
        self._compliant_count: Optional[int] = None
        # Number of devices in conflict
        self._conflict_count: Optional[int] = None
        # Number of error devices
        self._error_count: Optional[int] = None
        # Number of non compliant devices
        self._non_compliant_count: Optional[int] = None
        # Number of not applicable devices
        self._not_applicable_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Number of remediated devices
        self._remediated_count: Optional[int] = None
        # Name of a setting
        self._setting_name: Optional[str] = None
    
    @property
    def compliant_count(self,) -> Optional[int]:
        """
        Gets the compliantCount property value. Number of compliant devices
        Returns: Optional[int]
        """
        return self._compliant_count
    
    @compliant_count.setter
    def compliant_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantCount property value. Number of compliant devices
        Args:
            value: Value to set for the compliant_count property.
        """
        self._compliant_count = value
    
    @property
    def conflict_count(self,) -> Optional[int]:
        """
        Gets the conflictCount property value. Number of devices in conflict
        Returns: Optional[int]
        """
        return self._conflict_count
    
    @conflict_count.setter
    def conflict_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictCount property value. Number of devices in conflict
        Args:
            value: Value to set for the conflict_count property.
        """
        self._conflict_count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementIntentDeviceSettingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementIntentDeviceSettingStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementIntentDeviceSettingStateSummary()
    
    @property
    def error_count(self,) -> Optional[int]:
        """
        Gets the errorCount property value. Number of error devices
        Returns: Optional[int]
        """
        return self._error_count
    
    @error_count.setter
    def error_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorCount property value. Number of error devices
        Args:
            value: Value to set for the error_count property.
        """
        self._error_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "compliantCount": lambda n : setattr(self, 'compliant_count', n.get_int_value()),
            "conflictCount": lambda n : setattr(self, 'conflict_count', n.get_int_value()),
            "errorCount": lambda n : setattr(self, 'error_count', n.get_int_value()),
            "nonCompliantCount": lambda n : setattr(self, 'non_compliant_count', n.get_int_value()),
            "notApplicableCount": lambda n : setattr(self, 'not_applicable_count', n.get_int_value()),
            "remediatedCount": lambda n : setattr(self, 'remediated_count', n.get_int_value()),
            "settingName": lambda n : setattr(self, 'setting_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def non_compliant_count(self,) -> Optional[int]:
        """
        Gets the nonCompliantCount property value. Number of non compliant devices
        Returns: Optional[int]
        """
        return self._non_compliant_count
    
    @non_compliant_count.setter
    def non_compliant_count(self,value: Optional[int] = None) -> None:
        """
        Sets the nonCompliantCount property value. Number of non compliant devices
        Args:
            value: Value to set for the non_compliant_count property.
        """
        self._non_compliant_count = value
    
    @property
    def not_applicable_count(self,) -> Optional[int]:
        """
        Gets the notApplicableCount property value. Number of not applicable devices
        Returns: Optional[int]
        """
        return self._not_applicable_count
    
    @not_applicable_count.setter
    def not_applicable_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableCount property value. Number of not applicable devices
        Args:
            value: Value to set for the not_applicable_count property.
        """
        self._not_applicable_count = value
    
    @property
    def remediated_count(self,) -> Optional[int]:
        """
        Gets the remediatedCount property value. Number of remediated devices
        Returns: Optional[int]
        """
        return self._remediated_count
    
    @remediated_count.setter
    def remediated_count(self,value: Optional[int] = None) -> None:
        """
        Sets the remediatedCount property value. Number of remediated devices
        Args:
            value: Value to set for the remediated_count property.
        """
        self._remediated_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("compliantCount", self.compliant_count)
        writer.write_int_value("conflictCount", self.conflict_count)
        writer.write_int_value("errorCount", self.error_count)
        writer.write_int_value("nonCompliantCount", self.non_compliant_count)
        writer.write_int_value("notApplicableCount", self.not_applicable_count)
        writer.write_int_value("remediatedCount", self.remediated_count)
        writer.write_str_value("settingName", self.setting_name)
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. Name of a setting
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. Name of a setting
        Args:
            value: Value to set for the setting_name property.
        """
        self._setting_name = value
    

