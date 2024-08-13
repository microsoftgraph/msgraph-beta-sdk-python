from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ComanagedDevicesSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    Summary data for co managed devices
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Number of devices with CompliancePolicy swung-over. This property is read-only.
    compliance_policy_count: Optional[int] = None
    # Number of devices with ConfigurationSettings swung-over. This property is read-only.
    configuration_settings_count: Optional[int] = None
    # Number of devices with EndpointProtection swung-over. This property is read-only.
    endpoint_protection_count: Optional[int] = None
    # Number of devices with Inventory swung-over. This property is read-only.
    inventory_count: Optional[int] = None
    # Number of devices with ModernApps swung-over. This property is read-only.
    modern_apps_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of devices with OfficeApps swung-over. This property is read-only.
    office_apps_count: Optional[int] = None
    # Number of devices with ResourceAccess swung-over. This property is read-only.
    resource_access_count: Optional[int] = None
    # Number of Co-Managed Devices. This property is read-only.
    total_comanaged_count: Optional[int] = None
    # Number of devices with WindowsUpdateForBusiness swung-over. This property is read-only.
    windows_update_for_business_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComanagedDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComanagedDevicesSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComanagedDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "compliancePolicyCount": lambda n : setattr(self, 'compliance_policy_count', n.get_int_value()),
            "configurationSettingsCount": lambda n : setattr(self, 'configuration_settings_count', n.get_int_value()),
            "endpointProtectionCount": lambda n : setattr(self, 'endpoint_protection_count', n.get_int_value()),
            "inventoryCount": lambda n : setattr(self, 'inventory_count', n.get_int_value()),
            "modernAppsCount": lambda n : setattr(self, 'modern_apps_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "officeAppsCount": lambda n : setattr(self, 'office_apps_count', n.get_int_value()),
            "resourceAccessCount": lambda n : setattr(self, 'resource_access_count', n.get_int_value()),
            "totalComanagedCount": lambda n : setattr(self, 'total_comanaged_count', n.get_int_value()),
            "windowsUpdateForBusinessCount": lambda n : setattr(self, 'windows_update_for_business_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

