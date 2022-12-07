from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
managed_app_data_encryption_type = lazy_import('msgraph.generated.models.managed_app_data_encryption_type')
managed_app_policy_deployment_summary = lazy_import('msgraph.generated.models.managed_app_policy_deployment_summary')
managed_app_remediation_action = lazy_import('msgraph.generated.models.managed_app_remediation_action')
managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')
targeted_managed_app_protection = lazy_import('msgraph.generated.models.targeted_managed_app_protection')

class IosManagedAppProtection(targeted_managed_app_protection.TargetedManagedAppProtection):
    @property
    def allowed_ios_device_models(self,) -> Optional[str]:
        """
        Gets the allowedIosDeviceModels property value. Semicolon seperated list of device models allowed, as a string, for the managed app to work.
        Returns: Optional[str]
        """
        return self._allowed_ios_device_models
    
    @allowed_ios_device_models.setter
    def allowed_ios_device_models(self,value: Optional[str] = None) -> None:
        """
        Sets the allowedIosDeviceModels property value. Semicolon seperated list of device models allowed, as a string, for the managed app to work.
        Args:
            value: Value to set for the allowedIosDeviceModels property.
        """
        self._allowed_ios_device_models = value
    
    @property
    def app_action_if_ios_device_model_not_allowed(self,) -> Optional[managed_app_remediation_action.ManagedAppRemediationAction]:
        """
        Gets the appActionIfIosDeviceModelNotAllowed property value. An admin initiated action to be applied on a managed app.
        Returns: Optional[managed_app_remediation_action.ManagedAppRemediationAction]
        """
        return self._app_action_if_ios_device_model_not_allowed
    
    @app_action_if_ios_device_model_not_allowed.setter
    def app_action_if_ios_device_model_not_allowed(self,value: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None) -> None:
        """
        Sets the appActionIfIosDeviceModelNotAllowed property value. An admin initiated action to be applied on a managed app.
        Args:
            value: Value to set for the appActionIfIosDeviceModelNotAllowed property.
        """
        self._app_action_if_ios_device_model_not_allowed = value
    
    @property
    def app_data_encryption_type(self,) -> Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType]:
        """
        Gets the appDataEncryptionType property value. Represents the level to which app data is encrypted for managed apps
        Returns: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType]
        """
        return self._app_data_encryption_type
    
    @app_data_encryption_type.setter
    def app_data_encryption_type(self,value: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType] = None) -> None:
        """
        Sets the appDataEncryptionType property value. Represents the level to which app data is encrypted for managed apps
        Args:
            value: Value to set for the appDataEncryptionType property.
        """
        self._app_data_encryption_type = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new IosManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosManagedAppProtection"
        # Semicolon seperated list of device models allowed, as a string, for the managed app to work.
        self._allowed_ios_device_models: Optional[str] = None
        # An admin initiated action to be applied on a managed app.
        self._app_action_if_ios_device_model_not_allowed: Optional[managed_app_remediation_action.ManagedAppRemediationAction] = None
        # Represents the level to which app data is encrypted for managed apps
        self._app_data_encryption_type: Optional[managed_app_data_encryption_type.ManagedAppDataEncryptionType] = None
        # List of apps to which the policy is deployed.
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
        # A custom browser protocol to open weblink on iOS.
        self._custom_browser_protocol: Optional[str] = None
        # Protocol of a custom dialer app to click-to-open a phone number on iOS, for example, skype:.
        self._custom_dialer_app_protocol: Optional[str] = None
        # Count of apps to which the current policy is deployed.
        self._deployed_app_count: Optional[int] = None
        # Navigation property to deployment summary of the configuration.
        self._deployment_summary: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None
        # Disable protection of data transferred to other apps through IOS OpenIn option. This setting is only allowed to be True when AllowedOutboundDataTransferDestinations is set to ManagedApps.
        self._disable_protection_of_managed_outbound_open_in_data: Optional[bool] = None
        # Apps in this list will be exempt from the policy and will be able to receive data from managed apps.
        self._exempted_app_protocols: Optional[List[key_value_pair.KeyValuePair]] = None
        # A list of custom urls that are allowed to invocate an unmanaged app
        self._exempted_universal_links: Optional[List[str]] = None
        # Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
        self._face_id_blocked: Optional[bool] = None
        # Defines if open-in operation is supported from the managed app to the filesharing locations selected. This setting only applies when AllowedOutboundDataTransferDestinations is set to ManagedApps and DisableProtectionOfManagedOutboundOpenInData is set to False.
        self._filter_open_in_to_only_managed_apps: Optional[bool] = None
        # A list of custom urls that are allowed to invocate a managed app
        self._managed_universal_links: Optional[List[str]] = None
        # Versions less than the specified version will block the managed app from accessing company data.
        self._minimum_required_sdk_version: Optional[str] = None
        # Versions less than the specified version will result in warning message on the managed app from accessing company data.
        self._minimum_warning_sdk_version: Optional[str] = None
        # Versions less than the specified version will block the managed app from accessing company data.
        self._minimum_wipe_sdk_version: Optional[str] = None
        # Protect incoming data from unknown source. This setting is only allowed to be True when AllowedInboundDataTransferSources is set to AllApps.
        self._protect_inbound_data_from_unknown_sources: Optional[bool] = None
        # Defines if third party keyboards are allowed while accessing a managed app
        self._third_party_keyboards_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosManagedAppProtection()
    
    @property
    def custom_browser_protocol(self,) -> Optional[str]:
        """
        Gets the customBrowserProtocol property value. A custom browser protocol to open weblink on iOS.
        Returns: Optional[str]
        """
        return self._custom_browser_protocol
    
    @custom_browser_protocol.setter
    def custom_browser_protocol(self,value: Optional[str] = None) -> None:
        """
        Sets the customBrowserProtocol property value. A custom browser protocol to open weblink on iOS.
        Args:
            value: Value to set for the customBrowserProtocol property.
        """
        self._custom_browser_protocol = value
    
    @property
    def custom_dialer_app_protocol(self,) -> Optional[str]:
        """
        Gets the customDialerAppProtocol property value. Protocol of a custom dialer app to click-to-open a phone number on iOS, for example, skype:.
        Returns: Optional[str]
        """
        return self._custom_dialer_app_protocol
    
    @custom_dialer_app_protocol.setter
    def custom_dialer_app_protocol(self,value: Optional[str] = None) -> None:
        """
        Sets the customDialerAppProtocol property value. Protocol of a custom dialer app to click-to-open a phone number on iOS, for example, skype:.
        Args:
            value: Value to set for the customDialerAppProtocol property.
        """
        self._custom_dialer_app_protocol = value
    
    @property
    def deployed_app_count(self,) -> Optional[int]:
        """
        Gets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Returns: Optional[int]
        """
        return self._deployed_app_count
    
    @deployed_app_count.setter
    def deployed_app_count(self,value: Optional[int] = None) -> None:
        """
        Sets the deployedAppCount property value. Count of apps to which the current policy is deployed.
        Args:
            value: Value to set for the deployedAppCount property.
        """
        self._deployed_app_count = value
    
    @property
    def deployment_summary(self,) -> Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]:
        """
        Gets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Returns: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary]
        """
        return self._deployment_summary
    
    @deployment_summary.setter
    def deployment_summary(self,value: Optional[managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary] = None) -> None:
        """
        Sets the deploymentSummary property value. Navigation property to deployment summary of the configuration.
        Args:
            value: Value to set for the deploymentSummary property.
        """
        self._deployment_summary = value
    
    @property
    def disable_protection_of_managed_outbound_open_in_data(self,) -> Optional[bool]:
        """
        Gets the disableProtectionOfManagedOutboundOpenInData property value. Disable protection of data transferred to other apps through IOS OpenIn option. This setting is only allowed to be True when AllowedOutboundDataTransferDestinations is set to ManagedApps.
        Returns: Optional[bool]
        """
        return self._disable_protection_of_managed_outbound_open_in_data
    
    @disable_protection_of_managed_outbound_open_in_data.setter
    def disable_protection_of_managed_outbound_open_in_data(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableProtectionOfManagedOutboundOpenInData property value. Disable protection of data transferred to other apps through IOS OpenIn option. This setting is only allowed to be True when AllowedOutboundDataTransferDestinations is set to ManagedApps.
        Args:
            value: Value to set for the disableProtectionOfManagedOutboundOpenInData property.
        """
        self._disable_protection_of_managed_outbound_open_in_data = value
    
    @property
    def exempted_app_protocols(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the exemptedAppProtocols property value. Apps in this list will be exempt from the policy and will be able to receive data from managed apps.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._exempted_app_protocols
    
    @exempted_app_protocols.setter
    def exempted_app_protocols(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the exemptedAppProtocols property value. Apps in this list will be exempt from the policy and will be able to receive data from managed apps.
        Args:
            value: Value to set for the exemptedAppProtocols property.
        """
        self._exempted_app_protocols = value
    
    @property
    def exempted_universal_links(self,) -> Optional[List[str]]:
        """
        Gets the exemptedUniversalLinks property value. A list of custom urls that are allowed to invocate an unmanaged app
        Returns: Optional[List[str]]
        """
        return self._exempted_universal_links
    
    @exempted_universal_links.setter
    def exempted_universal_links(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the exemptedUniversalLinks property value. A list of custom urls that are allowed to invocate an unmanaged app
        Args:
            value: Value to set for the exemptedUniversalLinks property.
        """
        self._exempted_universal_links = value
    
    @property
    def face_id_blocked(self,) -> Optional[bool]:
        """
        Gets the faceIdBlocked property value. Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
        Returns: Optional[bool]
        """
        return self._face_id_blocked
    
    @face_id_blocked.setter
    def face_id_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the faceIdBlocked property value. Indicates whether use of the FaceID is allowed in place of a pin if PinRequired is set to True.
        Args:
            value: Value to set for the faceIdBlocked property.
        """
        self._face_id_blocked = value
    
    @property
    def filter_open_in_to_only_managed_apps(self,) -> Optional[bool]:
        """
        Gets the filterOpenInToOnlyManagedApps property value. Defines if open-in operation is supported from the managed app to the filesharing locations selected. This setting only applies when AllowedOutboundDataTransferDestinations is set to ManagedApps and DisableProtectionOfManagedOutboundOpenInData is set to False.
        Returns: Optional[bool]
        """
        return self._filter_open_in_to_only_managed_apps
    
    @filter_open_in_to_only_managed_apps.setter
    def filter_open_in_to_only_managed_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the filterOpenInToOnlyManagedApps property value. Defines if open-in operation is supported from the managed app to the filesharing locations selected. This setting only applies when AllowedOutboundDataTransferDestinations is set to ManagedApps and DisableProtectionOfManagedOutboundOpenInData is set to False.
        Args:
            value: Value to set for the filterOpenInToOnlyManagedApps property.
        """
        self._filter_open_in_to_only_managed_apps = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_ios_device_models": lambda n : setattr(self, 'allowed_ios_device_models', n.get_str_value()),
            "app_action_if_ios_device_model_not_allowed": lambda n : setattr(self, 'app_action_if_ios_device_model_not_allowed', n.get_enum_value(managed_app_remediation_action.ManagedAppRemediationAction)),
            "app_data_encryption_type": lambda n : setattr(self, 'app_data_encryption_type', n.get_enum_value(managed_app_data_encryption_type.ManagedAppDataEncryptionType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
            "custom_browser_protocol": lambda n : setattr(self, 'custom_browser_protocol', n.get_str_value()),
            "custom_dialer_app_protocol": lambda n : setattr(self, 'custom_dialer_app_protocol', n.get_str_value()),
            "deployed_app_count": lambda n : setattr(self, 'deployed_app_count', n.get_int_value()),
            "deployment_summary": lambda n : setattr(self, 'deployment_summary', n.get_object_value(managed_app_policy_deployment_summary.ManagedAppPolicyDeploymentSummary)),
            "disable_protection_of_managed_outbound_open_in_data": lambda n : setattr(self, 'disable_protection_of_managed_outbound_open_in_data', n.get_bool_value()),
            "exempted_app_protocols": lambda n : setattr(self, 'exempted_app_protocols', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "exempted_universal_links": lambda n : setattr(self, 'exempted_universal_links', n.get_collection_of_primitive_values(str)),
            "face_id_blocked": lambda n : setattr(self, 'face_id_blocked', n.get_bool_value()),
            "filter_open_in_to_only_managed_apps": lambda n : setattr(self, 'filter_open_in_to_only_managed_apps', n.get_bool_value()),
            "managed_universal_links": lambda n : setattr(self, 'managed_universal_links', n.get_collection_of_primitive_values(str)),
            "minimum_required_sdk_version": lambda n : setattr(self, 'minimum_required_sdk_version', n.get_str_value()),
            "minimum_warning_sdk_version": lambda n : setattr(self, 'minimum_warning_sdk_version', n.get_str_value()),
            "minimum_wipe_sdk_version": lambda n : setattr(self, 'minimum_wipe_sdk_version', n.get_str_value()),
            "protect_inbound_data_from_unknown_sources": lambda n : setattr(self, 'protect_inbound_data_from_unknown_sources', n.get_bool_value()),
            "third_party_keyboards_blocked": lambda n : setattr(self, 'third_party_keyboards_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_universal_links(self,) -> Optional[List[str]]:
        """
        Gets the managedUniversalLinks property value. A list of custom urls that are allowed to invocate a managed app
        Returns: Optional[List[str]]
        """
        return self._managed_universal_links
    
    @managed_universal_links.setter
    def managed_universal_links(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the managedUniversalLinks property value. A list of custom urls that are allowed to invocate a managed app
        Args:
            value: Value to set for the managedUniversalLinks property.
        """
        self._managed_universal_links = value
    
    @property
    def minimum_required_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_required_sdk_version
    
    @minimum_required_sdk_version.setter
    def minimum_required_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Args:
            value: Value to set for the minimumRequiredSdkVersion property.
        """
        self._minimum_required_sdk_version = value
    
    @property
    def minimum_warning_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningSdkVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_warning_sdk_version
    
    @minimum_warning_sdk_version.setter
    def minimum_warning_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningSdkVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data.
        Args:
            value: Value to set for the minimumWarningSdkVersion property.
        """
        self._minimum_warning_sdk_version = value
    
    @property
    def minimum_wipe_sdk_version(self,) -> Optional[str]:
        """
        Gets the minimumWipeSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_wipe_sdk_version
    
    @minimum_wipe_sdk_version.setter
    def minimum_wipe_sdk_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWipeSdkVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Args:
            value: Value to set for the minimumWipeSdkVersion property.
        """
        self._minimum_wipe_sdk_version = value
    
    @property
    def protect_inbound_data_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the protectInboundDataFromUnknownSources property value. Protect incoming data from unknown source. This setting is only allowed to be True when AllowedInboundDataTransferSources is set to AllApps.
        Returns: Optional[bool]
        """
        return self._protect_inbound_data_from_unknown_sources
    
    @protect_inbound_data_from_unknown_sources.setter
    def protect_inbound_data_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the protectInboundDataFromUnknownSources property value. Protect incoming data from unknown source. This setting is only allowed to be True when AllowedInboundDataTransferSources is set to AllApps.
        Args:
            value: Value to set for the protectInboundDataFromUnknownSources property.
        """
        self._protect_inbound_data_from_unknown_sources = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def third_party_keyboards_blocked(self,) -> Optional[bool]:
        """
        Gets the thirdPartyKeyboardsBlocked property value. Defines if third party keyboards are allowed while accessing a managed app
        Returns: Optional[bool]
        """
        return self._third_party_keyboards_blocked
    
    @third_party_keyboards_blocked.setter
    def third_party_keyboards_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the thirdPartyKeyboardsBlocked property value. Defines if third party keyboards are allowed while accessing a managed app
        Args:
            value: Value to set for the thirdPartyKeyboardsBlocked property.
        """
        self._third_party_keyboards_blocked = value
    

