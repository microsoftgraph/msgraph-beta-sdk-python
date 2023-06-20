from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, teamwork_device_activity, teamwork_device_activity_state, teamwork_device_configuration, teamwork_device_health, teamwork_device_health_status, teamwork_device_operation, teamwork_device_type, teamwork_hardware_detail, teamwork_user_identity

from . import entity

@dataclass
class TeamworkDevice(entity.Entity):
    # The activity properties that change based on the device usage.
    activity: Optional[teamwork_device_activity.TeamworkDeviceActivity] = None
    # The activity state of the device. The possible values are: unknown, busy, idle, unavailable, unknownFutureValue.
    activity_state: Optional[teamwork_device_activity_state.TeamworkDeviceActivityState] = None
    # The company asset tag assigned by the admin on the device.
    company_asset_tag: Optional[str] = None
    # The configuration properties of the device.
    configuration: Optional[teamwork_device_configuration.TeamworkDeviceConfiguration] = None
    # Identity of the user who enrolled the device to the tenant.
    created_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the device was enrolled to the tenant.
    created_date_time: Optional[datetime] = None
    # The signed-in user on the device.
    current_user: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
    # The deviceType property
    device_type: Optional[teamwork_device_type.TeamworkDeviceType] = None
    # The hardwareDetail property
    hardware_detail: Optional[teamwork_hardware_detail.TeamworkHardwareDetail] = None
    # The health properties of the device.
    health: Optional[teamwork_device_health.TeamworkDeviceHealth] = None
    # The health status of the device. The possible values are: unknown, offline, critical, nonUrgent, healthy, unknownFutureValue.
    health_status: Optional[teamwork_device_health_status.TeamworkDeviceHealthStatus] = None
    # Identity of the user who last modified the device details.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # The UTC date and time when the device detail was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The notes added by the admin to the device.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The async operations on the device.
    operations: Optional[List[teamwork_device_operation.TeamworkDeviceOperation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDevice
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TeamworkDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity_set, teamwork_device_activity, teamwork_device_activity_state, teamwork_device_configuration, teamwork_device_health, teamwork_device_health_status, teamwork_device_operation, teamwork_device_type, teamwork_hardware_detail, teamwork_user_identity

        from . import entity, identity_set, teamwork_device_activity, teamwork_device_activity_state, teamwork_device_configuration, teamwork_device_health, teamwork_device_health_status, teamwork_device_operation, teamwork_device_type, teamwork_hardware_detail, teamwork_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_object_value(teamwork_device_activity.TeamworkDeviceActivity)),
            "activityState": lambda n : setattr(self, 'activity_state', n.get_enum_value(teamwork_device_activity_state.TeamworkDeviceActivityState)),
            "companyAssetTag": lambda n : setattr(self, 'company_asset_tag', n.get_str_value()),
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(teamwork_device_configuration.TeamworkDeviceConfiguration)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "currentUser": lambda n : setattr(self, 'current_user', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
            "deviceType": lambda n : setattr(self, 'device_type', n.get_enum_value(teamwork_device_type.TeamworkDeviceType)),
            "hardwareDetail": lambda n : setattr(self, 'hardware_detail', n.get_object_value(teamwork_hardware_detail.TeamworkHardwareDetail)),
            "health": lambda n : setattr(self, 'health', n.get_object_value(teamwork_device_health.TeamworkDeviceHealth)),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(teamwork_device_health_status.TeamworkDeviceHealthStatus)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(teamwork_device_operation.TeamworkDeviceOperation)),
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
        writer.write_object_value("activity", self.activity)
        writer.write_enum_value("activityState", self.activity_state)
        writer.write_str_value("companyAssetTag", self.company_asset_tag)
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("currentUser", self.current_user)
        writer.write_enum_value("deviceType", self.device_type)
        writer.write_object_value("hardwareDetail", self.hardware_detail)
        writer.write_object_value("health", self.health)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("notes", self.notes)
        writer.write_collection_of_object_values("operations", self.operations)
    

