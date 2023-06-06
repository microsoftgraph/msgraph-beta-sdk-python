from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import microsoft_store_for_business_license_type, mobile_app, mobile_contained_app, vpp_licensing_type

from . import mobile_app

@dataclass
class MicrosoftStoreForBusinessApp(mobile_app.MobileApp):
    odata_type = "#microsoft.graph.microsoftStoreForBusinessApp"
    # The collection of contained apps in a mobileApp acting as a package.
    contained_apps: Optional[List[mobile_contained_app.MobileContainedApp]] = None
    # The licenseType property
    license_type: Optional[microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType] = None
    # The supported License Type.
    licensing_type: Optional[vpp_licensing_type.VppLicensingType] = None
    # The app package identifier
    package_identity_name: Optional[str] = None
    # The app product key
    product_key: Optional[str] = None
    # The total number of Microsoft Store for Business licenses.
    total_license_count: Optional[int] = None
    # The number of Microsoft Store for Business licenses in use.
    used_license_count: Optional[int] = None
    
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
        from . import microsoft_store_for_business_license_type, mobile_app, mobile_contained_app, vpp_licensing_type

        fields: Dict[str, Callable[[Any], None]] = {
            "containedApps": lambda n : setattr(self, 'contained_apps', n.get_collection_of_object_values(mobile_contained_app.MobileContainedApp)),
            "licenseType": lambda n : setattr(self, 'license_type', n.get_enum_value(microsoft_store_for_business_license_type.MicrosoftStoreForBusinessLicenseType)),
            "licensingType": lambda n : setattr(self, 'licensing_type', n.get_object_value(vpp_licensing_type.VppLicensingType)),
            "packageIdentityName": lambda n : setattr(self, 'package_identity_name', n.get_str_value()),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
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
        writer.write_collection_of_object_values("containedApps", self.contained_apps)
        writer.write_enum_value("licenseType", self.license_type)
        writer.write_object_value("licensingType", self.licensing_type)
        writer.write_str_value("packageIdentityName", self.package_identity_name)
        writer.write_str_value("productKey", self.product_key)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
    

