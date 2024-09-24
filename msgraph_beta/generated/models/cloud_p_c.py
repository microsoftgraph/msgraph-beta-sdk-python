from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_connection_setting import CloudPcConnectionSetting
    from .cloud_pc_connection_settings import CloudPcConnectionSettings
    from .cloud_pc_connectivity_result import CloudPcConnectivityResult
    from .cloud_pc_disaster_recovery_capability import CloudPcDisasterRecoveryCapability
    from .cloud_pc_disk_encryption_state import CloudPcDiskEncryptionState
    from .cloud_pc_login_result import CloudPcLoginResult
    from .cloud_pc_operating_system import CloudPcOperatingSystem
    from .cloud_pc_partner_agent_install_result import CloudPcPartnerAgentInstallResult
    from .cloud_pc_power_state import CloudPcPowerState
    from .cloud_pc_provisioning_type import CloudPcProvisioningType
    from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
    from .cloud_pc_service_plan_type import CloudPcServicePlanType
    from .cloud_pc_status import CloudPcStatus
    from .cloud_pc_status_detail import CloudPcStatusDetail
    from .cloud_pc_status_details import CloudPcStatusDetails
    from .cloud_pc_user_account_type import CloudPcUserAccountType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPC(Entity):
    # The Microsoft Entra device ID of the Cloud PC.
    aad_device_id: Optional[str] = None
    # The allotment name divides tenant licenses into smaller batches or groups that help restrict the number of licenses available for use in a specific assignment. When the provisioningType is dedicated, the allotment name is null. Read-only.
    allotment_display_name: Optional[str] = None
    # The connection setting of the Cloud PC. Possible values: enableSingleSignOn. Read Only.
    connection_setting: Optional[CloudPcConnectionSetting] = None
    # The connectionSettings property
    connection_settings: Optional[CloudPcConnectionSettings] = None
    # The connectivity health check result of a Cloud PC, including the updated timestamp and whether the Cloud PC can be connected.
    connectivity_result: Optional[CloudPcConnectivityResult] = None
    # The name of the geographical region where the Cloud PC is currently provisioned. For example, westus3, eastus2, and southeastasia. Read-only.
    device_region_name: Optional[str] = None
    # The disaster recovery status of the Cloud PC, including the primary region, secondary region, and capability type. The default value is null that indicates that the disaster recovery setting is disabled. To receive a response with the disasterRecoveryCapability property, $select and $filter it by disasterRecoveryCapability/{subProperty} in the request URL. For more information, see Example 4: List Cloud PCs filtered by disaster recovery capability type. Read-only.
    disaster_recovery_capability: Optional[CloudPcDisasterRecoveryCapability] = None
    # The disk encryption applied to the Cloud PC. Possible values: notAvailable, notEncrypted, encryptedUsingPlatformManagedKey, encryptedUsingCustomerManagedKey, and unknownFutureValue.
    disk_encryption_state: Optional[CloudPcDiskEncryptionState] = None
    # The display name of the Cloud PC.
    display_name: Optional[str] = None
    # The date and time when the grace period ends and reprovisioning or deprovisioning happens. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    grace_period_end_date_time: Optional[datetime.datetime] = None
    # Name of the OS image that's on the Cloud PC.
    image_display_name: Optional[str] = None
    # The last login result of the Cloud PC. For example, { 'time': '2014-01-01T00:00:00Z'}.
    last_login_result: Optional[CloudPcLoginResult] = None
    # The last modified date and time of the Cloud PC. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014, is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The last remote action result of the enterprise Cloud PCs. The supported remote actions are: Reboot, Rename, Reprovision, Restore, Troubleshoot.
    last_remote_action_result: Optional[CloudPcRemoteActionResult] = None
    # The Intune device ID of the Cloud PC.
    managed_device_id: Optional[str] = None
    # The Intune device name of the Cloud PC.
    managed_device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Azure network connection that is applied during the provisioning of Cloud PCs.
    on_premises_connection_name: Optional[str] = None
    # The version of the operating system (OS) to provision on Cloud PCs. Possible values are: windows10, windows11, unknownFutureValue.
    os_version: Optional[CloudPcOperatingSystem] = None
    # The results of every partner agent's installation status on Cloud PC.
    partner_agent_install_results: Optional[List[CloudPcPartnerAgentInstallResult]] = None
    # The power state of a Cloud PC. The possible values are: running, poweredOff, unknown. This property only supports shift work Cloud PCs.
    power_state: Optional[CloudPcPowerState] = None
    # The provisioning policy ID of the Cloud PC.
    provisioning_policy_id: Optional[str] = None
    # The provisioning policy that is applied during the provisioning of Cloud PCs.
    provisioning_policy_name: Optional[str] = None
    # The type of licenses to be used when provisioning Cloud PCs using this policy. Possible values are: dedicated, shared, unknownFutureValue,sharedByUser, sharedByEntraGroup. You must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: sharedByUser, sharedByEntraGroup. The default value is dedicated. CAUTION: The shared member is deprecated and will stop returning on April 30, 2027； in the future, use the sharedByUser member.
    provisioning_type: Optional[CloudPcProvisioningType] = None
    # The scopeIds property
    scope_ids: Optional[List[str]] = None
    # The service plan ID of the Cloud PC.
    service_plan_id: Optional[str] = None
    # The service plan name of the Cloud PC.
    service_plan_name: Optional[str] = None
    # The service plan type of the Cloud PC.
    service_plan_type: Optional[CloudPcServicePlanType] = None
    # The status property
    status: Optional[CloudPcStatus] = None
    # Indicates the detailed status associated with Cloud PC, including error/warning code, error/warning message, additionalInformation. For example, { 'code': 'internalServerError', 'message': 'There was an error during the Cloud PC upgrade. Please contact support.', 'additionalInformation': null }.
    status_detail: Optional[CloudPcStatusDetail] = None
    # The details of the Cloud PC status. For example, { 'code': 'internalServerError', 'message': 'There was an error during the Cloud PC upgrade. Please contact support.', 'additionalInformation': null }. This property is deprecated and will no longer be supported effective August 31, 2024. Use statusDetail instead.
    status_details: Optional[CloudPcStatusDetails] = None
    # The account type of the user on provisioned Cloud PCs. Possible values are: standardUser, administrator, unknownFutureValue.
    user_account_type: Optional[CloudPcUserAccountType] = None
    # The user principal name (UPN) of the user assigned to the Cloud PC.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPC:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPC
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPC()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_connection_setting import CloudPcConnectionSetting
        from .cloud_pc_connection_settings import CloudPcConnectionSettings
        from .cloud_pc_connectivity_result import CloudPcConnectivityResult
        from .cloud_pc_disaster_recovery_capability import CloudPcDisasterRecoveryCapability
        from .cloud_pc_disk_encryption_state import CloudPcDiskEncryptionState
        from .cloud_pc_login_result import CloudPcLoginResult
        from .cloud_pc_operating_system import CloudPcOperatingSystem
        from .cloud_pc_partner_agent_install_result import CloudPcPartnerAgentInstallResult
        from .cloud_pc_power_state import CloudPcPowerState
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
        from .cloud_pc_service_plan_type import CloudPcServicePlanType
        from .cloud_pc_status import CloudPcStatus
        from .cloud_pc_status_detail import CloudPcStatusDetail
        from .cloud_pc_status_details import CloudPcStatusDetails
        from .cloud_pc_user_account_type import CloudPcUserAccountType
        from .entity import Entity

        from .cloud_pc_connection_setting import CloudPcConnectionSetting
        from .cloud_pc_connection_settings import CloudPcConnectionSettings
        from .cloud_pc_connectivity_result import CloudPcConnectivityResult
        from .cloud_pc_disaster_recovery_capability import CloudPcDisasterRecoveryCapability
        from .cloud_pc_disk_encryption_state import CloudPcDiskEncryptionState
        from .cloud_pc_login_result import CloudPcLoginResult
        from .cloud_pc_operating_system import CloudPcOperatingSystem
        from .cloud_pc_partner_agent_install_result import CloudPcPartnerAgentInstallResult
        from .cloud_pc_power_state import CloudPcPowerState
        from .cloud_pc_provisioning_type import CloudPcProvisioningType
        from .cloud_pc_remote_action_result import CloudPcRemoteActionResult
        from .cloud_pc_service_plan_type import CloudPcServicePlanType
        from .cloud_pc_status import CloudPcStatus
        from .cloud_pc_status_detail import CloudPcStatusDetail
        from .cloud_pc_status_details import CloudPcStatusDetails
        from .cloud_pc_user_account_type import CloudPcUserAccountType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "aadDeviceId": lambda n : setattr(self, 'aad_device_id', n.get_str_value()),
            "allotmentDisplayName": lambda n : setattr(self, 'allotment_display_name', n.get_str_value()),
            "connectionSetting": lambda n : setattr(self, 'connection_setting', n.get_object_value(CloudPcConnectionSetting)),
            "connectionSettings": lambda n : setattr(self, 'connection_settings', n.get_object_value(CloudPcConnectionSettings)),
            "connectivityResult": lambda n : setattr(self, 'connectivity_result', n.get_object_value(CloudPcConnectivityResult)),
            "deviceRegionName": lambda n : setattr(self, 'device_region_name', n.get_str_value()),
            "disasterRecoveryCapability": lambda n : setattr(self, 'disaster_recovery_capability', n.get_object_value(CloudPcDisasterRecoveryCapability)),
            "diskEncryptionState": lambda n : setattr(self, 'disk_encryption_state', n.get_enum_value(CloudPcDiskEncryptionState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "gracePeriodEndDateTime": lambda n : setattr(self, 'grace_period_end_date_time', n.get_datetime_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "lastLoginResult": lambda n : setattr(self, 'last_login_result', n.get_object_value(CloudPcLoginResult)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastRemoteActionResult": lambda n : setattr(self, 'last_remote_action_result', n.get_object_value(CloudPcRemoteActionResult)),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "onPremisesConnectionName": lambda n : setattr(self, 'on_premises_connection_name', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_enum_value(CloudPcOperatingSystem)),
            "partnerAgentInstallResults": lambda n : setattr(self, 'partner_agent_install_results', n.get_collection_of_object_values(CloudPcPartnerAgentInstallResult)),
            "powerState": lambda n : setattr(self, 'power_state', n.get_enum_value(CloudPcPowerState)),
            "provisioningPolicyId": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "provisioningPolicyName": lambda n : setattr(self, 'provisioning_policy_name', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(CloudPcProvisioningType)),
            "scopeIds": lambda n : setattr(self, 'scope_ids', n.get_collection_of_primitive_values(str)),
            "servicePlanId": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
            "servicePlanName": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
            "servicePlanType": lambda n : setattr(self, 'service_plan_type', n.get_enum_value(CloudPcServicePlanType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcStatus)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_object_value(CloudPcStatusDetail)),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_object_value(CloudPcStatusDetails)),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(CloudPcUserAccountType)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("aadDeviceId", self.aad_device_id)
        writer.write_str_value("allotmentDisplayName", self.allotment_display_name)
        writer.write_object_value("connectionSetting", self.connection_setting)
        writer.write_object_value("connectionSettings", self.connection_settings)
        writer.write_object_value("connectivityResult", self.connectivity_result)
        writer.write_str_value("deviceRegionName", self.device_region_name)
        writer.write_object_value("disasterRecoveryCapability", self.disaster_recovery_capability)
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
        writer.write_enum_value("powerState", self.power_state)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_str_value("provisioningPolicyName", self.provisioning_policy_name)
        writer.write_enum_value("provisioningType", self.provisioning_type)
        writer.write_collection_of_primitive_values("scopeIds", self.scope_ids)
        writer.write_str_value("servicePlanId", self.service_plan_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_enum_value("servicePlanType", self.service_plan_type)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("statusDetail", self.status_detail)
        writer.write_object_value("statusDetails", self.status_details)
        writer.write_enum_value("userAccountType", self.user_account_type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

