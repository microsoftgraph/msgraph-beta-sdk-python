from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import enrollment_state, entity, windows_autopilot_deployment_profile, windows_autopilot_device_remediation_state, windows_autopilot_profile_assignment_detailed_status, windows_autopilot_profile_assignment_status

from . import entity

class WindowsAutopilotDeviceIdentity(entity.Entity):
    """
    The windowsAutopilotDeviceIdentity resource represents a Windows Autopilot Device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new windowsAutopilotDeviceIdentity and sets the default values.
        """
        super().__init__()
        # Addressable user name.
        self._addressable_user_name: Optional[str] = None
        # AAD Device ID - to be deprecated
        self._azure_active_directory_device_id: Optional[str] = None
        # AAD Device ID
        self._azure_ad_device_id: Optional[str] = None
        # Deployment profile currently assigned to the Windows autopilot device.
        self._deployment_profile: Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile] = None
        # Profile set time of the Windows autopilot device.
        self._deployment_profile_assigned_date_time: Optional[datetime] = None
        # The deploymentProfileAssignmentDetailedStatus property
        self._deployment_profile_assignment_detailed_status: Optional[windows_autopilot_profile_assignment_detailed_status.WindowsAutopilotProfileAssignmentDetailedStatus] = None
        # The deploymentProfileAssignmentStatus property
        self._deployment_profile_assignment_status: Optional[windows_autopilot_profile_assignment_status.WindowsAutopilotProfileAssignmentStatus] = None
        # Surface Hub Device Account Password
        self._device_account_password: Optional[str] = None
        # Surface Hub Device Account Upn
        self._device_account_upn: Optional[str] = None
        # Surface Hub Device Friendly Name
        self._device_friendly_name: Optional[str] = None
        # Display Name
        self._display_name: Optional[str] = None
        # The enrollmentState property
        self._enrollment_state: Optional[enrollment_state.EnrollmentState] = None
        # Group Tag of the Windows autopilot device.
        self._group_tag: Optional[str] = None
        # Deployment profile intended to be assigned to the Windows autopilot device.
        self._intended_deployment_profile: Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile] = None
        # Intune Last Contacted Date Time of the Windows autopilot device.
        self._last_contacted_date_time: Optional[datetime] = None
        # Managed Device ID
        self._managed_device_id: Optional[str] = None
        # Oem manufacturer of the Windows autopilot device.
        self._manufacturer: Optional[str] = None
        # Model name of the Windows autopilot device.
        self._model: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Product Key of the Windows autopilot device.
        self._product_key: Optional[str] = None
        # Purchase Order Identifier of the Windows autopilot device.
        self._purchase_order_identifier: Optional[str] = None
        # Device remediation status, indicating whether or not hardware has been changed for an Autopilot-registered device.
        self._remediation_state: Optional[windows_autopilot_device_remediation_state.WindowsAutopilotDeviceRemediationState] = None
        # RemediationState set time of Autopilot device.
        self._remediation_state_last_modified_date_time: Optional[datetime] = None
        # Resource Name.
        self._resource_name: Optional[str] = None
        # Serial number of the Windows autopilot device.
        self._serial_number: Optional[str] = None
        # SKU Number
        self._sku_number: Optional[str] = None
        # System Family
        self._system_family: Optional[str] = None
        # User Principal Name.
        self._user_principal_name: Optional[str] = None
    
    @property
    def addressable_user_name(self,) -> Optional[str]:
        """
        Gets the addressableUserName property value. Addressable user name.
        Returns: Optional[str]
        """
        return self._addressable_user_name
    
    @addressable_user_name.setter
    def addressable_user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the addressableUserName property value. Addressable user name.
        Args:
            value: Value to set for the addressable_user_name property.
        """
        self._addressable_user_name = value
    
    @property
    def azure_active_directory_device_id(self,) -> Optional[str]:
        """
        Gets the azureActiveDirectoryDeviceId property value. AAD Device ID - to be deprecated
        Returns: Optional[str]
        """
        return self._azure_active_directory_device_id
    
    @azure_active_directory_device_id.setter
    def azure_active_directory_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureActiveDirectoryDeviceId property value. AAD Device ID - to be deprecated
        Args:
            value: Value to set for the azure_active_directory_device_id property.
        """
        self._azure_active_directory_device_id = value
    
    @property
    def azure_ad_device_id(self,) -> Optional[str]:
        """
        Gets the azureAdDeviceId property value. AAD Device ID
        Returns: Optional[str]
        """
        return self._azure_ad_device_id
    
    @azure_ad_device_id.setter
    def azure_ad_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureAdDeviceId property value. AAD Device ID
        Args:
            value: Value to set for the azure_ad_device_id property.
        """
        self._azure_ad_device_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsAutopilotDeviceIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsAutopilotDeviceIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsAutopilotDeviceIdentity()
    
    @property
    def deployment_profile(self,) -> Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]:
        """
        Gets the deploymentProfile property value. Deployment profile currently assigned to the Windows autopilot device.
        Returns: Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]
        """
        return self._deployment_profile
    
    @deployment_profile.setter
    def deployment_profile(self,value: Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile] = None) -> None:
        """
        Sets the deploymentProfile property value. Deployment profile currently assigned to the Windows autopilot device.
        Args:
            value: Value to set for the deployment_profile property.
        """
        self._deployment_profile = value
    
    @property
    def deployment_profile_assigned_date_time(self,) -> Optional[datetime]:
        """
        Gets the deploymentProfileAssignedDateTime property value. Profile set time of the Windows autopilot device.
        Returns: Optional[datetime]
        """
        return self._deployment_profile_assigned_date_time
    
    @deployment_profile_assigned_date_time.setter
    def deployment_profile_assigned_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deploymentProfileAssignedDateTime property value. Profile set time of the Windows autopilot device.
        Args:
            value: Value to set for the deployment_profile_assigned_date_time property.
        """
        self._deployment_profile_assigned_date_time = value
    
    @property
    def deployment_profile_assignment_detailed_status(self,) -> Optional[windows_autopilot_profile_assignment_detailed_status.WindowsAutopilotProfileAssignmentDetailedStatus]:
        """
        Gets the deploymentProfileAssignmentDetailedStatus property value. The deploymentProfileAssignmentDetailedStatus property
        Returns: Optional[windows_autopilot_profile_assignment_detailed_status.WindowsAutopilotProfileAssignmentDetailedStatus]
        """
        return self._deployment_profile_assignment_detailed_status
    
    @deployment_profile_assignment_detailed_status.setter
    def deployment_profile_assignment_detailed_status(self,value: Optional[windows_autopilot_profile_assignment_detailed_status.WindowsAutopilotProfileAssignmentDetailedStatus] = None) -> None:
        """
        Sets the deploymentProfileAssignmentDetailedStatus property value. The deploymentProfileAssignmentDetailedStatus property
        Args:
            value: Value to set for the deployment_profile_assignment_detailed_status property.
        """
        self._deployment_profile_assignment_detailed_status = value
    
    @property
    def deployment_profile_assignment_status(self,) -> Optional[windows_autopilot_profile_assignment_status.WindowsAutopilotProfileAssignmentStatus]:
        """
        Gets the deploymentProfileAssignmentStatus property value. The deploymentProfileAssignmentStatus property
        Returns: Optional[windows_autopilot_profile_assignment_status.WindowsAutopilotProfileAssignmentStatus]
        """
        return self._deployment_profile_assignment_status
    
    @deployment_profile_assignment_status.setter
    def deployment_profile_assignment_status(self,value: Optional[windows_autopilot_profile_assignment_status.WindowsAutopilotProfileAssignmentStatus] = None) -> None:
        """
        Sets the deploymentProfileAssignmentStatus property value. The deploymentProfileAssignmentStatus property
        Args:
            value: Value to set for the deployment_profile_assignment_status property.
        """
        self._deployment_profile_assignment_status = value
    
    @property
    def device_account_password(self,) -> Optional[str]:
        """
        Gets the deviceAccountPassword property value. Surface Hub Device Account Password
        Returns: Optional[str]
        """
        return self._device_account_password
    
    @device_account_password.setter
    def device_account_password(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAccountPassword property value. Surface Hub Device Account Password
        Args:
            value: Value to set for the device_account_password property.
        """
        self._device_account_password = value
    
    @property
    def device_account_upn(self,) -> Optional[str]:
        """
        Gets the deviceAccountUpn property value. Surface Hub Device Account Upn
        Returns: Optional[str]
        """
        return self._device_account_upn
    
    @device_account_upn.setter
    def device_account_upn(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceAccountUpn property value. Surface Hub Device Account Upn
        Args:
            value: Value to set for the device_account_upn property.
        """
        self._device_account_upn = value
    
    @property
    def device_friendly_name(self,) -> Optional[str]:
        """
        Gets the deviceFriendlyName property value. Surface Hub Device Friendly Name
        Returns: Optional[str]
        """
        return self._device_friendly_name
    
    @device_friendly_name.setter
    def device_friendly_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceFriendlyName property value. Surface Hub Device Friendly Name
        Args:
            value: Value to set for the device_friendly_name property.
        """
        self._device_friendly_name = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display Name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display Name
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def enrollment_state(self,) -> Optional[enrollment_state.EnrollmentState]:
        """
        Gets the enrollmentState property value. The enrollmentState property
        Returns: Optional[enrollment_state.EnrollmentState]
        """
        return self._enrollment_state
    
    @enrollment_state.setter
    def enrollment_state(self,value: Optional[enrollment_state.EnrollmentState] = None) -> None:
        """
        Sets the enrollmentState property value. The enrollmentState property
        Args:
            value: Value to set for the enrollment_state property.
        """
        self._enrollment_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import enrollment_state, entity, windows_autopilot_deployment_profile, windows_autopilot_device_remediation_state, windows_autopilot_profile_assignment_detailed_status, windows_autopilot_profile_assignment_status

        fields: Dict[str, Callable[[Any], None]] = {
            "addressableUserName": lambda n : setattr(self, 'addressable_user_name', n.get_str_value()),
            "azureActiveDirectoryDeviceId": lambda n : setattr(self, 'azure_active_directory_device_id', n.get_str_value()),
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "deploymentProfile": lambda n : setattr(self, 'deployment_profile', n.get_object_value(windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile)),
            "deploymentProfileAssignedDateTime": lambda n : setattr(self, 'deployment_profile_assigned_date_time', n.get_datetime_value()),
            "deploymentProfileAssignmentDetailedStatus": lambda n : setattr(self, 'deployment_profile_assignment_detailed_status', n.get_enum_value(windows_autopilot_profile_assignment_detailed_status.WindowsAutopilotProfileAssignmentDetailedStatus)),
            "deploymentProfileAssignmentStatus": lambda n : setattr(self, 'deployment_profile_assignment_status', n.get_enum_value(windows_autopilot_profile_assignment_status.WindowsAutopilotProfileAssignmentStatus)),
            "deviceAccountPassword": lambda n : setattr(self, 'device_account_password', n.get_str_value()),
            "deviceAccountUpn": lambda n : setattr(self, 'device_account_upn', n.get_str_value()),
            "deviceFriendlyName": lambda n : setattr(self, 'device_friendly_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "enrollmentState": lambda n : setattr(self, 'enrollment_state', n.get_enum_value(enrollment_state.EnrollmentState)),
            "groupTag": lambda n : setattr(self, 'group_tag', n.get_str_value()),
            "intendedDeploymentProfile": lambda n : setattr(self, 'intended_deployment_profile', n.get_object_value(windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile)),
            "lastContactedDateTime": lambda n : setattr(self, 'last_contacted_date_time', n.get_datetime_value()),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "productKey": lambda n : setattr(self, 'product_key', n.get_str_value()),
            "purchaseOrderIdentifier": lambda n : setattr(self, 'purchase_order_identifier', n.get_str_value()),
            "remediationState": lambda n : setattr(self, 'remediation_state', n.get_enum_value(windows_autopilot_device_remediation_state.WindowsAutopilotDeviceRemediationState)),
            "remediationStateLastModifiedDateTime": lambda n : setattr(self, 'remediation_state_last_modified_date_time', n.get_datetime_value()),
            "resourceName": lambda n : setattr(self, 'resource_name', n.get_str_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "skuNumber": lambda n : setattr(self, 'sku_number', n.get_str_value()),
            "systemFamily": lambda n : setattr(self, 'system_family', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_tag(self,) -> Optional[str]:
        """
        Gets the groupTag property value. Group Tag of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._group_tag
    
    @group_tag.setter
    def group_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the groupTag property value. Group Tag of the Windows autopilot device.
        Args:
            value: Value to set for the group_tag property.
        """
        self._group_tag = value
    
    @property
    def intended_deployment_profile(self,) -> Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]:
        """
        Gets the intendedDeploymentProfile property value. Deployment profile intended to be assigned to the Windows autopilot device.
        Returns: Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile]
        """
        return self._intended_deployment_profile
    
    @intended_deployment_profile.setter
    def intended_deployment_profile(self,value: Optional[windows_autopilot_deployment_profile.WindowsAutopilotDeploymentProfile] = None) -> None:
        """
        Sets the intendedDeploymentProfile property value. Deployment profile intended to be assigned to the Windows autopilot device.
        Args:
            value: Value to set for the intended_deployment_profile property.
        """
        self._intended_deployment_profile = value
    
    @property
    def last_contacted_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastContactedDateTime property value. Intune Last Contacted Date Time of the Windows autopilot device.
        Returns: Optional[datetime]
        """
        return self._last_contacted_date_time
    
    @last_contacted_date_time.setter
    def last_contacted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastContactedDateTime property value. Intune Last Contacted Date Time of the Windows autopilot device.
        Args:
            value: Value to set for the last_contacted_date_time property.
        """
        self._last_contacted_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Managed Device ID
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Managed Device ID
        Args:
            value: Value to set for the managed_device_id property.
        """
        self._managed_device_id = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Oem manufacturer of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Oem manufacturer of the Windows autopilot device.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model name of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model name of the Windows autopilot device.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def product_key(self,) -> Optional[str]:
        """
        Gets the productKey property value. Product Key of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._product_key
    
    @product_key.setter
    def product_key(self,value: Optional[str] = None) -> None:
        """
        Sets the productKey property value. Product Key of the Windows autopilot device.
        Args:
            value: Value to set for the product_key property.
        """
        self._product_key = value
    
    @property
    def purchase_order_identifier(self,) -> Optional[str]:
        """
        Gets the purchaseOrderIdentifier property value. Purchase Order Identifier of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._purchase_order_identifier
    
    @purchase_order_identifier.setter
    def purchase_order_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the purchaseOrderIdentifier property value. Purchase Order Identifier of the Windows autopilot device.
        Args:
            value: Value to set for the purchase_order_identifier property.
        """
        self._purchase_order_identifier = value
    
    @property
    def remediation_state(self,) -> Optional[windows_autopilot_device_remediation_state.WindowsAutopilotDeviceRemediationState]:
        """
        Gets the remediationState property value. Device remediation status, indicating whether or not hardware has been changed for an Autopilot-registered device.
        Returns: Optional[windows_autopilot_device_remediation_state.WindowsAutopilotDeviceRemediationState]
        """
        return self._remediation_state
    
    @remediation_state.setter
    def remediation_state(self,value: Optional[windows_autopilot_device_remediation_state.WindowsAutopilotDeviceRemediationState] = None) -> None:
        """
        Sets the remediationState property value. Device remediation status, indicating whether or not hardware has been changed for an Autopilot-registered device.
        Args:
            value: Value to set for the remediation_state property.
        """
        self._remediation_state = value
    
    @property
    def remediation_state_last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the remediationStateLastModifiedDateTime property value. RemediationState set time of Autopilot device.
        Returns: Optional[datetime]
        """
        return self._remediation_state_last_modified_date_time
    
    @remediation_state_last_modified_date_time.setter
    def remediation_state_last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the remediationStateLastModifiedDateTime property value. RemediationState set time of Autopilot device.
        Args:
            value: Value to set for the remediation_state_last_modified_date_time property.
        """
        self._remediation_state_last_modified_date_time = value
    
    @property
    def resource_name(self,) -> Optional[str]:
        """
        Gets the resourceName property value. Resource Name.
        Returns: Optional[str]
        """
        return self._resource_name
    
    @resource_name.setter
    def resource_name(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceName property value. Resource Name.
        Args:
            value: Value to set for the resource_name property.
        """
        self._resource_name = value
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. Serial number of the Windows autopilot device.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. Serial number of the Windows autopilot device.
        Args:
            value: Value to set for the serial_number property.
        """
        self._serial_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("addressableUserName", self.addressable_user_name)
        writer.write_str_value("azureActiveDirectoryDeviceId", self.azure_active_directory_device_id)
        writer.write_str_value("azureAdDeviceId", self.azure_ad_device_id)
        writer.write_object_value("deploymentProfile", self.deployment_profile)
        writer.write_datetime_value("deploymentProfileAssignedDateTime", self.deployment_profile_assigned_date_time)
        writer.write_enum_value("deploymentProfileAssignmentDetailedStatus", self.deployment_profile_assignment_detailed_status)
        writer.write_enum_value("deploymentProfileAssignmentStatus", self.deployment_profile_assignment_status)
        writer.write_str_value("deviceAccountPassword", self.device_account_password)
        writer.write_str_value("deviceAccountUpn", self.device_account_upn)
        writer.write_str_value("deviceFriendlyName", self.device_friendly_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("enrollmentState", self.enrollment_state)
        writer.write_str_value("groupTag", self.group_tag)
        writer.write_object_value("intendedDeploymentProfile", self.intended_deployment_profile)
        writer.write_datetime_value("lastContactedDateTime", self.last_contacted_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("productKey", self.product_key)
        writer.write_str_value("purchaseOrderIdentifier", self.purchase_order_identifier)
        writer.write_enum_value("remediationState", self.remediation_state)
        writer.write_datetime_value("remediationStateLastModifiedDateTime", self.remediation_state_last_modified_date_time)
        writer.write_str_value("resourceName", self.resource_name)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_str_value("skuNumber", self.sku_number)
        writer.write_str_value("systemFamily", self.system_family)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def sku_number(self,) -> Optional[str]:
        """
        Gets the skuNumber property value. SKU Number
        Returns: Optional[str]
        """
        return self._sku_number
    
    @sku_number.setter
    def sku_number(self,value: Optional[str] = None) -> None:
        """
        Sets the skuNumber property value. SKU Number
        Args:
            value: Value to set for the sku_number property.
        """
        self._sku_number = value
    
    @property
    def system_family(self,) -> Optional[str]:
        """
        Gets the systemFamily property value. System Family
        Returns: Optional[str]
        """
        return self._system_family
    
    @system_family.setter
    def system_family(self,value: Optional[str] = None) -> None:
        """
        Sets the systemFamily property value. System Family
        Args:
            value: Value to set for the system_family property.
        """
        self._system_family = value
    
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
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    

