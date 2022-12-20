from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class CloudPcOverview(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcOverview and sets the default values.
        """
        super().__init__()
        # Date and time the entity was last updated in the multi-tenant management platform. Optional. Read-only.
        self._last_refreshed_date_time: Optional[datetime] = None
        # The number of cloud PC connections that have a status of failed. Optional. Read-only.
        self._number_of_cloud_pc_connection_status_failed: Optional[int] = None
        # The number of cloud PC connections that have a status of passed. Optional. Read-only.
        self._number_of_cloud_pc_connection_status_passed: Optional[int] = None
        # The number of cloud PC connections that have a status of pending. Optional. Read-only.
        self._number_of_cloud_pc_connection_status_pending: Optional[int] = None
        # The number of cloud PC connections that have a status of running. Optional. Read-only.
        self._number_of_cloud_pc_connection_status_running: Optional[int] = None
        # The number of cloud PC connections that have a status of unknownFutureValue. Optional. Read-only.
        self._number_of_cloud_pc_connection_status_unkown_future_value: Optional[int] = None
        # The number of cloud PCs that have a status of deprovisioning. Optional. Read-only.
        self._number_of_cloud_pc_status_deprovisioning: Optional[int] = None
        # The number of cloud PCs that have a status of failed. Optional. Read-only.
        self._number_of_cloud_pc_status_failed: Optional[int] = None
        # The number of cloud PCs that have a status of inGracePeriod. Optional. Read-only.
        self._number_of_cloud_pc_status_in_grace_period: Optional[int] = None
        # The number of cloud PCs that have a status of notProvisioned. Optional. Read-only.
        self._number_of_cloud_pc_status_not_provisioned: Optional[int] = None
        # The number of cloud PCs that have a status of provisioned. Optional. Read-only.
        self._number_of_cloud_pc_status_provisioned: Optional[int] = None
        # The number of cloud PCs that have a status of provisioning. Optional. Read-only.
        self._number_of_cloud_pc_status_provisioning: Optional[int] = None
        # The number of cloud PCs that have a status of unknown. Optional. Read-only.
        self._number_of_cloud_pc_status_unknown: Optional[int] = None
        # The number of cloud PCs that have a status of upgrading. Optional. Read-only.
        self._number_of_cloud_pc_status_upgrading: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The display name for the managed tenant. Optional. Read-only.
        self._tenant_display_name: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The total number of cloud PC devices that have the Business SKU. Optional. Read-only.
        self._total_business_licenses: Optional[int] = None
        # The total number of cloud PC connection statuses for the given managed tenant. Optional. Read-only.
        self._total_cloud_pc_connection_status: Optional[int] = None
        # The total number of cloud PC statues for the given managed tenant. Optional. Read-only.
        self._total_cloud_pc_status: Optional[int] = None
        # The total number of cloud PC devices that have the Enterprise SKU. Optional. Read-only.
        self._total_enterprise_licenses: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcOverview()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "last_refreshed_date_time": lambda n : setattr(self, 'last_refreshed_date_time', n.get_datetime_value()),
            "number_of_cloud_pc_connection_status_failed": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_failed', n.get_int_value()),
            "number_of_cloud_pc_connection_status_passed": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_passed', n.get_int_value()),
            "number_of_cloud_pc_connection_status_pending": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_pending', n.get_int_value()),
            "number_of_cloud_pc_connection_status_running": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_running', n.get_int_value()),
            "number_of_cloud_pc_connection_status_unkown_future_value": lambda n : setattr(self, 'number_of_cloud_pc_connection_status_unkown_future_value', n.get_int_value()),
            "number_of_cloud_pc_status_deprovisioning": lambda n : setattr(self, 'number_of_cloud_pc_status_deprovisioning', n.get_int_value()),
            "number_of_cloud_pc_status_failed": lambda n : setattr(self, 'number_of_cloud_pc_status_failed', n.get_int_value()),
            "number_of_cloud_pc_status_in_grace_period": lambda n : setattr(self, 'number_of_cloud_pc_status_in_grace_period', n.get_int_value()),
            "number_of_cloud_pc_status_not_provisioned": lambda n : setattr(self, 'number_of_cloud_pc_status_not_provisioned', n.get_int_value()),
            "number_of_cloud_pc_status_provisioned": lambda n : setattr(self, 'number_of_cloud_pc_status_provisioned', n.get_int_value()),
            "number_of_cloud_pc_status_provisioning": lambda n : setattr(self, 'number_of_cloud_pc_status_provisioning', n.get_int_value()),
            "number_of_cloud_pc_status_unknown": lambda n : setattr(self, 'number_of_cloud_pc_status_unknown', n.get_int_value()),
            "number_of_cloud_pc_status_upgrading": lambda n : setattr(self, 'number_of_cloud_pc_status_upgrading', n.get_int_value()),
            "tenant_display_name": lambda n : setattr(self, 'tenant_display_name', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "total_business_licenses": lambda n : setattr(self, 'total_business_licenses', n.get_int_value()),
            "total_cloud_pc_connection_status": lambda n : setattr(self, 'total_cloud_pc_connection_status', n.get_int_value()),
            "total_cloud_pc_status": lambda n : setattr(self, 'total_cloud_pc_status', n.get_int_value()),
            "total_enterprise_licenses": lambda n : setattr(self, 'total_enterprise_licenses', n.get_int_value()),
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
    def number_of_cloud_pc_connection_status_failed(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcConnectionStatusFailed property value. The number of cloud PC connections that have a status of failed. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_connection_status_failed
    
    @number_of_cloud_pc_connection_status_failed.setter
    def number_of_cloud_pc_connection_status_failed(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcConnectionStatusFailed property value. The number of cloud PC connections that have a status of failed. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcConnectionStatusFailed property.
        """
        self._number_of_cloud_pc_connection_status_failed = value
    
    @property
    def number_of_cloud_pc_connection_status_passed(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcConnectionStatusPassed property value. The number of cloud PC connections that have a status of passed. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_connection_status_passed
    
    @number_of_cloud_pc_connection_status_passed.setter
    def number_of_cloud_pc_connection_status_passed(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcConnectionStatusPassed property value. The number of cloud PC connections that have a status of passed. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcConnectionStatusPassed property.
        """
        self._number_of_cloud_pc_connection_status_passed = value
    
    @property
    def number_of_cloud_pc_connection_status_pending(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcConnectionStatusPending property value. The number of cloud PC connections that have a status of pending. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_connection_status_pending
    
    @number_of_cloud_pc_connection_status_pending.setter
    def number_of_cloud_pc_connection_status_pending(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcConnectionStatusPending property value. The number of cloud PC connections that have a status of pending. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcConnectionStatusPending property.
        """
        self._number_of_cloud_pc_connection_status_pending = value
    
    @property
    def number_of_cloud_pc_connection_status_running(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcConnectionStatusRunning property value. The number of cloud PC connections that have a status of running. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_connection_status_running
    
    @number_of_cloud_pc_connection_status_running.setter
    def number_of_cloud_pc_connection_status_running(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcConnectionStatusRunning property value. The number of cloud PC connections that have a status of running. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcConnectionStatusRunning property.
        """
        self._number_of_cloud_pc_connection_status_running = value
    
    @property
    def number_of_cloud_pc_connection_status_unkown_future_value(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcConnectionStatusUnkownFutureValue property value. The number of cloud PC connections that have a status of unknownFutureValue. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_connection_status_unkown_future_value
    
    @number_of_cloud_pc_connection_status_unkown_future_value.setter
    def number_of_cloud_pc_connection_status_unkown_future_value(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcConnectionStatusUnkownFutureValue property value. The number of cloud PC connections that have a status of unknownFutureValue. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcConnectionStatusUnkownFutureValue property.
        """
        self._number_of_cloud_pc_connection_status_unkown_future_value = value
    
    @property
    def number_of_cloud_pc_status_deprovisioning(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusDeprovisioning property value. The number of cloud PCs that have a status of deprovisioning. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_deprovisioning
    
    @number_of_cloud_pc_status_deprovisioning.setter
    def number_of_cloud_pc_status_deprovisioning(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusDeprovisioning property value. The number of cloud PCs that have a status of deprovisioning. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusDeprovisioning property.
        """
        self._number_of_cloud_pc_status_deprovisioning = value
    
    @property
    def number_of_cloud_pc_status_failed(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusFailed property value. The number of cloud PCs that have a status of failed. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_failed
    
    @number_of_cloud_pc_status_failed.setter
    def number_of_cloud_pc_status_failed(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusFailed property value. The number of cloud PCs that have a status of failed. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusFailed property.
        """
        self._number_of_cloud_pc_status_failed = value
    
    @property
    def number_of_cloud_pc_status_in_grace_period(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusInGracePeriod property value. The number of cloud PCs that have a status of inGracePeriod. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_in_grace_period
    
    @number_of_cloud_pc_status_in_grace_period.setter
    def number_of_cloud_pc_status_in_grace_period(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusInGracePeriod property value. The number of cloud PCs that have a status of inGracePeriod. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusInGracePeriod property.
        """
        self._number_of_cloud_pc_status_in_grace_period = value
    
    @property
    def number_of_cloud_pc_status_not_provisioned(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusNotProvisioned property value. The number of cloud PCs that have a status of notProvisioned. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_not_provisioned
    
    @number_of_cloud_pc_status_not_provisioned.setter
    def number_of_cloud_pc_status_not_provisioned(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusNotProvisioned property value. The number of cloud PCs that have a status of notProvisioned. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusNotProvisioned property.
        """
        self._number_of_cloud_pc_status_not_provisioned = value
    
    @property
    def number_of_cloud_pc_status_provisioned(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusProvisioned property value. The number of cloud PCs that have a status of provisioned. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_provisioned
    
    @number_of_cloud_pc_status_provisioned.setter
    def number_of_cloud_pc_status_provisioned(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusProvisioned property value. The number of cloud PCs that have a status of provisioned. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusProvisioned property.
        """
        self._number_of_cloud_pc_status_provisioned = value
    
    @property
    def number_of_cloud_pc_status_provisioning(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusProvisioning property value. The number of cloud PCs that have a status of provisioning. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_provisioning
    
    @number_of_cloud_pc_status_provisioning.setter
    def number_of_cloud_pc_status_provisioning(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusProvisioning property value. The number of cloud PCs that have a status of provisioning. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusProvisioning property.
        """
        self._number_of_cloud_pc_status_provisioning = value
    
    @property
    def number_of_cloud_pc_status_unknown(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusUnknown property value. The number of cloud PCs that have a status of unknown. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_unknown
    
    @number_of_cloud_pc_status_unknown.setter
    def number_of_cloud_pc_status_unknown(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusUnknown property value. The number of cloud PCs that have a status of unknown. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusUnknown property.
        """
        self._number_of_cloud_pc_status_unknown = value
    
    @property
    def number_of_cloud_pc_status_upgrading(self,) -> Optional[int]:
        """
        Gets the numberOfCloudPcStatusUpgrading property value. The number of cloud PCs that have a status of upgrading. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._number_of_cloud_pc_status_upgrading
    
    @number_of_cloud_pc_status_upgrading.setter
    def number_of_cloud_pc_status_upgrading(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfCloudPcStatusUpgrading property value. The number of cloud PCs that have a status of upgrading. Optional. Read-only.
        Args:
            value: Value to set for the numberOfCloudPcStatusUpgrading property.
        """
        self._number_of_cloud_pc_status_upgrading = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("lastRefreshedDateTime", self.last_refreshed_date_time)
        writer.write_int_value("numberOfCloudPcConnectionStatusFailed", self.number_of_cloud_pc_connection_status_failed)
        writer.write_int_value("numberOfCloudPcConnectionStatusPassed", self.number_of_cloud_pc_connection_status_passed)
        writer.write_int_value("numberOfCloudPcConnectionStatusPending", self.number_of_cloud_pc_connection_status_pending)
        writer.write_int_value("numberOfCloudPcConnectionStatusRunning", self.number_of_cloud_pc_connection_status_running)
        writer.write_int_value("numberOfCloudPcConnectionStatusUnkownFutureValue", self.number_of_cloud_pc_connection_status_unkown_future_value)
        writer.write_int_value("numberOfCloudPcStatusDeprovisioning", self.number_of_cloud_pc_status_deprovisioning)
        writer.write_int_value("numberOfCloudPcStatusFailed", self.number_of_cloud_pc_status_failed)
        writer.write_int_value("numberOfCloudPcStatusInGracePeriod", self.number_of_cloud_pc_status_in_grace_period)
        writer.write_int_value("numberOfCloudPcStatusNotProvisioned", self.number_of_cloud_pc_status_not_provisioned)
        writer.write_int_value("numberOfCloudPcStatusProvisioned", self.number_of_cloud_pc_status_provisioned)
        writer.write_int_value("numberOfCloudPcStatusProvisioning", self.number_of_cloud_pc_status_provisioning)
        writer.write_int_value("numberOfCloudPcStatusUnknown", self.number_of_cloud_pc_status_unknown)
        writer.write_int_value("numberOfCloudPcStatusUpgrading", self.number_of_cloud_pc_status_upgrading)
        writer.write_str_value("tenantDisplayName", self.tenant_display_name)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_int_value("totalBusinessLicenses", self.total_business_licenses)
        writer.write_int_value("totalCloudPcConnectionStatus", self.total_cloud_pc_connection_status)
        writer.write_int_value("totalCloudPcStatus", self.total_cloud_pc_status)
        writer.write_int_value("totalEnterpriseLicenses", self.total_enterprise_licenses)
    
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
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def total_business_licenses(self,) -> Optional[int]:
        """
        Gets the totalBusinessLicenses property value. The total number of cloud PC devices that have the Business SKU. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._total_business_licenses
    
    @total_business_licenses.setter
    def total_business_licenses(self,value: Optional[int] = None) -> None:
        """
        Sets the totalBusinessLicenses property value. The total number of cloud PC devices that have the Business SKU. Optional. Read-only.
        Args:
            value: Value to set for the totalBusinessLicenses property.
        """
        self._total_business_licenses = value
    
    @property
    def total_cloud_pc_connection_status(self,) -> Optional[int]:
        """
        Gets the totalCloudPcConnectionStatus property value. The total number of cloud PC connection statuses for the given managed tenant. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._total_cloud_pc_connection_status
    
    @total_cloud_pc_connection_status.setter
    def total_cloud_pc_connection_status(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCloudPcConnectionStatus property value. The total number of cloud PC connection statuses for the given managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the totalCloudPcConnectionStatus property.
        """
        self._total_cloud_pc_connection_status = value
    
    @property
    def total_cloud_pc_status(self,) -> Optional[int]:
        """
        Gets the totalCloudPcStatus property value. The total number of cloud PC statues for the given managed tenant. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._total_cloud_pc_status
    
    @total_cloud_pc_status.setter
    def total_cloud_pc_status(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCloudPcStatus property value. The total number of cloud PC statues for the given managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the totalCloudPcStatus property.
        """
        self._total_cloud_pc_status = value
    
    @property
    def total_enterprise_licenses(self,) -> Optional[int]:
        """
        Gets the totalEnterpriseLicenses property value. The total number of cloud PC devices that have the Enterprise SKU. Optional. Read-only.
        Returns: Optional[int]
        """
        return self._total_enterprise_licenses
    
    @total_enterprise_licenses.setter
    def total_enterprise_licenses(self,value: Optional[int] = None) -> None:
        """
        Sets the totalEnterpriseLicenses property value. The total number of cloud PC devices that have the Enterprise SKU. Optional. Read-only.
        Args:
            value: Value to set for the totalEnterpriseLicenses property.
        """
        self._total_enterprise_licenses = value
    

