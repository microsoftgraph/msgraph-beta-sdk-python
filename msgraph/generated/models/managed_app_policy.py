from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_managed_app_protection, default_managed_app_protection, entity, ios_managed_app_protection, managed_app_configuration, managed_app_protection, mdm_windows_information_protection_policy, targeted_managed_app_configuration, targeted_managed_app_protection, windows_information_protection, windows_information_protection_policy, windows_managed_app_protection

from . import entity

@dataclass
class ManagedAppPolicy(entity.Entity):
    """
    The ManagedAppPolicy resource represents a base type for platform specific policies.
    """
    # The date and time the policy was created.
    created_date_time: Optional[datetime] = None
    # The policy's description.
    description: Optional[str] = None
    # Policy display name.
    display_name: Optional[str] = None
    # Last time the policy was modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Scope Tags for this Entity instance.
    role_scope_tag_ids: Optional[List[str]] = None
    # Version of the entity.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidManagedAppProtection":
                from . import android_managed_app_protection

                return android_managed_app_protection.AndroidManagedAppProtection()
            if mapping_value == "#microsoft.graph.defaultManagedAppProtection":
                from . import default_managed_app_protection

                return default_managed_app_protection.DefaultManagedAppProtection()
            if mapping_value == "#microsoft.graph.iosManagedAppProtection":
                from . import ios_managed_app_protection

                return ios_managed_app_protection.IosManagedAppProtection()
            if mapping_value == "#microsoft.graph.managedAppConfiguration":
                from . import managed_app_configuration

                return managed_app_configuration.ManagedAppConfiguration()
            if mapping_value == "#microsoft.graph.managedAppProtection":
                from . import managed_app_protection

                return managed_app_protection.ManagedAppProtection()
            if mapping_value == "#microsoft.graph.mdmWindowsInformationProtectionPolicy":
                from . import mdm_windows_information_protection_policy

                return mdm_windows_information_protection_policy.MdmWindowsInformationProtectionPolicy()
            if mapping_value == "#microsoft.graph.targetedManagedAppConfiguration":
                from . import targeted_managed_app_configuration

                return targeted_managed_app_configuration.TargetedManagedAppConfiguration()
            if mapping_value == "#microsoft.graph.targetedManagedAppProtection":
                from . import targeted_managed_app_protection

                return targeted_managed_app_protection.TargetedManagedAppProtection()
            if mapping_value == "#microsoft.graph.windowsInformationProtection":
                from . import windows_information_protection

                return windows_information_protection.WindowsInformationProtection()
            if mapping_value == "#microsoft.graph.windowsInformationProtectionPolicy":
                from . import windows_information_protection_policy

                return windows_information_protection_policy.WindowsInformationProtectionPolicy()
            if mapping_value == "#microsoft.graph.windowsManagedAppProtection":
                from . import windows_managed_app_protection

                return windows_managed_app_protection.WindowsManagedAppProtection()
        return ManagedAppPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_managed_app_protection, default_managed_app_protection, entity, ios_managed_app_protection, managed_app_configuration, managed_app_protection, mdm_windows_information_protection_policy, targeted_managed_app_configuration, targeted_managed_app_protection, windows_information_protection, windows_information_protection_policy, windows_managed_app_protection

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_str_value("version", self.version)
    

