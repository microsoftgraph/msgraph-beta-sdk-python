from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_managed_store_app_track = lazy_import('msgraph.generated.models.android_managed_store_app_track')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')

class AndroidManagedStoreApp(mobile_app.MobileApp):
    @property
    def app_identifier(self,) -> Optional[str]:
        """
        Gets the appIdentifier property value. The Identity Name.
        Returns: Optional[str]
        """
        return self._app_identifier
    
    @app_identifier.setter
    def app_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the appIdentifier property value. The Identity Name.
        Args:
            value: Value to set for the appIdentifier property.
        """
        self._app_identifier = value
    
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The Play for Work Store app URL.
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The Play for Work Store app URL.
        Args:
            value: Value to set for the appStoreUrl property.
        """
        self._app_store_url = value
    
    @property
    def app_tracks(self,) -> Optional[List[android_managed_store_app_track.AndroidManagedStoreAppTrack]]:
        """
        Gets the appTracks property value. The tracks that are visible to this enterprise.
        Returns: Optional[List[android_managed_store_app_track.AndroidManagedStoreAppTrack]]
        """
        return self._app_tracks
    
    @app_tracks.setter
    def app_tracks(self,value: Optional[List[android_managed_store_app_track.AndroidManagedStoreAppTrack]] = None) -> None:
        """
        Sets the appTracks property value. The tracks that are visible to this enterprise.
        Args:
            value: Value to set for the appTracks property.
        """
        self._app_tracks = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidManagedStoreApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidManagedStoreApp"
        # The Identity Name.
        self._app_identifier: Optional[str] = None
        # The Play for Work Store app URL.
        self._app_store_url: Optional[str] = None
        # The tracks that are visible to this enterprise.
        self._app_tracks: Optional[List[android_managed_store_app_track.AndroidManagedStoreAppTrack]] = None
        # Indicates whether the app is only available to a given enterprise's users.
        self._is_private: Optional[bool] = None
        # Indicates whether the app is a preinstalled system app.
        self._is_system_app: Optional[bool] = None
        # The package identifier.
        self._package_id: Optional[str] = None
        # Whether this app supports OEMConfig policy.
        self._supports_oem_config: Optional[bool] = None
        # The total number of VPP licenses.
        self._total_license_count: Optional[int] = None
        # The number of VPP licenses in use.
        self._used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_identifier": lambda n : setattr(self, 'app_identifier', n.get_str_value()),
            "app_store_url": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "app_tracks": lambda n : setattr(self, 'app_tracks', n.get_collection_of_object_values(android_managed_store_app_track.AndroidManagedStoreAppTrack)),
            "is_private": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "is_system_app": lambda n : setattr(self, 'is_system_app', n.get_bool_value()),
            "package_id": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "supports_oem_config": lambda n : setattr(self, 'supports_oem_config', n.get_bool_value()),
            "total_license_count": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "used_license_count": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_private(self,) -> Optional[bool]:
        """
        Gets the isPrivate property value. Indicates whether the app is only available to a given enterprise's users.
        Returns: Optional[bool]
        """
        return self._is_private
    
    @is_private.setter
    def is_private(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPrivate property value. Indicates whether the app is only available to a given enterprise's users.
        Args:
            value: Value to set for the isPrivate property.
        """
        self._is_private = value
    
    @property
    def is_system_app(self,) -> Optional[bool]:
        """
        Gets the isSystemApp property value. Indicates whether the app is a preinstalled system app.
        Returns: Optional[bool]
        """
        return self._is_system_app
    
    @is_system_app.setter
    def is_system_app(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSystemApp property value. Indicates whether the app is a preinstalled system app.
        Args:
            value: Value to set for the isSystemApp property.
        """
        self._is_system_app = value
    
    @property
    def package_id(self,) -> Optional[str]:
        """
        Gets the packageId property value. The package identifier.
        Returns: Optional[str]
        """
        return self._package_id
    
    @package_id.setter
    def package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the packageId property value. The package identifier.
        Args:
            value: Value to set for the packageId property.
        """
        self._package_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def supports_oem_config(self,) -> Optional[bool]:
        """
        Gets the supportsOemConfig property value. Whether this app supports OEMConfig policy.
        Returns: Optional[bool]
        """
        return self._supports_oem_config
    
    @supports_oem_config.setter
    def supports_oem_config(self,value: Optional[bool] = None) -> None:
        """
        Sets the supportsOemConfig property value. Whether this app supports OEMConfig policy.
        Args:
            value: Value to set for the supportsOemConfig property.
        """
        self._supports_oem_config = value
    
    @property
    def total_license_count(self,) -> Optional[int]:
        """
        Gets the totalLicenseCount property value. The total number of VPP licenses.
        Returns: Optional[int]
        """
        return self._total_license_count
    
    @total_license_count.setter
    def total_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalLicenseCount property value. The total number of VPP licenses.
        Args:
            value: Value to set for the totalLicenseCount property.
        """
        self._total_license_count = value
    
    @property
    def used_license_count(self,) -> Optional[int]:
        """
        Gets the usedLicenseCount property value. The number of VPP licenses in use.
        Returns: Optional[int]
        """
        return self._used_license_count
    
    @used_license_count.setter
    def used_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the usedLicenseCount property value. The number of VPP licenses in use.
        Args:
            value: Value to set for the usedLicenseCount property.
        """
        self._used_license_count = value
    

