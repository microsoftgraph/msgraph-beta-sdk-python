from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_connection = lazy_import('msgraph.generated.models.teamwork_connection')
teamwork_hardware_health = lazy_import('msgraph.generated.models.teamwork_hardware_health')
teamwork_login_status = lazy_import('msgraph.generated.models.teamwork_login_status')
teamwork_peripherals_health = lazy_import('msgraph.generated.models.teamwork_peripherals_health')
teamwork_software_update_health = lazy_import('msgraph.generated.models.teamwork_software_update_health')

class TeamworkDeviceHealth(entity.Entity):
    @property
    def connection(self,) -> Optional[teamwork_connection.TeamworkConnection]:
        """
        Gets the connection property value. The connection property
        Returns: Optional[teamwork_connection.TeamworkConnection]
        """
        return self._connection
    
    @connection.setter
    def connection(self,value: Optional[teamwork_connection.TeamworkConnection] = None) -> None:
        """
        Sets the connection property value. The connection property
        Args:
            value: Value to set for the connection property.
        """
        self._connection = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamworkDeviceHealth and sets the default values.
        """
        super().__init__()
        # The connection property
        self._connection: Optional[teamwork_connection.TeamworkConnection] = None
        # Identity of the user who created the device health document.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device health document was created.
        self._created_date_time: Optional[datetime] = None
        # Health details about the device hardware.
        self._hardware_health: Optional[teamwork_hardware_health.TeamworkHardwareHealth] = None
        # Identity of the user who last modified the device health details.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device health detail was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The login status of Microsoft Teams, Skype for Business, and Exchange.
        self._login_status: Optional[teamwork_login_status.TeamworkLoginStatus] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Health details about all peripherals (for example, speaker and microphone) attached to a device.
        self._peripherals_health: Optional[teamwork_peripherals_health.TeamworkPeripheralsHealth] = None
        # Software updates available for the device.
        self._software_update_health: Optional[teamwork_software_update_health.TeamworkSoftwareUpdateHealth] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user who created the device health document.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who created the device health document.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The UTC date and time when the device health document was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The UTC date and time when the device health document was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDeviceHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceHealth
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDeviceHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connection": lambda n : setattr(self, 'connection', n.get_object_value(teamwork_connection.TeamworkConnection)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "hardware_health": lambda n : setattr(self, 'hardware_health', n.get_object_value(teamwork_hardware_health.TeamworkHardwareHealth)),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "login_status": lambda n : setattr(self, 'login_status', n.get_object_value(teamwork_login_status.TeamworkLoginStatus)),
            "peripherals_health": lambda n : setattr(self, 'peripherals_health', n.get_object_value(teamwork_peripherals_health.TeamworkPeripheralsHealth)),
            "software_update_health": lambda n : setattr(self, 'software_update_health', n.get_object_value(teamwork_software_update_health.TeamworkSoftwareUpdateHealth)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hardware_health(self,) -> Optional[teamwork_hardware_health.TeamworkHardwareHealth]:
        """
        Gets the hardwareHealth property value. Health details about the device hardware.
        Returns: Optional[teamwork_hardware_health.TeamworkHardwareHealth]
        """
        return self._hardware_health
    
    @hardware_health.setter
    def hardware_health(self,value: Optional[teamwork_hardware_health.TeamworkHardwareHealth] = None) -> None:
        """
        Sets the hardwareHealth property value. Health details about the device hardware.
        Args:
            value: Value to set for the hardwareHealth property.
        """
        self._hardware_health = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user who last modified the device health details.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who last modified the device health details.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The UTC date and time when the device health detail was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The UTC date and time when the device health detail was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def login_status(self,) -> Optional[teamwork_login_status.TeamworkLoginStatus]:
        """
        Gets the loginStatus property value. The login status of Microsoft Teams, Skype for Business, and Exchange.
        Returns: Optional[teamwork_login_status.TeamworkLoginStatus]
        """
        return self._login_status
    
    @login_status.setter
    def login_status(self,value: Optional[teamwork_login_status.TeamworkLoginStatus] = None) -> None:
        """
        Sets the loginStatus property value. The login status of Microsoft Teams, Skype for Business, and Exchange.
        Args:
            value: Value to set for the loginStatus property.
        """
        self._login_status = value
    
    @property
    def peripherals_health(self,) -> Optional[teamwork_peripherals_health.TeamworkPeripheralsHealth]:
        """
        Gets the peripheralsHealth property value. Health details about all peripherals (for example, speaker and microphone) attached to a device.
        Returns: Optional[teamwork_peripherals_health.TeamworkPeripheralsHealth]
        """
        return self._peripherals_health
    
    @peripherals_health.setter
    def peripherals_health(self,value: Optional[teamwork_peripherals_health.TeamworkPeripheralsHealth] = None) -> None:
        """
        Sets the peripheralsHealth property value. Health details about all peripherals (for example, speaker and microphone) attached to a device.
        Args:
            value: Value to set for the peripheralsHealth property.
        """
        self._peripherals_health = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("connection", self.connection)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("hardwareHealth", self.hardware_health)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("loginStatus", self.login_status)
        writer.write_object_value("peripheralsHealth", self.peripherals_health)
        writer.write_object_value("softwareUpdateHealth", self.software_update_health)
    
    @property
    def software_update_health(self,) -> Optional[teamwork_software_update_health.TeamworkSoftwareUpdateHealth]:
        """
        Gets the softwareUpdateHealth property value. Software updates available for the device.
        Returns: Optional[teamwork_software_update_health.TeamworkSoftwareUpdateHealth]
        """
        return self._software_update_health
    
    @software_update_health.setter
    def software_update_health(self,value: Optional[teamwork_software_update_health.TeamworkSoftwareUpdateHealth] = None) -> None:
        """
        Sets the softwareUpdateHealth property value. Software updates available for the device.
        Args:
            value: Value to set for the softwareUpdateHealth property.
        """
        self._software_update_health = value
    

