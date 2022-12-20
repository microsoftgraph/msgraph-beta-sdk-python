from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ManagedDeviceComplianceTrend(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def compliant_device_count(self,) -> Optional[int]:
        """
        Gets the compliantDeviceCount property value. The number of devices with a compliant status. Required. Read-only.
        Returns: Optional[int]
        """
        return self._compliant_device_count
    
    @compliant_device_count.setter
    def compliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantDeviceCount property value. The number of devices with a compliant status. Required. Read-only.
        Args:
            value: Value to set for the compliantDeviceCount property.
        """
        self._compliant_device_count = value
    
    @property
    def config_manager_device_count(self,) -> Optional[int]:
        """
        Gets the configManagerDeviceCount property value. The number of devices manged by Configuration Manager. Required. Read-only.
        Returns: Optional[int]
        """
        return self._config_manager_device_count
    
    @config_manager_device_count.setter
    def config_manager_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the configManagerDeviceCount property value. The number of devices manged by Configuration Manager. Required. Read-only.
        Args:
            value: Value to set for the configManagerDeviceCount property.
        """
        self._config_manager_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceComplianceTrend and sets the default values.
        """
        super().__init__()
        # The number of devices with a compliant status. Required. Read-only.
        self._compliant_device_count: Optional[int] = None
        # The number of devices manged by Configuration Manager. Required. Read-only.
        self._config_manager_device_count: Optional[int] = None
        # The date and time compliance snapshot was performed. Required. Read-only.
        self._count_date_time: Optional[str] = None
        # The number of devices with an error status. Required. Read-only.
        self._error_device_count: Optional[int] = None
        # The number of devices that are in a grace period status. Required. Read-only.
        self._in_grace_period_device_count: Optional[int] = None
        # The number of devices that are in a non-compliant status. Required. Read-only.
        self._noncompliant_device_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The display name for the managed tenant. Optional. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        self._tenant_id: Optional[str] = None
        # The number of devices in an unknown status. Required. Read-only.
        self._unknown_device_count: Optional[int] = None
    
    @property
    def count_date_time(self,) -> Optional[str]:
        """
        Gets the countDateTime property value. The date and time compliance snapshot was performed. Required. Read-only.
        Returns: Optional[str]
        """
        return self._count_date_time
    
    @count_date_time.setter
    def count_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the countDateTime property value. The date and time compliance snapshot was performed. Required. Read-only.
        Args:
            value: Value to set for the countDateTime property.
        """
        self._count_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceComplianceTrend:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceComplianceTrend
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceComplianceTrend()
    
    @property
    def error_device_count(self,) -> Optional[int]:
        """
        Gets the errorDeviceCount property value. The number of devices with an error status. Required. Read-only.
        Returns: Optional[int]
        """
        return self._error_device_count
    
    @error_device_count.setter
    def error_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the errorDeviceCount property value. The number of devices with an error status. Required. Read-only.
        Args:
            value: Value to set for the errorDeviceCount property.
        """
        self._error_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "config_manager_device_count": lambda n : setattr(self, 'config_manager_device_count', n.get_int_value()),
            "count_date_time": lambda n : setattr(self, 'count_date_time', n.get_str_value()),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "in_grace_period_device_count": lambda n : setattr(self, 'in_grace_period_device_count', n.get_int_value()),
            "noncompliant_device_count": lambda n : setattr(self, 'noncompliant_device_count', n.get_int_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def in_grace_period_device_count(self,) -> Optional[int]:
        """
        Gets the inGracePeriodDeviceCount property value. The number of devices that are in a grace period status. Required. Read-only.
        Returns: Optional[int]
        """
        return self._in_grace_period_device_count
    
    @in_grace_period_device_count.setter
    def in_grace_period_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the inGracePeriodDeviceCount property value. The number of devices that are in a grace period status. Required. Read-only.
        Args:
            value: Value to set for the inGracePeriodDeviceCount property.
        """
        self._in_grace_period_device_count = value
    
    @property
    def noncompliant_device_count(self,) -> Optional[int]:
        """
        Gets the noncompliantDeviceCount property value. The number of devices that are in a non-compliant status. Required. Read-only.
        Returns: Optional[int]
        """
        return self._noncompliant_device_count
    
    @noncompliant_device_count.setter
    def noncompliant_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the noncompliantDeviceCount property value. The number of devices that are in a non-compliant status. Required. Read-only.
        Args:
            value: Value to set for the noncompliantDeviceCount property.
        """
        self._noncompliant_device_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("compliantDeviceCount", self.compliant_device_count)
        writer.write_int_value("configManagerDeviceCount", self.config_manager_device_count)
        writer.write_str_value("countDateTime", self.count_date_time)
        writer.write_int_value("errorDeviceCount", self.error_device_count)
        writer.write_int_value("inGracePeriodDeviceCount", self.in_grace_period_device_count)
        writer.write_int_value("noncompliantDeviceCount", self.noncompliant_device_count)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("unknownDeviceCount", self.unknown_device_count)
    
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
    
    @property
    def unknown_device_count(self,) -> Optional[int]:
        """
        Gets the unknownDeviceCount property value. The number of devices in an unknown status. Required. Read-only.
        Returns: Optional[int]
        """
        return self._unknown_device_count
    
    @unknown_device_count.setter
    def unknown_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownDeviceCount property value. The number of devices in an unknown status. Required. Read-only.
        Args:
            value: Value to set for the unknownDeviceCount property.
        """
        self._unknown_device_count = value
    

