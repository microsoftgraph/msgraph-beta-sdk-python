from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_camera_configuration = lazy_import('msgraph.generated.models.teamwork_camera_configuration')
teamwork_device_software_versions = lazy_import('msgraph.generated.models.teamwork_device_software_versions')
teamwork_display_configuration = lazy_import('msgraph.generated.models.teamwork_display_configuration')
teamwork_hardware_configuration = lazy_import('msgraph.generated.models.teamwork_hardware_configuration')
teamwork_microphone_configuration = lazy_import('msgraph.generated.models.teamwork_microphone_configuration')
teamwork_speaker_configuration = lazy_import('msgraph.generated.models.teamwork_speaker_configuration')
teamwork_system_configuration = lazy_import('msgraph.generated.models.teamwork_system_configuration')
teamwork_teams_client_configuration = lazy_import('msgraph.generated.models.teamwork_teams_client_configuration')

class TeamworkDeviceConfiguration(entity.Entity):
    @property
    def camera_configuration(self,) -> Optional[teamwork_camera_configuration.TeamworkCameraConfiguration]:
        """
        Gets the cameraConfiguration property value. The camera configuration. Applicable only for Microsoft Teams Rooms-enabled devices.
        Returns: Optional[teamwork_camera_configuration.TeamworkCameraConfiguration]
        """
        return self._camera_configuration
    
    @camera_configuration.setter
    def camera_configuration(self,value: Optional[teamwork_camera_configuration.TeamworkCameraConfiguration] = None) -> None:
        """
        Sets the cameraConfiguration property value. The camera configuration. Applicable only for Microsoft Teams Rooms-enabled devices.
        Args:
            value: Value to set for the cameraConfiguration property.
        """
        self._camera_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDeviceConfiguration and sets the default values.
        """
        super().__init__()
        # The camera configuration. Applicable only for Microsoft Teams Rooms-enabled devices.
        self._camera_configuration: Optional[teamwork_camera_configuration.TeamworkCameraConfiguration] = None
        # Identity of the user who created the device configuration document.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device configuration document was created.
        self._created_date_time: Optional[datetime] = None
        # The display configuration.
        self._display_configuration: Optional[teamwork_display_configuration.TeamworkDisplayConfiguration] = None
        # The hardware configuration. Applicable only for Teams Rooms-enabled devices.
        self._hardware_configuration: Optional[teamwork_hardware_configuration.TeamworkHardwareConfiguration] = None
        # Identity of the user who last modified the device configuration.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device configuration was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The microphone configuration. Applicable only for Teams Rooms-enabled devices.
        self._microphone_configuration: Optional[teamwork_microphone_configuration.TeamworkMicrophoneConfiguration] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Information related to software versions for the device, such as firmware, operating system, Teams client, and admin agent.
        self._software_versions: Optional[teamwork_device_software_versions.TeamworkDeviceSoftwareVersions] = None
        # The speaker configuration. Applicable only for Teams Rooms-enabled devices.
        self._speaker_configuration: Optional[teamwork_speaker_configuration.TeamworkSpeakerConfiguration] = None
        # The system configuration. Not applicable for Teams Rooms-enabled devices.
        self._system_configuration: Optional[teamwork_system_configuration.TeamworkSystemConfiguration] = None
        # The Teams client configuration. Applicable only for Teams Rooms-enabled devices.
        self._teams_client_configuration: Optional[teamwork_teams_client_configuration.TeamworkTeamsClientConfiguration] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user who created the device configuration document.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the device configuration document.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The UTC date and time when the device configuration document was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The UTC date and time when the device configuration document was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDeviceConfiguration()
    
    @property
    def display_configuration(self,) -> Optional[teamwork_display_configuration.TeamworkDisplayConfiguration]:
        """
        Gets the displayConfiguration property value. The display configuration.
        Returns: Optional[teamwork_display_configuration.TeamworkDisplayConfiguration]
        """
        return self._display_configuration
    
    @display_configuration.setter
    def display_configuration(self,value: Optional[teamwork_display_configuration.TeamworkDisplayConfiguration] = None) -> None:
        """
        Sets the displayConfiguration property value. The display configuration.
        Args:
            value: Value to set for the displayConfiguration property.
        """
        self._display_configuration = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "camera_configuration": lambda n : setattr(self, 'camera_configuration', n.get_object_value(teamwork_camera_configuration.TeamworkCameraConfiguration)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_configuration": lambda n : setattr(self, 'display_configuration', n.get_object_value(teamwork_display_configuration.TeamworkDisplayConfiguration)),
            "hardware_configuration": lambda n : setattr(self, 'hardware_configuration', n.get_object_value(teamwork_hardware_configuration.TeamworkHardwareConfiguration)),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "microphone_configuration": lambda n : setattr(self, 'microphone_configuration', n.get_object_value(teamwork_microphone_configuration.TeamworkMicrophoneConfiguration)),
            "software_versions": lambda n : setattr(self, 'software_versions', n.get_object_value(teamwork_device_software_versions.TeamworkDeviceSoftwareVersions)),
            "speaker_configuration": lambda n : setattr(self, 'speaker_configuration', n.get_object_value(teamwork_speaker_configuration.TeamworkSpeakerConfiguration)),
            "system_configuration": lambda n : setattr(self, 'system_configuration', n.get_object_value(teamwork_system_configuration.TeamworkSystemConfiguration)),
            "teams_client_configuration": lambda n : setattr(self, 'teams_client_configuration', n.get_object_value(teamwork_teams_client_configuration.TeamworkTeamsClientConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hardware_configuration(self,) -> Optional[teamwork_hardware_configuration.TeamworkHardwareConfiguration]:
        """
        Gets the hardwareConfiguration property value. The hardware configuration. Applicable only for Teams Rooms-enabled devices.
        Returns: Optional[teamwork_hardware_configuration.TeamworkHardwareConfiguration]
        """
        return self._hardware_configuration
    
    @hardware_configuration.setter
    def hardware_configuration(self,value: Optional[teamwork_hardware_configuration.TeamworkHardwareConfiguration] = None) -> None:
        """
        Sets the hardwareConfiguration property value. The hardware configuration. Applicable only for Teams Rooms-enabled devices.
        Args:
            value: Value to set for the hardwareConfiguration property.
        """
        self._hardware_configuration = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user who last modified the device configuration.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who last modified the device configuration.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The UTC date and time when the device configuration was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The UTC date and time when the device configuration was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def microphone_configuration(self,) -> Optional[teamwork_microphone_configuration.TeamworkMicrophoneConfiguration]:
        """
        Gets the microphoneConfiguration property value. The microphone configuration. Applicable only for Teams Rooms-enabled devices.
        Returns: Optional[teamwork_microphone_configuration.TeamworkMicrophoneConfiguration]
        """
        return self._microphone_configuration
    
    @microphone_configuration.setter
    def microphone_configuration(self,value: Optional[teamwork_microphone_configuration.TeamworkMicrophoneConfiguration] = None) -> None:
        """
        Sets the microphoneConfiguration property value. The microphone configuration. Applicable only for Teams Rooms-enabled devices.
        Args:
            value: Value to set for the microphoneConfiguration property.
        """
        self._microphone_configuration = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("cameraConfiguration", self.camera_configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("displayConfiguration", self.display_configuration)
        writer.write_object_value("hardwareConfiguration", self.hardware_configuration)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("microphoneConfiguration", self.microphone_configuration)
        writer.write_object_value("softwareVersions", self.software_versions)
        writer.write_object_value("speakerConfiguration", self.speaker_configuration)
        writer.write_object_value("systemConfiguration", self.system_configuration)
        writer.write_object_value("teamsClientConfiguration", self.teams_client_configuration)
    
    @property
    def software_versions(self,) -> Optional[teamwork_device_software_versions.TeamworkDeviceSoftwareVersions]:
        """
        Gets the softwareVersions property value. Information related to software versions for the device, such as firmware, operating system, Teams client, and admin agent.
        Returns: Optional[teamwork_device_software_versions.TeamworkDeviceSoftwareVersions]
        """
        return self._software_versions
    
    @software_versions.setter
    def software_versions(self,value: Optional[teamwork_device_software_versions.TeamworkDeviceSoftwareVersions] = None) -> None:
        """
        Sets the softwareVersions property value. Information related to software versions for the device, such as firmware, operating system, Teams client, and admin agent.
        Args:
            value: Value to set for the softwareVersions property.
        """
        self._software_versions = value
    
    @property
    def speaker_configuration(self,) -> Optional[teamwork_speaker_configuration.TeamworkSpeakerConfiguration]:
        """
        Gets the speakerConfiguration property value. The speaker configuration. Applicable only for Teams Rooms-enabled devices.
        Returns: Optional[teamwork_speaker_configuration.TeamworkSpeakerConfiguration]
        """
        return self._speaker_configuration
    
    @speaker_configuration.setter
    def speaker_configuration(self,value: Optional[teamwork_speaker_configuration.TeamworkSpeakerConfiguration] = None) -> None:
        """
        Sets the speakerConfiguration property value. The speaker configuration. Applicable only for Teams Rooms-enabled devices.
        Args:
            value: Value to set for the speakerConfiguration property.
        """
        self._speaker_configuration = value
    
    @property
    def system_configuration(self,) -> Optional[teamwork_system_configuration.TeamworkSystemConfiguration]:
        """
        Gets the systemConfiguration property value. The system configuration. Not applicable for Teams Rooms-enabled devices.
        Returns: Optional[teamwork_system_configuration.TeamworkSystemConfiguration]
        """
        return self._system_configuration
    
    @system_configuration.setter
    def system_configuration(self,value: Optional[teamwork_system_configuration.TeamworkSystemConfiguration] = None) -> None:
        """
        Sets the systemConfiguration property value. The system configuration. Not applicable for Teams Rooms-enabled devices.
        Args:
            value: Value to set for the systemConfiguration property.
        """
        self._system_configuration = value
    
    @property
    def teams_client_configuration(self,) -> Optional[teamwork_teams_client_configuration.TeamworkTeamsClientConfiguration]:
        """
        Gets the teamsClientConfiguration property value. The Teams client configuration. Applicable only for Teams Rooms-enabled devices.
        Returns: Optional[teamwork_teams_client_configuration.TeamworkTeamsClientConfiguration]
        """
        return self._teams_client_configuration
    
    @teams_client_configuration.setter
    def teams_client_configuration(self,value: Optional[teamwork_teams_client_configuration.TeamworkTeamsClientConfiguration] = None) -> None:
        """
        Sets the teamsClientConfiguration property value. The Teams client configuration. Applicable only for Teams Rooms-enabled devices.
        Args:
            value: Value to set for the teamsClientConfiguration property.
        """
        self._teams_client_configuration = value
    

