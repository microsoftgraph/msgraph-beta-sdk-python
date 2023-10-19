from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario import BusinessScenario
    from .virtual_events_root import VirtualEventsRoot

@dataclass
class SolutionsRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The businessScenarios property
    business_scenarios: Optional[List[BusinessScenario]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The virtualEvents property
    virtual_events: Optional[VirtualEventsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SolutionsRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SolutionsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario import BusinessScenario
        from .virtual_events_root import VirtualEventsRoot

        from .business_scenario import BusinessScenario
        from .virtual_events_root import VirtualEventsRoot

        fields: Dict[str, Callable[[Any], None]] = {
            "businessScenarios": lambda n : setattr(self, 'business_scenarios', n.get_collection_of_object_values(BusinessScenario)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "virtualEvents": lambda n : setattr(self, 'virtual_events', n.get_object_value(VirtualEventsRoot)),
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
        writer.write_collection_of_object_values("businessScenarios", self.business_scenarios)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_object_value("virtualEvents", self.virtual_events)
        writer.write_additional_data_value(self.additional_data)
    

