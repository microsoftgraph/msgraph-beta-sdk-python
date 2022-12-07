from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_constraint = lazy_import('msgraph.generated.models.device_management_constraint')
device_management_enum_value = lazy_import('msgraph.generated.models.device_management_enum_value')

class DeviceManagementEnumConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementEnumConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementEnumConstraint"
        # List of valid values for this string
        self._values: Optional[List[device_management_enum_value.DeviceManagementEnumValue]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementEnumConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementEnumConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementEnumConstraint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "values": lambda n : setattr(self, 'values', n.get_collection_of_object_values(device_management_enum_value.DeviceManagementEnumValue)),
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
        writer.write_collection_of_object_values("values", self.values)
    
    @property
    def values(self,) -> Optional[List[device_management_enum_value.DeviceManagementEnumValue]]:
        """
        Gets the values property value. List of valid values for this string
        Returns: Optional[List[device_management_enum_value.DeviceManagementEnumValue]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[device_management_enum_value.DeviceManagementEnumValue]] = None) -> None:
        """
        Sets the values property value. List of valid values for this string
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

