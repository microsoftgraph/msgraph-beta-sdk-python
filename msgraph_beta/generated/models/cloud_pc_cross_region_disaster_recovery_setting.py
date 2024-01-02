from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting

@dataclass
class CloudPcCrossRegionDisasterRecoverySetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The crossRegionDisasterRecoveryEnabled property
    cross_region_disaster_recovery_enabled: Optional[bool] = None
    # The disasterRecoveryNetworkSetting property
    disaster_recovery_network_setting: Optional[CloudPcDisasterRecoveryNetworkSetting] = None
    # The maintainCrossRegionRestorePointEnabled property
    maintain_cross_region_restore_point_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcCrossRegionDisasterRecoverySetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcCrossRegionDisasterRecoverySetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcCrossRegionDisasterRecoverySetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting

        from .cloud_pc_disaster_recovery_network_setting import CloudPcDisasterRecoveryNetworkSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "crossRegionDisasterRecoveryEnabled": lambda n : setattr(self, 'cross_region_disaster_recovery_enabled', n.get_bool_value()),
            "disasterRecoveryNetworkSetting": lambda n : setattr(self, 'disaster_recovery_network_setting', n.get_object_value(CloudPcDisasterRecoveryNetworkSetting)),
            "maintainCrossRegionRestorePointEnabled": lambda n : setattr(self, 'maintain_cross_region_restore_point_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("crossRegionDisasterRecoveryEnabled", self.cross_region_disaster_recovery_enabled)
        writer.write_object_value("disasterRecoveryNetworkSetting", self.disaster_recovery_network_setting)
        writer.write_bool_value("maintainCrossRegionRestorePointEnabled", self.maintain_cross_region_restore_point_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

