from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_restore_point_setting, cloud_pc_user_setting_assignment, entity

from . import entity

@dataclass
class CloudPcUserSetting(entity.Entity):
    # Represents the set of Microsoft 365 groups and security groups in Azure Active Directory that have cloudPCUserSetting assigned. Returned only on $expand. For an example, see Get cloudPcUserSettingample.
    assignments: Optional[List[cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment]] = None
    # The date and time the setting was created. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
    created_date_time: Optional[datetime] = None
    # The setting name displayed in the user interface.
    display_name: Optional[str] = None
    # The last date and time the setting was modified. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
    last_modified_date_time: Optional[datetime] = None
    # Indicates whether the local admin option is enabled. Default value is false. To enable the local admin option, change the setting to true. If the local admin option is enabled, the end user can be an admin of the Cloud PC device.
    local_admin_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines how frequently a restore point is created that is, a snapshot is taken) for users' provisioned Cloud PCs (default is 12 hours), and whether the user is allowed to restore their own Cloud PCs to a backup made at a specific point in time.
    restore_point_setting: Optional[cloud_pc_restore_point_setting.CloudPcRestorePointSetting] = None
    # Indicates whether the self-service option is enabled. Default value is false. To enable the self-service option, change the setting to true. If the self-service option is enabled, the end user is allowed to perform some self-service operations, such as upgrading the Cloud PC through the end user portal.
    self_service_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcUserSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcUserSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_restore_point_setting, cloud_pc_user_setting_assignment, entity

        from . import cloud_pc_restore_point_setting, cloud_pc_user_setting_assignment, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localAdminEnabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "restorePointSetting": lambda n : setattr(self, 'restore_point_setting', n.get_object_value(cloud_pc_restore_point_setting.CloudPcRestorePointSetting)),
            "selfServiceEnabled": lambda n : setattr(self, 'self_service_enabled', n.get_bool_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_object_value("restorePointSetting", self.restore_point_setting)
        writer.write_bool_value("selfServiceEnabled", self.self_service_enabled)
    

