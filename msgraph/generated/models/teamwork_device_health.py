from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, teamwork_connection, teamwork_hardware_health, teamwork_login_status, teamwork_peripherals_health, teamwork_software_update_health

from . import entity

@dataclass
class TeamworkDeviceHealth(entity.Entity):
    # The connection property
    connection: Optional[teamwork_connection.TeamworkConnection] = None
    # Identity of the user who created the device health document.
    created_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the device health document was created.
    created_date_time: Optional[datetime] = None
    # Health details about the device hardware.
    hardware_health: Optional[teamwork_hardware_health.TeamworkHardwareHealth] = None
    # Identity of the user who last modified the device health details.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the device health detail was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The login status of Microsoft Teams, Skype for Business, and Exchange.
    login_status: Optional[teamwork_login_status.TeamworkLoginStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Health details about all peripherals (for example, speaker and microphone) attached to a device.
    peripherals_health: Optional[teamwork_peripherals_health.TeamworkPeripheralsHealth] = None
    # Software updates available for the device.
    software_update_health: Optional[teamwork_software_update_health.TeamworkSoftwareUpdateHealth] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDeviceHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDeviceHealth
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDeviceHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, teamwork_connection, teamwork_hardware_health, teamwork_login_status, teamwork_peripherals_health, teamwork_software_update_health

        from . import entity, identity_set, teamwork_connection, teamwork_hardware_health, teamwork_login_status, teamwork_peripherals_health, teamwork_software_update_health

        fields: Dict[str, Callable[[Any], None]] = {
            "connection": lambda n : setattr(self, 'connection', n.get_object_value(teamwork_connection.TeamworkConnection)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "hardwareHealth": lambda n : setattr(self, 'hardware_health', n.get_object_value(teamwork_hardware_health.TeamworkHardwareHealth)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "loginStatus": lambda n : setattr(self, 'login_status', n.get_object_value(teamwork_login_status.TeamworkLoginStatus)),
            "peripheralsHealth": lambda n : setattr(self, 'peripherals_health', n.get_object_value(teamwork_peripherals_health.TeamworkPeripheralsHealth)),
            "softwareUpdateHealth": lambda n : setattr(self, 'software_update_health', n.get_object_value(teamwork_software_update_health.TeamworkSoftwareUpdateHealth)),
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
        writer.write_object_value("connection", self.connection)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("hardwareHealth", self.hardware_health)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("loginStatus", self.login_status)
        writer.write_object_value("peripheralsHealth", self.peripherals_health)
        writer.write_object_value("softwareUpdateHealth", self.software_update_health)
    

