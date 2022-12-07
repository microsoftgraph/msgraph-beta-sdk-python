from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_permission_action = lazy_import('msgraph.generated.models.android_permission_action')
android_profile_applicability = lazy_import('msgraph.generated.models.android_profile_applicability')
managed_device_mobile_app_configuration = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration')

class AndroidManagedStoreAppConfiguration(managed_device_mobile_app_configuration.ManagedDeviceMobileAppConfiguration):
    @property
    def app_supports_oem_config(self,) -> Optional[bool]:
        """
        Gets the appSupportsOemConfig property value. Whether or not this AppConfig is an OEMConfig policy.
        Returns: Optional[bool]
        """
        return self._app_supports_oem_config
    
    @app_supports_oem_config.setter
    def app_supports_oem_config(self,value: Optional[bool] = None) -> None:
        """
        Sets the appSupportsOemConfig property value. Whether or not this AppConfig is an OEMConfig policy.
        Args:
            value: Value to set for the appSupportsOemConfig property.
        """
        self._app_supports_oem_config = value
    
    @property
    def connected_apps_enabled(self,) -> Optional[bool]:
        """
        Gets the connectedAppsEnabled property value. Setting to specify whether to allow ConnectedApps experience for this app.
        Returns: Optional[bool]
        """
        return self._connected_apps_enabled
    
    @connected_apps_enabled.setter
    def connected_apps_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the connectedAppsEnabled property value. Setting to specify whether to allow ConnectedApps experience for this app.
        Args:
            value: Value to set for the connectedAppsEnabled property.
        """
        self._connected_apps_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidManagedStoreAppConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidManagedStoreAppConfiguration"
        # Whether or not this AppConfig is an OEMConfig policy.
        self._app_supports_oem_config: Optional[bool] = None
        # Setting to specify whether to allow ConnectedApps experience for this app.
        self._connected_apps_enabled: Optional[bool] = None
        # Android Enterprise app configuration package id.
        self._package_id: Optional[str] = None
        # Android Enterprise app configuration JSON payload.
        self._payload_json: Optional[str] = None
        # List of Android app permissions and corresponding permission actions.
        self._permission_actions: Optional[List[android_permission_action.AndroidPermissionAction]] = None
        # Android profile applicability
        self._profile_applicability: Optional[android_profile_applicability.AndroidProfileApplicability] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidManagedStoreAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidManagedStoreAppConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidManagedStoreAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_supports_oem_config": lambda n : setattr(self, 'app_supports_oem_config', n.get_bool_value()),
            "connected_apps_enabled": lambda n : setattr(self, 'connected_apps_enabled', n.get_bool_value()),
            "package_id": lambda n : setattr(self, 'package_id', n.get_str_value()),
            "payload_json": lambda n : setattr(self, 'payload_json', n.get_str_value()),
            "permission_actions": lambda n : setattr(self, 'permission_actions', n.get_collection_of_object_values(android_permission_action.AndroidPermissionAction)),
            "profile_applicability": lambda n : setattr(self, 'profile_applicability', n.get_enum_value(android_profile_applicability.AndroidProfileApplicability)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def package_id(self,) -> Optional[str]:
        """
        Gets the packageId property value. Android Enterprise app configuration package id.
        Returns: Optional[str]
        """
        return self._package_id
    
    @package_id.setter
    def package_id(self,value: Optional[str] = None) -> None:
        """
        Sets the packageId property value. Android Enterprise app configuration package id.
        Args:
            value: Value to set for the packageId property.
        """
        self._package_id = value
    
    @property
    def payload_json(self,) -> Optional[str]:
        """
        Gets the payloadJson property value. Android Enterprise app configuration JSON payload.
        Returns: Optional[str]
        """
        return self._payload_json
    
    @payload_json.setter
    def payload_json(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadJson property value. Android Enterprise app configuration JSON payload.
        Args:
            value: Value to set for the payloadJson property.
        """
        self._payload_json = value
    
    @property
    def permission_actions(self,) -> Optional[List[android_permission_action.AndroidPermissionAction]]:
        """
        Gets the permissionActions property value. List of Android app permissions and corresponding permission actions.
        Returns: Optional[List[android_permission_action.AndroidPermissionAction]]
        """
        return self._permission_actions
    
    @permission_actions.setter
    def permission_actions(self,value: Optional[List[android_permission_action.AndroidPermissionAction]] = None) -> None:
        """
        Sets the permissionActions property value. List of Android app permissions and corresponding permission actions.
        Args:
            value: Value to set for the permissionActions property.
        """
        self._permission_actions = value
    
    @property
    def profile_applicability(self,) -> Optional[android_profile_applicability.AndroidProfileApplicability]:
        """
        Gets the profileApplicability property value. Android profile applicability
        Returns: Optional[android_profile_applicability.AndroidProfileApplicability]
        """
        return self._profile_applicability
    
    @profile_applicability.setter
    def profile_applicability(self,value: Optional[android_profile_applicability.AndroidProfileApplicability] = None) -> None:
        """
        Sets the profileApplicability property value. Android profile applicability
        Args:
            value: Value to set for the profileApplicability property.
        """
        self._profile_applicability = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("appSupportsOemConfig", self.app_supports_oem_config)
        writer.write_bool_value("connectedAppsEnabled", self.connected_apps_enabled)
        writer.write_str_value("packageId", self.package_id)
        writer.write_str_value("payloadJson", self.payload_json)
        writer.write_collection_of_object_values("permissionActions", self.permission_actions)
        writer.write_enum_value("profileApplicability", self.profile_applicability)
    

