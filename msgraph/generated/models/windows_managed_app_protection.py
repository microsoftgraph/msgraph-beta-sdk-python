from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_app_device_threat_level = lazy_import('msgraph.generated.models.managed_app_device_threat_level')
managed_app_policy = lazy_import('msgraph.generated.models.managed_app_policy')
managed_app_remediation_action = lazy_import('msgraph.generated.models.managed_app_remediation_action')
managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')
targeted_managed_app_policy_assignment = lazy_import('msgraph.generated.models.targeted_managed_app_policy_assignment')
windows_managed_app_clipboard_sharing_level = lazy_import('msgraph.generated.models.windows_managed_app_clipboard_sharing_level')
windows_managed_app_data_transfer_level = lazy_import('msgraph.generated.models.windows_managed_app_data_transfer_level')

class WindowsManagedAppProtection(managed_app_policy.ManagedAppPolicy):
    @property
    def allowed_inbound_data_transfer_sources(self,) -> Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel]:
        """
        Gets the allowedInboundDataTransferSources property value. Data can be transferred from/to these classes of apps
        Returns: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel]
        """
        return self._allowed_inbound_data_transfer_sources
    
    @allowed_inbound_data_transfer_sources.setter
    def allowed_inbound_data_transfer_sources(self,value: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel] = None) -> None:
        """
        Sets the allowedInboundDataTransferSources property value. Data can be transferred from/to these classes of apps
        Args:
            value: Value to set for the allowedInboundDataTransferSources property.
        """
        self._allowed_inbound_data_transfer_sources = value
    
    @property
    def allowed_outbound_clipboard_sharing_level(self,) -> Optional[windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel]:
        """
        Gets the allowedOutboundClipboardSharingLevel property value. Represents the level to which the device's clipboard may be shared between apps
        Returns: Optional[windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel]
        """
        return self._allowed_outbound_clipboard_sharing_level
    
    @allowed_outbound_clipboard_sharing_level.setter
    def allowed_outbound_clipboard_sharing_level(self,value: Optional[windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel] = None) -> None:
        """
        Sets the allowedOutboundClipboardSharingLevel property value. Represents the level to which the device's clipboard may be shared between apps
        Args:
            value: Value to set for the allowedOutboundClipboardSharingLevel property.
        """
        self._allowed_outbound_clipboard_sharing_level = value
    
    @property
    def allowed_outbound_data_transfer_destinations(self,) -> Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel]:
        """
        Gets the allowedOutboundDataTransferDestinations property value. Data can be transferred from/to these classes of apps
        Returns: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel]
        """
        return self._allowed_outbound_data_transfer_destinations
    
    @allowed_outbound_data_transfer_destinations.setter
    def allowed_outbound_data_transfer_destinations(self,value: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel] = None) -> None:
        """
        Sets the allowedOutboundDataTransferDestinations property value. Data can be transferred from/to these classes of apps
        Args:
            value: Value to set for the allowedOutboundDataTransferDestinations property.
        """
        self._allowed_outbound_data_transfer_destinations = value
    
    @property
    def app_action_if_unable_to_authenticate_user(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfUnableToAuthenticateUser property value. If set, it will specify what action to take in the case where the user is unable to checkin because their authentication token is invalid. This happens when the user is deleted or disabled in AAD. Some possible values are block or wipe. If this property is not set, no action will be taken. Possible values are: block, wipe, warn.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_unable_to_authenticate_user
    
    @app_action_if_unable_to_authenticate_user.setter
    def app_action_if_unable_to_authenticate_user(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfUnableToAuthenticateUser property value. If set, it will specify what action to take in the case where the user is unable to checkin because their authentication token is invalid. This happens when the user is deleted or disabled in AAD. Some possible values are block or wipe. If this property is not set, no action will be taken. Possible values are: block, wipe, warn.
        Args:
            value: Value to set for the appActionIfUnableToAuthenticateUser property.
        """
        self._app_action_if_unable_to_authenticate_user = value
    
    @property
    def apps(self,) -> Optional[List[managed_mobile_app.ManagedMobileApp]]:
        """
        Gets the apps property value. List of apps to which the policy is deployed.
        Returns: Optional[List[managed_mobile_app.ManagedMobileApp]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[managed_mobile_app.ManagedMobileApp]] = None) -> None:
        """
        Sets the apps property value. List of apps to which the policy is deployed.
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
    @property
    def assignments(self,) -> Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]]:
        """
        Gets the assignments property value. Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        Returns: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsManagedAppProtection"
        # Data can be transferred from/to these classes of apps
        self._allowed_inbound_data_transfer_sources: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel] = None
        # Represents the level to which the device's clipboard may be shared between apps
        self._allowed_outbound_clipboard_sharing_level: Optional[windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel] = None
        # Data can be transferred from/to these classes of apps
        self._allowed_outbound_data_transfer_destinations: Optional[windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel] = None
        # If set, it will specify what action to take in the case where the user is unable to checkin because their authentication token is invalid. This happens when the user is deleted or disabled in AAD. Some possible values are block or wipe. If this property is not set, no action will be taken. Possible values are: block, wipe, warn.
        self._app_action_if_unable_to_authenticate_user: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # Navigation property to list of inclusion and exclusion groups to which the policy is deployed.
        self._assignments: Optional[List[targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment]] = None
        # Indicates the total number of applications for which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # When TRUE, indicates that the policy is deployed to some inclusion groups. When FALSE, indicates that the policy is not deployed to any inclusion groups. Default value is FALSE.
        self._is_assigned: Optional[bool] = None
        # The maxium threat level allowed for an app to be compliant.
        self._maximum_allowed_device_threat_level: Optional[managed_app_device_threat_level.ManagedAppDeviceThreatLevel] = None
        # Versions bigger than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._maximum_required_os_version: Optional[str] = None
        # Versions bigger than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._maximum_warning_os_version: Optional[str] = None
        # Versions bigger than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        self._maximum_wipe_os_version: Optional[str] = None
        # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_required_app_version: Optional[str] = None
        # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_required_os_version: Optional[str] = None
        # Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_required_sdk_version: Optional[str] = None
        # Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_warning_app_version: Optional[str] = None
        # Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_warning_os_version: Optional[str] = None
        # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_wipe_app_version: Optional[str] = None
        # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_wipe_os_version: Optional[str] = None
        # Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        self._minimum_wipe_sdk_version: Optional[str] = None
        # An admin initiated action to be applied on a managed app.
        self._mobile_threat_defense_remediation_action: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # The period after which access is checked when the device is not connected to the internet. For example, PT5M indicates that the interval is 5 minutes in duration. A timespan value of PT0S indicates that access will be blocked immediately when the device is not connected to the internet.
        self._period_offline_before_access_check: Optional[Timedelta] = None
        # The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped. For example, P5D indicates that the interval is 5 days in duration. A timespan value of PT0S indicates that managed data will never be wiped when the device is not connected to the internet.
        self._period_offline_before_wipe_is_enforced: Optional[Timedelta] = None
        # When TRUE, indicates that printing is blocked from managed apps. When FALSE, indicates that printing is allowed from managed apps. Default value is FALSE.
        self._print_blocked: Optional[bool] = None
    
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
    
    @property
    def deployed_app_count(self,) -> Optional[int]:
        """
        Gets the deployedAppCount property value. Indicates the total number of applications for which the current policy is deployed.
        Returns: Optional[int]
        """
        return self._deployed_app_count
    
    @deployed_app_count.setter
    def deployed_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deployedAppCount property value. Indicates the total number of applications for which the current policy is deployed.
        Args:
            value: Value to set for the deployedAppCount property.
        """
        self._deployed_app_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_inbound_data_transfer_sources": lambda n : setattr(self, 'allowed_inbound_data_transfer_sources', n.get_enum_value(windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel)),
            "allowed_outbound_clipboard_sharing_level": lambda n : setattr(self, 'allowed_outbound_clipboard_sharing_level', n.get_enum_value(windows_managed_app_clipboard_sharing_level.WindowsManagedAppClipboardSharingLevel)),
            "allowed_outbound_data_transfer_destinations": lambda n : setattr(self, 'allowed_outbound_data_transfer_destinations', n.get_enum_value(windows_managed_app_data_transfer_level.WindowsManagedAppDataTransferLevel)),
            "app_action_if_unable_to_authenticate_user": lambda n : setattr(self, 'app_action_if_unable_to_authenticate_user', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(targeted_managed_app_policy_assignment.TargetedManagedAppPolicyAssignment)),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "is_assigned": lambda n : setattr(self, 'is_assigned', n.get_bool_value()),
            "maximum_allowed_device_threat_level": lambda n : setattr(self, 'maximum_allowed_device_threat_level', n.get_enum_value(managed_app_device_threat_level.ManagedAppDeviceThreatLevel)),
            "maximum_required_os_version": lambda n : setattr(self, 'maximum_required_os_version', n.get_str_value()),
            "maximum_warning_os_version": lambda n : setattr(self, 'maximum_warning_os_version', n.get_str_value()),
            "maximum_wipe_os_version": lambda n : setattr(self, 'maximum_wipe_os_version', n.get_str_value()),
            "minimum_required_app_version": lambda n : setattr(self, 'minimum_required_app_version', n.get_str_value()),
            "minimum_required_os_version": lambda n : setattr(self, 'minimum_required_os_version', n.get_str_value()),
            "minimum_required_sdk_version": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimum_warning_app_version": lambda n : setattr(self, 'minimum_warning_app_version', n.get_str_value()),
            "minimum_warning_os_version": lambda n : setattr(self, 'minimum_warning_os_version', n.get_str_value()),
            "minimum_wipe_app_version": lambda n : setattr(self, 'minimum_wipe_app_version', n.get_str_value()),
            "minimum_wipe_os_version": lambda n : setattr(self, 'minimum_wipe_os_version', n.get_str_value()),
            "minimum_wipe_sdk_version": lambda n : setattr(self, 'minimum_wipe_sdk_version', n.get_str_value()),
            "mobile_threat_defense_remediation_action": lambda n : setattr(self, 'mobile_threat_defense_remediation_action', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "period_offline_before_access_check": lambda n : setattr(self, 'period_offline_before_access_check', n.get_object_value(Timedelta)),
            "period_offline_before_wipe_is_enforced": lambda n : setattr(self, 'period_offline_before_wipe_is_enforced', n.get_object_value(Timedelta)),
            "print_blocked": lambda n : setattr(self, 'print_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_assigned(self,) -> Optional[bool]:
        """
        Gets the isAssigned property value. When TRUE, indicates that the policy is deployed to some inclusion groups. When FALSE, indicates that the policy is not deployed to any inclusion groups. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._is_assigned
    
    @is_assigned.setter
    def is_assigned(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAssigned property value. When TRUE, indicates that the policy is deployed to some inclusion groups. When FALSE, indicates that the policy is not deployed to any inclusion groups. Default value is FALSE.
        Args:
            value: Value to set for the isAssigned property.
        """
        self._is_assigned = value
    
    @property
    def maximum_allowed_device_threat_level(self,) -> Optional[managed_app_device_threat_level.ManagedAppDeviceThreatLevel]:
        """
        Gets the maximumAllowedDeviceThreatLevel property value. The maxium threat level allowed for an app to be compliant.
        Returns: Optional[managed_app_device_threat_level.ManagedAppDeviceThreatLevel]
        """
        return self._maximum_allowed_device_threat_level
    
    @maximum_allowed_device_threat_level.setter
    def maximum_allowed_device_threat_level(self,value: Optional[managed_app_device_threat_level.ManagedAppDeviceThreatLevel] = None) -> None:
        """
        Sets the maximumAllowedDeviceThreatLevel property value. The maxium threat level allowed for an app to be compliant.
        Args:
            value: Value to set for the maximumAllowedDeviceThreatLevel property.
        """
        self._maximum_allowed_device_threat_level = value
    
    @property
    def maximum_required_os_version(self,) -> Optional[str]:
        """
        Gets the maximumRequiredOsVersion property value. Versions bigger than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._maximum_required_os_version
    
    @maximum_required_os_version.setter
    def maximum_required_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the maximumRequiredOsVersion property value. Versions bigger than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the maximumRequiredOsVersion property.
        """
        self._maximum_required_os_version = value
    
    @property
    def maximum_warning_os_version(self,) -> Optional[str]:
        """
        Gets the maximumWarningOsVersion property value. Versions bigger than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._maximum_warning_os_version
    
    @maximum_warning_os_version.setter
    def maximum_warning_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the maximumWarningOsVersion property value. Versions bigger than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the maximumWarningOsVersion property.
        """
        self._maximum_warning_os_version = value
    
    @property
    def maximum_wipe_os_version(self,) -> Optional[str]:
        """
        Gets the maximumWipeOsVersion property value. Versions bigger than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._maximum_wipe_os_version
    
    @maximum_wipe_os_version.setter
    def maximum_wipe_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the maximumWipeOsVersion property value. Versions bigger than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the maximumWipeOsVersion property.
        """
        self._maximum_wipe_os_version = value
    
    @property
    def minimum_required_app_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredAppVersion property value. Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_required_app_version
    
    @minimum_required_app_version.setter
    def minimum_required_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredAppVersion property value. Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumRequiredAppVersion property.
        """
        self._minimum_required_app_version = value
    
    @property
    def minimum_required_os_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredOsVersion property value. Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_required_os_version
    
    @minimum_required_os_version.setter
    def minimum_required_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredOsVersion property value. Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumRequiredOsVersion property.
        """
        self._minimum_required_os_version = value
    
    @property
    def minimum_required_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_required_sdk_version
    
    @minimum_required_sdk_version.setter
    def minimum_required_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumRequiredSdkVersion property.
        """
        self._minimum_required_sdk_version = value
    
    @property
    def minimum_warning_app_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningAppVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_warning_app_version
    
    @minimum_warning_app_version.setter
    def minimum_warning_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningAppVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumWarningAppVersion property.
        """
        self._minimum_warning_app_version = value
    
    @property
    def minimum_warning_os_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningOsVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_warning_os_version
    
    @minimum_warning_os_version.setter
    def minimum_warning_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningOsVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumWarningOsVersion property.
        """
        self._minimum_warning_os_version = value
    
    @property
    def minimum_wipe_app_version(self,) -> Optional[str]:
        """
        Gets the minimumWipeAppVersion property value. Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_wipe_app_version
    
    @minimum_wipe_app_version.setter
    def minimum_wipe_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWipeAppVersion property value. Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumWipeAppVersion property.
        """
        self._minimum_wipe_app_version = value
    
    @property
    def minimum_wipe_os_version(self,) -> Optional[str]:
        """
        Gets the minimumWipeOsVersion property value. Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_wipe_os_version
    
    @minimum_wipe_os_version.setter
    def minimum_wipe_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWipeOsVersion property value. Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumWipeOsVersion property.
        """
        self._minimum_wipe_os_version = value
    
    @property
    def minimum_wipe_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumWipeSdkVersion property value. Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Returns: Optional[str]
        """
        return self._minimum_wipe_sdk_version
    
    @minimum_wipe_sdk_version.setter
    def minimum_wipe_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWipeSdkVersion property value. Versions less than the specified version will wipe the managed app and the associated company data. For example: '8.1.0' or '13.1.1'.
        Args:
            value: Value to set for the minimumWipeSdkVersion property.
        """
        self._minimum_wipe_sdk_version = value
    
    @property
    def mobile_threat_defense_remediation_action(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the mobileThreatDefenseRemediationAction property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._mobile_threat_defense_remediation_action
    
    @mobile_threat_defense_remediation_action.setter
    def mobile_threat_defense_remediation_action(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the mobileThreatDefenseRemediationAction property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the mobileThreatDefenseRemediationAction property.
        """
        self._mobile_threat_defense_remediation_action = value
    
    @property
    def period_offline_before_access_check(self,) -> Optional[Timedelta]:
        """
        Gets the periodOfflineBeforeAccessCheck property value. The period after which access is checked when the device is not connected to the internet. For example, PT5M indicates that the interval is 5 minutes in duration. A timespan value of PT0S indicates that access will be blocked immediately when the device is not connected to the internet.
        Returns: Optional[Timedelta]
        """
        return self._period_offline_before_access_check
    
    @period_offline_before_access_check.setter
    def period_offline_before_access_check(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the periodOfflineBeforeAccessCheck property value. The period after which access is checked when the device is not connected to the internet. For example, PT5M indicates that the interval is 5 minutes in duration. A timespan value of PT0S indicates that access will be blocked immediately when the device is not connected to the internet.
        Args:
            value: Value to set for the periodOfflineBeforeAccessCheck property.
        """
        self._period_offline_before_access_check = value
    
    @property
    def period_offline_before_wipe_is_enforced(self,) -> Optional[Timedelta]:
        """
        Gets the periodOfflineBeforeWipeIsEnforced property value. The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped. For example, P5D indicates that the interval is 5 days in duration. A timespan value of PT0S indicates that managed data will never be wiped when the device is not connected to the internet.
        Returns: Optional[Timedelta]
        """
        return self._period_offline_before_wipe_is_enforced
    
    @period_offline_before_wipe_is_enforced.setter
    def period_offline_before_wipe_is_enforced(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the periodOfflineBeforeWipeIsEnforced property value. The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped. For example, P5D indicates that the interval is 5 days in duration. A timespan value of PT0S indicates that managed data will never be wiped when the device is not connected to the internet.
        Args:
            value: Value to set for the periodOfflineBeforeWipeIsEnforced property.
        """
        self._period_offline_before_wipe_is_enforced = value
    
    @property
    def print_blocked(self,) -> Optional[bool]:
        """
        Gets the printBlocked property value. When TRUE, indicates that printing is blocked from managed apps. When FALSE, indicates that printing is allowed from managed apps. Default value is FALSE.
        Returns: Optional[bool]
        """
        return self._print_blocked
    
    @print_blocked.setter
    def print_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the printBlocked property value. When TRUE, indicates that printing is blocked from managed apps. When FALSE, indicates that printing is allowed from managed apps. Default value is FALSE.
        Args:
            value: Value to set for the printBlocked property.
        """
        self._print_blocked = value
    
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
        writer.write_enum_value("appActionIfUnableToAuthenticateUser", self.app_action_if_unable_to_authenticate_user)
        writer.write_collection_of_object_values("apps", self.apps)
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
        writer.write_object_value("periodOfflineBeforeAccessCheck", self.period_offline_before_access_check)
        writer.write_object_value("periodOfflineBeforeWipeIsEnforced", self.period_offline_before_wipe_is_enforced)
        writer.write_bool_value("printBlocked", self.print_blocked)
    

