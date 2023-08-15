from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .edition_upgrade_license_type import EditionUpgradeLicenseType
    from .windows10_edition_type import Windows10EditionType
    from .windows_s_mode_configuration import WindowsSModeConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class EditionUpgradeConfiguration(DeviceConfiguration):
    """
    Windows 10 Edition Upgrade configuration.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.editionUpgradeConfiguration"
    # Edition Upgrade License File Content.
    license: Optional[str] = None
    # Edition Upgrade License type
    license_type: Optional[EditionUpgradeLicenseType] = None
    # Edition Upgrade Product Key.
    product_key: Optional[str] = None
    # Windows 10 Edition type.
    target_edition: Optional[Windows10EditionType] = None
    # The possible options to configure S mode unlock
    windows_s_mode: Optional[WindowsSModeConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EditionUpgradeConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditionUpgradeConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EditionUpgradeConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .edition_upgrade_license_type import EditionUpgradeLicenseType
        from .windows10_edition_type import Windows10EditionType
        from .windows_s_mode_configuration import WindowsSModeConfiguration

        from .device_configuration import DeviceConfiguration
        from .edition_upgrade_license_type import EditionUpgradeLicenseType
        from .windows10_edition_type import Windows10EditionType
        from .windows_s_mode_configuration import WindowsSModeConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "license": lambda n : setattr(self, 'license', n.get_str_value()),
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(EditionUpgradeLicenseType)),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "targetEdition": lambda n : setattr(self, 'target_edition', n.get_enum_value(Windows10EditionType)),
            "windowsSMode": lambda n : setattr(self, 'windows_s_mode', n.get_enum_value(WindowsSModeConfiguration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("license", self.license)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_str_value("productKey", self.product_key)
        writer.write_enum_value("targetEdition", self.target_edition)
        writer.write_enum_value("windowsSMode", self.windows_s_mode)
    

