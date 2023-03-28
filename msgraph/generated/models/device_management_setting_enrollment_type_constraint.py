from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_constraint

from . import device_management_constraint

class DeviceManagementSettingEnrollmentTypeConstraint(device_management_constraint.DeviceManagementConstraint):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagementSettingEnrollmentTypeConstraint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceManagementSettingEnrollmentTypeConstraint"
        # List of enrollment types
        self._enrollment_types: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettingEnrollmentTypeConstraint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettingEnrollmentTypeConstraint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettingEnrollmentTypeConstraint()
    
    @property
    def enrollment_types(self,) -> Optional[List[str]]:
        """
        Gets the enrollmentTypes property value. List of enrollment types
        Returns: Optional[List[str]]
        """
        return self._enrollment_types
    
    @enrollment_types.setter
    def enrollment_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the enrollmentTypes property value. List of enrollment types
        Args:
            value: Value to set for the enrollment_types property.
        """
        self._enrollment_types = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_constraint

        fields: Dict[str, Callable[[Any], None]] = {
            "enrollmentTypes": lambda n : setattr(self, 'enrollment_types', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("enrollmentTypes", self.enrollment_types)
    

