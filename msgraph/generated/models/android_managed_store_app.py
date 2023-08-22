from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_store_app_track import AndroidManagedStoreAppTrack
    from .android_managed_store_web_app import AndroidManagedStoreWebApp
    from .mobile_app import MobileApp

from .mobile_app import MobileApp

@dataclass
class AndroidManagedStoreApp(MobileApp):
    """
    Contains properties and inherited properties for Android Managed Store Apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidManagedStoreApp"
    # The Identity Name.
    app_identifier: Optional[str] = None
    # The Play for Work Store app URL.
    app_store_url: Optional[str] = None
    # The tracks that are visible to this enterprise.
    app_tracks: Optional[List[AndroidManagedStoreAppTrack]] = None
    # Indicates whether the app is only available to a given enterprise's users.
    is_private: Optional[bool] = None
    # Indicates whether the app is a preinstalled system app.
    is_system_app: Optional[bool] = None
    # The package identifier.
    package_id: Optional[str] = None
    # Whether this app supports OEMConfig policy.
    supports_oem_config: Optional[bool] = None
    # The total number of VPP licenses.
    total_license_count: Optional[int] = None
    # The number of VPP licenses in use.
    used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedStoreWebApp".casefold():
            from .android_managed_store_web_app import AndroidManagedStoreWebApp

            return AndroidManagedStoreWebApp()
        return AndroidManagedStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_store_app_track import AndroidManagedStoreAppTrack
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .mobile_app import MobileApp

        from .android_managed_store_app_track import AndroidManagedStoreAppTrack
        from .android_managed_store_web_app import AndroidManagedStoreWebApp
        from .mobile_app import MobileApp

        fields: Dict[str, Callable[[Any], None]] = {
            "appIdentifier": lambda n : setattr(self, 'app_identifier', n.get_str_value()),
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "appTracks": lambda n : setattr(self, 'app_tracks', n.get_collection_of_object_values(AndroidManagedStoreAppTrack)),
            "isPrivate": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "isSystemApp": lambda n : setattr(self, 'is_system_app', n.get_bool_value()),
            "packageId": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "supportsOemConfig": lambda n : setattr(self, 'supports_oem_config', n.get_bool_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
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
        writer.write_str_value("appIdentifier", self.app_identifier)
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_collection_of_object_values("appTracks", self.app_tracks)
        writer.write_bool_value("isPrivate", self.is_private)
        writer.write_bool_value("isSystemApp", self.is_system_app)
        writer.write_str_value("packageId", self.package_id)
        writer.write_bool_value("supportsOemConfig", self.supports_oem_config)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    

