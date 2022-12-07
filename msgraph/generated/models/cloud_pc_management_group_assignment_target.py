from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_management_assignment_target = lazy_import('msgraph.generated.models.cloud_pc_management_assignment_target')

class CloudPcManagementGroupAssignmentTarget(cloud_pc_management_assignment_target.CloudPcManagementAssignmentTarget):
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcManagementGroupAssignmentTarget and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.cloudPcManagementGroupAssignmentTarget"
        # The id of the assignment's target group
        self._group_id: Optional[str] = None
        # The servicePlanId property
        self._service_plan_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcManagementGroupAssignmentTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcManagementGroupAssignmentTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcManagementGroupAssignmentTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group_id": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "service_plan_id": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_id(self,) -> Optional[str]:
        """
        Gets the groupId property value. The id of the assignment's target group
        Returns: Optional[str]
        """
        return self._group_id
    
    @group_id.setter
    def group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the groupId property value. The id of the assignment's target group
        Args:
            value: Value to set for the groupId property.
        """
        self._group_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("servicePlanId", self.service_plan_id)
    
    @property
    def service_plan_id(self,) -> Optional[str]:
        """
        Gets the servicePlanId property value. The servicePlanId property
        Returns: Optional[str]
        """
        return self._service_plan_id
    
    @service_plan_id.setter
    def service_plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanId property value. The servicePlanId property
        Args:
            value: Value to set for the servicePlanId property.
        """
        self._service_plan_id = value
    

