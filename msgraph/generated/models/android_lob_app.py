from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_minimum_operating_system, mobile_lob_app

from . import mobile_lob_app

class AndroidLobApp(mobile_lob_app.MobileLobApp):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidLobApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidLobApp"
        # The Identity Name. This property is being deprecated in 2302(February 2023).
        self._identity_name: Optional[str] = None
        # The identity version. This property is being deprecated in 2302(February 2023).
        self._identity_version: Optional[str] = None
        # The value for the minimum applicable operating system.
        self._minimum_supported_operating_system: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None
        # The package identifier.
        self._package_id: Optional[str] = None
        # The version code of Android Line of Business (LoB) app.
        self._version_code: Optional[str] = None
        # The version name of Android Line of Business (LoB) app.
        self._version_name: Optional[str] = None
    
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
    
    @property
    def identity_name(self,) -> Optional[str]:
        """
        Gets the identityName property value. The Identity Name. This property is being deprecated in 2302(February 2023).
        Returns: Optional[str]
        """
        return self._identity_name
    
    @identity_name.setter
    def identity_name(self,value: Optional[str] = None) -> None:
        """
        Sets the identityName property value. The Identity Name. This property is being deprecated in 2302(February 2023).
        Args:
            value: Value to set for the identity_name property.
        """
        self._identity_name = value
    
    @property
    def identity_version(self,) -> Optional[str]:
        """
        Gets the identityVersion property value. The identity version. This property is being deprecated in 2302(February 2023).
        Returns: Optional[str]
        """
        return self._identity_version
    
    @identity_version.setter
    def identity_version(self,value: Optional[str] = None) -> None:
        """
        Sets the identityVersion property value. The identity version. This property is being deprecated in 2302(February 2023).
        Args:
            value: Value to set for the identity_version property.
        """
        self._identity_version = value
    
    @property
    def minimum_supported_operating_system(self,) -> Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]:
        """
        Gets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Returns: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem]
        """
        return self._minimum_supported_operating_system
    
    @minimum_supported_operating_system.setter
    def minimum_supported_operating_system(self,value: Optional[android_minimum_operating_system.AndroidMinimumOperatingSystem] = None) -> None:
        """
        Sets the minimumSupportedOperatingSystem property value. The value for the minimum applicable operating system.
        Args:
            value: Value to set for the minimum_supported_operating_system property.
        """
        self._minimum_supported_operating_system = value
    
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
            value: Value to set for the package_id property.
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
        writer.write_str_value("identityName", self.identity_name)
        writer.write_str_value("identityVersion", self.identity_version)
        writer.write_object_value("minimumSupportedOperatingSystem", self.minimum_supported_operating_system)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("versionCode", self.version_code)
        writer.write_str_value("versionName", self.version_name)
    
    @property
    def version_code(self,) -> Optional[str]:
        """
        Gets the versionCode property value. The version code of Android Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._version_code
    
    @version_code.setter
    def version_code(self,value: Optional[str] = None) -> None:
        """
        Sets the versionCode property value. The version code of Android Line of Business (LoB) app.
        Args:
            value: Value to set for the version_code property.
        """
        self._version_code = value
    
    @property
    def version_name(self,) -> Optional[str]:
        """
        Gets the versionName property value. The version name of Android Line of Business (LoB) app.
        Returns: Optional[str]
        """
        return self._version_name
    
    @version_name.setter
    def version_name(self,value: Optional[str] = None) -> None:
        """
        Sets the versionName property value. The version name of Android Line of Business (LoB) app.
        Args:
            value: Value to set for the version_name property.
        """
        self._version_name = value
    

