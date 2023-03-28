from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_policy_policy_set_item, device_configuration_policy_set_item, device_management_configuration_policy_policy_set_item, device_management_script_policy_set_item, enrollment_restrictions_configuration_policy_set_item, entity, error_code, ios_lob_app_provisioning_configuration_policy_set_item, managed_app_protection_policy_set_item, managed_device_mobile_app_configuration_policy_set_item, mdm_windows_information_protection_policy_policy_set_item, mobile_app_policy_set_item, policy_set_status, targeted_managed_app_configuration_policy_set_item, windows10_enrollment_completion_page_configuration_policy_set_item, windows_autopilot_deployment_profile_policy_set_item

from . import entity

class PolicySetItem(entity.Entity):
    """
    A class containing the properties used for PolicySet Item.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new policySetItem and sets the default values.
        """
        super().__init__()
        # Creation time of the PolicySetItem.
        self._created_date_time: Optional[datetime] = None
        # DisplayName of the PolicySetItem.
        self._display_name: Optional[str] = None
        # The errorCode property
        self._error_code: Optional[error_code.ErrorCode] = None
        # Tags of the guided deployment
        self._guided_deployment_tags: Optional[List[str]] = None
        # policySetType of the PolicySetItem.
        self._item_type: Optional[str] = None
        # Last modified time of the PolicySetItem.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # PayloadId of the PolicySetItem.
        self._payload_id: Optional[str] = None
        # The enum to specify the status of PolicySet.
        self._status: Optional[policy_set_status.PolicySetStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Creation time of the PolicySetItem.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Creation time of the PolicySetItem.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicySetItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceCompliancePolicyPolicySetItem":
                from . import device_compliance_policy_policy_set_item

                return device_compliance_policy_policy_set_item.DeviceCompliancePolicyPolicySetItem()
            if mapping_value == "#microsoft.graph.deviceConfigurationPolicySetItem":
                from . import device_configuration_policy_set_item

                return device_configuration_policy_set_item.DeviceConfigurationPolicySetItem()
            if mapping_value == "#microsoft.graph.deviceManagementConfigurationPolicyPolicySetItem":
                from . import device_management_configuration_policy_policy_set_item

                return device_management_configuration_policy_policy_set_item.DeviceManagementConfigurationPolicyPolicySetItem()
            if mapping_value == "#microsoft.graph.deviceManagementScriptPolicySetItem":
                from . import device_management_script_policy_set_item

                return device_management_script_policy_set_item.DeviceManagementScriptPolicySetItem()
            if mapping_value == "#microsoft.graph.enrollmentRestrictionsConfigurationPolicySetItem":
                from . import enrollment_restrictions_configuration_policy_set_item

                return enrollment_restrictions_configuration_policy_set_item.EnrollmentRestrictionsConfigurationPolicySetItem()
            if mapping_value == "#microsoft.graph.iosLobAppProvisioningConfigurationPolicySetItem":
                from . import ios_lob_app_provisioning_configuration_policy_set_item

                return ios_lob_app_provisioning_configuration_policy_set_item.IosLobAppProvisioningConfigurationPolicySetItem()
            if mapping_value == "#microsoft.graph.managedAppProtectionPolicySetItem":
                from . import managed_app_protection_policy_set_item

                return managed_app_protection_policy_set_item.ManagedAppProtectionPolicySetItem()
            if mapping_value == "#microsoft.graph.managedDeviceMobileAppConfigurationPolicySetItem":
                from . import managed_device_mobile_app_configuration_policy_set_item

                return managed_device_mobile_app_configuration_policy_set_item.ManagedDeviceMobileAppConfigurationPolicySetItem()
            if mapping_value == "#microsoft.graph.mdmWindowsInformationProtectionPolicyPolicySetItem":
                from . import mdm_windows_information_protection_policy_policy_set_item

                return mdm_windows_information_protection_policy_policy_set_item.MdmWindowsInformationProtectionPolicyPolicySetItem()
            if mapping_value == "#microsoft.graph.mobileAppPolicySetItem":
                from . import mobile_app_policy_set_item

                return mobile_app_policy_set_item.MobileAppPolicySetItem()
            if mapping_value == "#microsoft.graph.targetedManagedAppConfigurationPolicySetItem":
                from . import targeted_managed_app_configuration_policy_set_item

                return targeted_managed_app_configuration_policy_set_item.TargetedManagedAppConfigurationPolicySetItem()
            if mapping_value == "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem":
                from . import windows10_enrollment_completion_page_configuration_policy_set_item

                return windows10_enrollment_completion_page_configuration_policy_set_item.Windows10EnrollmentCompletionPageConfigurationPolicySetItem()
            if mapping_value == "#microsoft.graph.windowsAutopilotDeploymentProfilePolicySetItem":
                from . import windows_autopilot_deployment_profile_policy_set_item

                return windows_autopilot_deployment_profile_policy_set_item.WindowsAutopilotDeploymentProfilePolicySetItem()
        return PolicySetItem()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. DisplayName of the PolicySetItem.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. DisplayName of the PolicySetItem.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def error_code(self,) -> Optional[error_code.ErrorCode]:
        """
        Gets the errorCode property value. The errorCode property
        Returns: Optional[error_code.ErrorCode]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[error_code.ErrorCode] = None) -> None:
        """
        Sets the errorCode property value. The errorCode property
        Args:
            value: Value to set for the error_code property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def guided_deployment_tags(self,) -> Optional[List[str]]:
        """
        Gets the guidedDeploymentTags property value. Tags of the guided deployment
        Returns: Optional[List[str]]
        """
        return self._guided_deployment_tags
    
    @guided_deployment_tags.setter
    def guided_deployment_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the guidedDeploymentTags property value. Tags of the guided deployment
        Args:
            value: Value to set for the guided_deployment_tags property.
        """
        self._guided_deployment_tags = value
    
    @property
    def item_type(self,) -> Optional[str]:
        """
        Gets the itemType property value. policySetType of the PolicySetItem.
        Returns: Optional[str]
        """
        return self._item_type
    
    @item_type.setter
    def item_type(self,value: Optional[str] = None) -> None:
        """
        Sets the itemType property value. policySetType of the PolicySetItem.
        Args:
            value: Value to set for the item_type property.
        """
        self._item_type = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified time of the PolicySetItem.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified time of the PolicySetItem.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def payload_id(self,) -> Optional[str]:
        """
        Gets the payloadId property value. PayloadId of the PolicySetItem.
        Returns: Optional[str]
        """
        return self._payload_id
    
    @payload_id.setter
    def payload_id(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadId property value. PayloadId of the PolicySetItem.
        Args:
            value: Value to set for the payload_id property.
        """
        self._payload_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_collection_of_primitive_values("guidedDeploymentTags", self.guided_deployment_tags)
        writer.write_str_value("itemType", self.item_type)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[policy_set_status.PolicySetStatus]:
        """
        Gets the status property value. The enum to specify the status of PolicySet.
        Returns: Optional[policy_set_status.PolicySetStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[policy_set_status.PolicySetStatus] = None) -> None:
        """
        Sets the status property value. The enum to specify the status of PolicySet.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

