from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_fota_deployment_assignment, entity, zebra_fota_deployment_settings, zebra_fota_deployment_status

from . import entity

@dataclass
class ZebraFotaDeployment(entity.Entity):
    """
    The Zebra FOTA deployment entity that describes settings, deployment device groups required to create a FOTA deployment, and deployment status.
    """
    # Collection of Android FOTA Assignment
    deployment_assignments: Optional[List[android_fota_deployment_assignment.AndroidFotaDeploymentAssignment]] = None
    # The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
    deployment_settings: Optional[zebra_fota_deployment_settings.ZebraFotaDeploymentSettings] = None
    # Represents the deployment status from Zebra. The status is a high level status of the deployment as opposed being a detailed status per device.
    deployment_status: Optional[zebra_fota_deployment_status.ZebraFotaDeploymentStatus] = None
    # A human readable description of the deployment.
    description: Optional[str] = None
    # A human readable name of the deployment.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance
    role_scope_tag_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ZebraFotaDeployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeployment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ZebraFotaDeployment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_fota_deployment_assignment, entity, zebra_fota_deployment_settings, zebra_fota_deployment_status

        fields: Dict[str, Callable[[Any], None]] = {
            "deploymentAssignments": lambda n : setattr(self, 'deployment_assignments', n.get_collection_of_object_values(android_fota_deployment_assignment.AndroidFotaDeploymentAssignment)),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(zebra_fota_deployment_settings.ZebraFotaDeploymentSettings)),
            "deploymentStatus": lambda n : setattr(self, 'deployment_status', n.get_object_value(zebra_fota_deployment_status.ZebraFotaDeploymentStatus)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("deploymentAssignments", self.deployment_assignments)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
        writer.write_object_value("deploymentStatus", self.deployment_status)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

