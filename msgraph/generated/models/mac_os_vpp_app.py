from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
    from .mac_os_vpp_app_revoke_licenses_action_result import MacOsVppAppRevokeLicensesActionResult
    from .mobile_app import MobileApp
    from .vpp_licensing_type import VppLicensingType
    from .vpp_token_account_type import VppTokenAccountType

from .mobile_app import MobileApp

@dataclass
class MacOsVppApp(MobileApp):
    """
    Contains properties and inherited properties for MacOS Volume-Purchased Program (VPP) Apps.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOsVppApp"
    # The store URL.
    app_store_url: Optional[str] = None
    # The licenses assigned to this app.
    assigned_licenses: Optional[List[MacOsVppAppAssignedLicense]] = None
    # The Identity Name.
    bundle_id: Optional[str] = None
    # The supported License Type.
    licensing_type: Optional[VppLicensingType] = None
    # The VPP application release date and time.
    release_date_time: Optional[datetime.datetime] = None
    # Results of revoke license actions on this app.
    revoke_license_action_results: Optional[List[MacOsVppAppRevokeLicensesActionResult]] = None
    # The total number of VPP licenses.
    total_license_count: Optional[int] = None
    # The number of VPP licenses in use.
    used_license_count: Optional[int] = None
    # Possible types of an Apple Volume Purchase Program token.
    vpp_token_account_type: Optional[VppTokenAccountType] = None
    # The Apple Id associated with the given Apple Volume Purchase Program Token.
    vpp_token_apple_id: Optional[str] = None
    # Identifier of the VPP token associated with this app.
    vpp_token_id: Optional[str] = None
    # The organization associated with the Apple Volume Purchase Program Token
    vpp_token_organization_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOsVppApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOsVppApp
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MacOsVppApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
        from .mac_os_vpp_app_revoke_licenses_action_result import MacOsVppAppRevokeLicensesActionResult
        from .mobile_app import MobileApp
        from .vpp_licensing_type import VppLicensingType
        from .vpp_token_account_type import VppTokenAccountType

        from .mac_os_vpp_app_assigned_license import MacOsVppAppAssignedLicense
        from .mac_os_vpp_app_revoke_licenses_action_result import MacOsVppAppRevokeLicensesActionResult
        from .mobile_app import MobileApp
        from .vpp_licensing_type import VppLicensingType
        from .vpp_token_account_type import VppTokenAccountType

        fields: Dict[str, Callable[[Any], None]] = {
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(MacOsVppAppAssignedLicense)),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "licensingType": lambda n : setattr(self, 'licensing_type', n.get_object_value(VppLicensingType)),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "revokeLicenseActionResults": lambda n : setattr(self, 'revoke_license_action_results', n.get_collection_of_object_values(MacOsVppAppRevokeLicensesActionResult)),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vppTokenAccountType": lambda n : setattr(self, 'vpp_token_account_type', n.get_enum_value(VppTokenAccountType)),
            "vppTokenAppleId": lambda n : setattr(self, 'vpp_token_apple_id', n.get_str_value()),
            "vppTokenId": lambda n : setattr(self, 'vpp_token_id', n.get_str_value()),
            "vppTokenOrganizationName": lambda n : setattr(self, 'vpp_token_organization_name', n.get_str_value()),
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
        writer.write_str_value("appStoreUrl", self.app_store_url)
        writer.write_collection_of_object_values("assignedLicenses", self.assigned_licenses)
        writer.write_str_value("bundleId", self.bundle_id)
        writer.write_object_value("licensingType", self.licensing_type)
        writer.write_datetime_value("releaseDateTime", self.release_date_time)
        writer.write_collection_of_object_values("revokeLicenseActionResults", self.revoke_license_action_results)
        writer.write_int_value("totalLicenseCount", self.total_license_count)
        writer.write_int_value("usedLicenseCount", self.used_license_count)
        writer.write_enum_value("vppTokenAccountType", self.vpp_token_account_type)
        writer.write_str_value("vppTokenAppleId", self.vpp_token_apple_id)
        writer.write_str_value("vppTokenId", self.vpp_token_id)
        writer.write_str_value("vppTokenOrganizationName", self.vpp_token_organization_name)
    

