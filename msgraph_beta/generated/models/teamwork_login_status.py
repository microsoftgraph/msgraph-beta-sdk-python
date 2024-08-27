from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_connection import TeamworkConnection

@dataclass
class TeamworkLoginStatus(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Information about the Exchange connection.
    exchange_connection: Optional[TeamworkConnection] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the Skype for Business connection.
    skype_connection: Optional[TeamworkConnection] = None
    # Information about the Teams connection.
    teams_connection: Optional[TeamworkConnection] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkLoginStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkLoginStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkLoginStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_connection import TeamworkConnection

        from .teamwork_connection import TeamworkConnection

        fields: Dict[str, Callable[[Any], None]] = {
            "exchangeConnection": lambda n : setattr(self, 'exchange_connection', n.get_object_value(TeamworkConnection)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "skypeConnection": lambda n : setattr(self, 'skype_connection', n.get_object_value(TeamworkConnection)),
            "teamsConnection": lambda n : setattr(self, 'teams_connection', n.get_object_value(TeamworkConnection)),
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
        writer.write_object_value("exchangeConnection", self.exchange_connection)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("skypeConnection", self.skype_connection)
        writer.write_object_value("teamsConnection", self.teams_connection)
        writer.write_additional_data_value(self.additional_data)
    

