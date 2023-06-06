from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_resource_access_profile_assignment, entity, windows10_x_certificate_profile, windows10_x_s_c_e_p_certificate_profile, windows10_x_trusted_root_certificate, windows10_x_vpn_configuration, windows10_x_wifi_configuration

from . import entity

@dataclass
class DeviceManagementResourceAccessProfileBase(entity.Entity):
    """
    Base Profile Type for Resource Access
    """
    # The list of assignments for the device configuration profile.
    assignments: Optional[List[device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment]] = None
    # DateTime profile was created
    creation_date_time: Optional[datetime] = None
    # Profile description
    description: Optional[str] = None
    # Profile display name
    display_name: Optional[str] = None
    # DateTime profile was last modified
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Scope Tags
    role_scope_tag_ids: Optional[List[str]] = None
    # Version of the profile
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementResourceAccessProfileBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementResourceAccessProfileBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windows10XCertificateProfile":
                from . import windows10_x_certificate_profile

                return windows10_x_certificate_profile.Windows10XCertificateProfile()
            if mapping_value == "#microsoft.graph.windows10XSCEPCertificateProfile":
                from . import windows10_x_s_c_e_p_certificate_profile

                return windows10_x_s_c_e_p_certificate_profile.Windows10XSCEPCertificateProfile()
            if mapping_value == "#microsoft.graph.windows10XTrustedRootCertificate":
                from . import windows10_x_trusted_root_certificate

                return windows10_x_trusted_root_certificate.Windows10XTrustedRootCertificate()
            if mapping_value == "#microsoft.graph.windows10XVpnConfiguration":
                from . import windows10_x_vpn_configuration

                return windows10_x_vpn_configuration.Windows10XVpnConfiguration()
            if mapping_value == "#microsoft.graph.windows10XWifiConfiguration":
                from . import windows10_x_wifi_configuration

                return windows10_x_wifi_configuration.Windows10XWifiConfiguration()
        return DeviceManagementResourceAccessProfileBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_resource_access_profile_assignment, entity, windows10_x_certificate_profile, windows10_x_s_c_e_p_certificate_profile, windows10_x_trusted_root_certificate, windows10_x_vpn_configuration, windows10_x_wifi_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_management_resource_access_profile_assignment.DeviceManagementResourceAccessProfileAssignment)),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "roleScopeTagIds": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
        writer.write_int_value("version", self.version)
    

