from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

microsoft_store_for_business_license_type = lazy_import('msgraph.generated.models.microsoft_store_for_business_license_type')
mobile_app = lazy_import('msgraph.generated.models.mobile_app')
mobile_contained_app = lazy_import('msgraph.generated.models.mobile_contained_app')
vpp_licensing_type = lazy_import('msgraph.generated.models.vpp_licensing_type')

class MicrosoftStoreForBusinessApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new MicrosoftStoreForBusinessApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.microsoftStoreForBusinessApp"
        # The collection of contained apps in a mobileApp acting as a package.
        self._contained_apps: Optional[List[mobile_contained_app.MobileContainedApp]] = None
        # The licenseType property
        self._license_type: Optional[microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType] = None
        # The supported License Type.
        self._licensing_type: Optional[vpp_licensing_type.VppLicensingType] = None
        # The app package identifier
        self._package_identity_name: Optional[str] = None
        # The app product key
        self._product_key: Optional[str] = None
        # The total number of Microsoft Store for Business licenses.
        self._total_license_count: Optional[int] = None
        # The number of Microsoft Store for Business licenses in use.
        self._used_license_count: Optional[int] = None
    
    @property
    def contained_apps(self,) -> Optional[List[mobile_contained_app.MobileContainedApp]]:
        """
        Gets the containedApps property value. The collection of contained apps in a mobileApp acting as a package.
        Returns: Optional[List[mobile_contained_app.MobileContainedApp]]
        """
        return self._contained_apps
    
    @contained_apps.setter
    def contained_apps(self,value: Optional[List[mobile_contained_app.MobileContainedApp]] = None) -> None:
        """
        Sets the containedApps property value. The collection of contained apps in a mobileApp acting as a package.
        Args:
            value: Value to set for the containedApps property.
        """
        self._contained_apps = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftStoreForBusinessApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftStoreForBusinessApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftStoreForBusinessApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "contained_apps": lambda n : setattr(self, 'contained_apps', n.get_collection_of_object_values(mobile_contained_app.MobileContainedApp)),
            "license_type": lambda n : setattr(self, 'license_type', n.get_enum_value(microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType)),
            "licensing_type": lambda n : setattr(self, 'licensing_type', n.get_object_value(vpp_licensing_type.VppLicensingType)),
            "package_identity_name": lambda n : setattr(self, 'package_identity_name', n.get_str_value()),
            "product_key": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "total_license_count": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "used_license_count": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def license_type(self,) -> Optional[microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType]:
        """
        Gets the licenseType property value. The licenseType property
        Returns: Optional[microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType]
        """
        return self._license_type
    
    @license_type.setter
    def license_type(self,value: Optional[microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType] = None) -> None:
        """
        Sets the licenseType property value. The licenseType property
        Args:
            value: Value to set for the licenseType property.
        """
        self._license_type = value
    
    @property
    def licensing_type(self,) -> Optional[vpp_licensing_type.VppLicensingType]:
        """
        Gets the licensingType property value. The supported License Type.
        Returns: Optional[vpp_licensing_type.VppLicensingType]
        """
        return self._licensing_type
    
    @licensing_type.setter
    def licensing_type(self,value: Optional[vpp_licensing_type.VppLicensingType] = None) -> None:
        """
        Sets the licensingType property value. The supported License Type.
        Args:
            value: Value to set for the licensingType property.
        """
        self._licensing_type = value
    
    @property
    def package_identity_name(self,) -> Optional[str]:
        """
        Gets the packageIdentityName property value. The app package identifier
        Returns: Optional[str]
        """
        return self._package_identity_name
    
    @package_identity_name.setter
    def package_identity_name(self,value: Optional[str] = None) -> None:
        """
        Sets the packageIdentityName property value. The app package identifier
        Args:
            value: Value to set for the packageIdentityName property.
        """
        self._package_identity_name = value
    
    @property
    def product_key(self,) -> Optional[str]:
        """
        Gets the productKey property value. The app product key
        Returns: Optional[str]
        """
        return self._product_key
    
    @product_key.setter
    def product_key(self,value: Optional[str] = None) -> None:
        """
        Sets the productKey property value. The app product key
        Args:
            value: Value to set for the productKey property.
        """
        self._product_key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("containedApps", self.contained_apps)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_object_value("licensingType", self.licensing_type)
        writer.write_str_value("packageIdentityName", self.package_identity_name)
        writer.write_str_value("productKey", self.product_key)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    
    @property
    def total_license_count(self,) -> Optional[int]:
        """
        Gets the totalLicenseCount property value. The total number of Microsoft Store for Business licenses.
        Returns: Optional[int]
        """
        return self._total_license_count
    
    @total_license_count.setter
    def total_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalLicenseCount property value. The total number of Microsoft Store for Business licenses.
        Args:
            value: Value to set for the totalLicenseCount property.
        """
        self._total_license_count = value
    
    @property
    def used_license_count(self,) -> Optional[int]:
        """
        Gets the usedLicenseCount property value. The number of Microsoft Store for Business licenses in use.
        Returns: Optional[int]
        """
        return self._used_license_count
    
    @used_license_count.setter
    def used_license_count(self,value: Optional[int] = None) -> None:
        """
        Sets the usedLicenseCount property value. The number of Microsoft Store for Business licenses in use.
        Args:
            value: Value to set for the usedLicenseCount property.
        """
        self._used_license_count = value
    

