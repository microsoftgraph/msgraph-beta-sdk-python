from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_connection import TeamworkConnection
    from .teamwork_peripheral import TeamworkPeripheral

@dataclass
class TeamworkPeripheralHealth(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The connected state and time since the peripheral device was connected.
    connection: Optional[TeamworkConnection] = None
    # True if the peripheral is optional. Used for health computation.
    is_optional: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The peripheral property
    peripheral: Optional[TeamworkPeripheral] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkPeripheralHealth:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkPeripheralHealth
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkPeripheralHealth()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_connection import TeamworkConnection
        from .teamwork_peripheral import TeamworkPeripheral

        from .teamwork_connection import TeamworkConnection
        from .teamwork_peripheral import TeamworkPeripheral

        fields: Dict[str, Callable[[Any], None]] = {
            "connection": lambda n : setattr(self, 'connection', n.get_object_value(TeamworkConnection)),
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
        writer.write_object_value("connection", self.connection)
        writer.write_bool_value("isOptional", self.is_optional)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("peripheral", self.peripheral)
        writer.write_additional_data_value(self.additional_data)
    

