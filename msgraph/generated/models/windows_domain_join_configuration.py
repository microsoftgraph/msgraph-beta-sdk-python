from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_configuration

from . import device_configuration

@dataclass
class WindowsDomainJoinConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.windowsDomainJoinConfiguration"
    # Active Directory domain name to join.
    active_directory_domain_name: Optional[str] = None
    # Fixed prefix to be used for computer name.
    computer_name_static_prefix: Optional[str] = None
    # Dynamically generated characters used as suffix for computer name. Valid values 3 to 14
    computer_name_suffix_random_char_count: Optional[int] = None
    # Reference to device configurations required for network connectivity
    network_access_configurations: Optional[List[device_configuration.DeviceConfiguration]] = None
    # Organizational unit (OU) where the computer account will be created. If this parameter is NULL, the well known computer object container will be used as published in the domain.
    organizational_unit: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDomainJoinConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDomainJoinConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDomainJoinConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "activeDirectoryDomainName": lambda n : setattr(self, 'active_directory_domain_name', n.get_str_value()),
            "computerNameStaticPrefix": lambda n : setattr(self, 'computer_name_static_prefix', n.get_str_value()),
            "computerNameSuffixRandomCharCount": lambda n : setattr(self, 'computer_name_suffix_random_char_count', n.get_int_value()),
            "networkAccessConfigurations": lambda n : setattr(self, 'network_access_configurations', n.get_collection_of_object_values(device_configuration.DeviceConfiguration)),
            "organizationalUnit": lambda n : setattr(self, 'organizational_unit', n.get_str_value()),
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
        writer.write_str_value("activeDirectoryDomainName", self.active_directory_domain_name)
        writer.write_str_value("computerNameStaticPrefix", self.computer_name_static_prefix)
        writer.write_int_value("computerNameSuffixRandomCharCount", self.computer_name_suffix_random_char_count)
        writer.write_collection_of_object_values("networkAccessConfigurations", self.network_access_configurations)
        writer.write_str_value("organizationalUnit", self.organizational_unit)
    

