from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import planner_bucket_property_rule, planner_plan_property_rule, planner_rule_kind, planner_task_property_rule

class PlannerPropertyRule(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerPropertyRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Identifies which type of property rules is represented by this instance. The possible values are: taskRule, bucketRule, planRule, unknownFutureValue.
        self._rule_kind: Optional[planner_rule_kind.PlannerRuleKind] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPropertyRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.plannerBucketPropertyRule":
                from . import planner_bucket_property_rule

                return planner_bucket_property_rule.PlannerBucketPropertyRule()
            if mapping_value == "#microsoft.graph.plannerPlanPropertyRule":
                from . import planner_plan_property_rule

                return planner_plan_property_rule.PlannerPlanPropertyRule()
            if mapping_value == "#microsoft.graph.plannerTaskPropertyRule":
                from . import planner_task_property_rule

                return planner_task_property_rule.PlannerTaskPropertyRule()
        return PlannerPropertyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import planner_bucket_property_rule, planner_plan_property_rule, planner_rule_kind, planner_task_property_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "ruleKind": lambda n : setattr(self, 'rule_kind', n.get_enum_value(planner_rule_kind.PlannerRuleKind)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def rule_kind(self,) -> Optional[planner_rule_kind.PlannerRuleKind]:
        """
        Gets the ruleKind property value. Identifies which type of property rules is represented by this instance. The possible values are: taskRule, bucketRule, planRule, unknownFutureValue.
        Returns: Optional[planner_rule_kind.PlannerRuleKind]
        """
        return self._rule_kind
    
    @rule_kind.setter
    def rule_kind(self,value: Optional[planner_rule_kind.PlannerRuleKind] = None) -> None:
        """
        Sets the ruleKind property value. Identifies which type of property rules is represented by this instance. The possible values are: taskRule, bucketRule, planRule, unknownFutureValue.
        Args:
            value: Value to set for the rule_kind property.
        """
        self._rule_kind = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("ruleKind", self.rule_kind)
        writer.write_additional_data_value(self.additional_data)
    

