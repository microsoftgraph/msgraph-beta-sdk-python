from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_management_assignment_target = lazy_import('msgraph.generated.models.cloud_pc_management_assignment_target')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcProvisioningPolicyAssignment(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcProvisioningPolicyAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The assignment target for the provisioning policy. Currently, the only target supported for this policy is a user group. For details, see cloudPcManagementGroupAssignmentTarget.
        self._target: Optional[cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget] = None
    
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
        fields = {
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
    

