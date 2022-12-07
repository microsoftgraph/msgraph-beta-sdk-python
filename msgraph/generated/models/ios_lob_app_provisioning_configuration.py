from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
ios_lob_app_provisioning_configuration_assignment = lazy_import('msgraph.generated.models.ios_lob_app_provisioning_configuration_assignment')
managed_device_mobile_app_configuration_device_status = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_device_status')
managed_device_mobile_app_configuration_user_status = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_user_status')
mobile_app_provisioning_config_group_assignment = lazy_import('msgraph.generated.models.mobile_app_provisioning_config_group_assignment')

class IosLobAppProvisioningConfiguration(entity.Entity):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the iOS Lob App Provisioning Configuration resource.
    """
    @property
    def assignments(self,) -> Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]]:
        """
        Gets the assignments property value. The associated group assignments for IosLobAppProvisioningConfiguration.
        Returns: Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The associated group assignments for IosLobAppProvisioningConfiguration.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new iosLobAppProvisioningConfiguration and sets the default values.
        """
        super().__init__()
        # The associated group assignments for IosLobAppProvisioningConfiguration.
        self._assignments: Optional[List[ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the Device Configuration.
        self._description: Optional[str] = None
        # The list of device installation states for this mobile app configuration.
        self._device_statuses: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # Optional profile expiration date and time.
        self._expiration_date_time: Optional[datetime] = None
        # The associated group assignments.
        self._group_assignments: Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Payload. (UTF8 encoded byte array)
        self._payload: Optional[bytes] = None
        # Payload file name (.mobileprovision
        self._payload_file_name: Optional[str] = None
        # List of Scope Tags for this iOS LOB app provisioning configuration entity.
        self._role_scope_tag_ids: Optional[List[str]] = None
        # The list of user installation states for this mobile app configuration.
        self._user_statuses: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]] = None
        # Version of the device configuration.
        self._version: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosLobAppProvisioningConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosLobAppProvisioningConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosLobAppProvisioningConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin provided description of the Device Configuration.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin provided description of the Device Configuration.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_statuses(self,) -> Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]]:
        """
        Gets the deviceStatuses property value. The list of device installation states for this mobile app configuration.
        Returns: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. The list of device installation states for this mobile app configuration.
        Args:
            value: Value to set for the deviceStatuses property.
        """
        self._device_statuses = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided name of the device configuration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided name of the device configuration.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the expirationDateTime property value. Optional profile expiration date and time.
        Returns: Optional[datetime]
        """
        return self._expiration_date_time
    
    @expiration_date_time.setter
    def expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the expirationDateTime property value. Optional profile expiration date and time.
        Args:
            value: Value to set for the expirationDateTime property.
        """
        self._expiration_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(ios_lob_app_provisioning_configuration_assignment.IosLobAppProvisioningConfigurationAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_statuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "expiration_date_time": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "group_assignments": lambda n : setattr(self, 'group_assignments', n.get_collection_of_object_values(mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payload": lambda n : setattr(self, 'payload', n.get_bytes_value()),
            "payload_file_name": lambda n : setattr(self, 'payload_file_name', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "user_statuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_assignments(self,) -> Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]]:
        """
        Gets the groupAssignments property value. The associated group assignments.
        Returns: Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]]
        """
        return self._group_assignments
    
    @group_assignments.setter
    def group_assignments(self,value: Optional[List[mobile_app_provisioning_config_group_assignment.MobileAppProvisioningConfigGroupAssignment]] = None) -> None:
        """
        Sets the groupAssignments property value. The associated group assignments.
        Args:
            value: Value to set for the groupAssignments property.
        """
        self._group_assignments = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def payload(self,) -> Optional[bytes]:
        """
        Gets the payload property value. Payload. (UTF8 encoded byte array)
        Returns: Optional[bytes]
        """
        return self._payload
    
    @payload.setter
    def payload(self,value: Optional[bytes] = None) -> None:
        """
        Sets the payload property value. Payload. (UTF8 encoded byte array)
        Args:
            value: Value to set for the payload property.
        """
        self._payload = value
    
    @property
    def payload_file_name(self,) -> Optional[str]:
        """
        Gets the payloadFileName property value. Payload file name (.mobileprovision
        Returns: Optional[str]
        """
        return self._payload_file_name
    
    @payload_file_name.setter
    def payload_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadFileName property value. Payload file name (.mobileprovision
        Args:
            value: Value to set for the payloadFileName property.
        """
        self._payload_file_name = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this iOS LOB app provisioning configuration entity.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this iOS LOB app provisioning configuration entity.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_collection_of_object_values("groupAssignments", self.group_assignments)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("payload", self.payload)
        writer.write_str_value("payloadFileName", self.payload_file_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    
    @property
    def user_statuses(self,) -> Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]]:
        """
        Gets the userStatuses property value. The list of user installation states for this mobile app configuration.
        Returns: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]] = None) -> None:
        """
        Sets the userStatuses property value. The list of user installation states for this mobile app configuration.
        Args:
            value: Value to set for the userStatuses property.
        """
        self._user_statuses = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the device configuration.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the device configuration.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

