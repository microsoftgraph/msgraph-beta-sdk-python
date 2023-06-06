from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import dep_enrollment_base_profile, dep_enrollment_profile, dep_i_o_s_enrollment_profile, dep_mac_o_s_enrollment_profile, entity

from . import entity

@dataclass
class EnrollmentProfile(entity.Entity):
    """
    The enrollmentProfile resource represents a collection of configurations which must be provided pre-enrollment to enable enrolling certain devices whose identities have been pre-staged. Pre-staged device identities are assigned to this type of profile to apply the profile's configurations at enrollment of the corresponding device.
    """
    # Configuration endpoint url to use for Enrollment
    configuration_endpoint_url: Optional[str] = None
    # Description of the profile
    description: Optional[str] = None
    # Name of the profile
    display_name: Optional[str] = None
    # Indicates to authenticate with Apple Setup Assistant instead of Company Portal.
    enable_authentication_via_company_portal: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates that Company Portal is required on setup assistant enrolled devices
    require_company_portal_on_setup_assistant_enrolled_devices: Optional[bool] = None
    # Indicates if the profile requires user authentication
    requires_user_authentication: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EnrollmentProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EnrollmentProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.depEnrollmentBaseProfile":
                from . import dep_enrollment_base_profile

                return dep_enrollment_base_profile.DepEnrollmentBaseProfile()
            if mapping_value == "#microsoft.graph.depEnrollmentProfile":
                from . import dep_enrollment_profile

                return dep_enrollment_profile.DepEnrollmentProfile()
            if mapping_value == "#microsoft.graph.depIOSEnrollmentProfile":
                from . import dep_i_o_s_enrollment_profile

                return dep_i_o_s_enrollment_profile.DepIOSEnrollmentProfile()
            if mapping_value == "#microsoft.graph.depMacOSEnrollmentProfile":
                from . import dep_mac_o_s_enrollment_profile

                return dep_mac_o_s_enrollment_profile.DepMacOSEnrollmentProfile()
        return EnrollmentProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import dep_enrollment_base_profile, dep_enrollment_profile, dep_i_o_s_enrollment_profile, dep_mac_o_s_enrollment_profile, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "configurationEndpointUrl": lambda n : setattr(self, 'configuration_endpoint_url', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enableAuthenticationViaCompanyPortal": lambda n : setattr(self, 'enable_authentication_via_company_portal', n.get_bool_value()),
            "requiresUserAuthentication": lambda n : setattr(self, 'requires_user_authentication', n.get_bool_value()),
            "requireCompanyPortalOnSetupAssistantEnrolledDevices": lambda n : setattr(self, 'require_company_portal_on_setup_assistant_enrolled_devices', n.get_bool_value()),
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
        writer.write_str_value("configurationEndpointUrl", self.configuration_endpoint_url)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("enableAuthenticationViaCompanyPortal", self.enable_authentication_via_company_portal)
        writer.write_bool_value("requiresUserAuthentication", self.requires_user_authentication)
        writer.write_bool_value("requireCompanyPortalOnSetupAssistantEnrolledDevices", self.require_company_portal_on_setup_assistant_enrolled_devices)
    

