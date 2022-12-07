from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

driver_update_profile_approval_type = lazy_import('msgraph.generated.models.driver_update_profile_approval_type')
entity = lazy_import('msgraph.generated.models.entity')
windows_driver_update_inventory = lazy_import('msgraph.generated.models.windows_driver_update_inventory')
windows_driver_update_profile_assignment = lazy_import('msgraph.generated.models.windows_driver_update_profile_assignment')
windows_driver_update_profile_inventory_sync_status = lazy_import('msgraph.generated.models.windows_driver_update_profile_inventory_sync_status')

class WindowsDriverUpdateProfile(entity.Entity):
    """
    Windows Driver Update Profile
    """
    @property
    def approval_type(self,) -> Optional[driver_update_profile_approval_type.DriverUpdateProfileApprovalType]:
        """
        Gets the approvalType property value. An enum type to represent approval type of a driver update profile.
        Returns: Optional[driver_update_profile_approval_type.DriverUpdateProfileApprovalType]
        """
        return self._approval_type
    
    @approval_type.setter
    def approval_type(self,value: Optional[driver_update_profile_approval_type.DriverUpdateProfileApprovalType] = None) -> None:
        """
        Sets the approvalType property value. An enum type to represent approval type of a driver update profile.
        Args:
            value: Value to set for the approvalType property.
        """
        self._approval_type = value
    
    @property
    def assignments(self,) -> Optional[List[windows_driver_update_profile_assignment.WindowsDriverUpdateProfileAssignment]]:
        """
        Gets the assignments property value. The list of group assignments of the profile.
        Returns: Optional[List[windows_driver_update_profile_assignment.WindowsDriverUpdateProfileAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[windows_driver_update_profile_assignment.WindowsDriverUpdateProfileAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignments of the profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsDriverUpdateProfile and sets the default values.
        """
        super().__init__()
        # An enum type to represent approval type of a driver update profile.
        self._approval_type: Optional[driver_update_profile_approval_type.DriverUpdateProfileApprovalType] = None
        # The list of group assignments of the profile.
        self._assignments: Optional[List[windows_driver_update_profile_assignment.WindowsDriverUpdateProfileAssignment]] = None
        # The date time that the profile was created.
        self._created_date_time: Optional[datetime] = None
        # Deployment deferral settings in days, only applicable when ApprovalType is set to automatic approval.
        self._deployment_deferral_in_days: Optional[int] = None
        # The description of the profile which is specified by the user.
        self._description: Optional[str] = None
        # Number of devices reporting for this profile
        self._device_reporting: Optional[int] = None
        # The display name for the profile.
        self._display_name: Optional[str] = None
        # Driver inventories for this profile.
        self._driver_inventories: Optional[List[windows_driver_update_inventory.WindowsDriverUpdateInventory]] = None
        # Driver inventory sync status for this profile.
        self._inventory_sync_status: Optional[windows_driver_update_profile_inventory_sync_status.WindowsDriverUpdateProfileInventorySyncStatus] = None
        # The date time that the profile was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # Number of new driver updates available for this profile.
        self._new_updates: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of Scope Tags for this Driver Update entity.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date time that the profile was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date time that the profile was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDriverUpdateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDriverUpdateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDriverUpdateProfile()
    
    @property
    def deployment_deferral_in_days(self,) -> Optional[int]:
        """
        Gets the deploymentDeferralInDays property value. Deployment deferral settings in days, only applicable when ApprovalType is set to automatic approval.
        Returns: Optional[int]
        """
        return self._deployment_deferral_in_days
    
    @deployment_deferral_in_days.setter
    def deployment_deferral_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deploymentDeferralInDays property value. Deployment deferral settings in days, only applicable when ApprovalType is set to automatic approval.
        Args:
            value: Value to set for the deploymentDeferralInDays property.
        """
        self._deployment_deferral_in_days = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the profile which is specified by the user.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the profile which is specified by the user.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_reporting(self,) -> Optional[int]:
        """
        Gets the deviceReporting property value. Number of devices reporting for this profile
        Returns: Optional[int]
        """
        return self._device_reporting
    
    @device_reporting.setter
    def device_reporting(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceReporting property value. Number of devices reporting for this profile
        Args:
            value: Value to set for the deviceReporting property.
        """
        self._device_reporting = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the profile.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the profile.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def driver_inventories(self,) -> Optional[List[windows_driver_update_inventory.WindowsDriverUpdateInventory]]:
        """
        Gets the driverInventories property value. Driver inventories for this profile.
        Returns: Optional[List[windows_driver_update_inventory.WindowsDriverUpdateInventory]]
        """
        return self._driver_inventories
    
    @driver_inventories.setter
    def driver_inventories(self,value: Optional[List[windows_driver_update_inventory.WindowsDriverUpdateInventory]] = None) -> None:
        """
        Sets the driverInventories property value. Driver inventories for this profile.
        Args:
            value: Value to set for the driverInventories property.
        """
        self._driver_inventories = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "approval_type": lambda n : setattr(self, 'approval_type', n.get_enum_value(driver_update_profile_approval_type.DriverUpdateProfileApprovalType)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(windows_driver_update_profile_assignment.WindowsDriverUpdateProfileAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deployment_deferral_in_days": lambda n : setattr(self, 'deployment_deferral_in_days', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_reporting": lambda n : setattr(self, 'device_reporting', n.get_int_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "driver_inventories": lambda n : setattr(self, 'driver_inventories', n.get_collection_of_object_values(windows_driver_update_inventory.WindowsDriverUpdateInventory)),
            "inventory_sync_status": lambda n : setattr(self, 'inventory_sync_status', n.get_object_value(windows_driver_update_profile_inventory_sync_status.WindowsDriverUpdateProfileInventorySyncStatus)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "new_updates": lambda n : setattr(self, 'new_updates', n.get_int_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inventory_sync_status(self,) -> Optional[windows_driver_update_profile_inventory_sync_status.WindowsDriverUpdateProfileInventorySyncStatus]:
        """
        Gets the inventorySyncStatus property value. Driver inventory sync status for this profile.
        Returns: Optional[windows_driver_update_profile_inventory_sync_status.WindowsDriverUpdateProfileInventorySyncStatus]
        """
        return self._inventory_sync_status
    
    @inventory_sync_status.setter
    def inventory_sync_status(self,value: Optional[windows_driver_update_profile_inventory_sync_status.WindowsDriverUpdateProfileInventorySyncStatus] = None) -> None:
        """
        Sets the inventorySyncStatus property value. Driver inventory sync status for this profile.
        Args:
            value: Value to set for the inventorySyncStatus property.
        """
        self._inventory_sync_status = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date time that the profile was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date time that the profile was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def new_updates(self,) -> Optional[int]:
        """
        Gets the newUpdates property value. Number of new driver updates available for this profile.
        Returns: Optional[int]
        """
        return self._new_updates
    
    @new_updates.setter
    def new_updates(self,value: Optional[int] = None) -> None:
        """
        Sets the newUpdates property value. Number of new driver updates available for this profile.
        Args:
            value: Value to set for the newUpdates property.
        """
        self._new_updates = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. List of Scope Tags for this Driver Update entity.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. List of Scope Tags for this Driver Update entity.
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
        writer.write_enum_value("approvalType", self.approval_type)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("deploymentDeferralInDays", self.deployment_deferral_in_days)
        writer.write_str_value("description", self.description)
        writer.write_int_value("deviceReporting", self.device_reporting)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("driverInventories", self.driver_inventories)
        writer.write_object_value("inventorySyncStatus", self.inventory_sync_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_int_value("newUpdates", self.new_updates)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

