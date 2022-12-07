from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
deployable_content = lazy_import('msgraph.generated.models.windows_updates.deployable_content')
deployment_audience = lazy_import('msgraph.generated.models.windows_updates.deployment_audience')
deployment_settings = lazy_import('msgraph.generated.models.windows_updates.deployment_settings')
deployment_state = lazy_import('msgraph.generated.models.windows_updates.deployment_state')

class Deployment(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def audience(self,) -> Optional[deployment_audience.DeploymentAudience]:
        """
        Gets the audience property value. Specifies the audience to which content is deployed.
        Returns: Optional[deployment_audience.DeploymentAudience]
        """
        return self._audience
    
    @audience.setter
    def audience(self,value: Optional[deployment_audience.DeploymentAudience] = None) -> None:
        """
        Sets the audience property value. Specifies the audience to which content is deployed.
        Args:
            value: Value to set for the audience property.
        """
        self._audience = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deployment and sets the default values.
        """
        super().__init__()
        # Specifies the audience to which content is deployed.
        self._audience: Optional[deployment_audience.DeploymentAudience] = None
        # Specifies what content to deploy. Cannot be changed. Returned by default.
        self._content: Optional[deployable_content.DeployableContent] = None
        # The date and time the deployment was created. Returned by default. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The date and time the deployment was last modified. Returned by default. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Settings specified on the specific deployment governing how to deploy content. Returned by default.
        self._settings: Optional[deployment_settings.DeploymentSettings] = None
        # Execution status of the deployment. Returned by default.
        self._state: Optional[deployment_state.DeploymentState] = None
    
    @property
    def content(self,) -> Optional[deployable_content.DeployableContent]:
        """
        Gets the content property value. Specifies what content to deploy. Cannot be changed. Returned by default.
        Returns: Optional[deployable_content.DeployableContent]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[deployable_content.DeployableContent] = None) -> None:
        """
        Sets the content property value. Specifies what content to deploy. Cannot be changed. Returned by default.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the deployment was created. Returned by default. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the deployment was created. Returned by default. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Deployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Deployment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Deployment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audience": lambda n : setattr(self, 'audience', n.get_object_value(deployment_audience.DeploymentAudience)),
            "content": lambda n : setattr(self, 'content', n.get_object_value(deployable_content.DeployableContent)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(deployment_settings.DeploymentSettings)),
            "state": lambda n : setattr(self, 'state', n.get_object_value(deployment_state.DeploymentState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the deployment was last modified. Returned by default. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the deployment was last modified. Returned by default. Read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
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
        writer.write_object_value("audience", self.audience)
        writer.write_object_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("state", self.state)
    
    @property
    def settings(self,) -> Optional[deployment_settings.DeploymentSettings]:
        """
        Gets the settings property value. Settings specified on the specific deployment governing how to deploy content. Returned by default.
        Returns: Optional[deployment_settings.DeploymentSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[deployment_settings.DeploymentSettings] = None) -> None:
        """
        Sets the settings property value. Settings specified on the specific deployment governing how to deploy content. Returned by default.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def state(self,) -> Optional[deployment_state.DeploymentState]:
        """
        Gets the state property value. Execution status of the deployment. Returned by default.
        Returns: Optional[deployment_state.DeploymentState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[deployment_state.DeploymentState] = None) -> None:
        """
        Sets the state property value. Execution status of the deployment. Returned by default.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

