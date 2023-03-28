from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_assignment_target, entity

from . import entity

class GroupPolicyConfigurationAssignment(entity.Entity):
    """
    The group policy configuration assignment entity assigns one or more AAD groups to a specific group policy configuration.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyConfigurationAssignment and sets the default values.
        """
        super().__init__()
        # The date and time the entity was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The type of groups targeted the group policy configuration.
        self._target: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyConfigurationAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyConfigurationAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyConfigurationAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_assignment_target, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "target": lambda n : setattr(self, 'target', n.get_object_value(device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the entity was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]:
        """
        Gets the target property value. The type of groups targeted the group policy configuration.
        Returns: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[device_and_app_management_assignment_target.DeviceAndAppManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The type of groups targeted the group policy configuration.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

