from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

mobile_app = lazy_import('msgraph.generated.models.mobile_app')

class AndroidForWorkApp(mobile_app.MobileApp):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidForWorkApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidForWorkApp"
        # The Identity Name.
        self._app_identifier: Optional[str] = None
        # The Play for Work Store app URL.
        self._app_store_url: Optional[str] = None
        # The package identifier.
        self._package_id: Optional[str] = None
        # The total number of VPP licenses.
        self._total_license_count: Optional[int] = None
        # The number of VPP licenses in use.
        self._used_license_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidForWorkApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidForWorkApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidForWorkApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_identifier": lambda n : setattr(self, 'app_identifier', n.get_str_value()),
            "app_store_url": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "package_id": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "total_license_count": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "used_license_count": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_str_value("packageId", self.package_id)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    
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
    

