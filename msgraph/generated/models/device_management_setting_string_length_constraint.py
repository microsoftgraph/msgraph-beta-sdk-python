from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_constraint

from . import device_management_constraint

class DeviceManagementSettingStringLengthConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingStringLengthConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingStringLengthConstraint"
        # The maximum permitted string length
        self._maximum_length: Optional[int] = None
        # The minimum permitted string length
        self._minimum_length: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingStringLengthConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingStringLengthConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingStringLengthConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "maximumLength": lambda n : setattr(self, 'maximum_length', n.get_int_value()),
            "minimumLength": lambda n : setattr(self, 'minimum_length', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def maximum_length(self,) -> Optional[int]:
        """
        Gets the maximumLength property value. The maximum permitted string length
        Returns: Optional[int]
        """
        return self._maximum_length
    
    @maximum_length.setter
    def maximum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumLength property value. The maximum permitted string length
        Args:
            value: Value to set for the maximum_length property.
        """
        self._maximum_length = value
    
    @property
    def minimum_length(self,) -> Optional[int]:
        """
        Gets the minimumLength property value. The minimum permitted string length
        Returns: Optional[int]
        """
        return self._minimum_length
    
    @minimum_length.setter
    def minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumLength property value. The minimum permitted string length
        Args:
            value: Value to set for the minimum_length property.
        """
        self._minimum_length = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("maximumLength", self.maximum_length)
        writer.write_int_value("minimumLength", self.minimum_length)
    

