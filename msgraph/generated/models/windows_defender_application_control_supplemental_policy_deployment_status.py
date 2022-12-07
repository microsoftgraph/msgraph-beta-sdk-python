from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
windows_defender_application_control_supplemental_policy = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy')
windows_defender_application_control_supplemental_policy_statuses = lazy_import('msgraph.generated.models.windows_defender_application_control_supplemental_policy_statuses')

class WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus(entity.Entity):
    """
    Contains properties for the deployment state of a WindowsDefenderApplicationControl supplemental policy for a device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsDefenderApplicationControlSupplementalPolicyDeploymentStatus and sets the default values.
        """
        super().__init__()
        # Enum values for the various WindowsDefenderApplicationControl supplemental policy deployment statuses.
        self._deployment_status: Optional[windows_defender_application_control_supplemental_policy_statuses.WindowsDefenderApplicationControlSupplementalPolicyStatuses] = None
        # Device ID.
        self._device_id: Optional[str] = None
        # Device name.
        self._device_name: Optional[str] = None
        # Last sync date time.
        self._last_sync_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Windows OS Version Description.
        self._os_description: Optional[str] = None
        # Windows OS Version.
        self._os_version: Optional[str] = None
        # The navigation link to the WindowsDefenderApplicationControl supplemental policy.
        self._policy: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy] = None
        # Human readable version of the WindowsDefenderApplicationControl supplemental policy.
        self._policy_version: Optional[str] = None
        # The name of the user of this device.
        self._user_name: Optional[str] = None
        # User Principal Name.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsDefenderApplicationControlSupplementalPolicyDeploymentStatus()
    
    @property
    def deployment_status(self,) -> Optional[windows_defender_application_control_supplemental_policy_statuses.WindowsDefenderApplicationControlSupplementalPolicyStatuses]:
        """
        Gets the deploymentStatus property value. Enum values for the various WindowsDefenderApplicationControl supplemental policy deployment statuses.
        Returns: Optional[windows_defender_application_control_supplemental_policy_statuses.WindowsDefenderApplicationControlSupplementalPolicyStatuses]
        """
        return self._deployment_status
    
    @deployment_status.setter
    def deployment_status(self,value: Optional[windows_defender_application_control_supplemental_policy_statuses.WindowsDefenderApplicationControlSupplementalPolicyStatuses] = None) -> None:
        """
        Sets the deploymentStatus property value. Enum values for the various WindowsDefenderApplicationControl supplemental policy deployment statuses.
        Args:
            value: Value to set for the deploymentStatus property.
        """
        self._deployment_status = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Device ID.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Device ID.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name.
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deployment_status": lambda n : setattr(self, 'deployment_status', n.get_enum_value(windows_defender_application_control_supplemental_policy_statuses.WindowsDefenderApplicationControlSupplementalPolicyStatuses)),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "os_description": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy)),
            "policy_version": lambda n : setattr(self, 'policy_version', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. Last sync date time.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. Last sync date time.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def os_description(self,) -> Optional[str]:
        """
        Gets the osDescription property value. Windows OS Version Description.
        Returns: Optional[str]
        """
        return self._os_description
    
    @os_description.setter
    def os_description(self,value: Optional[str] = None) -> None:
        """
        Sets the osDescription property value. Windows OS Version Description.
        Args:
            value: Value to set for the osDescription property.
        """
        self._os_description = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Windows OS Version.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Windows OS Version.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def policy(self,) -> Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]:
        """
        Gets the policy property value. The navigation link to the WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy]
        """
        return self._policy
    
    @policy.setter
    def policy(self,value: Optional[windows_defender_application_control_supplemental_policy.WindowsDefenderApplicationControlSupplementalPolicy] = None) -> None:
        """
        Sets the policy property value. The navigation link to the WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the policy property.
        """
        self._policy = value
    
    @property
    def policy_version(self,) -> Optional[str]:
        """
        Gets the policyVersion property value. Human readable version of the WindowsDefenderApplicationControl supplemental policy.
        Returns: Optional[str]
        """
        return self._policy_version
    
    @policy_version.setter
    def policy_version(self,value: Optional[str] = None) -> None:
        """
        Sets the policyVersion property value. Human readable version of the WindowsDefenderApplicationControl supplemental policy.
        Args:
            value: Value to set for the policyVersion property.
        """
        self._policy_version = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("deploymentStatus", self.deployment_status)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyVersion", self.policy_version)
        writer.write_str_value("userName", self.user_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. The name of the user of this device.
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. The name of the user of this device.
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

