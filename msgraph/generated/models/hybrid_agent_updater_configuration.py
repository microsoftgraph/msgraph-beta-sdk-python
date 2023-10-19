from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .update_window import UpdateWindow

@dataclass
class HybridAgentUpdaterConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates if updater configuration will be skipped and the agent will receive an update when the next version of the agent is available.
    allow_update_configuration_override: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    defer_update_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The updateWindow property
    update_window: Optional[UpdateWindow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HybridAgentUpdaterConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HybridAgentUpdaterConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HybridAgentUpdaterConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .update_window import UpdateWindow

        from .update_window import UpdateWindow

        fields: Dict[str, Callable[[Any], None]] = {
            "allowUpdateConfigurationOverride": lambda n : setattr(self, 'allow_update_configuration_override', n.get_bool_value()),
            "deferUpdateDateTime": lambda n : setattr(self, 'defer_update_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updateWindow": lambda n : setattr(self, 'update_window', n.get_object_value(UpdateWindow)),
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
        writer.write_bool_value("allowUpdateConfigurationOverride", self.allow_update_configuration_override)
        writer.write_datetime_value("deferUpdateDateTime", self.defer_update_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("updateWindow", self.update_window)
        writer.write_additional_data_value(self.additional_data)
    

