from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
    from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType

@dataclass
class TeamsAppDashboardCardContentSource(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The configuration for the bot source. Required if sourceType is set to bot.
    bot_configuration: Optional[TeamsAppDashboardCardBotConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the type of source that powers the content of the dashboard card. The possible values are: bot, unknownFutureValue.
    source_type: Optional[TeamsAppDashboardCardSourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppDashboardCardContentSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppDashboardCardContentSource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppDashboardCardContentSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
        from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType

        from .teams_app_dashboard_card_bot_configuration import TeamsAppDashboardCardBotConfiguration
        from .teams_app_dashboard_card_source_type import TeamsAppDashboardCardSourceType

        fields: Dict[str, Callable[[Any], None]] = {
            "botConfiguration": lambda n : setattr(self, 'bot_configuration', n.get_object_value(TeamsAppDashboardCardBotConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceType": lambda n : setattr(self, 'source_type', n.get_enum_value(TeamsAppDashboardCardSourceType)),
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
        writer.write_object_value("botConfiguration", self.bot_configuration)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("sourceType", self.source_type)
        writer.write_additional_data_value(self.additional_data)
    

