from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_management_assignment_target, entity, user

from . import entity

class CloudPcProvisioningPolicyAssignment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcProvisioningPolicyAssignment and sets the default values.
        """
        super().__init__()
        # The assignedUsers property
        self._assigned_users: Optional[List[user.User]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The assignment target for the provisioning policy. Currently, the only target supported for this policy is a user group. For details, see cloudPcManagementGroupAssignmentTarget.
        self._target: Optional[cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget] = None
    
    @property
    def assigned_users(self,) -> Optional[List[user.User]]:
        """
        Gets the assignedUsers property value. The assignedUsers property
        Returns: Optional[List[user.User]]
        """
        return self._assigned_users
    
    @assigned_users.setter
    def assigned_users(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the assignedUsers property value. The assignedUsers property
        Args:
            value: Value to set for the assigned_users property.
        """
        self._assigned_users = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcProvisioningPolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcProvisioningPolicyAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcProvisioningPolicyAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_management_assignment_target, entity, user

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedUsers": lambda n : setattr(self, 'assigned_users', n.get_collection_of_object_values(user.User)),
            "target": lambda n : setattr(self, 'target', n.get_object_value(cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget)),
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
        writer.write_collection_of_object_values("assignedUsers", self.assigned_users)
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget]:
        """
        Gets the target property value. The assignment target for the provisioning policy. Currently, the only target supported for this policy is a user group. For details, see cloudPcManagementGroupAssignmentTarget.
        Returns: Optional[cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget] = None) -> None:
        """
        Sets the target property value. The assignment target for the provisioning policy. Currently, the only target supported for this policy is a user group. For details, see cloudPcManagementGroupAssignmentTarget.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

