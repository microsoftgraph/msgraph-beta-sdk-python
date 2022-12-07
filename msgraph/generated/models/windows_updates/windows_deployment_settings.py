from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

deployment_settings = lazy_import('msgraph.generated.models.windows_updates.deployment_settings')
user_experience_settings = lazy_import('msgraph.generated.models.windows_updates.user_experience_settings')

class WindowsDeploymentSettings(deployment_settings.DeploymentSettings):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsDeploymentSettings and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdates.windowsDeploymentSettings"
        # Settings governing the user's update experience on a device.
        self._user_experience: Optional[user_experience_settings.UserExperienceSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDeploymentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDeploymentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDeploymentSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_experience": lambda n : setattr(self, 'user_experience', n.get_object_value(user_experience_settings.UserExperienceSettings)),
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
        writer.write_object_value("userExperience", self.user_experience)
    
    @property
    def user_experience(self,) -> Optional[user_experience_settings.UserExperienceSettings]:
        """
        Gets the userExperience property value. Settings governing the user's update experience on a device.
        Returns: Optional[user_experience_settings.UserExperienceSettings]
        """
        return self._user_experience
    
    @user_experience.setter
    def user_experience(self,value: Optional[user_experience_settings.UserExperienceSettings] = None) -> None:
        """
        Sets the userExperience property value. Settings governing the user's update experience on a device.
        Args:
            value: Value to set for the userExperience property.
        """
        self._user_experience = value
    

