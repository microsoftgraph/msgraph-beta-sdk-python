from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AggregatedPolicyCompliance(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def compliance_policy_id(self,) -> Optional[str]:
        """
        Gets the compliancePolicyId property value. Identifier for the device compliance policy. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._compliance_policy_id
    
    @compliance_policy_id.setter
    def compliance_policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the compliancePolicyId property value. Identifier for the device compliance policy. Optional. Read-only.
        Args:
            value: Value to set for the compliancePolicyId property.
        """
        self._compliance_policy_id = value
    
    @property
    def compliance_policy_name(self,) -> Optional[str]:
        """
        Gets the compliancePolicyName property value. Name of the device compliance policy. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._compliance_policy_name
    
    @compliance_policy_name.setter
    def compliance_policy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the compliancePolicyName property value. Name of the device compliance policy. Optional. Read-only.
        Args:
            value: Value to set for the compliancePolicyName property.
        """
        self._compliance_policy_name = value
    
    @property
    def compliance_policy_platform(self,) -> Optional[str]:
        """
        Gets the compliancePolicyPlatform property value. Platform for the device compliance policy. Possible values are: android, androidForWork, iOS, macOS, windowsPhone81, windows81AndLater, windows10AndLater, androidWorkProfile, androidAOSP, all. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._compliance_policy_platform
    
    @compliance_policy_platform.setter
    def compliance_policy_platform(self,value: Optional[str] = None) -> None:
        """
        Sets the compliancePolicyPlatform property value. Platform for the device compliance policy. Possible values are: android, androidForWork, iOS, macOS, windowsPhone81, windows81AndLater, windows10AndLater, androidWorkProfile, androidAOSP, all. Optional. Read-only.
        Args:
            value: Value to set for the compliancePolicyPlatform property.
        """
        self._compliance_policy_platform = value
    
    @property
    def compliance_policy_type(self,) -> Optional[str]:
        """
        Gets the compliancePolicyType property value. The type of compliance policy. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._compliance_policy_type
    
    @compliance_policy_type.setter
    def compliance_policy_type(self,value: Optional[str] = None) -> None:
        """
        Sets the compliancePolicyType property value. The type of compliance policy. Optional. Read-only.
        Args:
            value: Value to set for the compliancePolicyType property.
        """
        self._compliance_policy_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new aggregatedPolicyCompliance and sets the default values.
        """
        super().__init__()
        # Identifier for the device compliance policy. Optional. Read-only.
        self._compliance_policy_id: Optional[str] = None
        # Name of the device compliance policy. Optional. Read-only.
        self._compliance_policy_name: Optional[str] = None
        # Platform for the device compliance policy. Possible values are: android, androidForWork, iOS, macOS, windowsPhone81, windows81AndLater, windows10AndLater, androidWorkProfile, androidAOSP, all. Optional. Read-only.
        self._compliance_policy_platform: Optional[str] = None
        # The type of compliance policy. Optional. Read-only.
        self._compliance_policy_type: Optional[str] = None
        # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The number of devices that are in a compliant status. Optional. Read-only.
        self._number_of_compliant_devices: Optional[int] = None
        # The number of devices that are in an error status. Optional. Read-only.
        self._number_of_error_devices: Optional[int] = None
        # The number of device that are in a non-compliant status. Optional. Read-only.
        self._number_of_non_compliant_devices: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The date and time the device policy was last modified. Optional. Read-only.
        self._policy_modified_date_time: Optional[datetime] = None
        # The display name for the managed tenant. Optional. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AggregatedPolicyCompliance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AggregatedPolicyCompliance
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AggregatedPolicyCompliance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_policy_id": lambda n : setattr(self, 'compliance_policy_id', n.get_str_value()),
            "compliance_policy_name": lambda n : setattr(self, 'compliance_policy_name', n.get_str_value()),
            "compliance_policy_platform": lambda n : setattr(self, 'compliance_policy_platform', n.get_str_value()),
            "compliance_policy_type": lambda n : setattr(self, 'compliance_policy_type', n.get_str_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "number_of_compliant_devices": lambda n : setattr(self, 'number_of_compliant_devices', n.get_int_value()),
            "number_of_error_devices": lambda n : setattr(self, 'number_of_error_devices', n.get_int_value()),
            "number_of_non_compliant_devices": lambda n : setattr(self, 'number_of_non_compliant_devices', n.get_int_value()),
            "policy_modified_date_time": lambda n : setattr(self, 'policy_modified_date_time', n.get_datetime_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refreshed_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_refreshed_date_time
    
    @last_refreshed_date_time.setter
    def last_refreshed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshedDateTime property value. Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        Args:
            value: Value to set for the lastRefreshedDateTime property.
        """
        self._last_refreshed_date_time = value
    
    @property
    def number_of_compliant_devices(self,) -> Optional[int]:
        """
        Gets the numberOfCompliantDevices property value. The number of devices that are in a compliant status. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_compliant_devices
    
    @number_of_compliant_devices.setter
    def number_of_compliant_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCompliantDevices property value. The number of devices that are in a compliant status. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCompliantDevices property.
        """
        self._number_of_compliant_devices = value
    
    @property
    def number_of_error_devices(self,) -> Optional[int]:
        """
        Gets the numberOfErrorDevices property value. The number of devices that are in an error status. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_error_devices
    
    @number_of_error_devices.setter
    def number_of_error_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfErrorDevices property value. The number of devices that are in an error status. Optional. Read-only.
        Args:
            value: Value to set for the numberOfErrorDevices property.
        """
        self._number_of_error_devices = value
    
    @property
    def number_of_non_compliant_devices(self,) -> Optional[int]:
        """
        Gets the numberOfNonCompliantDevices property value. The number of device that are in a non-compliant status. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_non_compliant_devices
    
    @number_of_non_compliant_devices.setter
    def number_of_non_compliant_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfNonCompliantDevices property value. The number of device that are in a non-compliant status. Optional. Read-only.
        Args:
            value: Value to set for the numberOfNonCompliantDevices property.
        """
        self._number_of_non_compliant_devices = value
    
    @property
    def policy_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the policyModifiedDateTime property value. The date and time the device policy was last modified. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._policy_modified_date_time
    
    @policy_modified_date_time.setter
    def policy_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the policyModifiedDateTime property value. The date and time the device policy was last modified. Optional. Read-only.
        Args:
            value: Value to set for the policyModifiedDateTime property.
        """
        self._policy_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("compliancePolicyId", self.compliance_policy_id)
        writer.write_str_value("compliancePolicyName", self.compliance_policy_name)
        writer.write_str_value("compliancePolicyPlatform", self.compliance_policy_platform)
        writer.write_str_value("compliancePolicyType", self.compliance_policy_type)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("numberOfCompliantDevices", self.number_of_compliant_devices)
        writer.write_int_value("numberOfErrorDevices", self.number_of_error_devices)
        writer.write_int_value("numberOfNonCompliantDevices", self.number_of_non_compliant_devices)
        writer.write_datetime_value("policyModifiedDateTime", self.policy_modified_date_time)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def tenant_display_name(self,) -> Optional[str]:
        """
        Gets the tenantDisplayName property value. The display name for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_display_name
    
    @tenant_display_name.setter
    def tenant_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantDisplayName property value. The display name for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenantDisplayName property.
        """
        self._tenant_display_name = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

