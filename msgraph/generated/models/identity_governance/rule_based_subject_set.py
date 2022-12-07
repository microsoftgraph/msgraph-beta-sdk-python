from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class RuleBasedSubjectSet(subject_set.SubjectSet):
    def __init__(self,) -> None:
        """
        Instantiates a new RuleBasedSubjectSet and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.identityGovernance.ruleBasedSubjectSet"
        # The rule for the subject set. Lifecycle Workflows supports a rich set of user properties for configuring the rules using $filter query expressions. For more information, see supported user and query parameters.
        self._rule: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RuleBasedSubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RuleBasedSubjectSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RuleBasedSubjectSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def rule(self,) -> Optional[str]:
        """
        Gets the rule property value. The rule for the subject set. Lifecycle Workflows supports a rich set of user properties for configuring the rules using $filter query expressions. For more information, see supported user and query parameters.
        Returns: Optional[str]
        """
        return self._rule
    
    @rule.setter
    def rule(self,value: Optional[str] = None) -> None:
        """
        Sets the rule property value. The rule for the subject set. Lifecycle Workflows supports a rich set of user properties for configuring the rules using $filter query expressions. For more information, see supported user and query parameters.
        Args:
            value: Value to set for the rule property.
        """
        self._rule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("rule", self.rule)
    

