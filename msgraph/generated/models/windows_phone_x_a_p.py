from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mobile_lob_app, windows_minimum_operating_system

from . import mobile_lob_app

class WindowsPhoneXAP(mobile_lob_app.MobileLobApp):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsPhoneXAP and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhoneXAP"
        # The identity version.
        self._identity_version: Optional[str] = None
        # The minimum operating system required for a Windows mobile app.
        self._minimum_supported_operating_system: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None
        # The Product Identifier.
        self._product_identifier: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhoneXAP:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhoneXAP
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhoneXAP()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mobile_lob_app, windows_minimum_operating_system

        fields: Dict[str, Callable[[Any], None]] = {
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(windows_minimum_operating_system.WindowsMinimumOperatingSystem)),
            "productIdentifier": lambda n : setattr(self, 'product_identifier', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity_version(self,) -> Optional[str]:
        """
        Gets the identityVersion property value. The identity version.
        Returns: Optional[str]
        """
        return self._identity_version
    
    @identity_version.setter
    def identity_version(self,value: Optional[str] = None) -> None:
        """
        Sets the identityVersion property value. The identity version.
        Args:
            value: Value to set for the identity_version property.
        """
        self._identity_version = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The minimum operating system required for a Windows mobile app.
        Returns: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[windows_minimum_operating_system.WindowsMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The minimum operating system required for a Windows mobile app.
        Args:
            value: Value to set for the minimum_supported_operating_system property.
        """
        self._minimum_supported_operating_system = value
    
    @property
    def product_identifier(self,) -> Optional[str]:
        """
        Gets the productIdentifier property value. The Product Identifier.
        Returns: Optional[str]
        """
        return self._product_identifier
    
    @product_identifier.setter
    def product_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the productIdentifier property value. The Product Identifier.
        Args:
            value: Value to set for the product_identifier property.
        """
        self._product_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("productIdentifier", self.product_identifier)
    

