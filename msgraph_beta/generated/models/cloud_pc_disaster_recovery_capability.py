from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_disaster_recovery_capability_type import CloudPcDisasterRecoveryCapabilityType

@dataclass
class CloudPcDisasterRecoveryCapability(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The disaster recovery action that can be performed for the Cloud PC. The possible values are: none, failover, failback, unknownFutureValue.
    capability_type: Optional[CloudPcDisasterRecoveryCapabilityType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The primary and mainly used region where the Cloud PC is located.
    primary_region: Optional[str] = None
    # The secondary region to which the Cloud PC can be failed over during a regional outage.
    secondary_region: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcDisasterRecoveryCapability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDisasterRecoveryCapability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcDisasterRecoveryCapability()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_disaster_recovery_capability_type import CloudPcDisasterRecoveryCapabilityType

        from .cloud_pc_disaster_recovery_capability_type import CloudPcDisasterRecoveryCapabilityType

        fields: Dict[str, Callable[[Any], None]] = {
            "capabilityType": lambda n : setattr(self, 'capability_type', n.get_enum_value(CloudPcDisasterRecoveryCapabilityType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primaryRegion": lambda n : setattr(self, 'primary_region', n.get_str_value()),
            "secondaryRegion": lambda n : setattr(self, 'secondary_region', n.get_str_value()),
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
        writer.write_enum_value("capabilityType", self.capability_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("primaryRegion", self.primary_region)
        writer.write_str_value("secondaryRegion", self.secondary_region)
        writer.write_additional_data_value(self.additional_data)
    

