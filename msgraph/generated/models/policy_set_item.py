from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_policy_policy_set_item, device_configuration_policy_set_item, device_management_configuration_policy_policy_set_item, device_management_script_policy_set_item, enrollment_restrictions_configuration_policy_set_item, entity, error_code, ios_lob_app_provisioning_configuration_policy_set_item, managed_app_protection_policy_set_item, managed_device_mobile_app_configuration_policy_set_item, mdm_windows_information_protection_policy_policy_set_item, mobile_app_policy_set_item, policy_set_status, targeted_managed_app_configuration_policy_set_item, windows10_enrollment_completion_page_configuration_policy_set_item, windows_autopilot_deployment_profile_policy_set_item

from . import entity

@dataclass
class PolicySetItem(entity.Entity):
    """
    A class containing the properties used for PolicySet Item.
    """
    # Creation time of the PolicySetItem.
    created_date_time: Optional[datetime] = None
    # DisplayName of the PolicySetItem.
    display_name: Optional[str] = None
    # The errorCode property
    error_code: Optional[error_code.ErrorCode] = None
    # Tags of the guided deployment
    guided_deployment_tags: Optional[List[str]] = None
    # policySetType of the PolicySetItem.
    item_type: Optional[str] = None
    # Last modified time of the PolicySetItem.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # PayloadId of the PolicySetItem.
    payload_id: Optional[str] = None
    # The enum to specify the status of PolicySet.
    status: Optional[policy_set_status.PolicySetStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicySetItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyPolicySetItem".casefold():
            from . import device_compliance_policy_policy_set_item

            return device_compliance_policy_policy_set_item.DeviceCompliancePolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationPolicySetItem".casefold():
            from . import device_configuration_policy_set_item

            return device_configuration_policy_set_item.DeviceConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementConfigurationPolicyPolicySetItem".casefold():
            from . import device_management_configuration_policy_policy_set_item

            return device_management_configuration_policy_policy_set_item.DeviceManagementConfigurationPolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementScriptPolicySetItem".casefold():
            from . import device_management_script_policy_set_item

            return device_management_script_policy_set_item.DeviceManagementScriptPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem".casefold():
            from . import enrollment_restrictions_configuration_policy_set_item

            return enrollment_restrictions_configuration_policy_set_item.EnrollmentRestrictionsConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem".casefold():
            from . import ios_lob_app_provisioning_configuration_policy_set_item

            return ios_lob_app_provisioning_configuration_policy_set_item.IosLobAppProvisioningConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtectionPolicySetItem".casefold():
            from . import managed_app_protection_policy_set_item

            return managed_app_protection_policy_set_item.ManagedAppProtectionPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationPolicySetItem".casefold():
            from . import managed_device_mobile_app_configuration_policy_set_item

            return managed_device_mobile_app_configuration_policy_set_item.ManagedDeviceMobileAppConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicyPolicySetItem".casefold():
            from . import mdm_windows_information_protection_policy_policy_set_item

            return mdm_windows_information_protection_policy_policy_set_item.MdmWindowsInformationProtectionPolicyPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppPolicySetItem".casefold():
            from . import mobile_app_policy_set_item

            return mobile_app_policy_set_item.MobileAppPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfigurationPolicySetItem".casefold():
            from . import targeted_managed_app_configuration_policy_set_item

            return targeted_managed_app_configuration_policy_set_item.TargetedManagedAppConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem".casefold():
            from . import windows10_enrollment_completion_page_configuration_policy_set_item

            return windows10_enrollment_completion_page_configuration_policy_set_item.Windows10EnrollmentCompletionPageConfigurationPolicySetItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfilePolicySetItem".casefold():
            from . import windows_autopilot_deployment_profile_policy_set_item

            return windows_autopilot_deployment_profile_policy_set_item.WindowsAutopilotDeploymentProfilePolicySetItem()
        return PolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_policy_policy_set_item, device_configuration_policy_set_item, device_management_configuration_policy_policy_set_item, device_management_script_policy_set_item, enrollment_restrictions_configuration_policy_set_item, entity, error_code, ios_lob_app_provisioning_configuration_policy_set_item, managed_app_protection_policy_set_item, managed_device_mobile_app_configuration_policy_set_item, mdm_windows_information_protection_policy_policy_set_item, mobile_app_policy_set_item, policy_set_status, targeted_managed_app_configuration_policy_set_item, windows10_enrollment_completion_page_configuration_policy_set_item, windows_autopilot_deployment_profile_policy_set_item

        from . import device_compliance_policy_policy_set_item, device_configuration_policy_set_item, device_management_configuration_policy_policy_set_item, device_management_script_policy_set_item, enrollment_restrictions_configuration_policy_set_item, entity, error_code, ios_lob_app_provisioning_configuration_policy_set_item, managed_app_protection_policy_set_item, managed_device_mobile_app_configuration_policy_set_item, mdm_windows_information_protection_policy_policy_set_item, mobile_app_policy_set_item, policy_set_status, targeted_managed_app_configuration_policy_set_item, windows10_enrollment_completion_page_configuration_policy_set_item, windows_autopilot_deployment_profile_policy_set_item

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(error_code.ErrorCode)),
            "guidedDeploymentTags": lambda n : setattr(self, 'guided_deployment_tags', n.get_collection_of_primitive_values(str)),
            "itemType": lambda n : setattr(self, 'item_type', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(policy_set_status.PolicySetStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_collection_of_primitive_values("guidedDeploymentTags", self.guided_deployment_tags)
        writer.write_str_value("itemType", self.item_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("status", self.status)
    

