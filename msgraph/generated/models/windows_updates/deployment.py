from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import deployable_content, deployment_audience, deployment_settings, deployment_state
    from .. import entity

from .. import entity

@dataclass
class Deployment(entity.Entity):
    # Specifies the audience to which content is deployed.
    audience: Optional[deployment_audience.DeploymentAudience] = None
    # Specifies what content to deploy. Cannot be changed. Returned by default.
    content: Optional[deployable_content.DeployableContent] = None
    # The date and time the deployment was created. Returned by default. Read-only.
    created_date_time: Optional[datetime] = None
    # The date and time the deployment was last modified. Returned by default. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Settings specified on the specific deployment governing how to deploy content. Returned by default.
    settings: Optional[deployment_settings.DeploymentSettings] = None
    # Execution status of the deployment. Returned by default.
    state: Optional[deployment_state.DeploymentState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Deployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Deployment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Deployment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import deployable_content, deployment_audience, deployment_settings, deployment_state
        from .. import entity

        from . import deployable_content, deployment_audience, deployment_settings, deployment_state
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "audience": lambda n : setattr(self, 'audience', n.get_object_value(deployment_audience.DeploymentAudience)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(deployable_content.DeployableContent)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(deployment_settings.DeploymentSettings)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(deployment_state.DeploymentState)),
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
        writer.write_object_value("audience", self.audience)
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("state", self.state)
    

