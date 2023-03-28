from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_device_type, ios_vpp_app_assigned_license, ios_vpp_app_revoke_licenses_action_result, mobile_app, vpp_licensing_type, vpp_token_account_type

from . import mobile_app

class IosVppApp(mobile_app.MobileApp):
    def __init__(self,) -> None:
        """
        Instantiates a new IosVppApp and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosVppApp"
        # The store URL.
        self._app_store_url: Optional[str] = None
        # The applicable iOS Device Type.
        self._applicable_device_type: Optional[ios_device_type.IosDeviceType] = None
        # The licenses assigned to this app.
        self._assigned_licenses: Optional[List[ios_vpp_app_assigned_license.IosVppAppAssignedLicense]] = None
        # The Identity Name.
        self._bundle_id: Optional[str] = None
        # The supported License Type.
        self._licensing_type: Optional[vpp_licensing_type.VppLicensingType] = None
        # The VPP application release date and time.
        self._release_date_time: Optional[datetime] = None
        # Results of revoke license actions on this app.
        self._revoke_license_action_results: Optional[List[ios_vpp_app_revoke_licenses_action_result.IosVppAppRevokeLicensesActionResult]] = None
        # The total number of VPP licenses.
        self._total_license_count: Optional[int] = None
        # The number of VPP licenses in use.
        self._used_license_count: Optional[int] = None
        # Possible types of an Apple Volume Purchase Program token.
        self._vpp_token_account_type: Optional[vpp_token_account_type.VppTokenAccountType] = None
        # The Apple Id associated with the given Apple Volume Purchase Program Token.
        self._vpp_token_apple_id: Optional[str] = None
        # Identifier of the VPP token associated with this app.
        self._vpp_token_id: Optional[str] = None
        # The organization associated with the Apple Volume Purchase Program Token
        self._vpp_token_organization_name: Optional[str] = None
    
    @property
    def app_store_url(self,) -> Optional[str]:
        """
        Gets the appStoreUrl property value. The store URL.
        Returns: Optional[str]
        """
        return self._app_store_url
    
    @app_store_url.setter
    def app_store_url(self,value: Optional[str] = None) -> None:
        """
        Sets the appStoreUrl property value. The store URL.
        Args:
            value: Value to set for the app_store_url property.
        """
        self._app_store_url = value
    
    @property
    def applicable_device_type(self,) -> Optional[ios_device_type.IosDeviceType]:
        """
        Gets the applicableDeviceType property value. The applicable iOS Device Type.
        Returns: Optional[ios_device_type.IosDeviceType]
        """
        return self._applicable_device_type
    
    @applicable_device_type.setter
    def applicable_device_type(self,value: Optional[ios_device_type.IosDeviceType] = None) -> None:
        """
        Sets the applicableDeviceType property value. The applicable iOS Device Type.
        Args:
            value: Value to set for the applicable_device_type property.
        """
        self._applicable_device_type = value
    
    @property
    def assigned_licenses(self,) -> Optional[List[ios_vpp_app_assigned_license.IosVppAppAssignedLicense]]:
        """
        Gets the assignedLicenses property value. The licenses assigned to this app.
        Returns: Optional[List[ios_vpp_app_assigned_license.IosVppAppAssignedLicense]]
        """
        return self._assigned_licenses
    
    @assigned_licenses.setter
    def assigned_licenses(self,value: Optional[List[ios_vpp_app_assigned_license.IosVppAppAssignedLicense]] = None) -> None:
        """
        Sets the assignedLicenses property value. The licenses assigned to this app.
        Args:
            value: Value to set for the assigned_licenses property.
        """
        self._assigned_licenses = value
    
    @property
    def bundle_id(self,) -> Optional[str]:
        """
        Gets the bundleId property value. The Identity Name.
        Returns: Optional[str]
        """
        return self._bundle_id
    
    @bundle_id.setter
    def bundle_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bundleId property value. The Identity Name.
        Args:
            value: Value to set for the bundle_id property.
        """
        self._bundle_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosVppApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosVppApp
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosVppApp()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_device_type, ios_vpp_app_assigned_license, ios_vpp_app_revoke_licenses_action_result, mobile_app, vpp_licensing_type, vpp_token_account_type

        fields: Dict[str, Callable[[Any], None]] = {
            "applicableDeviceType": lambda n : setattr(self, 'applicable_device_type', n.get_object_value(ios_device_type.IosDeviceType)),
            "appStoreUrl": lambda n : setattr(self, 'app_store_url', n.get_str_value()),
            "assignedLicenses": lambda n : setattr(self, 'assigned_licenses', n.get_collection_of_object_values(ios_vpp_app_assigned_license.IosVppAppAssignedLicense)),
            "bundleId": lambda n : setattr(self, 'bundle_id', n.get_str_value()),
            "licensingType": lambda n : setattr(self, 'licensing_type', n.get_object_value(vpp_licensing_type.VppLicensingType)),
            "releaseDateTime": lambda n : setattr(self, 'release_date_time', n.get_datetime_value()),
            "revokeLicenseActionResults": lambda n : setattr(self, 'revoke_license_action_results', n.get_collection_of_object_values(ios_vpp_app_revoke_licenses_action_result.IosVppAppRevokeLicensesActionResult)),
            "totalLicenseCount": lambda n : setattr(self, 'total_license_count', n.get_int_value()),
            "usedLicenseCount": lambda n : setattr(self, 'used_license_count', n.get_int_value()),
            "vppTokenAccountType": lambda n : setattr(self, 'vpp_token_account_type', n.get_enum_value(vpp_token_account_type.VppTokenAccountType)),
            "vppTokenAppleId": lambda n : setattr(self, 'vpp_token_apple_id', n.get_str_value()),
            "vppTokenId": lambda n : setattr(self, 'vpp_token_id', n.get_str_value()),
            "vppTokenOrganizationName": lambda n : setattr(self, 'vpp_token_organization_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
            value: Value to set for the licensing_type property.
        """
        self._licensing_type = value
    
    @property
    def release_date_time(self,) -> Optional[datetime]:
        """
        Gets the releaseDateTime property value. The VPP application release date and time.
        Returns: Optional[datetime]
        """
        return self._release_date_time
    
    @release_date_time.setter
    def release_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the releaseDateTime property value. The VPP application release date and time.
        Args:
            value: Value to set for the release_date_time property.
        """
        self._release_date_time = value
    
    @property
    def revoke_license_action_results(self,) -> Optional[List[ios_vpp_app_revoke_licenses_action_result.IosVppAppRevokeLicensesActionResult]]:
        """
        Gets the revokeLicenseActionResults property value. Results of revoke license actions on this app.
        Returns: Optional[List[ios_vpp_app_revoke_licenses_action_result.IosVppAppRevokeLicensesActionResult]]
        """
        return self._revoke_license_action_results
    
    @revoke_license_action_results.setter
    def revoke_license_action_results(self,value: Optional[List[ios_vpp_app_revoke_licenses_action_result.IosVppAppRevokeLicensesActionResult]] = None) -> None:
        """
        Sets the revokeLicenseActionResults property value. Results of revoke license actions on this app.
        Args:
            value: Value to set for the revoke_license_action_results property.
        """
        self._revoke_license_action_results = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("applicableDeviceType", self.applicable_device_type)
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
            value: Value to set for the total_license_count property.
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
            value: Value to set for the used_license_count property.
        """
        self._used_license_count = value
    
    @property
    def vpp_token_account_type(self,) -> Optional[vpp_token_account_type.VppTokenAccountType]:
        """
        Gets the vppTokenAccountType property value. Possible types of an Apple Volume Purchase Program token.
        Returns: Optional[vpp_token_account_type.VppTokenAccountType]
        """
        return self._vpp_token_account_type
    
    @vpp_token_account_type.setter
    def vpp_token_account_type(self,value: Optional[vpp_token_account_type.VppTokenAccountType] = None) -> None:
        """
        Sets the vppTokenAccountType property value. Possible types of an Apple Volume Purchase Program token.
        Args:
            value: Value to set for the vpp_token_account_type property.
        """
        self._vpp_token_account_type = value
    
    @property
    def vpp_token_apple_id(self,) -> Optional[str]:
        """
        Gets the vppTokenAppleId property value. The Apple Id associated with the given Apple Volume Purchase Program Token.
        Returns: Optional[str]
        """
        return self._vpp_token_apple_id
    
    @vpp_token_apple_id.setter
    def vpp_token_apple_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vppTokenAppleId property value. The Apple Id associated with the given Apple Volume Purchase Program Token.
        Args:
            value: Value to set for the vpp_token_apple_id property.
        """
        self._vpp_token_apple_id = value
    
    @property
    def vpp_token_id(self,) -> Optional[str]:
        """
        Gets the vppTokenId property value. Identifier of the VPP token associated with this app.
        Returns: Optional[str]
        """
        return self._vpp_token_id
    
    @vpp_token_id.setter
    def vpp_token_id(self,value: Optional[str] = None) -> None:
        """
        Sets the vppTokenId property value. Identifier of the VPP token associated with this app.
        Args:
            value: Value to set for the vpp_token_id property.
        """
        self._vpp_token_id = value
    
    @property
    def vpp_token_organization_name(self,) -> Optional[str]:
        """
        Gets the vppTokenOrganizationName property value. The organization associated with the Apple Volume Purchase Program Token
        Returns: Optional[str]
        """
        return self._vpp_token_organization_name
    
    @vpp_token_organization_name.setter
    def vpp_token_organization_name(self,value: Optional[str] = None) -> None:
        """
        Sets the vppTokenOrganizationName property value. The organization associated with the Apple Volume Purchase Program Token
        Args:
            value: Value to set for the vpp_token_organization_name property.
        """
        self._vpp_token_organization_name = value
    

