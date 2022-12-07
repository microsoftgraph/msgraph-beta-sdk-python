from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

change_uefi_settings_permission = lazy_import('msgraph.generated.models.change_uefi_settings_permission')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')

class Windows10DeviceFirmwareConfigurationInterface(device_configuration.DeviceConfiguration):
    @property
    def bluetooth(self,) -> Optional[enablement.Enablement]:
        """
        Gets the bluetooth property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._bluetooth
    
    @bluetooth.setter
    def bluetooth(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the bluetooth property value. Possible values of a property
        Args:
            value: Value to set for the bluetooth property.
        """
        self._bluetooth = value
    
    @property
    def boot_from_built_in_network_adapters(self,) -> Optional[enablement.Enablement]:
        """
        Gets the bootFromBuiltInNetworkAdapters property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._boot_from_built_in_network_adapters
    
    @boot_from_built_in_network_adapters.setter
    def boot_from_built_in_network_adapters(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the bootFromBuiltInNetworkAdapters property value. Possible values of a property
        Args:
            value: Value to set for the bootFromBuiltInNetworkAdapters property.
        """
        self._boot_from_built_in_network_adapters = value
    
    @property
    def boot_from_external_media(self,) -> Optional[enablement.Enablement]:
        """
        Gets the bootFromExternalMedia property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._boot_from_external_media
    
    @boot_from_external_media.setter
    def boot_from_external_media(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the bootFromExternalMedia property value. Possible values of a property
        Args:
            value: Value to set for the bootFromExternalMedia property.
        """
        self._boot_from_external_media = value
    
    @property
    def cameras(self,) -> Optional[enablement.Enablement]:
        """
        Gets the cameras property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._cameras
    
    @cameras.setter
    def cameras(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the cameras property value. Possible values of a property
        Args:
            value: Value to set for the cameras property.
        """
        self._cameras = value
    
    @property
    def change_uefi_settings_permission(self,) -> Optional[change_uefi_settings_permission.ChangeUefiSettingsPermission]:
        """
        Gets the changeUefiSettingsPermission property value. Defines the permission level granted to users to enable them change Uefi settings
        Returns: Optional[change_uefi_settings_permission.ChangeUefiSettingsPermission]
        """
        return self._change_uefi_settings_permission
    
    @change_uefi_settings_permission.setter
    def change_uefi_settings_permission(self,value: Optional[change_uefi_settings_permission.ChangeUefiSettingsPermission] = None) -> None:
        """
        Sets the changeUefiSettingsPermission property value. Defines the permission level granted to users to enable them change Uefi settings
        Args:
            value: Value to set for the changeUefiSettingsPermission property.
        """
        self._change_uefi_settings_permission = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10DeviceFirmwareConfigurationInterface and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface"
        # Possible values of a property
        self._bluetooth: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._boot_from_built_in_network_adapters: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._boot_from_external_media: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._cameras: Optional[enablement.Enablement] = None
        # Defines the permission level granted to users to enable them change Uefi settings
        self._change_uefi_settings_permission: Optional[change_uefi_settings_permission.ChangeUefiSettingsPermission] = None
        # Possible values of a property
        self._front_camera: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._infrared_camera: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._microphone: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._microphones_and_speakers: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._near_field_communication: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._radios: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._rear_camera: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._sd_card: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._simultaneous_multi_threading: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._usb_type_a_port: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._virtualization_of_cpu_and_i_o: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._wake_on_l_a_n: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._wake_on_power: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._wi_fi: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._windows_platform_binary_table: Optional[enablement.Enablement] = None
        # Possible values of a property
        self._wireless_wide_area_network: Optional[enablement.Enablement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10DeviceFirmwareConfigurationInterface:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10DeviceFirmwareConfigurationInterface
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10DeviceFirmwareConfigurationInterface()
    
    @property
    def front_camera(self,) -> Optional[enablement.Enablement]:
        """
        Gets the frontCamera property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._front_camera
    
    @front_camera.setter
    def front_camera(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the frontCamera property value. Possible values of a property
        Args:
            value: Value to set for the frontCamera property.
        """
        self._front_camera = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bluetooth": lambda n : setattr(self, 'bluetooth', n.get_enum_value(enablement.Enablement)),
            "boot_from_built_in_network_adapters": lambda n : setattr(self, 'boot_from_built_in_network_adapters', n.get_enum_value(enablement.Enablement)),
            "boot_from_external_media": lambda n : setattr(self, 'boot_from_external_media', n.get_enum_value(enablement.Enablement)),
            "cameras": lambda n : setattr(self, 'cameras', n.get_enum_value(enablement.Enablement)),
            "change_uefi_settings_permission": lambda n : setattr(self, 'change_uefi_settings_permission', n.get_enum_value(change_uefi_settings_permission.ChangeUefiSettingsPermission)),
            "front_camera": lambda n : setattr(self, 'front_camera', n.get_enum_value(enablement.Enablement)),
            "infrared_camera": lambda n : setattr(self, 'infrared_camera', n.get_enum_value(enablement.Enablement)),
            "microphone": lambda n : setattr(self, 'microphone', n.get_enum_value(enablement.Enablement)),
            "microphones_and_speakers": lambda n : setattr(self, 'microphones_and_speakers', n.get_enum_value(enablement.Enablement)),
            "near_field_communication": lambda n : setattr(self, 'near_field_communication', n.get_enum_value(enablement.Enablement)),
            "radios": lambda n : setattr(self, 'radios', n.get_enum_value(enablement.Enablement)),
            "rear_camera": lambda n : setattr(self, 'rear_camera', n.get_enum_value(enablement.Enablement)),
            "sd_card": lambda n : setattr(self, 'sd_card', n.get_enum_value(enablement.Enablement)),
            "simultaneous_multi_threading": lambda n : setattr(self, 'simultaneous_multi_threading', n.get_enum_value(enablement.Enablement)),
            "usb_type_a_port": lambda n : setattr(self, 'usb_type_a_port', n.get_enum_value(enablement.Enablement)),
            "virtualization_of_cpu_and_i_o": lambda n : setattr(self, 'virtualization_of_cpu_and_i_o', n.get_enum_value(enablement.Enablement)),
            "wake_on_l_a_n": lambda n : setattr(self, 'wake_on_l_a_n', n.get_enum_value(enablement.Enablement)),
            "wake_on_power": lambda n : setattr(self, 'wake_on_power', n.get_enum_value(enablement.Enablement)),
            "wi_fi": lambda n : setattr(self, 'wi_fi', n.get_enum_value(enablement.Enablement)),
            "windows_platform_binary_table": lambda n : setattr(self, 'windows_platform_binary_table', n.get_enum_value(enablement.Enablement)),
            "wireless_wide_area_network": lambda n : setattr(self, 'wireless_wide_area_network', n.get_enum_value(enablement.Enablement)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def infrared_camera(self,) -> Optional[enablement.Enablement]:
        """
        Gets the infraredCamera property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._infrared_camera
    
    @infrared_camera.setter
    def infrared_camera(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the infraredCamera property value. Possible values of a property
        Args:
            value: Value to set for the infraredCamera property.
        """
        self._infrared_camera = value
    
    @property
    def microphone(self,) -> Optional[enablement.Enablement]:
        """
        Gets the microphone property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._microphone
    
    @microphone.setter
    def microphone(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the microphone property value. Possible values of a property
        Args:
            value: Value to set for the microphone property.
        """
        self._microphone = value
    
    @property
    def microphones_and_speakers(self,) -> Optional[enablement.Enablement]:
        """
        Gets the microphonesAndSpeakers property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._microphones_and_speakers
    
    @microphones_and_speakers.setter
    def microphones_and_speakers(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the microphonesAndSpeakers property value. Possible values of a property
        Args:
            value: Value to set for the microphonesAndSpeakers property.
        """
        self._microphones_and_speakers = value
    
    @property
    def near_field_communication(self,) -> Optional[enablement.Enablement]:
        """
        Gets the nearFieldCommunication property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._near_field_communication
    
    @near_field_communication.setter
    def near_field_communication(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the nearFieldCommunication property value. Possible values of a property
        Args:
            value: Value to set for the nearFieldCommunication property.
        """
        self._near_field_communication = value
    
    @property
    def radios(self,) -> Optional[enablement.Enablement]:
        """
        Gets the radios property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._radios
    
    @radios.setter
    def radios(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the radios property value. Possible values of a property
        Args:
            value: Value to set for the radios property.
        """
        self._radios = value
    
    @property
    def rear_camera(self,) -> Optional[enablement.Enablement]:
        """
        Gets the rearCamera property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._rear_camera
    
    @rear_camera.setter
    def rear_camera(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the rearCamera property value. Possible values of a property
        Args:
            value: Value to set for the rearCamera property.
        """
        self._rear_camera = value
    
    @property
    def sd_card(self,) -> Optional[enablement.Enablement]:
        """
        Gets the sdCard property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._sd_card
    
    @sd_card.setter
    def sd_card(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the sdCard property value. Possible values of a property
        Args:
            value: Value to set for the sdCard property.
        """
        self._sd_card = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("bluetooth", self.bluetooth)
        writer.write_enum_value("bootFromBuiltInNetworkAdapters", self.boot_from_built_in_network_adapters)
        writer.write_enum_value("bootFromExternalMedia", self.boot_from_external_media)
        writer.write_enum_value("cameras", self.cameras)
        writer.write_enum_value("changeUefiSettingsPermission", self.change_uefi_settings_permission)
        writer.write_enum_value("frontCamera", self.front_camera)
        writer.write_enum_value("infraredCamera", self.infrared_camera)
        writer.write_enum_value("microphone", self.microphone)
        writer.write_enum_value("microphonesAndSpeakers", self.microphones_and_speakers)
        writer.write_enum_value("nearFieldCommunication", self.near_field_communication)
        writer.write_enum_value("radios", self.radios)
        writer.write_enum_value("rearCamera", self.rear_camera)
        writer.write_enum_value("sdCard", self.sd_card)
        writer.write_enum_value("simultaneousMultiThreading", self.simultaneous_multi_threading)
        writer.write_enum_value("usbTypeAPort", self.usb_type_a_port)
        writer.write_enum_value("virtualizationOfCpuAndIO", self.virtualization_of_cpu_and_i_o)
        writer.write_enum_value("wakeOnLAN", self.wake_on_l_a_n)
        writer.write_enum_value("wakeOnPower", self.wake_on_power)
        writer.write_enum_value("wiFi", self.wi_fi)
        writer.write_enum_value("windowsPlatformBinaryTable", self.windows_platform_binary_table)
        writer.write_enum_value("wirelessWideAreaNetwork", self.wireless_wide_area_network)
    
    @property
    def simultaneous_multi_threading(self,) -> Optional[enablement.Enablement]:
        """
        Gets the simultaneousMultiThreading property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._simultaneous_multi_threading
    
    @simultaneous_multi_threading.setter
    def simultaneous_multi_threading(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the simultaneousMultiThreading property value. Possible values of a property
        Args:
            value: Value to set for the simultaneousMultiThreading property.
        """
        self._simultaneous_multi_threading = value
    
    @property
    def usb_type_a_port(self,) -> Optional[enablement.Enablement]:
        """
        Gets the usbTypeAPort property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._usb_type_a_port
    
    @usb_type_a_port.setter
    def usb_type_a_port(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the usbTypeAPort property value. Possible values of a property
        Args:
            value: Value to set for the usbTypeAPort property.
        """
        self._usb_type_a_port = value
    
    @property
    def virtualization_of_cpu_and_i_o(self,) -> Optional[enablement.Enablement]:
        """
        Gets the virtualizationOfCpuAndIO property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._virtualization_of_cpu_and_i_o
    
    @virtualization_of_cpu_and_i_o.setter
    def virtualization_of_cpu_and_i_o(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the virtualizationOfCpuAndIO property value. Possible values of a property
        Args:
            value: Value to set for the virtualizationOfCpuAndIO property.
        """
        self._virtualization_of_cpu_and_i_o = value
    
    @property
    def wake_on_l_a_n(self,) -> Optional[enablement.Enablement]:
        """
        Gets the wakeOnLAN property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._wake_on_l_a_n
    
    @wake_on_l_a_n.setter
    def wake_on_l_a_n(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the wakeOnLAN property value. Possible values of a property
        Args:
            value: Value to set for the wakeOnLAN property.
        """
        self._wake_on_l_a_n = value
    
    @property
    def wake_on_power(self,) -> Optional[enablement.Enablement]:
        """
        Gets the wakeOnPower property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._wake_on_power
    
    @wake_on_power.setter
    def wake_on_power(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the wakeOnPower property value. Possible values of a property
        Args:
            value: Value to set for the wakeOnPower property.
        """
        self._wake_on_power = value
    
    @property
    def wi_fi(self,) -> Optional[enablement.Enablement]:
        """
        Gets the wiFi property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._wi_fi
    
    @wi_fi.setter
    def wi_fi(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the wiFi property value. Possible values of a property
        Args:
            value: Value to set for the wiFi property.
        """
        self._wi_fi = value
    
    @property
    def windows_platform_binary_table(self,) -> Optional[enablement.Enablement]:
        """
        Gets the windowsPlatformBinaryTable property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._windows_platform_binary_table
    
    @windows_platform_binary_table.setter
    def windows_platform_binary_table(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the windowsPlatformBinaryTable property value. Possible values of a property
        Args:
            value: Value to set for the windowsPlatformBinaryTable property.
        """
        self._windows_platform_binary_table = value
    
    @property
    def wireless_wide_area_network(self,) -> Optional[enablement.Enablement]:
        """
        Gets the wirelessWideAreaNetwork property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._wireless_wide_area_network
    
    @wireless_wide_area_network.setter
    def wireless_wide_area_network(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the wirelessWideAreaNetwork property value. Possible values of a property
        Args:
            value: Value to set for the wirelessWideAreaNetwork property.
        """
        self._wireless_wide_area_network = value
    

