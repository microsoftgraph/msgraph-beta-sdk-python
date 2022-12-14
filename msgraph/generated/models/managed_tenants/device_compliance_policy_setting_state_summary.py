from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class DeviceCompliancePolicySettingStateSummary(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    @property
    def conflict_device_count(self,) -> Optional[int]:
        """
        Gets the conflictDeviceCount property value. The number of devices in a conflict state. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._conflict_device_count
    
    @conflict_device_count.setter
    def conflict_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the conflictDeviceCount property value. The number of devices in a conflict state. Optional. Read-only.
        Args:
            value: Value to set for the conflictDeviceCount property.
        """
        self._conflict_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceCompliancePolicySettingStateSummary and sets the default values.
        """
        super().__init__()
        # The number of devices in a conflict state. Optional. Read-only.
        self._conflict_device_count: Optional[int] = None
        # The number of devices in an error state. Optional. Read-only.
        self._error_device_count: Optional[int] = None
        # The number of devices in a failed state. Optional. Read-only.
        self._failed_device_count: Optional[int] = None
        # The identifer for the Microsoft Intune account. Required. Read-only.
        self._intune_account_id: Optional[str] = None
        # The identifier for the Intune setting. Optional. Read-only.
        self._intune_setting_id: Optional[str] = None
        # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The number of devices in a not applicable state. Optional. Read-only.
        self._not_applicable_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The number of devices in a pending state. Optional. Read-only.
        self._pending_device_count: Optional[int] = None
        # The type for the device compliance policy. Optional. Read-only.
        self._policy_type: Optional[str] = None
        # The name for the setting within the device compliance policy. Optional. Read-only.
        self._setting_name: Optional[str] = None
        # The number of devices in a succeeded state. Optional. Read-only.
        self._succeeded_device_count: Optional[int] = None
        # The display name for the managed tenant. Required. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Required. Read-only.
        self._tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicySettingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicySettingStateSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicySettingStateSummary()
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. The number of devices in an error state. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. The number of devices in an error state. Optional. Read-only.
        Args:
            value: Value to set for the errorDeviceCount property.
        """
        self._error_device_count = value
    
    @property
    def failed_device_count(self,) -> Optional[int]:
        """
        Gets the failedDeviceCount property value. The number of devices in a failed state. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._failed_device_count
    
    @failed_device_count.setter
    def failed_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedDeviceCount property value. The number of devices in a failed state. Optional. Read-only.
        Args:
            value: Value to set for the failedDeviceCount property.
        """
        self._failed_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conflict_device_count": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "failed_device_count": lambda n : setattr(self, 'failed_device_count', n.get_int_value()),
            "intune_account_id": lambda n : setattr(self, 'intune_account_id', n.get_str_value()),
            "intune_setting_id": lambda n : setattr(self, 'intune_setting_id', n.get_str_value()),
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "not_applicable_device_count": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "pending_device_count": lambda n : setattr(self, 'pending_device_count', n.get_int_value()),
            "policy_type": lambda n : setattr(self, 'policy_type', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "succeeded_device_count": lambda n : setattr(self, 'succeeded_device_count', n.get_int_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def intune_account_id(self,) -> Optional[str]:
        """
        Gets the intuneAccountId property value. The identifer for the Microsoft Intune account. Required. Read-only.
        Returns: Optional[str]
        """
        return self._intune_account_id
    
    @intune_account_id.setter
    def intune_account_id(self,value: Optional[str] = None) -> None:
        """
        Sets the intuneAccountId property value. The identifer for the Microsoft Intune account. Required. Read-only.
        Args:
            value: Value to set for the intuneAccountId property.
        """
        self._intune_account_id = value
    
    @property
    def intune_setting_id(self,) -> Optional[str]:
        """
        Gets the intuneSettingId property value. The identifier for the Intune setting. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._intune_setting_id
    
    @intune_setting_id.setter
    def intune_setting_id(self,value: Optional[str] = None) -> None:
        """
        Sets the intuneSettingId property value. The identifier for the Intune setting. Optional. Read-only.
        Args:
            value: Value to set for the intuneSettingId property.
        """
        self._intune_setting_id = value
    
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
    def not_applicable_device_count(self,) -> Optional[int]:
        """
        Gets the notApplicableDeviceCount property value. The number of devices in a not applicable state. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._not_applicable_device_count
    
    @not_applicable_device_count.setter
    def not_applicable_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notApplicableDeviceCount property value. The number of devices in a not applicable state. Optional. Read-only.
        Args:
            value: Value to set for the notApplicableDeviceCount property.
        """
        self._not_applicable_device_count = value
    
    @property
    def pending_device_count(self,) -> Optional[int]:
        """
        Gets the pendingDeviceCount property value. The number of devices in a pending state. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._pending_device_count
    
    @pending_device_count.setter
    def pending_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pendingDeviceCount property value. The number of devices in a pending state. Optional. Read-only.
        Args:
            value: Value to set for the pendingDeviceCount property.
        """
        self._pending_device_count = value
    
    @property
    def policy_type(self,) -> Optional[str]:
        """
        Gets the policyType property value. The type for the device compliance policy. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._policy_type
    
    @policy_type.setter
    def policy_type(self,value: Optional[str] = None) -> None:
        """
        Sets the policyType property value. The type for the device compliance policy. Optional. Read-only.
        Args:
            value: Value to set for the policyType property.
        """
        self._policy_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("conflictDeviceCount", self.conflict_device_count)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("failedDeviceCount", self.failed_device_count)
        writer.write_str_value("intuneAccountId", self.intune_account_id)
        writer.write_str_value("intuneSettingId", self.intune_setting_id)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("notApplicableDeviceCount", self.not_applicable_device_count)
        writer.write_int_value("pendingDeviceCount", self.pending_device_count)
        writer.write_str_value("policyType", self.policy_type)
        writer.write_str_value("settingName", self.setting_name)
        writer.write_int_value("succeededDeviceCount", self.succeeded_device_count)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def setting_name(self,) -> Optional[str]:
        """
        Gets the settingName property value. The name for the setting within the device compliance policy. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._setting_name
    
    @setting_name.setter
    def setting_name(self,value: Optional[str] = None) -> None:
        """
        Sets the settingName property value. The name for the setting within the device compliance policy. Optional. Read-only.
        Args:
            value: Value to set for the settingName property.
        """
        self._setting_name = value
    
    @property
    def succeeded_device_count(self,) -> Optional[int]:
        """
        Gets the succeededDeviceCount property value. The number of devices in a succeeded state. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._succeeded_device_count
    
    @succeeded_device_count.setter
    def succeeded_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the succeededDeviceCount property value. The number of devices in a succeeded state. Optional. Read-only.
        Args:
            value: Value to set for the succeededDeviceCount property.
        """
        self._succeeded_device_count = value
    
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
    

