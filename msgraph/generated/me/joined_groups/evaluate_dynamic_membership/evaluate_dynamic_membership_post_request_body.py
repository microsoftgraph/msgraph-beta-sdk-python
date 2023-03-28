from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class EvaluateDynamicMembershipPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new evaluateDynamicMembershipPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The memberId property
        self._member_id: Optional[str] = None
        # The membershipRule property
        self._membership_rule: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluateDynamicMembershipPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluateDynamicMembershipPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluateDynamicMembershipPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "membershipRule": lambda n : setattr(self, 'membership_rule', n.get_str_value()),
            "memberId": lambda n : setattr(self, 'member_id', n.get_str_value()),
        }
        return fields
    
    @property
    def member_id(self,) -> Optional[str]:
        """
        Gets the memberId property value. The memberId property
        Returns: Optional[str]
        """
        return self._member_id
    
    @member_id.setter
    def member_id(self,value: Optional[str] = None) -> None:
        """
        Sets the memberId property value. The memberId property
        Args:
            value: Value to set for the member_id property.
        """
        self._member_id = value
    
    @property
    def membership_rule(self,) -> Optional[str]:
        """
        Gets the membershipRule property value. The membershipRule property
        Returns: Optional[str]
        """
        return self._membership_rule
    
    @membership_rule.setter
    def membership_rule(self,value: Optional[str] = None) -> None:
        """
        Sets the membershipRule property value. The membershipRule property
        Args:
            value: Value to set for the membership_rule property.
        """
        self._membership_rule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("membershipRule", self.membership_rule)
        writer.write_str_value("memberId", self.member_id)
        writer.write_additional_data_value(self.additional_data)
    

