from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_creation_source_kind, planner_external_plan_source

@dataclass
class PlannerPlanCreation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies what kind of creation source the plan is created with. The possible values are: external, publication and unknownFutureValue.
    creation_source_kind: Optional[planner_creation_source_kind.PlannerCreationSourceKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanCreation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanCreation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerExternalPlanSource".casefold():
            from . import planner_external_plan_source

            return planner_external_plan_source.PlannerExternalPlanSource()
        return PlannerPlanCreation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_creation_source_kind, planner_external_plan_source

        from . import planner_creation_source_kind, planner_external_plan_source

        fields: Dict[str, Callable[[Any], None]] = {
            "creationSourceKind": lambda n : setattr(self, 'creation_source_kind', n.get_enum_value(planner_creation_source_kind.PlannerCreationSourceKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("creationSourceKind", self.creation_source_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

