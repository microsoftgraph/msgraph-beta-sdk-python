from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_connectivity_result = lazy_import('msgraph.generated.models.cloud_pc_connectivity_result')
cloud_pc_disk_encryption_state = lazy_import('msgraph.generated.models.cloud_pc_disk_encryption_state')
cloud_pc_login_result = lazy_import('msgraph.generated.models.cloud_pc_login_result')
cloud_pc_operating_system = lazy_import('msgraph.generated.models.cloud_pc_operating_system')
cloud_pc_partner_agent_install_result = lazy_import('msgraph.generated.models.cloud_pc_partner_agent_install_result')
cloud_pc_provisioning_type = lazy_import('msgraph.generated.models.cloud_pc_provisioning_type')
cloud_pc_remote_action_result = lazy_import('msgraph.generated.models.cloud_pc_remote_action_result')
cloud_pc_service_plan_type = lazy_import('msgraph.generated.models.cloud_pc_service_plan_type')
cloud_pc_status = lazy_import('msgraph.generated.models.cloud_pc_status')
cloud_pc_status_details = lazy_import('msgraph.generated.models.cloud_pc_status_details')
cloud_pc_user_account_type = lazy_import('msgraph.generated.models.cloud_pc_user_account_type')
entity = lazy_import('msgraph.generated.models.entity')

class CloudPC(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def aad_device_id(self,) -> Optional[str]:
        """
        Gets the aadDeviceId property value. The Azure Active Directory (Azure AD) device ID of the Cloud PC.
        Returns: Optional[str]
        """
        return self._aad_device_id
    
    @aad_device_id.setter
    def aad_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the aadDeviceId property value. The Azure Active Directory (Azure AD) device ID of the Cloud PC.
        Args:
            value: Value to set for the aadDeviceId property.
        """
        self._aad_device_id = value
    
    @property
    def connectivity_result(self,) -> Optional[cloud_pc_connectivity_result.CloudPcConnectivityResult]:
        """
        Gets the connectivityResult property value. The connectivity health check result of a Cloud PC, including the updated timestamp and whether the Cloud PC is able to be connected or not.
        Returns: Optional[cloud_pc_connectivity_result.CloudPcConnectivityResult]
        """
        return self._connectivity_result
    
    @connectivity_result.setter
    def connectivity_result(self,value: Optional[cloud_pc_connectivity_result.CloudPcConnectivityResult] = None) -> None:
        """
        Sets the connectivityResult property value. The connectivity health check result of a Cloud PC, including the updated timestamp and whether the Cloud PC is able to be connected or not.
        Args:
            value: Value to set for the connectivityResult property.
        """
        self._connectivity_result = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPC and sets the default values.
        """
        super().__init__()
        # The Azure Active Directory (Azure AD) device ID of the Cloud PC.
        self._aad_device_id: Optional[str] = None
        # The connectivity health check result of a Cloud PC, including the updated timestamp and whether the Cloud PC is able to be connected or not.
        self._connectivity_result: Optional[cloud_pc_connectivity_result.CloudPcConnectivityResult] = None
        # The diskEncryptionState property
        self._disk_encryption_state: Optional[cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState] = None
        # The display name of the Cloud PC.
        self._display_name: Optional[str] = None
        # The date and time when the grace period ends and reprovisioning/deprovisioning happens. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._grace_period_end_date_time: Optional[datetime] = None
        # Name of the OS image that's on the Cloud PC.
        self._image_display_name: Optional[str] = None
        # The last login result of the Cloud PC. For example, { 'time': '2014-01-01T00:00:00Z'}.
        self._last_login_result: Optional[cloud_pc_login_result.CloudPcLoginResult] = None
        # The last modified date and time of the Cloud PC. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_modified_date_time: Optional[datetime] = None
        # The last remote action result of the enterprise Cloud PCs. The supported remote actions are: Reboot, Rename, Reprovision, Restore, and Troubleshoot.
        self._last_remote_action_result: Optional[cloud_pc_remote_action_result.CloudPcRemoteActionResult] = None
        # The Intune device ID of the Cloud PC.
        self._managed_device_id: Optional[str] = None
        # The Intune device name of the Cloud PC.
        self._managed_device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Azure network connection that is applied during the provisioning of Cloud PCs.
        self._on_premises_connection_name: Optional[str] = None
        # The version of the operating system (OS) to provision on Cloud PCs. Possible values are: windows10, windows11, and unknownFutureValue.
        self._os_version: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None
        # The results of every partner agent's installation status on Cloud PC.
        self._partner_agent_install_results: Optional[List[cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult]] = None
        # The provisioning policy ID of the Cloud PC.
        self._provisioning_policy_id: Optional[str] = None
        # The provisioning policy that is applied during the provisioning of Cloud PCs.
        self._provisioning_policy_name: Optional[str] = None
        # The provisioningType property
        self._provisioning_type: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None
        # The service plan ID of the Cloud PC.
        self._service_plan_id: Optional[str] = None
        # The service plan name of the Cloud PC.
        self._service_plan_name: Optional[str] = None
        # The service plan type of the Cloud PC.
        self._service_plan_type: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType] = None
        # The status property
        self._status: Optional[cloud_pc_status.CloudPcStatus] = None
        # The details of the Cloud PC status.
        self._status_details: Optional[cloud_pc_status_details.CloudPcStatusDetails] = None
        # The account type of the user on provisioned Cloud PCs. Possible values are: standardUser, administrator, and unknownFutureValue.
        self._user_account_type: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None
        # The user principal name (UPN) of the user assigned to the Cloud PC.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPC:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPC
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPC()
    
    @property
    def disk_encryption_state(self,) -> Optional[cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState]:
        """
        Gets the diskEncryptionState property value. The diskEncryptionState property
        Returns: Optional[cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState]
        """
        return self._disk_encryption_state
    
    @disk_encryption_state.setter
    def disk_encryption_state(self,value: Optional[cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState] = None) -> None:
        """
        Sets the diskEncryptionState property value. The diskEncryptionState property
        Args:
            value: Value to set for the diskEncryptionState property.
        """
        self._disk_encryption_state = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the Cloud PC.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the Cloud PC.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aad_device_id": lambda n : setattr(self, 'aad_device_id', n.get_str_value()),
            "connectivity_result": lambda n : setattr(self, 'connectivity_result', n.get_object_value(cloud_pc_connectivity_result.CloudPcConnectivityResult)),
            "disk_encryption_state": lambda n : setattr(self, 'disk_encryption_state', n.get_enum_value(cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "grace_period_end_date_time": lambda n : setattr(self, 'grace_period_end_date_time', n.get_datetime_value()),
            "image_display_name": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "last_login_result": lambda n : setattr(self, 'last_login_result', n.get_object_value(cloud_pc_login_result.CloudPcLoginResult)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "last_remote_action_result": lambda n : setattr(self, 'last_remote_action_result', n.get_object_value(cloud_pc_remote_action_result.CloudPcRemoteActionResult)),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managed_device_name": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "on_premises_connection_name": lambda n : setattr(self, 'on_premises_connection_name', n.get_str_value()),
            "os_version": lambda n : setattr(self, 'os_version', n.get_enum_value(cloud_pc_operating_system.CloudPcOperatingSystem)),
            "partner_agent_install_results": lambda n : setattr(self, 'partner_agent_install_results', n.get_collection_of_object_values(cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult)),
            "provisioning_policy_id": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "provisioning_policy_name": lambda n : setattr(self, 'provisioning_policy_name', n.get_str_value()),
            "provisioning_type": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(cloud_pc_provisioning_type.CloudPcProvisioningType)),
            "service_plan_id": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
            "service_plan_name": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
            "service_plan_type": lambda n : setattr(self, 'service_plan_type', n.get_enum_value(cloud_pc_service_plan_type.CloudPcServicePlanType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_status.CloudPcStatus)),
            "status_details": lambda n : setattr(self, 'status_details', n.get_object_value(cloud_pc_status_details.CloudPcStatusDetails)),
            "user_account_type": lambda n : setattr(self, 'user_account_type', n.get_enum_value(cloud_pc_user_account_type.CloudPcUserAccountType)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def grace_period_end_date_time(self,) -> Optional[datetime]:
        """
        Gets the gracePeriodEndDateTime property value. The date and time when the grace period ends and reprovisioning/deprovisioning happens. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._grace_period_end_date_time
    
    @grace_period_end_date_time.setter
    def grace_period_end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the gracePeriodEndDateTime property value. The date and time when the grace period ends and reprovisioning/deprovisioning happens. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the gracePeriodEndDateTime property.
        """
        self._grace_period_end_date_time = value
    
    @property
    def image_display_name(self,) -> Optional[str]:
        """
        Gets the imageDisplayName property value. Name of the OS image that's on the Cloud PC.
        Returns: Optional[str]
        """
        return self._image_display_name
    
    @image_display_name.setter
    def image_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the imageDisplayName property value. Name of the OS image that's on the Cloud PC.
        Args:
            value: Value to set for the imageDisplayName property.
        """
        self._image_display_name = value
    
    @property
    def last_login_result(self,) -> Optional[cloud_pc_login_result.CloudPcLoginResult]:
        """
        Gets the lastLoginResult property value. The last login result of the Cloud PC. For example, { 'time': '2014-01-01T00:00:00Z'}.
        Returns: Optional[cloud_pc_login_result.CloudPcLoginResult]
        """
        return self._last_login_result
    
    @last_login_result.setter
    def last_login_result(self,value: Optional[cloud_pc_login_result.CloudPcLoginResult] = None) -> None:
        """
        Sets the lastLoginResult property value. The last login result of the Cloud PC. For example, { 'time': '2014-01-01T00:00:00Z'}.
        Args:
            value: Value to set for the lastLoginResult property.
        """
        self._last_login_result = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The last modified date and time of the Cloud PC. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The last modified date and time of the Cloud PC. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def last_remote_action_result(self,) -> Optional[cloud_pc_remote_action_result.CloudPcRemoteActionResult]:
        """
        Gets the lastRemoteActionResult property value. The last remote action result of the enterprise Cloud PCs. The supported remote actions are: Reboot, Rename, Reprovision, Restore, and Troubleshoot.
        Returns: Optional[cloud_pc_remote_action_result.CloudPcRemoteActionResult]
        """
        return self._last_remote_action_result
    
    @last_remote_action_result.setter
    def last_remote_action_result(self,value: Optional[cloud_pc_remote_action_result.CloudPcRemoteActionResult] = None) -> None:
        """
        Sets the lastRemoteActionResult property value. The last remote action result of the enterprise Cloud PCs. The supported remote actions are: Reboot, Rename, Reprovision, Restore, and Troubleshoot.
        Args:
            value: Value to set for the lastRemoteActionResult property.
        """
        self._last_remote_action_result = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The Intune device ID of the Cloud PC.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The Intune device ID of the Cloud PC.
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. The Intune device name of the Cloud PC.
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. The Intune device name of the Cloud PC.
        Args:
            value: Value to set for the managedDeviceName property.
        """
        self._managed_device_name = value
    
    @property
    def on_premises_connection_name(self,) -> Optional[str]:
        """
        Gets the onPremisesConnectionName property value. The Azure network connection that is applied during the provisioning of Cloud PCs.
        Returns: Optional[str]
        """
        return self._on_premises_connection_name
    
    @on_premises_connection_name.setter
    def on_premises_connection_name(self,value: Optional[str] = None) -> None:
        """
        Sets the onPremisesConnectionName property value. The Azure network connection that is applied during the provisioning of Cloud PCs.
        Args:
            value: Value to set for the onPremisesConnectionName property.
        """
        self._on_premises_connection_name = value
    
    @property
    def os_version(self,) -> Optional[cloud_pc_operating_system.CloudPcOperatingSystem]:
        """
        Gets the osVersion property value. The version of the operating system (OS) to provision on Cloud PCs. Possible values are: windows10, windows11, and unknownFutureValue.
        Returns: Optional[cloud_pc_operating_system.CloudPcOperatingSystem]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None) -> None:
        """
        Sets the osVersion property value. The version of the operating system (OS) to provision on Cloud PCs. Possible values are: windows10, windows11, and unknownFutureValue.
        Args:
            value: Value to set for the osVersion property.
        """
        self._os_version = value
    
    @property
    def partner_agent_install_results(self,) -> Optional[List[cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult]]:
        """
        Gets the partnerAgentInstallResults property value. The results of every partner agent's installation status on Cloud PC.
        Returns: Optional[List[cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult]]
        """
        return self._partner_agent_install_results
    
    @partner_agent_install_results.setter
    def partner_agent_install_results(self,value: Optional[List[cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult]] = None) -> None:
        """
        Sets the partnerAgentInstallResults property value. The results of every partner agent's installation status on Cloud PC.
        Args:
            value: Value to set for the partnerAgentInstallResults property.
        """
        self._partner_agent_install_results = value
    
    @property
    def provisioning_policy_id(self,) -> Optional[str]:
        """
        Gets the provisioningPolicyId property value. The provisioning policy ID of the Cloud PC.
        Returns: Optional[str]
        """
        return self._provisioning_policy_id
    
    @provisioning_policy_id.setter
    def provisioning_policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the provisioningPolicyId property value. The provisioning policy ID of the Cloud PC.
        Args:
            value: Value to set for the provisioningPolicyId property.
        """
        self._provisioning_policy_id = value
    
    @property
    def provisioning_policy_name(self,) -> Optional[str]:
        """
        Gets the provisioningPolicyName property value. The provisioning policy that is applied during the provisioning of Cloud PCs.
        Returns: Optional[str]
        """
        return self._provisioning_policy_name
    
    @provisioning_policy_name.setter
    def provisioning_policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the provisioningPolicyName property value. The provisioning policy that is applied during the provisioning of Cloud PCs.
        Args:
            value: Value to set for the provisioningPolicyName property.
        """
        self._provisioning_policy_name = value
    
    @property
    def provisioning_type(self,) -> Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]:
        """
        Gets the provisioningType property value. The provisioningType property
        Returns: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType]
        """
        return self._provisioning_type
    
    @provisioning_type.setter
    def provisioning_type(self,value: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None) -> None:
        """
        Sets the provisioningType property value. The provisioningType property
        Args:
            value: Value to set for the provisioningType property.
        """
        self._provisioning_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("aadDeviceId", self.aad_device_id)
        writer.write_object_value("connectivityResult", self.connectivity_result)
        writer.write_enum_value("diskEncryptionState", self.disk_encryption_state)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("gracePeriodEndDateTime", self.grace_period_end_date_time)
        writer.write_str_value("imageDisplayName", self.image_display_name)
        writer.write_object_value("lastLoginResult", self.last_login_result)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("lastRemoteActionResult", self.last_remote_action_result)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("onPremisesConnectionName", self.on_premises_connection_name)
        writer.write_enum_value("osVersion", self.os_version)
        writer.write_collection_of_object_values("partnerAgentInstallResults", self.partner_agent_install_results)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_str_value("provisioningPolicyName", self.provisioning_policy_name)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_str_value("servicePlanId", self.service_plan_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_enum_value("servicePlanType", self.service_plan_type)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("statusDetails", self.status_details)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def service_plan_id(self,) -> Optional[str]:
        """
        Gets the servicePlanId property value. The service plan ID of the Cloud PC.
        Returns: Optional[str]
        """
        return self._service_plan_id
    
    @service_plan_id.setter
    def service_plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanId property value. The service plan ID of the Cloud PC.
        Args:
            value: Value to set for the servicePlanId property.
        """
        self._service_plan_id = value
    
    @property
    def service_plan_name(self,) -> Optional[str]:
        """
        Gets the servicePlanName property value. The service plan name of the Cloud PC.
        Returns: Optional[str]
        """
        return self._service_plan_name
    
    @service_plan_name.setter
    def service_plan_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanName property value. The service plan name of the Cloud PC.
        Args:
            value: Value to set for the servicePlanName property.
        """
        self._service_plan_name = value
    
    @property
    def service_plan_type(self,) -> Optional[cloud_pc_service_plan_type.CloudPcServicePlanType]:
        """
        Gets the servicePlanType property value. The service plan type of the Cloud PC.
        Returns: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType]
        """
        return self._service_plan_type
    
    @service_plan_type.setter
    def service_plan_type(self,value: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType] = None) -> None:
        """
        Sets the servicePlanType property value. The service plan type of the Cloud PC.
        Args:
            value: Value to set for the servicePlanType property.
        """
        self._service_plan_type = value
    
    @property
    def status(self,) -> Optional[cloud_pc_status.CloudPcStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[cloud_pc_status.CloudPcStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_status.CloudPcStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def status_details(self,) -> Optional[cloud_pc_status_details.CloudPcStatusDetails]:
        """
        Gets the statusDetails property value. The details of the Cloud PC status.
        Returns: Optional[cloud_pc_status_details.CloudPcStatusDetails]
        """
        return self._status_details
    
    @status_details.setter
    def status_details(self,value: Optional[cloud_pc_status_details.CloudPcStatusDetails] = None) -> None:
        """
        Sets the statusDetails property value. The details of the Cloud PC status.
        Args:
            value: Value to set for the statusDetails property.
        """
        self._status_details = value
    
    @property
    def user_account_type(self,) -> Optional[cloud_pc_user_account_type.CloudPcUserAccountType]:
        """
        Gets the userAccountType property value. The account type of the user on provisioned Cloud PCs. Possible values are: standardUser, administrator, and unknownFutureValue.
        Returns: Optional[cloud_pc_user_account_type.CloudPcUserAccountType]
        """
        return self._user_account_type
    
    @user_account_type.setter
    def user_account_type(self,value: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None) -> None:
        """
        Sets the userAccountType property value. The account type of the user on provisioned Cloud PCs. Possible values are: standardUser, administrator, and unknownFutureValue.
        Args:
            value: Value to set for the userAccountType property.
        """
        self._user_account_type = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user assigned to the Cloud PC.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user assigned to the Cloud PC.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

