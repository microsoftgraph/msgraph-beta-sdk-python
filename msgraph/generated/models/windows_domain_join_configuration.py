from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')

class WindowsDomainJoinConfiguration(device_configuration.DeviceConfiguration):
    @property
    def active_directory_domain_name(self,) -> Optional[str]:
        """
        Gets the activeDirectoryDomainName property value. Active Directory domain name to join.
        Returns: Optional[str]
        """
        return self._active_directory_domain_name
    
    @active_directory_domain_name.setter
    def active_directory_domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the activeDirectoryDomainName property value. Active Directory domain name to join.
        Args:
            value: Value to set for the activeDirectoryDomainName property.
        """
        self._active_directory_domain_name = value
    
    @property
    def computer_name_static_prefix(self,) -> Optional[str]:
        """
        Gets the computerNameStaticPrefix property value. Fixed prefix to be used for computer name.
        Returns: Optional[str]
        """
        return self._computer_name_static_prefix
    
    @computer_name_static_prefix.setter
    def computer_name_static_prefix(self,value: Optional[str] = None) -> None:
        """
        Sets the computerNameStaticPrefix property value. Fixed prefix to be used for computer name.
        Args:
            value: Value to set for the computerNameStaticPrefix property.
        """
        self._computer_name_static_prefix = value
    
    @property
    def computer_name_suffix_random_char_count(self,) -> Optional[int]:
        """
        Gets the computerNameSuffixRandomCharCount property value. Dynamically generated characters used as suffix for computer name. Valid values 3 to 14
        Returns: Optional[int]
        """
        return self._computer_name_suffix_random_char_count
    
    @computer_name_suffix_random_char_count.setter
    def computer_name_suffix_random_char_count(self,value: Optional[int] = None) -> None:
        """
        Sets the computerNameSuffixRandomCharCount property value. Dynamically generated characters used as suffix for computer name. Valid values 3 to 14
        Args:
            value: Value to set for the computerNameSuffixRandomCharCount property.
        """
        self._computer_name_suffix_random_char_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsDomainJoinConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsDomainJoinConfiguration"
        # Active Directory domain name to join.
        self._active_directory_domain_name: Optional[str] = None
        # Fixed prefix to be used for computer name.
        self._computer_name_static_prefix: Optional[str] = None
        # Dynamically generated characters used as suffix for computer name. Valid values 3 to 14
        self._computer_name_suffix_random_char_count: Optional[int] = None
        # Reference to device configurations required for network connectivity
        self._network_access_configurations: Optional[List[device_configuration.DeviceConfiguration]] = None
        # Organizational unit (OU) where the computer account will be created. If this parameter is NULL, the well known computer object container will be used as published in the domain.
        self._organizational_unit: Optional[str] = None
    
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
        fields = {
            "active_directory_domain_name": lambda n : setattr(self, 'active_directory_domain_name', n.get_str_value()),
            "computer_name_static_prefix": lambda n : setattr(self, 'computer_name_static_prefix', n.get_str_value()),
            "computer_name_suffix_random_char_count": lambda n : setattr(self, 'computer_name_suffix_random_char_count', n.get_int_value()),
            "network_access_configurations": lambda n : setattr(self, 'network_access_configurations', n.get_collection_of_object_values(device_configuration.DeviceConfiguration)),
            "organizational_unit": lambda n : setattr(self, 'organizational_unit', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def network_access_configurations(self,) -> Optional[List[device_configuration.DeviceConfiguration]]:
        """
        Gets the networkAccessConfigurations property value. Reference to device configurations required for network connectivity
        Returns: Optional[List[device_configuration.DeviceConfiguration]]
        """
        return self._network_access_configurations
    
    @network_access_configurations.setter
    def network_access_configurations(self,value: Optional[List[device_configuration.DeviceConfiguration]] = None) -> None:
        """
        Sets the networkAccessConfigurations property value. Reference to device configurations required for network connectivity
        Args:
            value: Value to set for the networkAccessConfigurations property.
        """
        self._network_access_configurations = value
    
    @property
    def organizational_unit(self,) -> Optional[str]:
        """
        Gets the organizationalUnit property value. Organizational unit (OU) where the computer account will be created. If this parameter is NULL, the well known computer object container will be used as published in the domain.
        Returns: Optional[str]
        """
        return self._organizational_unit
    
    @organizational_unit.setter
    def organizational_unit(self,value: Optional[str] = None) -> None:
        """
        Sets the organizationalUnit property value. Organizational unit (OU) where the computer account will be created. If this parameter is NULL, the well known computer object container will be used as published in the domain.
        Args:
            value: Value to set for the organizationalUnit property.
        """
        self._organizational_unit = value
    
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
    

