from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_and_app_management_assignment_source = lazy_import('msgraph.generated.models.device_and_app_management_assignment_source')
device_and_app_management_assignment_target = lazy_import('msgraph.generated.models.device_and_app_management_assignment_target')
entity = lazy_import('msgraph.generated.models.entity')

class DeviceCompliancePolicyAssignment(entity.Entity):
    """
    Device compliance policy assignment.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceCompliancePolicyAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents source of assignment.
        self._source: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource] = None
        # The identifier of the source of the assignment.
        self._source_id: Optional[str] = None
        # Target for the compliance policy assignment.
        self._target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "source": lambda n : setattr(self, 'source', n.get_enum_value(device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource)),
            "source_id": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
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
        writer.write_enum_value("source", self.source)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_object_value("target", self.target)
    
    @property
    def source(self,) -> Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]:
        """
        Gets the source property value. Represents source of assignment.
        Returns: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[device_and_app_management_assignment_source.DeviceAndAppManagementAssignmentSource] = None) -> None:
        """
        Sets the source property value. Represents source of assignment.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def source_id(self,) -> Optional[str]:
        """
        Gets the sourceId property value. The identifier of the source of the assignment.
        Returns: Optional[str]
        """
        return self._source_id
    
    @source_id.setter
    def source_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceId property value. The identifier of the source of the assignment.
        Args:
            value: Value to set for the sourceId property.
        """
        self._source_id = value
    
    @property
    def target(self,) -> Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]:
        """
        Gets the target property value. Target for the compliance policy assignment.
        Returns: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. Target for the compliance policy assignment.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

