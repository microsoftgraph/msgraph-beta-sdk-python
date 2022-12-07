from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

state_management_setting = lazy_import('msgraph.generated.models.state_management_setting')
windows_firewall_rule_interface_types = lazy_import('msgraph.generated.models.windows_firewall_rule_interface_types')
windows_firewall_rule_network_profile_types = lazy_import('msgraph.generated.models.windows_firewall_rule_network_profile_types')
windows_firewall_rule_traffic_direction_type = lazy_import('msgraph.generated.models.windows_firewall_rule_traffic_direction_type')

class WindowsFirewallRule(AdditionalDataHolder, Parsable):
    """
    A rule controlling traffic through the Windows Firewall.
    """
    @property
    def action(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the action property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the action property value. State Management Setting.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windowsFirewallRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # State Management Setting.
        self._action: Optional[state_management_setting.StateManagementSetting] = None
        # The description of the rule.
        self._description: Optional[str] = None
        # The display name of the rule. Does not need to be unique.
        self._display_name: Optional[str] = None
        # State Management Setting.
        self._edge_traversal: Optional[state_management_setting.StateManagementSetting] = None
        # The full file path of an app that's affected by the firewall rule.
        self._file_path: Optional[str] = None
        # Flags representing firewall rule interface types.
        self._interface_types: Optional[windows_firewall_rule_interface_types.WindowsFirewallRuleInterfaceTypes] = None
        # List of local addresses covered by the rule. Default is any address. Valid tokens include:'' indicates any local address. If present, this must be the only token included.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
        self._local_address_ranges: Optional[List[str]] = None
        # List of local port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
        self._local_port_ranges: Optional[List[str]] = None
        # Specifies the list of authorized local users for the app container. This is a string in Security Descriptor Definition Language (SDDL) format.
        self._local_user_authorizations: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The package family name of a Microsoft Store application that's affected by the firewall rule.
        self._package_family_name: Optional[str] = None
        # Flags representing which network profile types apply to a firewall rule.
        self._profile_types: Optional[windows_firewall_rule_network_profile_types.WindowsFirewallRuleNetworkProfileTypes] = None
        # 0-255 number representing the IP protocol (TCP = 6, UDP = 17). If not specified, the default is All. Valid values 0 to 255
        self._protocol: Optional[int] = None
        # List of tokens specifying the remote addresses covered by the rule. Tokens are case insensitive. Default is any address. Valid tokens include:'' indicates any remote address. If present, this must be the only token included.'Defaultgateway''DHCP''DNS''WINS''Intranet' (supported on Windows versions 1809+)'RmtIntranet' (supported on Windows versions 1809+)'Internet' (supported on Windows versions 1809+)'Ply2Renders' (supported on Windows versions 1809+)'LocalSubnet' indicates any local address on the local subnet.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
        self._remote_address_ranges: Optional[List[str]] = None
        # List of remote port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
        self._remote_port_ranges: Optional[List[str]] = None
        # The name used in cases when a service, not an application, is sending or receiving traffic.
        self._service_name: Optional[str] = None
        # Firewall rule traffic directions.
        self._traffic_direction: Optional[windows_firewall_rule_traffic_direction_type.WindowsFirewallRuleTrafficDirectionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsFirewallRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsFirewallRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsFirewallRule()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the rule.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the rule.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the rule. Does not need to be unique.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the rule. Does not need to be unique.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def edge_traversal(self,) -> Optional[state_management_setting.StateManagementSetting]:
        """
        Gets the edgeTraversal property value. State Management Setting.
        Returns: Optional[state_management_setting.StateManagementSetting]
        """
        return self._edge_traversal
    
    @edge_traversal.setter
    def edge_traversal(self,value: Optional[state_management_setting.StateManagementSetting] = None) -> None:
        """
        Sets the edgeTraversal property value. State Management Setting.
        Args:
            value: Value to set for the edgeTraversal property.
        """
        self._edge_traversal = value
    
    @property
    def file_path(self,) -> Optional[str]:
        """
        Gets the filePath property value. The full file path of an app that's affected by the firewall rule.
        Returns: Optional[str]
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self,value: Optional[str] = None) -> None:
        """
        Sets the filePath property value. The full file path of an app that's affected by the firewall rule.
        Args:
            value: Value to set for the filePath property.
        """
        self._file_path = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(state_management_setting.StateManagementSetting)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "edge_traversal": lambda n : setattr(self, 'edge_traversal', n.get_enum_value(state_management_setting.StateManagementSetting)),
            "file_path": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "interface_types": lambda n : setattr(self, 'interface_types', n.get_enum_value(windows_firewall_rule_interface_types.WindowsFirewallRuleInterfaceTypes)),
            "local_address_ranges": lambda n : setattr(self, 'local_address_ranges', n.get_collection_of_primitive_values(str)),
            "local_port_ranges": lambda n : setattr(self, 'local_port_ranges', n.get_collection_of_primitive_values(str)),
            "local_user_authorizations": lambda n : setattr(self, 'local_user_authorizations', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "package_family_name": lambda n : setattr(self, 'package_family_name', n.get_str_value()),
            "profile_types": lambda n : setattr(self, 'profile_types', n.get_enum_value(windows_firewall_rule_network_profile_types.WindowsFirewallRuleNetworkProfileTypes)),
            "protocol": lambda n : setattr(self, 'protocol', n.get_int_value()),
            "remote_address_ranges": lambda n : setattr(self, 'remote_address_ranges', n.get_collection_of_primitive_values(str)),
            "remote_port_ranges": lambda n : setattr(self, 'remote_port_ranges', n.get_collection_of_primitive_values(str)),
            "service_name": lambda n : setattr(self, 'service_name', n.get_str_value()),
            "traffic_direction": lambda n : setattr(self, 'traffic_direction', n.get_enum_value(windows_firewall_rule_traffic_direction_type.WindowsFirewallRuleTrafficDirectionType)),
        }
        return fields
    
    @property
    def interface_types(self,) -> Optional[windows_firewall_rule_interface_types.WindowsFirewallRuleInterfaceTypes]:
        """
        Gets the interfaceTypes property value. Flags representing firewall rule interface types.
        Returns: Optional[windows_firewall_rule_interface_types.WindowsFirewallRuleInterfaceTypes]
        """
        return self._interface_types
    
    @interface_types.setter
    def interface_types(self,value: Optional[windows_firewall_rule_interface_types.WindowsFirewallRuleInterfaceTypes] = None) -> None:
        """
        Sets the interfaceTypes property value. Flags representing firewall rule interface types.
        Args:
            value: Value to set for the interfaceTypes property.
        """
        self._interface_types = value
    
    @property
    def local_address_ranges(self,) -> Optional[List[str]]:
        """
        Gets the localAddressRanges property value. List of local addresses covered by the rule. Default is any address. Valid tokens include:'' indicates any local address. If present, this must be the only token included.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
        Returns: Optional[List[str]]
        """
        return self._local_address_ranges
    
    @local_address_ranges.setter
    def local_address_ranges(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the localAddressRanges property value. List of local addresses covered by the rule. Default is any address. Valid tokens include:'' indicates any local address. If present, this must be the only token included.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
        Args:
            value: Value to set for the localAddressRanges property.
        """
        self._local_address_ranges = value
    
    @property
    def local_port_ranges(self,) -> Optional[List[str]]:
        """
        Gets the localPortRanges property value. List of local port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
        Returns: Optional[List[str]]
        """
        return self._local_port_ranges
    
    @local_port_ranges.setter
    def local_port_ranges(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the localPortRanges property value. List of local port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
        Args:
            value: Value to set for the localPortRanges property.
        """
        self._local_port_ranges = value
    
    @property
    def local_user_authorizations(self,) -> Optional[str]:
        """
        Gets the localUserAuthorizations property value. Specifies the list of authorized local users for the app container. This is a string in Security Descriptor Definition Language (SDDL) format.
        Returns: Optional[str]
        """
        return self._local_user_authorizations
    
    @local_user_authorizations.setter
    def local_user_authorizations(self,value: Optional[str] = None) -> None:
        """
        Sets the localUserAuthorizations property value. Specifies the list of authorized local users for the app container. This is a string in Security Descriptor Definition Language (SDDL) format.
        Args:
            value: Value to set for the localUserAuthorizations property.
        """
        self._local_user_authorizations = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def package_family_name(self,) -> Optional[str]:
        """
        Gets the packageFamilyName property value. The package family name of a Microsoft Store application that's affected by the firewall rule.
        Returns: Optional[str]
        """
        return self._package_family_name
    
    @package_family_name.setter
    def package_family_name(self,value: Optional[str] = None) -> None:
        """
        Sets the packageFamilyName property value. The package family name of a Microsoft Store application that's affected by the firewall rule.
        Args:
            value: Value to set for the packageFamilyName property.
        """
        self._package_family_name = value
    
    @property
    def profile_types(self,) -> Optional[windows_firewall_rule_network_profile_types.WindowsFirewallRuleNetworkProfileTypes]:
        """
        Gets the profileTypes property value. Flags representing which network profile types apply to a firewall rule.
        Returns: Optional[windows_firewall_rule_network_profile_types.WindowsFirewallRuleNetworkProfileTypes]
        """
        return self._profile_types
    
    @profile_types.setter
    def profile_types(self,value: Optional[windows_firewall_rule_network_profile_types.WindowsFirewallRuleNetworkProfileTypes] = None) -> None:
        """
        Sets the profileTypes property value. Flags representing which network profile types apply to a firewall rule.
        Args:
            value: Value to set for the profileTypes property.
        """
        self._profile_types = value
    
    @property
    def protocol(self,) -> Optional[int]:
        """
        Gets the protocol property value. 0-255 number representing the IP protocol (TCP = 6, UDP = 17). If not specified, the default is All. Valid values 0 to 255
        Returns: Optional[int]
        """
        return self._protocol
    
    @protocol.setter
    def protocol(self,value: Optional[int] = None) -> None:
        """
        Sets the protocol property value. 0-255 number representing the IP protocol (TCP = 6, UDP = 17). If not specified, the default is All. Valid values 0 to 255
        Args:
            value: Value to set for the protocol property.
        """
        self._protocol = value
    
    @property
    def remote_address_ranges(self,) -> Optional[List[str]]:
        """
        Gets the remoteAddressRanges property value. List of tokens specifying the remote addresses covered by the rule. Tokens are case insensitive. Default is any address. Valid tokens include:'' indicates any remote address. If present, this must be the only token included.'Defaultgateway''DHCP''DNS''WINS''Intranet' (supported on Windows versions 1809+)'RmtIntranet' (supported on Windows versions 1809+)'Internet' (supported on Windows versions 1809+)'Ply2Renders' (supported on Windows versions 1809+)'LocalSubnet' indicates any local address on the local subnet.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
        Returns: Optional[List[str]]
        """
        return self._remote_address_ranges
    
    @remote_address_ranges.setter
    def remote_address_ranges(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the remoteAddressRanges property value. List of tokens specifying the remote addresses covered by the rule. Tokens are case insensitive. Default is any address. Valid tokens include:'' indicates any remote address. If present, this must be the only token included.'Defaultgateway''DHCP''DNS''WINS''Intranet' (supported on Windows versions 1809+)'RmtIntranet' (supported on Windows versions 1809+)'Internet' (supported on Windows versions 1809+)'Ply2Renders' (supported on Windows versions 1809+)'LocalSubnet' indicates any local address on the local subnet.A subnet can be specified using either the subnet mask or network prefix notation. If neither a subnet mask nor a network prefix is specified, the subnet mask defaults to 255.255.255.255.A valid IPv6 address.An IPv4 address range in the format of 'start address - end address' with no spaces included.An IPv6 address range in the format of 'start address - end address' with no spaces included.
        Args:
            value: Value to set for the remoteAddressRanges property.
        """
        self._remote_address_ranges = value
    
    @property
    def remote_port_ranges(self,) -> Optional[List[str]]:
        """
        Gets the remotePortRanges property value. List of remote port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
        Returns: Optional[List[str]]
        """
        return self._remote_port_ranges
    
    @remote_port_ranges.setter
    def remote_port_ranges(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the remotePortRanges property value. List of remote port ranges. For example, '100-120', '200', '300-320'. If not specified, the default is All.
        Args:
            value: Value to set for the remotePortRanges property.
        """
        self._remote_port_ranges = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("action", self.action)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("edgeTraversal", self.edge_traversal)
        writer.write_str_value("filePath", self.file_path)
        writer.write_enum_value("interfaceTypes", self.interface_types)
        writer.write_collection_of_primitive_values("localAddressRanges", self.local_address_ranges)
        writer.write_collection_of_primitive_values("localPortRanges", self.local_port_ranges)
        writer.write_str_value("localUserAuthorizations", self.local_user_authorizations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("packageFamilyName", self.package_family_name)
        writer.write_enum_value("profileTypes", self.profile_types)
        writer.write_int_value("protocol", self.protocol)
        writer.write_collection_of_primitive_values("remoteAddressRanges", self.remote_address_ranges)
        writer.write_collection_of_primitive_values("remotePortRanges", self.remote_port_ranges)
        writer.write_str_value("serviceName", self.service_name)
        writer.write_enum_value("trafficDirection", self.traffic_direction)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_name(self,) -> Optional[str]:
        """
        Gets the serviceName property value. The name used in cases when a service, not an application, is sending or receiving traffic.
        Returns: Optional[str]
        """
        return self._service_name
    
    @service_name.setter
    def service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the serviceName property value. The name used in cases when a service, not an application, is sending or receiving traffic.
        Args:
            value: Value to set for the serviceName property.
        """
        self._service_name = value
    
    @property
    def traffic_direction(self,) -> Optional[windows_firewall_rule_traffic_direction_type.WindowsFirewallRuleTrafficDirectionType]:
        """
        Gets the trafficDirection property value. Firewall rule traffic directions.
        Returns: Optional[windows_firewall_rule_traffic_direction_type.WindowsFirewallRuleTrafficDirectionType]
        """
        return self._traffic_direction
    
    @traffic_direction.setter
    def traffic_direction(self,value: Optional[windows_firewall_rule_traffic_direction_type.WindowsFirewallRuleTrafficDirectionType] = None) -> None:
        """
        Sets the trafficDirection property value. Firewall rule traffic directions.
        Args:
            value: Value to set for the trafficDirection property.
        """
        self._traffic_direction = value
    

