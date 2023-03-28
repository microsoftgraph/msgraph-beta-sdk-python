from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_constraint

from . import device_management_constraint

class DeviceManagementSettingIntegerConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingIntegerConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingIntegerConstraint"
        # The maximum permitted value
        self._maximum_value: Optional[int] = None
        # The minimum permitted value
        self._minimum_value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingIntegerConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingIntegerConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingIntegerConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumValue": lambda n : setattr(self, 'maximum_value', n.get_int_value()),
            "minimumValue": lambda n : setattr(self, 'minimum_value', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_value(self,) -> Optional[int]:
        """
        Gets the maximumValue property value. The maximum permitted value
        Returns: Optional[int]
        """
        return self._maximum_value
    
    @maximum_value.setter
    def maximum_value(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumValue property value. The maximum permitted value
        Args:
            value: Value to set for the maximum_value property.
        """
        self._maximum_value = value
    
    @property
    def minimum_value(self,) -> Optional[int]:
        """
        Gets the minimumValue property value. The minimum permitted value
        Returns: Optional[int]
        """
        return self._minimum_value
    
    @minimum_value.setter
    def minimum_value(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumValue property value. The minimum permitted value
        Args:
            value: Value to set for the minimum_value property.
        """
        self._minimum_value = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumValue", self.maximum_value)
        writer.write_int_value("minimumValue", self.minimum_value)
    

