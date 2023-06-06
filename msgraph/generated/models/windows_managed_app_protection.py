from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import managed_app_device_threat_level, managed_app_policy, managed_app_remediation_action, managed_mobile_app, targeted_managed_app_policy_assignment, windows_managed_app_clipboard_sharing_level, windows_managed_app_data_transfer_level

from . import managed_app_policy

@dataclass
class WindowsManagedAppProtection(managed_app_policy.ManagedAppPolicy):
    odata_type = "#microsoft.graph.windowsManagedAppProtection"
    # Data can be transferred from/to these classes of apps
    allowed_inbound_data_transfer_sources: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel] = None
    # Represents the level to which the device's clipboard may be shared between apps
    allowed_outbound_clipboard_sharing_level: Optional[windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel] = None
    # Data can be transferred from/to these classes of apps
    allowed_outbound_data_transfer_destinations: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel] = None
    # If set, it will specify what action to take in the case where the user is unable to checkin because their authentication token is invalid. This happens when the user is deleted or disabled in AAD. Some possible values are block or wipe. If this property is not set, no action will be taken. Possible values are: block, wipe, warn.
    app_action_if_unable_to_authenticate_user: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
    # List of apps to which the policy is deployed.
    apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
    # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
    assignments: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None
    # Indicates the total number of applications for which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # When TRUE, indicates that the policy is deployed to some inclusion groups. When FALSE, indicates that the policy is not deployed to any inclusion groups. Default value is FALSE.
    is_assigned: Optional[bool] = None
    # The maxium threat level allowed for an app to be compliant.
    maximum_allowed_device_threat_level: Optional[managed_app_device_threat_level.ManagedAppDeviceThreatLevel] = None
    # Versions bigger than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    maximum_required_os_version: Optional[str] = None
    # Versions bigger than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    maximum_warning_os_version: Optional[str] = None
    # Versions bigger than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    maximum_wipe_os_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_required_app_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_required_os_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_required_sdk_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_warning_app_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
    minimum_warning_os_version: Optional[str] = None
    # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    minimum_wipe_app_version: Optional[str] = None
    # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    minimum_wipe_os_version: Optional[str] = None
    # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
    minimum_wipe_sdk_version: Optional[str] = None
    # An admin initiated action to be applied on a managed app.
    mobile_threat_defense_remediation_action: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
    # The period after which access is checked when the device is not connected to the internet. For example, PT5M indicates that the interval is 5 minutes in duration. A timespan value of PT0S indicates that access will be blocked immediately when the device is not connected to the internet.
    period_offline_before_access_check: Optional[timedelta] = None
    # The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped. For example, P5D indicates that the interval is 5 days in duration. A timespan value of PT0S indicates that managed data will never be wiped when the device is not connected to the internet.
    period_offline_before_wipe_is_enforced: Optional[timedelta] = None
    # When TRUE, indicates that printing is blocked from managed apps. When FALSE, indicates that printing is allowed from managed apps. Default value is FALSE.
    print_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import managed_app_device_threat_level, managed_app_policy, managed_app_remediation_action, managed_mobile_app, targeted_managed_app_policy_assignment, windows_managed_app_clipboard_sharing_level, windows_managed_app_data_transfer_level

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedInboundDataTransferSources": lambda n : setattr(self, 'allowed_inbound_data_transfer_sources', n.get_enum_value(windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel)),
            "allowedOutboundClipboardSharingLevel": lambda n : setattr(self, 'allowed_outbound_clipboard_sharing_level', n.get_enum_value(windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel)),
            "allowedOutboundDataTransferDestinations": lambda n : setattr(self, 'allowed_outbound_data_transfer_destinations', n.get_enum_value(windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "appActionIfUnableToAuthenticateUser": lambda n : setattr(self, 'app_action_if_unable_to_authenticate_user', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment)),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "isAssigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "maximumAllowedDeviceThreatLevel": lambda n : setattr(self, 'maximum_allowed_device_threat_level', n.get_enum_value(managed_app_device_threat_level.ManagedAppDeviceThreatLevel)),
            "maximumRequiredOsVersion": lambda n : setattr(self, 'maximum_required_os_version', n.get_str_value()),
            "maximumWarningOsVersion": lambda n : setattr(self, 'maximum_warning_os_version', n.get_str_value()),
            "maximumWipeOsVersion": lambda n : setattr(self, 'maximum_wipe_os_version', n.get_str_value()),
            "minimumRequiredAppVersion": lambda n : setattr(self, 'minimum_required_app_version', n.get_str_value()),
            "minimumRequiredOsVersion": lambda n : setattr(self, 'minimum_required_os_version', n.get_str_value()),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimumWarningAppVersion": lambda n : setattr(self, 'minimum_warning_app_version', n.get_str_value()),
            "minimumWarningOsVersion": lambda n : setattr(self, 'minimum_warning_os_version', n.get_str_value()),
            "minimumWipeAppVersion": lambda n : setattr(self, 'minimum_wipe_app_version', n.get_str_value()),
            "minimumWipeOsVersion": lambda n : setattr(self, 'minimum_wipe_os_version', n.get_str_value()),
            "minimumWipeSdkVersion": lambda n : setattr(self, 'minimum_wipe_sdk_version', n.get_str_value()),
            "mobileThreatDefenseRemediationAction": lambda n : setattr(self, 'mobile_threat_defense_remediation_action', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "periodOfflineBeforeAccessCheck": lambda n : setattr(self, 'period_offline_before_access_check', n.get_timedelta_value()),
            "periodOfflineBeforeWipeIsEnforced": lambda n : setattr(self, 'period_offline_before_wipe_is_enforced', n.get_timedelta_value()),
            "printBlocked": lambda n : setattr(self, 'print_blocked', n.get_bool_value()),
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
        writer.write_enum_value("allowedInboundDataTransferSources", self.allowed_inbound_data_transfer_sources)
        writer.write_enum_value("allowedOutboundClipboardSharingLevel", self.allowed_outbound_clipboard_sharing_level)
        writer.write_enum_value("allowedOutboundDataTransferDestinations", self.allowed_outbound_data_transfer_destinations)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_enum_value("appActionIfUnableToAuthenticateUser", self.app_action_if_unable_to_authenticate_user)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_bool_value("isAssigned", self.is_assigned)
        writer.write_enum_value("maximumAllowedDeviceThreatLevel", self.maximum_allowed_device_threat_level)
        writer.write_str_value("maximumRequiredOsVersion", self.maximum_required_os_version)
        writer.write_str_value("maximumWarningOsVersion", self.maximum_warning_os_version)
        writer.write_str_value("maximumWipeOsVersion", self.maximum_wipe_os_version)
        writer.write_str_value("minimumRequiredAppVersion", self.minimum_required_app_version)
        writer.write_str_value("minimumRequiredOsVersion", self.minimum_required_os_version)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
        writer.write_str_value("minimumWarningAppVersion", self.minimum_warning_app_version)
        writer.write_str_value("minimumWarningOsVersion", self.minimum_warning_os_version)
        writer.write_str_value("minimumWipeAppVersion", self.minimum_wipe_app_version)
        writer.write_str_value("minimumWipeOsVersion", self.minimum_wipe_os_version)
        writer.write_str_value("minimumWipeSdkVersion", self.minimum_wipe_sdk_version)
        writer.write_enum_value("mobileThreatDefenseRemediationAction", self.mobile_threat_defense_remediation_action)
        writer.write_timedelta_value("periodOfflineBeforeAccessCheck", self.period_offline_before_access_check)
        writer.write_timedelta_value("periodOfflineBeforeWipeIsEnforced", self.period_offline_before_wipe_is_enforced)
        writer.write_bool_value("printBlocked", self.print_blocked)
    

