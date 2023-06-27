from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .expression_evaluation_details import ExpressionEvaluationDetails

@dataclass
class EvaluateDynamicMembershipResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # If a group ID is provided, the value is the membership rule for the group. If a group ID is not provided, the value is the membership rule that was provided as a parameter. For more information, see Dynamic membership rules for groups in Azure Active Directory.
    membership_rule: Optional[str] = None
    # Provides a detailed anaylsis of the membership evaluation result.
    membership_rule_evaluation_details: Optional[ExpressionEvaluationDetails] = None
    # The value is true if the user or device is a member of the group. The value can also be true if a membership rule was provided and the user or device passes the rule evaluation; otherwise false.
    membership_rule_evaluation_result: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateDynamicMembershipResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateDynamicMembershipResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EvaluateDynamicMembershipResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .expression_evaluation_details import ExpressionEvaluationDetails

        from .expression_evaluation_details import ExpressionEvaluationDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "membershipRule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
            "membershipRuleEvaluationDetails": lambda n : setattr(self, 'membership_rule_evaluation_details', n.get_object_value(ExpressionEvaluationDetails)),
            "membershipRuleEvaluationResult": lambda n : setattr(self, 'membership_rule_evaluation_result', n.get_bool_value()),
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
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_object_value("membershipRuleEvaluationDetails", self.membership_rule_evaluation_details)
        writer.write_bool_value("membershipRuleEvaluationResult", self.membership_rule_evaluation_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

