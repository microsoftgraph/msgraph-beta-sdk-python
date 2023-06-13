from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cloud_pc_connectivity_result, cloud_pc_disk_encryption_state, cloud_pc_login_result, cloud_pc_operating_system, cloud_pc_partner_agent_install_result, cloud_pc_power_state, cloud_pc_provisioning_type, cloud_pc_remote_action_result, cloud_pc_service_plan_type, cloud_pc_status, cloud_pc_status_details, cloud_pc_user_account_type, entity

from . import entity

@dataclass
class CloudPC(entity.Entity):
    # The Azure Active Directory (Azure AD) device ID of the Cloud PC.
    aad_device_id: Optional[str] = None
    # The connectivity health check result of a Cloud PC, including the updated timestamp and whether the Cloud PC can be connected.
    connectivity_result: Optional[cloud_pc_connectivity_result.CloudPcConnectivityResult] = None
    # The disk encryption applied to the Cloud PC. Possible values: notAvailable, notEncrypted, encryptedUsingPlatformManagedKey, encryptedUsingCustomerManagedKey, and unknownFutureValue.
    disk_encryption_state: Optional[cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState] = None
    # The display name of the Cloud PC.
    display_name: Optional[str] = None
    # The date and time when the grace period ends and reprovisioning/deprovisioning happens. Required only if the status is inGracePeriod. The timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    grace_period_end_date_time: Optional[datetime] = None
    # Name of the OS image that's on the Cloud PC.
    image_display_name: Optional[str] = None
    # The last login result of the Cloud PC. For example, { 'time': '2014-01-01T00:00:00Z'}.
    last_login_result: Optional[cloud_pc_login_result.CloudPcLoginResult] = None
    # The last modified date and time of the Cloud PC. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime] = None
    # The last remote action result of the enterprise Cloud PCs. The supported remote actions are: Reboot, Rename, Reprovision, Restore, and Troubleshoot.
    last_remote_action_result: Optional[cloud_pc_remote_action_result.CloudPcRemoteActionResult] = None
    # The Intune device ID of the Cloud PC.
    managed_device_id: Optional[str] = None
    # The Intune device name of the Cloud PC.
    managed_device_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Azure network connection that is applied during the provisioning of Cloud PCs.
    on_premises_connection_name: Optional[str] = None
    # The version of the operating system (OS) to provision on Cloud PCs. Possible values are: windows10, windows11, and unknownFutureValue.
    os_version: Optional[cloud_pc_operating_system.CloudPcOperatingSystem] = None
    # The results of every partner agent's installation status on Cloud PC.
    partner_agent_install_results: Optional[List[cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult]] = None
    # The powerState property
    power_state: Optional[cloud_pc_power_state.CloudPcPowerState] = None
    # The provisioning policy ID of the Cloud PC.
    provisioning_policy_id: Optional[str] = None
    # The provisioning policy that is applied during the provisioning of Cloud PCs.
    provisioning_policy_name: Optional[str] = None
    # The type of licenses to be used when provisioning Cloud PCs using this policy. Possible values are: dedicated, shared, unknownFutureValue. Default value is dedicated.
    provisioning_type: Optional[cloud_pc_provisioning_type.CloudPcProvisioningType] = None
    # The service plan ID of the Cloud PC.
    service_plan_id: Optional[str] = None
    # The service plan name of the Cloud PC.
    service_plan_name: Optional[str] = None
    # The service plan type of the Cloud PC.
    service_plan_type: Optional[cloud_pc_service_plan_type.CloudPcServicePlanType] = None
    # The status property
    status: Optional[cloud_pc_status.CloudPcStatus] = None
    # The details of the Cloud PC status.
    status_details: Optional[cloud_pc_status_details.CloudPcStatusDetails] = None
    # The account type of the user on provisioned Cloud PCs. Possible values are: standardUser, administrator, and unknownFutureValue.
    user_account_type: Optional[cloud_pc_user_account_type.CloudPcUserAccountType] = None
    # The user principal name (UPN) of the user assigned to the Cloud PC.
    user_principal_name: Optional[str] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cloud_pc_connectivity_result, cloud_pc_disk_encryption_state, cloud_pc_login_result, cloud_pc_operating_system, cloud_pc_partner_agent_install_result, cloud_pc_power_state, cloud_pc_provisioning_type, cloud_pc_remote_action_result, cloud_pc_service_plan_type, cloud_pc_status, cloud_pc_status_details, cloud_pc_user_account_type, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "aadDeviceId": lambda n : setattr(self, 'aad_device_id', n.get_str_value()),
            "connectivityResult": lambda n : setattr(self, 'connectivity_result', n.get_object_value(cloud_pc_connectivity_result.CloudPcConnectivityResult)),
            "diskEncryptionState": lambda n : setattr(self, 'disk_encryption_state', n.get_enum_value(cloud_pc_disk_encryption_state.CloudPcDiskEncryptionState)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "gracePeriodEndDateTime": lambda n : setattr(self, 'grace_period_end_date_time', n.get_datetime_value()),
            "imageDisplayName": lambda n : setattr(self, 'image_display_name', n.get_str_value()),
            "lastLoginResult": lambda n : setattr(self, 'last_login_result', n.get_object_value(cloud_pc_login_result.CloudPcLoginResult)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "lastRemoteActionResult": lambda n : setattr(self, 'last_remote_action_result', n.get_object_value(cloud_pc_remote_action_result.CloudPcRemoteActionResult)),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "onPremisesConnectionName": lambda n : setattr(self, 'on_premises_connection_name', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_enum_value(cloud_pc_operating_system.CloudPcOperatingSystem)),
            "partnerAgentInstallResults": lambda n : setattr(self, 'partner_agent_install_results', n.get_collection_of_object_values(cloud_pc_partner_agent_install_result.CloudPcPartnerAgentInstallResult)),
            "powerState": lambda n : setattr(self, 'power_state', n.get_enum_value(cloud_pc_power_state.CloudPcPowerState)),
            "provisioningPolicyId": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "provisioningPolicyName": lambda n : setattr(self, 'provisioning_policy_name', n.get_str_value()),
            "provisioningType": lambda n : setattr(self, 'provisioning_type', n.get_enum_value(cloud_pc_provisioning_type.CloudPcProvisioningType)),
            "servicePlanId": lambda n : setattr(self, 'service_plan_id', n.get_str_value()),
            "servicePlanName": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
            "servicePlanType": lambda n : setattr(self, 'service_plan_type', n.get_enum_value(cloud_pc_service_plan_type.CloudPcServicePlanType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_status.CloudPcStatus)),
            "statusDetails": lambda n : setattr(self, 'status_details', n.get_object_value(cloud_pc_status_details.CloudPcStatusDetails)),
            "userAccountType": lambda n : setattr(self, 'user_account_type', n.get_enum_value(cloud_pc_user_account_type.CloudPcUserAccountType)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("powerState", self.power_state)
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
    

