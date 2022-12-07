from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_restore_point_setting = lazy_import('msgraph.generated.models.cloud_pc_restore_point_setting')
cloud_pc_user_setting_assignment = lazy_import('msgraph.generated.models.cloud_pc_user_setting_assignment')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPcUserSetting(entity.Entity):
    @property
    def assignments(self,) -> Optional[List[cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment]]:
        """
        Gets the assignments property value. Represents the set of Microsoft 365 groups and security groups in Azure Active Directory that have cloudPCUserSetting assigned. Returned only on $expand. For an example, see Get cloudPcUserSettingample.
        Returns: Optional[List[cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment]] = None) -> None:
        """
        Sets the assignments property value. Represents the set of Microsoft 365 groups and security groups in Azure Active Directory that have cloudPCUserSetting assigned. Returned only on $expand. For an example, see Get cloudPcUserSettingample.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CloudPcUserSetting and sets the default values.
        """
        super().__init__()
        # Represents the set of Microsoft 365 groups and security groups in Azure Active Directory that have cloudPCUserSetting assigned. Returned only on $expand. For an example, see Get cloudPcUserSettingample.
        self._assignments: Optional[List[cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment]] = None
        # The date and time the setting was created. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        self._created_date_time: Optional[datetime] = None
        # The setting name displayed in the user interface.
        self._display_name: Optional[str] = None
        # The last date and time the setting was modified. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        self._last_modified_date_time: Optional[datetime] = None
        # Indicates whether the local admin option is enabled. Default value is false. To enable the local admin option, change the setting to true. If the local admin option is enabled, the end user can be an admin of the Cloud PC device.
        self._local_admin_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Defines how frequently a restore point is created that is, a snapshot is taken) for users' provisioned Cloud PCs (default is 12 hours), and whether the user is allowed to restore their own Cloud PCs to a backup made at a specific point in time.
        self._restore_point_setting: Optional[cloud_pc_restore_point_setting.CloudPcRestorePointSetting] = None
        # Indicates whether the self-service option is enabled. Default value is false. To enable the self-service option, change the setting to true. If the self-service option is enabled, the end user is allowed to perform some self-service operations, such as upgrading the Cloud PC through the end user portal.
        self._self_service_enabled: Optional[bool] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the setting was created. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the setting was created. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcUserSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcUserSetting
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcUserSetting()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The setting name displayed in the user interface.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The setting name displayed in the user interface.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(cloud_pc_user_setting_assignment.CloudPcUserSettingAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "local_admin_enabled": lambda n : setattr(self, 'local_admin_enabled', n.get_bool_value()),
            "restore_point_setting": lambda n : setattr(self, 'restore_point_setting', n.get_object_value(cloud_pc_restore_point_setting.CloudPcRestorePointSetting)),
            "self_service_enabled": lambda n : setattr(self, 'self_service_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The last date and time the setting was modified. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The last date and time the setting was modified. The Timestamp type represents the date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 looks like this: '2014-01-01T00:00:00Z'.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def local_admin_enabled(self,) -> Optional[bool]:
        """
        Gets the localAdminEnabled property value. Indicates whether the local admin option is enabled. Default value is false. To enable the local admin option, change the setting to true. If the local admin option is enabled, the end user can be an admin of the Cloud PC device.
        Returns: Optional[bool]
        """
        return self._local_admin_enabled
    
    @local_admin_enabled.setter
    def local_admin_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the localAdminEnabled property value. Indicates whether the local admin option is enabled. Default value is false. To enable the local admin option, change the setting to true. If the local admin option is enabled, the end user can be an admin of the Cloud PC device.
        Args:
            value: Value to set for the localAdminEnabled property.
        """
        self._local_admin_enabled = value
    
    @property
    def restore_point_setting(self,) -> Optional[cloud_pc_restore_point_setting.CloudPcRestorePointSetting]:
        """
        Gets the restorePointSetting property value. Defines how frequently a restore point is created that is, a snapshot is taken) for users' provisioned Cloud PCs (default is 12 hours), and whether the user is allowed to restore their own Cloud PCs to a backup made at a specific point in time.
        Returns: Optional[cloud_pc_restore_point_setting.CloudPcRestorePointSetting]
        """
        return self._restore_point_setting
    
    @restore_point_setting.setter
    def restore_point_setting(self,value: Optional[cloud_pc_restore_point_setting.CloudPcRestorePointSetting] = None) -> None:
        """
        Sets the restorePointSetting property value. Defines how frequently a restore point is created that is, a snapshot is taken) for users' provisioned Cloud PCs (default is 12 hours), and whether the user is allowed to restore their own Cloud PCs to a backup made at a specific point in time.
        Args:
            value: Value to set for the restorePointSetting property.
        """
        self._restore_point_setting = value
    
    @property
    def self_service_enabled(self,) -> Optional[bool]:
        """
        Gets the selfServiceEnabled property value. Indicates whether the self-service option is enabled. Default value is false. To enable the self-service option, change the setting to true. If the self-service option is enabled, the end user is allowed to perform some self-service operations, such as upgrading the Cloud PC through the end user portal.
        Returns: Optional[bool]
        """
        return self._self_service_enabled
    
    @self_service_enabled.setter
    def self_service_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the selfServiceEnabled property value. Indicates whether the self-service option is enabled. Default value is false. To enable the self-service option, change the setting to true. If the self-service option is enabled, the end user is allowed to perform some self-service operations, such as upgrading the Cloud PC through the end user portal.
        Args:
            value: Value to set for the selfServiceEnabled property.
        """
        self._self_service_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_bool_value("localAdminEnabled", self.local_admin_enabled)
        writer.write_object_value("restorePointSetting", self.restore_point_setting)
        writer.write_bool_value("selfServiceEnabled", self.self_service_enabled)
    

