from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_creation_source_kind, planner_external_task_source, planner_teams_publication_info

@dataclass
class PlannerTaskCreation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Specifies what kind of creation source the task is created with. The possible values are: external, publication and unknownFutureValue.
    creation_source_kind: Optional[planner_creation_source_kind.PlannerCreationSourceKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about the publication process that created this task. This field is deprecated and clients should move to using the new inheritance model.
    teams_publication_info: Optional[planner_teams_publication_info.PlannerTeamsPublicationInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTaskCreation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskCreation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.plannerExternalTaskSource":
                from . import planner_external_task_source

                return planner_external_task_source.PlannerExternalTaskSource()
            if mapping_value == "#microsoft.graph.plannerTeamsPublicationInfo":
                from . import planner_teams_publication_info

                return planner_teams_publication_info.PlannerTeamsPublicationInfo()
        return PlannerTaskCreation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_creation_source_kind, planner_external_task_source, planner_teams_publication_info

        fields: Dict[str, Callable[[Any], None]] = {
            "creationSourceKind": lambda n : setattr(self, 'creation_source_kind', n.get_enum_value(planner_creation_source_kind.PlannerCreationSourceKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "teamsPublicationInfo": lambda n : setattr(self, 'teams_publication_info', n.get_object_value(planner_teams_publication_info.PlannerTeamsPublicationInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("creationSourceKind", self.creation_source_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("teamsPublicationInfo", self.teams_publication_info)
        writer.write_additional_data_value(self.additional_data)
    

