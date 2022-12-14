from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_management_resource_access_profile_base = lazy_import('msgraph.generated.models.device_management_resource_access_profile_base')

class Windows10XWifiConfiguration(device_management_resource_access_profile_base.DeviceManagementResourceAccessProfileBase):
    @property
    def authentication_certificate_id(self,) -> Optional[Guid]:
        """
        Gets the authenticationCertificateId property value. ID to the Authentication Certificate
        Returns: Optional[Guid]
        """
        return self._authentication_certificate_id
    
    @authentication_certificate_id.setter
    def authentication_certificate_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the authenticationCertificateId property value. ID to the Authentication Certificate
        Args:
            value: Value to set for the authenticationCertificateId property.
        """
        self._authentication_certificate_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10XWifiConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10XWifiConfiguration"
        # ID to the Authentication Certificate
        self._authentication_certificate_id: Optional[Guid] = None
        # Custom XML commands that configures the VPN connection. (UTF8 byte encoding)
        self._custom_xml: Optional[bytes] = None
        # Custom Xml file name.
        self._custom_xml_file_name: Optional[str] = None
    
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
    
    @property
    def custom_xml(self,) -> Optional[bytes]:
        """
        Gets the customXml property value. Custom XML commands that configures the VPN connection. (UTF8 byte encoding)
        Returns: Optional[bytes]
        """
        return self._custom_xml
    
    @custom_xml.setter
    def custom_xml(self,value: Optional[bytes] = None) -> None:
        """
        Sets the customXml property value. Custom XML commands that configures the VPN connection. (UTF8 byte encoding)
        Args:
            value: Value to set for the customXml property.
        """
        self._custom_xml = value
    
    @property
    def custom_xml_file_name(self,) -> Optional[str]:
        """
        Gets the customXmlFileName property value. Custom Xml file name.
        Returns: Optional[str]
        """
        return self._custom_xml_file_name
    
    @custom_xml_file_name.setter
    def custom_xml_file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the customXmlFileName property value. Custom Xml file name.
        Args:
            value: Value to set for the customXmlFileName property.
        """
        self._custom_xml_file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_certificate_id": lambda n : setattr(self, 'authentication_certificate_id', n.get_object_value(Guid)),
            "custom_xml": lambda n : setattr(self, 'custom_xml', n.get_bytes_value()),
            "custom_xml_file_name": lambda n : setattr(self, 'custom_xml_file_name', n.get_str_value()),
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
        writer.write_object_value("authenticationCertificateId", self.authentication_certificate_id)
        writer.write_object_value("customXml", self.custom_xml)
        writer.write_str_value("customXmlFileName", self.custom_xml_file_name)
    

