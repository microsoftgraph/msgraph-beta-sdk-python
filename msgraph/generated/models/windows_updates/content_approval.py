from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_change, deployable_content, deployment, deployment_settings

from . import compliance_change

@dataclass
class ContentApproval(compliance_change.ComplianceChange):
    odata_type = "#microsoft.graph.windowsUpdates.contentApproval"
    # The content property
    content: Optional[deployable_content.DeployableContent] = None
    # Settings for governing how to deploy content.
    deployment_settings: Optional[deployment_settings.DeploymentSettings] = None
    # Deployments created as a result of applying the approval.
    deployments: Optional[List[deployment.Deployment]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentApproval
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ContentApproval()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_change, deployable_content, deployment, deployment_settings

        from . import compliance_change, deployable_content, deployment, deployment_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(deployable_content.DeployableContent)),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(deployment_settings.DeploymentSettings)),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(deployment.Deployment)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("content", self.content)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
        writer.write_collection_of_object_values("deployments", self.deployments)
    

