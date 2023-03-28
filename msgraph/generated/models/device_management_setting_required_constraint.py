from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_constraint

from . import device_management_constraint

class DeviceManagementSettingRequiredConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingRequiredConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingRequiredConstraint"
        # List of value which means not configured for the setting
        self._not_configured_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingRequiredConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingRequiredConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingRequiredConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "notConfiguredValue": lambda n : setattr(self, 'not_configured_value', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def not_configured_value(self,) -> Optional[str]:
        """
        Gets the notConfiguredValue property value. List of value which means not configured for the setting
        Returns: Optional[str]
        """
        return self._not_configured_value
    
    @not_configured_value.setter
    def not_configured_value(self,value: Optional[str] = None) -> None:
        """
        Sets the notConfiguredValue property value. List of value which means not configured for the setting
        Args:
            value: Value to set for the not_configured_value property.
        """
        self._not_configured_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("notConfiguredValue", self.not_configured_value)
    

