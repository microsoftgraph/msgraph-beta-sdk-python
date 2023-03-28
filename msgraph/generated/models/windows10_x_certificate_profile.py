from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_resource_access_profile_base, windows10_x_s_c_e_p_certificate_profile

from . import device_management_resource_access_profile_base

class Windows10XCertificateProfile(device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10XCertificateProfile and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10XCertificateProfile"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10XCertificateProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XCertificateProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.windows10XSCEPCertificateProfile":
                from . import windows10_x_s_c_e_p_certificate_profile

                return windows10_x_s_c_e_p_certificate_profile.Windows10XSCEPCertificateProfile()
        return Windows10XCertificateProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_resource_access_profile_base, windows10_x_s_c_e_p_certificate_profile

        fields: Dict[str, Callable[[Any], None]] = {
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
    

