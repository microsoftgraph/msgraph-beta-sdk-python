from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity_set, teamwork_device_activity, teamwork_device_activity_state, teamwork_device_configuration, teamwork_device_health, teamwork_device_health_status, teamwork_device_operation, teamwork_device_type, teamwork_hardware_detail, teamwork_user_identity

from . import entity

class TeamworkDevice(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamworkDevice and sets the default values.
        """
        super().__init__()
        # The activity properties that change based on the device usage.
        self._activity: Optional[teamwork_device_activity.TeamworkDeviceActivity] = None
        # The activity state of the device. The possible values are: unknown, busy, idle, unavailable, unknownFutureValue.
        self._activity_state: Optional[teamwork_device_activity_state.TeamworkDeviceActivityState] = None
        # The company asset tag assigned by the admin on the device.
        self._company_asset_tag: Optional[str] = None
        # The configuration properties of the device.
        self._configuration: Optional[teamwork_device_configuration.TeamworkDeviceConfiguration] = None
        # Identity of the user who enrolled the device to the tenant.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device was enrolled to the tenant.
        self._created_date_time: Optional[datetime] = None
        # The signed-in user on the device.
        self._current_user: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
        # The deviceType property
        self._device_type: Optional[teamwork_device_type.TeamworkDeviceType] = None
        # The hardwareDetail property
        self._hardware_detail: Optional[teamwork_hardware_detail.TeamworkHardwareDetail] = None
        # The health properties of the device.
        self._health: Optional[teamwork_device_health.TeamworkDeviceHealth] = None
        # The health status of the device. The possible values are: unknown, offline, critical, nonUrgent, healthy, unknownFutureValue.
        self._health_status: Optional[teamwork_device_health_status.TeamworkDeviceHealthStatus] = None
        # Identity of the user who last modified the device details.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The UTC date and time when the device detail was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The notes added by the admin to the device.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The async operations on the device.
        self._operations: Optional[List[teamwork_device_operation.TeamworkDeviceOperation]] = None
    
    @property
    def activity(self,) -> Optional[teamwork_device_activity.TeamworkDeviceActivity]:
        """
        Gets the activity property value. The activity properties that change based on the device usage.
        Returns: Optional[teamwork_device_activity.TeamworkDeviceActivity]
        """
        return self._activity
    
    @activity.setter
    def activity(self,value: Optional[teamwork_device_activity.TeamworkDeviceActivity] = None) -> None:
        """
        Sets the activity property value. The activity properties that change based on the device usage.
        Args:
            value: Value to set for the activity property.
        """
        self._activity = value
    
    @property
    def activity_state(self,) -> Optional[teamwork_device_activity_state.TeamworkDeviceActivityState]:
        """
        Gets the activityState property value. The activity state of the device. The possible values are: unknown, busy, idle, unavailable, unknownFutureValue.
        Returns: Optional[teamwork_device_activity_state.TeamworkDeviceActivityState]
        """
        return self._activity_state
    
    @activity_state.setter
    def activity_state(self,value: Optional[teamwork_device_activity_state.TeamworkDeviceActivityState] = None) -> None:
        """
        Sets the activityState property value. The activity state of the device. The possible values are: unknown, busy, idle, unavailable, unknownFutureValue.
        Args:
            value: Value to set for the activity_state property.
        """
        self._activity_state = value
    
    @property
    def company_asset_tag(self,) -> Optional[str]:
        """
        Gets the companyAssetTag property value. The company asset tag assigned by the admin on the device.
        Returns: Optional[str]
        """
        return self._company_asset_tag
    
    @company_asset_tag.setter
    def company_asset_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the companyAssetTag property value. The company asset tag assigned by the admin on the device.
        Args:
            value: Value to set for the company_asset_tag property.
        """
        self._company_asset_tag = value
    
    @property
    def configuration(self,) -> Optional[teamwork_device_configuration.TeamworkDeviceConfiguration]:
        """
        Gets the configuration property value. The configuration properties of the device.
        Returns: Optional[teamwork_device_configuration.TeamworkDeviceConfiguration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[teamwork_device_configuration.TeamworkDeviceConfiguration] = None) -> None:
        """
        Sets the configuration property value. The configuration properties of the device.
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user who enrolled the device to the tenant.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user who enrolled the device to the tenant.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The UTC date and time when the device was enrolled to the tenant.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The UTC date and time when the device was enrolled to the tenant.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkDevice()
    
    @property
    def current_user(self,) -> Optional[teamwork_user_identity.TeamworkUserIdentity]:
        """
        Gets the currentUser property value. The signed-in user on the device.
        Returns: Optional[teamwork_user_identity.TeamworkUserIdentity]
        """
        return self._current_user
    
    @current_user.setter
    def current_user(self,value: Optional[teamwork_user_identity.TeamworkUserIdentity] = None) -> None:
        """
        Sets the currentUser property value. The signed-in user on the device.
        Args:
            value: Value to set for the current_user property.
        """
        self._current_user = value
    
    @property
    def device_type(self,) -> Optional[teamwork_device_type.TeamworkDeviceType]:
        """
        Gets the deviceType property value. The deviceType property
        Returns: Optional[teamwork_device_type.TeamworkDeviceType]
        """
        return self._device_type
    
    @device_type.setter
    def device_type(self,value: Optional[teamwork_device_type.TeamworkDeviceType] = None) -> None:
        """
        Sets the deviceType property value. The deviceType property
        Args:
            value: Value to set for the device_type property.
        """
        self._device_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def hardware_detail(self,) -> Optional[teamwork_hardware_detail.TeamworkHardwareDetail]:
        """
        Gets the hardwareDetail property value. The hardwareDetail property
        Returns: Optional[teamwork_hardware_detail.TeamworkHardwareDetail]
        """
        return self._hardware_detail
    
    @hardware_detail.setter
    def hardware_detail(self,value: Optional[teamwork_hardware_detail.TeamworkHardwareDetail] = None) -> None:
        """
        Sets the hardwareDetail property value. The hardwareDetail property
        Args:
            value: Value to set for the hardware_detail property.
        """
        self._hardware_detail = value
    
    @property
    def health(self,) -> Optional[teamwork_device_health.TeamworkDeviceHealth]:
        """
        Gets the health property value. The health properties of the device.
        Returns: Optional[teamwork_device_health.TeamworkDeviceHealth]
        """
        return self._health
    
    @health.setter
    def health(self,value: Optional[teamwork_device_health.TeamworkDeviceHealth] = None) -> None:
        """
        Sets the health property value. The health properties of the device.
        Args:
            value: Value to set for the health property.
        """
        self._health = value
    
    @property
    def health_status(self,) -> Optional[teamwork_device_health_status.TeamworkDeviceHealthStatus]:
        """
        Gets the healthStatus property value. The health status of the device. The possible values are: unknown, offline, critical, nonUrgent, healthy, unknownFutureValue.
        Returns: Optional[teamwork_device_health_status.TeamworkDeviceHealthStatus]
        """
        return self._health_status
    
    @health_status.setter
    def health_status(self,value: Optional[teamwork_device_health_status.TeamworkDeviceHealthStatus] = None) -> None:
        """
        Sets the healthStatus property value. The health status of the device. The possible values are: unknown, offline, critical, nonUrgent, healthy, unknownFutureValue.
        Args:
            value: Value to set for the health_status property.
        """
        self._health_status = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user who last modified the device details.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user who last modified the device details.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The UTC date and time when the device detail was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The UTC date and time when the device detail was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. The notes added by the admin to the device.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. The notes added by the admin to the device.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def operations(self,) -> Optional[List[teamwork_device_operation.TeamworkDeviceOperation]]:
        """
        Gets the operations property value. The async operations on the device.
        Returns: Optional[List[teamwork_device_operation.TeamworkDeviceOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[teamwork_device_operation.TeamworkDeviceOperation]] = None) -> None:
        """
        Sets the operations property value. The async operations on the device.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

