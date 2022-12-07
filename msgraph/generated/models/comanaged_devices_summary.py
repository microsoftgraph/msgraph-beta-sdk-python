from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ComanagedDevicesSummary(AdditionalDataHolder, Parsable):
    """
    Summary data for co managed devices
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def compliance_policy_count(self,) -> Optional[int]:
        """
        Gets the compliancePolicyCount property value. Number of devices with CompliancePolicy swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._compliance_policy_count
    
    @compliance_policy_count.setter
    def compliance_policy_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliancePolicyCount property value. Number of devices with CompliancePolicy swung-over. This property is read-only.
        Args:
            value: Value to set for the compliancePolicyCount property.
        """
        self._compliance_policy_count = value
    
    @property
    def configuration_settings_count(self,) -> Optional[int]:
        """
        Gets the configurationSettingsCount property value. Number of devices with ConfigurationSettings swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._configuration_settings_count
    
    @configuration_settings_count.setter
    def configuration_settings_count(self,value: Optional[int] = None) -> None:
        """
        Sets the configurationSettingsCount property value. Number of devices with ConfigurationSettings swung-over. This property is read-only.
        Args:
            value: Value to set for the configurationSettingsCount property.
        """
        self._configuration_settings_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new comanagedDevicesSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of devices with CompliancePolicy swung-over. This property is read-only.
        self._compliance_policy_count: Optional[int] = None
        # Number of devices with ConfigurationSettings swung-over. This property is read-only.
        self._configuration_settings_count: Optional[int] = None
        # Number of devices with EndpointProtection swung-over. This property is read-only.
        self._endpoint_protection_count: Optional[int] = None
        # Number of devices with Inventory swung-over. This property is read-only.
        self._inventory_count: Optional[int] = None
        # Number of devices with ModernApps swung-over. This property is read-only.
        self._modern_apps_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of devices with OfficeApps swung-over. This property is read-only.
        self._office_apps_count: Optional[int] = None
        # Number of devices with ResourceAccess swung-over. This property is read-only.
        self._resource_access_count: Optional[int] = None
        # Number of Co-Managed Devices. This property is read-only.
        self._total_comanaged_count: Optional[int] = None
        # Number of devices with WindowsUpdateForBusiness swung-over. This property is read-only.
        self._windows_update_for_business_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComanagedDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComanagedDevicesSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ComanagedDevicesSummary()
    
    @property
    def endpoint_protection_count(self,) -> Optional[int]:
        """
        Gets the endpointProtectionCount property value. Number of devices with EndpointProtection swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._endpoint_protection_count
    
    @endpoint_protection_count.setter
    def endpoint_protection_count(self,value: Optional[int] = None) -> None:
        """
        Sets the endpointProtectionCount property value. Number of devices with EndpointProtection swung-over. This property is read-only.
        Args:
            value: Value to set for the endpointProtectionCount property.
        """
        self._endpoint_protection_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_policy_count": lambda n : setattr(self, 'compliance_policy_count', n.get_int_value()),
            "configuration_settings_count": lambda n : setattr(self, 'configuration_settings_count', n.get_int_value()),
            "endpoint_protection_count": lambda n : setattr(self, 'endpoint_protection_count', n.get_int_value()),
            "inventory_count": lambda n : setattr(self, 'inventory_count', n.get_int_value()),
            "modern_apps_count": lambda n : setattr(self, 'modern_apps_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "office_apps_count": lambda n : setattr(self, 'office_apps_count', n.get_int_value()),
            "resource_access_count": lambda n : setattr(self, 'resource_access_count', n.get_int_value()),
            "total_comanaged_count": lambda n : setattr(self, 'total_comanaged_count', n.get_int_value()),
            "windows_update_for_business_count": lambda n : setattr(self, 'windows_update_for_business_count', n.get_int_value()),
        }
        return fields
    
    @property
    def inventory_count(self,) -> Optional[int]:
        """
        Gets the inventoryCount property value. Number of devices with Inventory swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._inventory_count
    
    @inventory_count.setter
    def inventory_count(self,value: Optional[int] = None) -> None:
        """
        Sets the inventoryCount property value. Number of devices with Inventory swung-over. This property is read-only.
        Args:
            value: Value to set for the inventoryCount property.
        """
        self._inventory_count = value
    
    @property
    def modern_apps_count(self,) -> Optional[int]:
        """
        Gets the modernAppsCount property value. Number of devices with ModernApps swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._modern_apps_count
    
    @modern_apps_count.setter
    def modern_apps_count(self,value: Optional[int] = None) -> None:
        """
        Sets the modernAppsCount property value. Number of devices with ModernApps swung-over. This property is read-only.
        Args:
            value: Value to set for the modernAppsCount property.
        """
        self._modern_apps_count = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def office_apps_count(self,) -> Optional[int]:
        """
        Gets the officeAppsCount property value. Number of devices with OfficeApps swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._office_apps_count
    
    @office_apps_count.setter
    def office_apps_count(self,value: Optional[int] = None) -> None:
        """
        Sets the officeAppsCount property value. Number of devices with OfficeApps swung-over. This property is read-only.
        Args:
            value: Value to set for the officeAppsCount property.
        """
        self._office_apps_count = value
    
    @property
    def resource_access_count(self,) -> Optional[int]:
        """
        Gets the resourceAccessCount property value. Number of devices with ResourceAccess swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._resource_access_count
    
    @resource_access_count.setter
    def resource_access_count(self,value: Optional[int] = None) -> None:
        """
        Sets the resourceAccessCount property value. Number of devices with ResourceAccess swung-over. This property is read-only.
        Args:
            value: Value to set for the resourceAccessCount property.
        """
        self._resource_access_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_comanaged_count(self,) -> Optional[int]:
        """
        Gets the totalComanagedCount property value. Number of Co-Managed Devices. This property is read-only.
        Returns: Optional[int]
        """
        return self._total_comanaged_count
    
    @total_comanaged_count.setter
    def total_comanaged_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalComanagedCount property value. Number of Co-Managed Devices. This property is read-only.
        Args:
            value: Value to set for the totalComanagedCount property.
        """
        self._total_comanaged_count = value
    
    @property
    def windows_update_for_business_count(self,) -> Optional[int]:
        """
        Gets the windowsUpdateForBusinessCount property value. Number of devices with WindowsUpdateForBusiness swung-over. This property is read-only.
        Returns: Optional[int]
        """
        return self._windows_update_for_business_count
    
    @windows_update_for_business_count.setter
    def windows_update_for_business_count(self,value: Optional[int] = None) -> None:
        """
        Sets the windowsUpdateForBusinessCount property value. Number of devices with WindowsUpdateForBusiness swung-over. This property is read-only.
        Args:
            value: Value to set for the windowsUpdateForBusinessCount property.
        """
        self._windows_update_for_business_count = value
    

