from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import business_scenario, virtual_events_root

@dataclass
class SolutionsRoot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The businessScenarios property
    business_scenarios: Optional[List[business_scenario.BusinessScenario]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The virtualEvents property
    virtual_events: Optional[virtual_events_root.VirtualEventsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
        from . import business_scenario, virtual_events_root

        from . import business_scenario, virtual_events_root

        fields: Dict[str, Callable[[Any], None]] = {
            "businessScenarios": lambda n : setattr(self, 'business_scenarios', n.get_collection_of_object_values(business_scenario.BusinessScenario)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "virtualEvents": lambda n : setattr(self, 'virtual_events', n.get_object_value(virtual_events_root.VirtualEventsRoot)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("businessScenarios", self.business_scenarios)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("virtualEvents", self.virtual_events)
        writer.write_additional_data_value(self.additional_data)
    

