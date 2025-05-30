from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkConfiguredPeripheral(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # True if the current peripheral is optional. If set to false, this property is also used as part of the calculation of the health state for the device.
    is_optional: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The peripheral property
    peripheral: Optional[TeamworkPeripheral] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkConfiguredPeripheral:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkConfiguredPeripheral
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkConfiguredPeripheral()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_peripheral import TeamworkPeripheral

        fields: dict[str, Callable[[Any], None]] = {
            "isOptional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "peripheral": lambda n : setattr(self, 'peripheral', n.get_object_value(TeamworkPeripheral)),
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
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("peripheral", self.peripheral)
        writer.write_additional_data_value(self.additional_data)
    

