from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_fota_deployment_assignment import AndroidFotaDeploymentAssignment
    from .entity import Entity
    from .zebra_fota_deployment_settings import ZebraFotaDeploymentSettings
    from .zebra_fota_deployment_status import ZebraFotaDeploymentStatus

from .entity import Entity

@dataclass
class ZebraFotaDeployment(Entity):
    """
    The Zebra FOTA deployment entity that describes settings, deployment device groups required to create a FOTA deployment, and deployment status.
    """
    # Collection of Android FOTA Assignment
    deployment_assignments: Optional[List[AndroidFotaDeploymentAssignment]] = None
    # The Zebra FOTA deployment complex type that describes the settings required to create a FOTA deployment.
    deployment_settings: Optional[ZebraFotaDeploymentSettings] = None
    # Represents the deployment status from Zebra. The status is a high level status of the deployment as opposed being a detailed status per device.
    deployment_status: Optional[ZebraFotaDeploymentStatus] = None
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
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeployment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ZebraFotaDeployment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_fota_deployment_assignment import AndroidFotaDeploymentAssignment
        from .entity import Entity
        from .zebra_fota_deployment_settings import ZebraFotaDeploymentSettings
        from .zebra_fota_deployment_status import ZebraFotaDeploymentStatus

        from .android_fota_deployment_assignment import AndroidFotaDeploymentAssignment
        from .entity import Entity
        from .zebra_fota_deployment_settings import ZebraFotaDeploymentSettings
        from .zebra_fota_deployment_status import ZebraFotaDeploymentStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "deploymentAssignments": lambda n : setattr(self, 'deployment_assignments', n.get_collection_of_object_values(AndroidFotaDeploymentAssignment)),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(ZebraFotaDeploymentSettings)),
            "deploymentStatus": lambda n : setattr(self, 'deployment_status', n.get_object_value(ZebraFotaDeploymentStatus)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("deploymentAssignments", self.deployment_assignments)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
        writer.write_object_value("deploymentStatus", self.deployment_status)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

