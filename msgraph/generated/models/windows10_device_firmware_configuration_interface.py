from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_uefi_settings_permission, device_configuration, enablement

from . import device_configuration

@dataclass
class Windows10DeviceFirmwareConfigurationInterface(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.windows10DeviceFirmwareConfigurationInterface"
    # Possible values of a property
    bluetooth: Optional[enablement.Enablement] = None
    # Possible values of a property
    boot_from_built_in_network_adapters: Optional[enablement.Enablement] = None
    # Possible values of a property
    boot_from_external_media: Optional[enablement.Enablement] = None
    # Possible values of a property
    cameras: Optional[enablement.Enablement] = None
    # Defines the permission level granted to users to enable them change Uefi settings
    change_uefi_settings_permission: Optional[change_uefi_settings_permission.ChangeUefiSettingsPermission] = None
    # Possible values of a property
    front_camera: Optional[enablement.Enablement] = None
    # Possible values of a property
    infrared_camera: Optional[enablement.Enablement] = None
    # Possible values of a property
    microphone: Optional[enablement.Enablement] = None
    # Possible values of a property
    microphones_and_speakers: Optional[enablement.Enablement] = None
    # Possible values of a property
    near_field_communication: Optional[enablement.Enablement] = None
    # Possible values of a property
    radios: Optional[enablement.Enablement] = None
    # Possible values of a property
    rear_camera: Optional[enablement.Enablement] = None
    # Possible values of a property
    sd_card: Optional[enablement.Enablement] = None
    # Possible values of a property
    simultaneous_multi_threading: Optional[enablement.Enablement] = None
    # Possible values of a property
    usb_type_a_port: Optional[enablement.Enablement] = None
    # Possible values of a property
    virtualization_of_cpu_and_i_o: Optional[enablement.Enablement] = None
    # Possible values of a property
    wake_on_l_a_n: Optional[enablement.Enablement] = None
    # Possible values of a property
    wake_on_power: Optional[enablement.Enablement] = None
    # Possible values of a property
    wi_fi: Optional[enablement.Enablement] = None
    # Possible values of a property
    windows_platform_binary_table: Optional[enablement.Enablement] = None
    # Possible values of a property
    wireless_wide_area_network: Optional[enablement.Enablement] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_uefi_settings_permission, device_configuration, enablement

        fields: Dict[str, Callable[[Any], None]] = {
            "bluetooth": lambda n : setattr(self, 'bluetooth', n.get_enum_value(enablement.Enablement)),
            "bootFromBuiltInNetworkAdapters": lambda n : setattr(self, 'boot_from_built_in_network_adapters', n.get_enum_value(enablement.Enablement)),
            "bootFromExternalMedia": lambda n : setattr(self, 'boot_from_external_media', n.get_enum_value(enablement.Enablement)),
            "cameras": lambda n : setattr(self, 'cameras', n.get_enum_value(enablement.Enablement)),
            "changeUefiSettingsPermission": lambda n : setattr(self, 'change_uefi_settings_permission', n.get_enum_value(change_uefi_settings_permission.ChangeUefiSettingsPermission)),
            "frontCamera": lambda n : setattr(self, 'front_camera', n.get_enum_value(enablement.Enablement)),
            "infraredCamera": lambda n : setattr(self, 'infrared_camera', n.get_enum_value(enablement.Enablement)),
            "microphone": lambda n : setattr(self, 'microphone', n.get_enum_value(enablement.Enablement)),
            "microphonesAndSpeakers": lambda n : setattr(self, 'microphones_and_speakers', n.get_enum_value(enablement.Enablement)),
            "nearFieldCommunication": lambda n : setattr(self, 'near_field_communication', n.get_enum_value(enablement.Enablement)),
            "radios": lambda n : setattr(self, 'radios', n.get_enum_value(enablement.Enablement)),
            "rearCamera": lambda n : setattr(self, 'rear_camera', n.get_enum_value(enablement.Enablement)),
            "sdCard": lambda n : setattr(self, 'sd_card', n.get_enum_value(enablement.Enablement)),
            "simultaneousMultiThreading": lambda n : setattr(self, 'simultaneous_multi_threading', n.get_enum_value(enablement.Enablement)),
            "usbTypeAPort": lambda n : setattr(self, 'usb_type_a_port', n.get_enum_value(enablement.Enablement)),
            "virtualizationOfCpuAndIO": lambda n : setattr(self, 'virtualization_of_cpu_and_i_o', n.get_enum_value(enablement.Enablement)),
            "wakeOnLAN": lambda n : setattr(self, 'wake_on_l_a_n', n.get_enum_value(enablement.Enablement)),
            "wakeOnPower": lambda n : setattr(self, 'wake_on_power', n.get_enum_value(enablement.Enablement)),
            "windowsPlatformBinaryTable": lambda n : setattr(self, 'windows_platform_binary_table', n.get_enum_value(enablement.Enablement)),
            "wirelessWideAreaNetwork": lambda n : setattr(self, 'wireless_wide_area_network', n.get_enum_value(enablement.Enablement)),
            "wiFi": lambda n : setattr(self, 'wi_fi', n.get_enum_value(enablement.Enablement)),
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
        writer.write_enum_value("windowsPlatformBinaryTable", self.windows_platform_binary_table)
        writer.write_enum_value("wirelessWideAreaNetwork", self.wireless_wide_area_network)
        writer.write_enum_value("wiFi", self.wi_fi)
    

