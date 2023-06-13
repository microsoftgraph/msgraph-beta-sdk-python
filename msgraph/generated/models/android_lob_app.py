from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_minimum_operating_system, mobile_lob_app

from . import mobile_lob_app

@dataclass
class AndroidLobApp(mobile_lob_app.MobileLobApp):
    odata_type = "#microsoft.graph.androidLobApp"
    # The Identity Name. This property is being deprecated in 2302(February 2023).
    identity_name: Optional[str] = None
    # The identity version. This property is being deprecated in 2302(February 2023).
    identity_version: Optional[str] = None
    # The value for the minimum applicable operating system.
    minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
    # The package identifier.
    package_id: Optional[str] = None
    # The version code of Android Line of Business (LoB) app.
    version_code: Optional[str] = None
    # The version name of Android Line of Business (LoB) app.
    version_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidLobApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidLobApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidLobApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_minimum_operating_system, mobile_lob_app

        fields: Dict[str, Callable[[Any], None]] = {
            "identityName": lambda n : setattr(self, 'identity_name', n.get_str_value()),
            "identityVersion": lambda n : setattr(self, 'identity_version', n.get_str_value()),
            "minimumSupportedOperatingSystem": lambda n : setattr(self, 'minimum_supported_operating_system', n.get_object_value(android_minimum_operating_system.AndroidMinimumOperatingSystem)),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "versionCode": lambda n : setattr(self, 'version_code', n.get_str_value()),
            "versionName": lambda n : setattr(self, 'version_name', n.get_str_value()),
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
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("versionCode", self.version_code)
        writer.write_str_value("versionName", self.version_name)
    

