from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .business_scenario_group_target import BusinessScenarioGroupTarget
    from .planner_task_target_kind import PlannerTaskTargetKind

@dataclass
class BusinessScenarioTaskTargetBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The taskTargetKind property
    task_target_kind: Optional[PlannerTaskTargetKind] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BusinessScenarioTaskTargetBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenarioTaskTargetBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.businessScenarioGroupTarget".casefold():
            from .business_scenario_group_target import BusinessScenarioGroupTarget

            return BusinessScenarioGroupTarget()
        return BusinessScenarioTaskTargetBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .business_scenario_group_target import BusinessScenarioGroupTarget
        from .planner_task_target_kind import PlannerTaskTargetKind

        from .business_scenario_group_target import BusinessScenarioGroupTarget
        from .planner_task_target_kind import PlannerTaskTargetKind

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "taskTargetKind": lambda n : setattr(self, 'task_target_kind', n.get_enum_value(PlannerTaskTargetKind)),
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
        writer.write_enum_value("taskTargetKind", self.task_target_kind)
        writer.write_additional_data_value(self.additional_data)
    

