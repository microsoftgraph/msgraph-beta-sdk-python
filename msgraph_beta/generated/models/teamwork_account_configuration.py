from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teamwork_on_premises_calendar_sync_configuration import TeamworkOnPremisesCalendarSyncConfiguration
    from .teamwork_supported_client import TeamworkSupportedClient

@dataclass
class TeamworkAccountConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The account used to sync the calendar.
    on_premises_calendar_sync_configuration: Optional[TeamworkOnPremisesCalendarSyncConfiguration] = None
    # The supported client for Teams Rooms devices. The possible values are: unknown, skypeDefaultAndTeams, teamsDefaultAndSkype, skypeOnly, teamsOnly, unknownFutureValue.
    supported_client: Optional[TeamworkSupportedClient] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkAccountConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkAccountConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkAccountConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teamwork_on_premises_calendar_sync_configuration import TeamworkOnPremisesCalendarSyncConfiguration
        from .teamwork_supported_client import TeamworkSupportedClient

        from .teamwork_on_premises_calendar_sync_configuration import TeamworkOnPremisesCalendarSyncConfiguration
        from .teamwork_supported_client import TeamworkSupportedClient

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "onPremisesCalendarSyncConfiguration": lambda n : setattr(self, 'on_premises_calendar_sync_configuration', n.get_object_value(TeamworkOnPremisesCalendarSyncConfiguration)),
            "supportedClient": lambda n : setattr(self, 'supported_client', n.get_enum_value(TeamworkSupportedClient)),
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
        writer.write_object_value("onPremisesCalendarSyncConfiguration", self.on_premises_calendar_sync_configuration)
        writer.write_enum_value("supportedClient", self.supported_client)
        writer.write_additional_data_value(self.additional_data)
    

