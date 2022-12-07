from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

specified_captive_network_plugins = lazy_import('msgraph.generated.models.specified_captive_network_plugins')
vpn_service_exception_action = lazy_import('msgraph.generated.models.vpn_service_exception_action')
vpn_tunnel_configuration_type = lazy_import('msgraph.generated.models.vpn_tunnel_configuration_type')

class AppleVpnAlwaysOnConfiguration(AdditionalDataHolder, Parsable):
    """
    Always On VPN configuration for MacOS and iOS IKEv2
    """
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
    
    @property
    def air_print_exception_action(self,) -> Optional[vpn_service_exception_action.VpnServiceExceptionAction]:
        """
        Gets the airPrintExceptionAction property value. Determine whether AirPrint service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        Returns: Optional[vpn_service_exception_action.VpnServiceExceptionAction]
        """
        return self._air_print_exception_action
    
    @air_print_exception_action.setter
    def air_print_exception_action(self,value: Optional[vpn_service_exception_action.VpnServiceExceptionAction] = None) -> None:
        """
        Sets the airPrintExceptionAction property value. Determine whether AirPrint service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        Args:
            value: Value to set for the airPrintExceptionAction property.
        """
        self._air_print_exception_action = value
    
    @property
    def allow_all_captive_network_plugins(self,) -> Optional[bool]:
        """
        Gets the allowAllCaptiveNetworkPlugins property value. Specifies whether traffic from all captive network plugins should be allowed outside the vpn
        Returns: Optional[bool]
        """
        return self._allow_all_captive_network_plugins
    
    @allow_all_captive_network_plugins.setter
    def allow_all_captive_network_plugins(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowAllCaptiveNetworkPlugins property value. Specifies whether traffic from all captive network plugins should be allowed outside the vpn
        Args:
            value: Value to set for the allowAllCaptiveNetworkPlugins property.
        """
        self._allow_all_captive_network_plugins = value
    
    @property
    def allow_captive_web_sheet(self,) -> Optional[bool]:
        """
        Gets the allowCaptiveWebSheet property value. Determines whether traffic from the Websheet app is allowed outside of the VPN
        Returns: Optional[bool]
        """
        return self._allow_captive_web_sheet
    
    @allow_captive_web_sheet.setter
    def allow_captive_web_sheet(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowCaptiveWebSheet property value. Determines whether traffic from the Websheet app is allowed outside of the VPN
        Args:
            value: Value to set for the allowCaptiveWebSheet property.
        """
        self._allow_captive_web_sheet = value
    
    @property
    def allowed_captive_network_plugins(self,) -> Optional[specified_captive_network_plugins.SpecifiedCaptiveNetworkPlugins]:
        """
        Gets the allowedCaptiveNetworkPlugins property value. Determines whether all, some, or no non-native captive networking apps are allowed
        Returns: Optional[specified_captive_network_plugins.SpecifiedCaptiveNetworkPlugins]
        """
        return self._allowed_captive_network_plugins
    
    @allowed_captive_network_plugins.setter
    def allowed_captive_network_plugins(self,value: Optional[specified_captive_network_plugins.SpecifiedCaptiveNetworkPlugins] = None) -> None:
        """
        Sets the allowedCaptiveNetworkPlugins property value. Determines whether all, some, or no non-native captive networking apps are allowed
        Args:
            value: Value to set for the allowedCaptiveNetworkPlugins property.
        """
        self._allowed_captive_network_plugins = value
    
    @property
    def cellular_exception_action(self,) -> Optional[vpn_service_exception_action.VpnServiceExceptionAction]:
        """
        Gets the cellularExceptionAction property value. Determine whether Cellular service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        Returns: Optional[vpn_service_exception_action.VpnServiceExceptionAction]
        """
        return self._cellular_exception_action
    
    @cellular_exception_action.setter
    def cellular_exception_action(self,value: Optional[vpn_service_exception_action.VpnServiceExceptionAction] = None) -> None:
        """
        Sets the cellularExceptionAction property value. Determine whether Cellular service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        Args:
            value: Value to set for the cellularExceptionAction property.
        """
        self._cellular_exception_action = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new appleVpnAlwaysOnConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Determine whether AirPrint service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        self._air_print_exception_action: Optional[vpn_service_exception_action.VpnServiceExceptionAction] = None
        # Specifies whether traffic from all captive network plugins should be allowed outside the vpn
        self._allow_all_captive_network_plugins: Optional[bool] = None
        # Determines whether traffic from the Websheet app is allowed outside of the VPN
        self._allow_captive_web_sheet: Optional[bool] = None
        # Determines whether all, some, or no non-native captive networking apps are allowed
        self._allowed_captive_network_plugins: Optional[specified_captive_network_plugins.SpecifiedCaptiveNetworkPlugins] = None
        # Determine whether Cellular service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        self._cellular_exception_action: Optional[vpn_service_exception_action.VpnServiceExceptionAction] = None
        # Specifies how often in seconds to send a network address translation keepalive package through the VPN
        self._nat_keep_alive_interval_in_seconds: Optional[int] = None
        # Enable hardware offloading of NAT keepalive signals when the device is asleep
        self._nat_keep_alive_offload_enable: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type of tunnels that will be present to the VPN client for configuration
        self._tunnel_configuration: Optional[vpn_tunnel_configuration_type.VpnTunnelConfigurationType] = None
        # Allow the user to toggle the VPN configuration using the UI
        self._user_toggle_enabled: Optional[bool] = None
        # Determine whether voicemail service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        self._voicemail_exception_action: Optional[vpn_service_exception_action.VpnServiceExceptionAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppleVpnAlwaysOnConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppleVpnAlwaysOnConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppleVpnAlwaysOnConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "air_print_exception_action": lambda n : setattr(self, 'air_print_exception_action', n.get_enum_value(vpn_service_exception_action.VpnServiceExceptionAction)),
            "allow_all_captive_network_plugins": lambda n : setattr(self, 'allow_all_captive_network_plugins', n.get_bool_value()),
            "allow_captive_web_sheet": lambda n : setattr(self, 'allow_captive_web_sheet', n.get_bool_value()),
            "allowed_captive_network_plugins": lambda n : setattr(self, 'allowed_captive_network_plugins', n.get_object_value(specified_captive_network_plugins.SpecifiedCaptiveNetworkPlugins)),
            "cellular_exception_action": lambda n : setattr(self, 'cellular_exception_action', n.get_enum_value(vpn_service_exception_action.VpnServiceExceptionAction)),
            "nat_keep_alive_interval_in_seconds": lambda n : setattr(self, 'nat_keep_alive_interval_in_seconds', n.get_int_value()),
            "nat_keep_alive_offload_enable": lambda n : setattr(self, 'nat_keep_alive_offload_enable', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tunnel_configuration": lambda n : setattr(self, 'tunnel_configuration', n.get_enum_value(vpn_tunnel_configuration_type.VpnTunnelConfigurationType)),
            "user_toggle_enabled": lambda n : setattr(self, 'user_toggle_enabled', n.get_bool_value()),
            "voicemail_exception_action": lambda n : setattr(self, 'voicemail_exception_action', n.get_enum_value(vpn_service_exception_action.VpnServiceExceptionAction)),
        }
        return fields
    
    @property
    def nat_keep_alive_interval_in_seconds(self,) -> Optional[int]:
        """
        Gets the natKeepAliveIntervalInSeconds property value. Specifies how often in seconds to send a network address translation keepalive package through the VPN
        Returns: Optional[int]
        """
        return self._nat_keep_alive_interval_in_seconds
    
    @nat_keep_alive_interval_in_seconds.setter
    def nat_keep_alive_interval_in_seconds(self,value: Optional[int] = None) -> None:
        """
        Sets the natKeepAliveIntervalInSeconds property value. Specifies how often in seconds to send a network address translation keepalive package through the VPN
        Args:
            value: Value to set for the natKeepAliveIntervalInSeconds property.
        """
        self._nat_keep_alive_interval_in_seconds = value
    
    @property
    def nat_keep_alive_offload_enable(self,) -> Optional[bool]:
        """
        Gets the natKeepAliveOffloadEnable property value. Enable hardware offloading of NAT keepalive signals when the device is asleep
        Returns: Optional[bool]
        """
        return self._nat_keep_alive_offload_enable
    
    @nat_keep_alive_offload_enable.setter
    def nat_keep_alive_offload_enable(self,value: Optional[bool] = None) -> None:
        """
        Sets the natKeepAliveOffloadEnable property value. Enable hardware offloading of NAT keepalive signals when the device is asleep
        Args:
            value: Value to set for the natKeepAliveOffloadEnable property.
        """
        self._nat_keep_alive_offload_enable = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("airPrintExceptionAction", self.air_print_exception_action)
        writer.write_bool_value("allowAllCaptiveNetworkPlugins", self.allow_all_captive_network_plugins)
        writer.write_bool_value("allowCaptiveWebSheet", self.allow_captive_web_sheet)
        writer.write_object_value("allowedCaptiveNetworkPlugins", self.allowed_captive_network_plugins)
        writer.write_enum_value("cellularExceptionAction", self.cellular_exception_action)
        writer.write_int_value("natKeepAliveIntervalInSeconds", self.nat_keep_alive_interval_in_seconds)
        writer.write_bool_value("natKeepAliveOffloadEnable", self.nat_keep_alive_offload_enable)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tunnelConfiguration", self.tunnel_configuration)
        writer.write_bool_value("userToggleEnabled", self.user_toggle_enabled)
        writer.write_enum_value("voicemailExceptionAction", self.voicemail_exception_action)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def tunnel_configuration(self,) -> Optional[vpn_tunnel_configuration_type.VpnTunnelConfigurationType]:
        """
        Gets the tunnelConfiguration property value. The type of tunnels that will be present to the VPN client for configuration
        Returns: Optional[vpn_tunnel_configuration_type.VpnTunnelConfigurationType]
        """
        return self._tunnel_configuration
    
    @tunnel_configuration.setter
    def tunnel_configuration(self,value: Optional[vpn_tunnel_configuration_type.VpnTunnelConfigurationType] = None) -> None:
        """
        Sets the tunnelConfiguration property value. The type of tunnels that will be present to the VPN client for configuration
        Args:
            value: Value to set for the tunnelConfiguration property.
        """
        self._tunnel_configuration = value
    
    @property
    def user_toggle_enabled(self,) -> Optional[bool]:
        """
        Gets the userToggleEnabled property value. Allow the user to toggle the VPN configuration using the UI
        Returns: Optional[bool]
        """
        return self._user_toggle_enabled
    
    @user_toggle_enabled.setter
    def user_toggle_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the userToggleEnabled property value. Allow the user to toggle the VPN configuration using the UI
        Args:
            value: Value to set for the userToggleEnabled property.
        """
        self._user_toggle_enabled = value
    
    @property
    def voicemail_exception_action(self,) -> Optional[vpn_service_exception_action.VpnServiceExceptionAction]:
        """
        Gets the voicemailExceptionAction property value. Determine whether voicemail service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        Returns: Optional[vpn_service_exception_action.VpnServiceExceptionAction]
        """
        return self._voicemail_exception_action
    
    @voicemail_exception_action.setter
    def voicemail_exception_action(self,value: Optional[vpn_service_exception_action.VpnServiceExceptionAction] = None) -> None:
        """
        Sets the voicemailExceptionAction property value. Determine whether voicemail service will be exempt from the always-on VPN connection. Possible values are: forceTrafficViaVPN, allowTrafficOutside, dropTraffic.
        Args:
            value: Value to set for the voicemailExceptionAction property.
        """
        self._voicemail_exception_action = value
    

