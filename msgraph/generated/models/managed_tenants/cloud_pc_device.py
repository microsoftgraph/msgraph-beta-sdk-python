from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CloudPcDevice(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def cloud_pc_status(self,) -> Optional[str]:
        """
        Gets the cloudPcStatus property value. The status of the cloud PC. Possible values are: notProvisioned, provisioning, provisioned, upgrading, inGracePeriod, deprovisioning, failed. Required. Read-only.
        Returns: Optional[str]
        """
        return self._cloud_pc_status
    
    @cloud_pc_status.setter
    def cloud_pc_status(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcStatus property value. The status of the cloud PC. Possible values are: notProvisioned, provisioning, provisioned, upgrading, inGracePeriod, deprovisioning, failed. Required. Read-only.
        Args:
            value: Value to set for the cloudPcStatus property.
        """
        self._cloud_pc_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcDevice and sets the default values.
        """
        super().__init__()
        # The status of the cloud PC. Possible values are: notProvisioned, provisioning, provisioned, upgrading, inGracePeriod, deprovisioning, failed. Required. Read-only.
        self._cloud_pc_status: Optional[str] = None
        # The specification of the cloud PC device. Required. Read-only.
        self._device_specification: Optional[str] = None
        # The display name  of the cloud PC device. Required. Read-only.
        self._display_name: Optional[str] = None
        # Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The managed device identifier of the cloud PC device. Optional. Read-only.
        self._managed_device_id: Optional[str] = None
        # The managed device display name of the cloud PC device. Optional. Read-only.
        self._managed_device_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The provisioning policy identifier for the cloud PC device. Required. Read-only.
        self._provisioning_policy_id: Optional[str] = None
        # The service plan name of the cloud PC device. Required. Read-only.
        self._service_plan_name: Optional[str] = None
        # The service plan type of the cloud PC device. Required. Read-only.
        self._service_plan_type: Optional[str] = None
        # The display name for the managed tenant. Required. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        self._tenant_id: Optional[str] = None
        # The user principal name (UPN) of the user assigned to the cloud PC device. Required. Read-only.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcDevice()
    
    @property
    def device_specification(self,) -> Optional[str]:
        """
        Gets the deviceSpecification property value. The specification of the cloud PC device. Required. Read-only.
        Returns: Optional[str]
        """
        return self._device_specification
    
    @device_specification.setter
    def device_specification(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceSpecification property value. The specification of the cloud PC device. Required. Read-only.
        Args:
            value: Value to set for the deviceSpecification property.
        """
        self._device_specification = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name  of the cloud PC device. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name  of the cloud PC device. Required. Read-only.
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
            "cloud_pc_status": lambda n : setattr(self, 'cloud_pc_status', n.get_str_value()),
            "device_specification": lambda n : setattr(self, 'device_specification', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "managed_device_name": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "provisioning_policy_id": lambda n : setattr(self, 'provisioning_policy_id', n.get_str_value()),
            "service_plan_name": lambda n : setattr(self, 'service_plan_name', n.get_str_value()),
            "service_plan_type": lambda n : setattr(self, 'service_plan_type', n.get_str_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Required. Read-only.
        Args:
            value: Value to set for the lastRefreshedDateTime property.
        """
        self._last_refreshed_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The managed device identifier of the cloud PC device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The managed device identifier of the cloud PC device. Optional. Read-only.
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. The managed device display name of the cloud PC device. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. The managed device display name of the cloud PC device. Optional. Read-only.
        Args:
            value: Value to set for the managedDeviceName property.
        """
        self._managed_device_name = value
    
    @property
    def provisioning_policy_id(self,) -> Optional[str]:
        """
        Gets the provisioningPolicyId property value. The provisioning policy identifier for the cloud PC device. Required. Read-only.
        Returns: Optional[str]
        """
        return self._provisioning_policy_id
    
    @provisioning_policy_id.setter
    def provisioning_policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the provisioningPolicyId property value. The provisioning policy identifier for the cloud PC device. Required. Read-only.
        Args:
            value: Value to set for the provisioningPolicyId property.
        """
        self._provisioning_policy_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("cloudPcStatus", self.cloud_pc_status)
        writer.write_str_value("deviceSpecification", self.device_specification)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_str_value("provisioningPolicyId", self.provisioning_policy_id)
        writer.write_str_value("servicePlanName", self.service_plan_name)
        writer.write_str_value("servicePlanType", self.service_plan_type)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def service_plan_name(self,) -> Optional[str]:
        """
        Gets the servicePlanName property value. The service plan name of the cloud PC device. Required. Read-only.
        Returns: Optional[str]
        """
        return self._service_plan_name
    
    @service_plan_name.setter
    def service_plan_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanName property value. The service plan name of the cloud PC device. Required. Read-only.
        Args:
            value: Value to set for the servicePlanName property.
        """
        self._service_plan_name = value
    
    @property
    def service_plan_type(self,) -> Optional[str]:
        """
        Gets the servicePlanType property value. The service plan type of the cloud PC device. Required. Read-only.
        Returns: Optional[str]
        """
        return self._service_plan_type
    
    @service_plan_type.setter
    def service_plan_type(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePlanType property value. The service plan type of the cloud PC device. Required. Read-only.
        Args:
            value: Value to set for the servicePlanType property.
        """
        self._service_plan_type = value
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The display name for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantDisplayName property.
        """
        self._tenant_display_name = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. The user principal name (UPN) of the user assigned to the cloud PC device. Required. Read-only.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. The user principal name (UPN) of the user assigned to the cloud PC device. Required. Read-only.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

