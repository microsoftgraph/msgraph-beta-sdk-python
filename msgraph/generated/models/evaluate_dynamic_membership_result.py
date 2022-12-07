from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

expression_evaluation_details = lazy_import('msgraph.generated.models.expression_evaluation_details')

class EvaluateDynamicMembershipResult(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new evaluateDynamicMembershipResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If a group ID is provided, the value is the membership rule for the group. If a group ID is not provided, the value is the membership rule that was provided as a parameter. For more information, see Dynamic membership rules for groups in Azure Active Directory.
        self._membership_rule: Optional[str] = None
        # Provides a detailed anaylsis of the membership evaluation result.
        self._membership_rule_evaluation_details: Optional[expression_evaluation_details.ExpressionEvaluationDetails] = None
        # The value is true if the user or device is a member of the group. The value can also be true if a membership rule was provided and the user or device passes the rule evaluation; otherwise false.
        self._membership_rule_evaluation_result: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateDynamicMembershipResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateDynamicMembershipResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateDynamicMembershipResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "membership_rule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
            "membership_rule_evaluation_details": lambda n : setattr(self, 'membership_rule_evaluation_details', n.get_object_value(expression_evaluation_details.ExpressionEvaluationDetails)),
            "membership_rule_evaluation_result": lambda n : setattr(self, 'membership_rule_evaluation_result', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def membership_rule(self,) -> Optional[str]:
        """
        Gets the membershipRule property value. If a group ID is provided, the value is the membership rule for the group. If a group ID is not provided, the value is the membership rule that was provided as a parameter. For more information, see Dynamic membership rules for groups in Azure Active Directory.
        Returns: Optional[str]
        """
        return self._membership_rule
    
    @membership_rule.setter
    def membership_rule(self,value: Optional[str] = None) -> None:
        """
        Sets the membershipRule property value. If a group ID is provided, the value is the membership rule for the group. If a group ID is not provided, the value is the membership rule that was provided as a parameter. For more information, see Dynamic membership rules for groups in Azure Active Directory.
        Args:
            value: Value to set for the membershipRule property.
        """
        self._membership_rule = value
    
    @property
    def membership_rule_evaluation_details(self,) -> Optional[expression_evaluation_details.ExpressionEvaluationDetails]:
        """
        Gets the membershipRuleEvaluationDetails property value. Provides a detailed anaylsis of the membership evaluation result.
        Returns: Optional[expression_evaluation_details.ExpressionEvaluationDetails]
        """
        return self._membership_rule_evaluation_details
    
    @membership_rule_evaluation_details.setter
    def membership_rule_evaluation_details(self,value: Optional[expression_evaluation_details.ExpressionEvaluationDetails] = None) -> None:
        """
        Sets the membershipRuleEvaluationDetails property value. Provides a detailed anaylsis of the membership evaluation result.
        Args:
            value: Value to set for the membershipRuleEvaluationDetails property.
        """
        self._membership_rule_evaluation_details = value
    
    @property
    def membership_rule_evaluation_result(self,) -> Optional[bool]:
        """
        Gets the membershipRuleEvaluationResult property value. The value is true if the user or device is a member of the group. The value can also be true if a membership rule was provided and the user or device passes the rule evaluation; otherwise false.
        Returns: Optional[bool]
        """
        return self._membership_rule_evaluation_result
    
    @membership_rule_evaluation_result.setter
    def membership_rule_evaluation_result(self,value: Optional[bool] = None) -> None:
        """
        Sets the membershipRuleEvaluationResult property value. The value is true if the user or device is a member of the group. The value can also be true if a membership rule was provided and the user or device passes the rule evaluation; otherwise false.
        Args:
            value: Value to set for the membershipRuleEvaluationResult property.
        """
        self._membership_rule_evaluation_result = value
    
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_object_value("membershipRuleEvaluationDetails", self.membership_rule_evaluation_details)
        writer.write_bool_value("membershipRuleEvaluationResult", self.membership_rule_evaluation_result)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

