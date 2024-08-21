from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase
    from .planner_task_property_rule import PlannerTaskPropertyRule

@dataclass
class PlannerTaskRoleBasedRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Default rule that applies when a property or action-specific rule is not provided. Possible values are: Allow, Block
    default_rule: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Rules for specific properties and actions.
    property_rule: Optional[PlannerTaskPropertyRule] = None
    # The role these rules apply to.
    role: Optional[PlannerTaskConfigurationRoleBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTaskRoleBasedRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTaskRoleBasedRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTaskRoleBasedRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase
        from .planner_task_property_rule import PlannerTaskPropertyRule

        from .planner_task_configuration_role_base import PlannerTaskConfigurationRoleBase
        from .planner_task_property_rule import PlannerTaskPropertyRule

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultRule": lambda n : setattr(self, 'default_rule', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propertyRule": lambda n : setattr(self, 'property_rule', n.get_object_value(PlannerTaskPropertyRule)),
            "role": lambda n : setattr(self, 'role', n.get_object_value(PlannerTaskConfigurationRoleBase)),
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
        writer.write_str_value("defaultRule", self.default_rule)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("propertyRule", self.property_rule)
        writer.write_object_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

