from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import device_management_resource_access_profile_base

from . import device_management_resource_access_profile_base

@dataclass
class Windows10XWifiConfiguration(device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase):
    odata_type = "#microsoft.graph.windows10XWifiConfiguration"
    # ID to the Authentication Certificate
    authentication_certificate_id: Optional[UUID] = None
    # Custom XML commands that configures the VPN connection. (UTF8 byte encoding)
    custom_xml: Optional[bytes] = None
    # Custom Xml file name.
    custom_xml_file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10XWifiConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10XWifiConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10XWifiConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_resource_access_profile_base

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationCertificateId": lambda n : setattr(self, 'authentication_certificate_id', n.get_uuid_value()),
            "customXml": lambda n : setattr(self, 'custom_xml', n.get_bytes_value()),
            "customXmlFileName": lambda n : setattr(self, 'custom_xml_file_name', n.get_str_value()),
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
        writer.write_uuid_value("authenticationCertificateId", self.authentication_certificate_id)
        writer.write_object_value("customXml", self.custom_xml)
        writer.write_str_value("customXmlFileName", self.custom_xml_file_name)
    

