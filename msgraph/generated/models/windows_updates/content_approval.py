from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_change, deployable_content, deployment, deployment_settings

from . import compliance_change

class ContentApproval(compliance_change.ComplianceChange):
    def __init__(self,) -> None:
        """
        Instantiates a new ContentApproval and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.contentApproval"
        # The content property
        self._content: Optional[deployable_content.DeployableContent] = None
        # Settings for governing how to deploy content.
        self._deployment_settings: Optional[deployment_settings.DeploymentSettings] = None
        # Deployments created as a result of applying the approval.
        self._deployments: Optional[List[deployment.Deployment]] = None
    
    @property
    def content(self,) -> Optional[deployable_content.DeployableContent]:
        """
        Gets the content property value. The content property
        Returns: Optional[deployable_content.DeployableContent]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[deployable_content.DeployableContent] = None) -> None:
        """
        Sets the content property value. The content property
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentApproval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentApproval
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentApproval()
    
    @property
    def deployment_settings(self,) -> Optional[deployment_settings.DeploymentSettings]:
        """
        Gets the deploymentSettings property value. Settings for governing how to deploy content.
        Returns: Optional[deployment_settings.DeploymentSettings]
        """
        return self._deployment_settings
    
    @deployment_settings.setter
    def deployment_settings(self,value: Optional[deployment_settings.DeploymentSettings] = None) -> None:
        """
        Sets the deploymentSettings property value. Settings for governing how to deploy content.
        Args:
            value: Value to set for the deployment_settings property.
        """
        self._deployment_settings = value
    
    @property
    def deployments(self,) -> Optional[List[deployment.Deployment]]:
        """
        Gets the deployments property value. Deployments created as a result of applying the approval.
        Returns: Optional[List[deployment.Deployment]]
        """
        return self._deployments
    
    @deployments.setter
    def deployments(self,value: Optional[List[deployment.Deployment]] = None) -> None:
        """
        Sets the deployments property value. Deployments created as a result of applying the approval.
        Args:
            value: Value to set for the deployments property.
        """
        self._deployments = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_change, deployable_content, deployment, deployment_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(deployable_content.DeployableContent)),
            "deployments": lambda n : setattr(self, 'deployments', n.get_collection_of_object_values(deployment.Deployment)),
            "deploymentSettings": lambda n : setattr(self, 'deployment_settings', n.get_object_value(deployment_settings.DeploymentSettings)),
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
        writer.write_object_value("content", self.content)
        writer.write_collection_of_object_values("deployments", self.deployments)
        writer.write_object_value("deploymentSettings", self.deployment_settings)
    

