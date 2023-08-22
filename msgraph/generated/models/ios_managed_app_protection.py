from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair
    from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_remediation_action import ManagedAppRemediationAction
    from .managed_mobile_app import ManagedMobileApp
    from .targeted_managed_app_protection import TargetedManagedAppProtection

from .targeted_managed_app_protection import TargetedManagedAppProtection

@dataclass
class IosManagedAppProtection(TargetedManagedAppProtection):
    """
    Policy used to configure detailed management settings targeted to specific security groups and for a specified set of apps on an iOS device
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosManagedAppProtection"
    # Semicolon seperated list of device models allowed, as a string, for the managed app to work.
    allowed_ios_device_models: Optional[str] = None
    # An admin initiated action to be applied on a managed app.
    app_action_if_ios_device_model_not_allowed: Optional[ManagedAppRemediationAction] = None
    # Represents the level to which app data is encrypted for managed apps
    app_data_encryption_type: Optional[ManagedAppDataEncryptionType] = None
    # List of apps to which the policy is deployed.
    apps: Optional[List[ManagedMobileApp]] = None
    # A custom browser protocol to open weblink on iOS.
    custom_browser_protocol: Optional[str] = None
    # Protocol of a custom dialer app to click-to-open a phone number on iOS, for example, skype:.
    custom_dialer_app_protocol: Optional[str] = None
    # Count of apps to which the current policy is deployed.
    deployed_app_count: Optional[int] = None
    # Navigation property to deployment summary of the configuration.
    deployment_summary: Optional[ManagedAppPolicyDeploymentSummary] = None
    # Disable protection of data transferred to other apps through IOS OpenIn option. This setting is only allowed to be True when AllowedOutboundDataTransferDestinations is set to ManagedApps.
    disable_protection_of_managed_outbound_open_in_data: Optional[bool] = None
    # Apps in this list will be exempt from the policy and will be able to receive data from managed apps.
    exempted_app_protocols: Optional[List[KeyValuePair]] = None
    # A list of custom urls that are allowed to invocate an unmanaged app
    exempted_universal_links: Optional[List[str]] = None
    # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
    face_id_blocked: Optional[bool] = None
    # Defines if open-in operation is supported from the managed app to the filesharing locations selected. This setting only applies when AllowedOutboundDataTransferDestinations is set to ManagedApps and DisableProtectionOfManagedOutboundOpenInData is set to False.
    filter_open_in_to_only_managed_apps: Optional[bool] = None
    # A list of custom urls that are allowed to invocate a managed app
    managed_universal_links: Optional[List[str]] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_required_sdk_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data.
    minimum_warning_sdk_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_wipe_sdk_version: Optional[str] = None
    # Protect incoming data from unknown source. This setting is only allowed to be True when AllowedInboundDataTransferSources is set to AllApps.
    protect_inbound_data_from_unknown_sources: Optional[bool] = None
    # Defines if third party keyboards are allowed while accessing a managed app
    third_party_keyboards_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosManagedAppProtection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosManagedAppProtection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .key_value_pair import KeyValuePair
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_remediation_action import ManagedAppRemediationAction
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        from .key_value_pair import KeyValuePair
        from .managed_app_data_encryption_type import ManagedAppDataEncryptionType
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_remediation_action import ManagedAppRemediationAction
        from .managed_mobile_app import ManagedMobileApp
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedIosDeviceModels": lambda n : setattr(self, 'allowed_ios_device_models', n.get_str_value()),
            "appActionIfIosDeviceModelNotAllowed": lambda n : setattr(self, 'app_action_if_ios_device_model_not_allowed', n.get_enum_value(ManagedAppRemediationAction)),
            "appDataEncryptionType": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(ManagedMobileApp)),
            "customBrowserProtocol": lambda n : setattr(self, 'custom_browser_protocol', n.get_str_value()),
            "customDialerAppProtocol": lambda n : setattr(self, 'custom_dialer_app_protocol', n.get_str_value()),
            "deployedAppCount": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deploymentSummary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(ManagedAppPolicyDeploymentSummary)),
            "disableProtectionOfManagedOutboundOpenInData": lambda n : setattr(self, 'disable_protection_of_managed_outbound_open_in_data', n.get_bool_value()),
            "exemptedAppProtocols": lambda n : setattr(self, 'exempted_app_protocols', n.get_collection_of_object_values(KeyValuePair)),
            "exemptedUniversalLinks": lambda n : setattr(self, 'exempted_universal_links', n.get_collection_of_primitive_values(str)),
            "faceIdBlocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "filterOpenInToOnlyManagedApps": lambda n : setattr(self, 'filter_open_in_to_only_managed_apps', n.get_bool_value()),
            "managedUniversalLinks": lambda n : setattr(self, 'managed_universal_links', n.get_collection_of_primitive_values(str)),
            "minimumRequiredSdkVersion": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimumWarningSdkVersion": lambda n : setattr(self, 'minimum_warning_sdk_version', n.get_str_value()),
            "minimumWipeSdkVersion": lambda n : setattr(self, 'minimum_wipe_sdk_version', n.get_str_value()),
            "protectInboundDataFromUnknownSources": lambda n : setattr(self, 'protect_inbound_data_from_unknown_sources', n.get_bool_value()),
            "thirdPartyKeyboardsBlocked": lambda n : setattr(self, 'third_party_keyboards_blocked', n.get_bool_value()),
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
        writer.write_str_value("allowedIosDeviceModels", self.allowed_ios_device_models)
        writer.write_enum_value("appActionIfIosDeviceModelNotAllowed", self.app_action_if_ios_device_model_not_allowed)
        writer.write_enum_value("appDataEncryptionType", self.app_data_encryption_type)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_str_value("customBrowserProtocol", self.custom_browser_protocol)
        writer.write_str_value("customDialerAppProtocol", self.custom_dialer_app_protocol)
        writer.write_int_value("deployedAppCount", self.deployed_app_count)
        writer.write_object_value("deploymentSummary", self.deployment_summary)
        writer.write_bool_value("disableProtectionOfManagedOutboundOpenInData", self.disable_protection_of_managed_outbound_open_in_data)
        writer.write_collection_of_object_values("exemptedAppProtocols", self.exempted_app_protocols)
        writer.write_collection_of_primitive_values("exemptedUniversalLinks", self.exempted_universal_links)
        writer.write_bool_value("faceIdBlocked", self.face_id_blocked)
        writer.write_bool_value("filterOpenInToOnlyManagedApps", self.filter_open_in_to_only_managed_apps)
        writer.write_collection_of_primitive_values("managedUniversalLinks", self.managed_universal_links)
        writer.write_str_value("minimumRequiredSdkVersion", self.minimum_required_sdk_version)
        writer.write_str_value("minimumWarningSdkVersion", self.minimum_warning_sdk_version)
        writer.write_str_value("minimumWipeSdkVersion", self.minimum_wipe_sdk_version)
        writer.write_bool_value("protectInboundDataFromUnknownSources", self.protect_inbound_data_from_unknown_sources)
        writer.write_bool_value("thirdPartyKeyboardsBlocked", self.third_party_keyboards_blocked)
    

