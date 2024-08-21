from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UpdateWindow(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # End of a time window during which agents can receive updates
    update_window_end_time: Optional[datetime.time] = None
    # Start of a time window during which agents can receive updates
    update_window_start_time: Optional[datetime.time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateWindow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateWindow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updateWindowEndTime": lambda n : setattr(self, 'update_window_end_time', n.get_time_value()),
            "updateWindowStartTime": lambda n : setattr(self, 'update_window_start_time', n.get_time_value()),
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
        writer.write_time_value("updateWindowEndTime", self.update_window_end_time)
        writer.write_time_value("updateWindowStartTime", self.update_window_start_time)
        writer.write_additional_data_value(self.additional_data)
    

