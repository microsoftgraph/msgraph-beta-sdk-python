from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_history_definition = lazy_import('msgraph.generated.models.access_review_history_definition')
access_review_instance_decision_item = lazy_import('msgraph.generated.models.access_review_instance_decision_item')
access_review_policy = lazy_import('msgraph.generated.models.access_review_policy')
access_review_schedule_definition = lazy_import('msgraph.generated.models.access_review_schedule_definition')
entity = lazy_import('msgraph.generated.models.entity')

class AccessReviewSet(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewSet and sets the default values.
        """
        super().__init__()
        # Represents an Azure AD access review decision on an instance of a review.
        self._decisions: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]] = None
        # Represents the template and scheduling for an access review.
        self._definitions: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]] = None
        # Represents a collection of access review history data and the scopes used to collect that data.
        self._history_definitions: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resource that enables administrators to manage directory-level access review policies in their tenant.
        self._policy: Optional[access_review_policy.AccessReviewPolicy] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewSet()
    
    @property
    def decisions(self,) -> Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]]:
        """
        Gets the decisions property value. Represents an Azure AD access review decision on an instance of a review.
        Returns: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]]
        """
        return self._decisions
    
    @decisions.setter
    def decisions(self,value: Optional[List[access_review_instance_decision_item.AccessReviewInstanceDecisionItem]] = None) -> None:
        """
        Sets the decisions property value. Represents an Azure AD access review decision on an instance of a review.
        Args:
            value: Value to set for the decisions property.
        """
        self._decisions = value
    
    @property
    def definitions(self,) -> Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]]:
        """
        Gets the definitions property value. Represents the template and scheduling for an access review.
        Returns: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]]
        """
        return self._definitions
    
    @definitions.setter
    def definitions(self,value: Optional[List[access_review_schedule_definition.AccessReviewScheduleDefinition]] = None) -> None:
        """
        Sets the definitions property value. Represents the template and scheduling for an access review.
        Args:
            value: Value to set for the definitions property.
        """
        self._definitions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "decisions": lambda n : setattr(self, 'decisions', n.get_collection_of_object_values(access_review_instance_decision_item.AccessReviewInstanceDecisionItem)),
            "definitions": lambda n : setattr(self, 'definitions', n.get_collection_of_object_values(access_review_schedule_definition.AccessReviewScheduleDefinition)),
            "history_definitions": lambda n : setattr(self, 'history_definitions', n.get_collection_of_object_values(access_review_history_definition.AccessReviewHistoryDefinition)),
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(access_review_policy.AccessReviewPolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history_definitions(self,) -> Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]]:
        """
        Gets the historyDefinitions property value. Represents a collection of access review history data and the scopes used to collect that data.
        Returns: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]]
        """
        return self._history_definitions
    
    @history_definitions.setter
    def history_definitions(self,value: Optional[List[access_review_history_definition.AccessReviewHistoryDefinition]] = None) -> None:
        """
        Sets the historyDefinitions property value. Represents a collection of access review history data and the scopes used to collect that data.
        Args:
            value: Value to set for the historyDefinitions property.
        """
        self._history_definitions = value
    
    @property
    def policy(self,) -> Optional[access_review_policy.AccessReviewPolicy]:
        """
        Gets the policy property value. Resource that enables administrators to manage directory-level access review policies in their tenant.
        Returns: Optional[access_review_policy.AccessReviewPolicy]
        """
        return self._policy
    
    @policy.setter
    def policy(self,value: Optional[access_review_policy.AccessReviewPolicy] = None) -> None:
        """
        Sets the policy property value. Resource that enables administrators to manage directory-level access review policies in their tenant.
        Args:
            value: Value to set for the policy property.
        """
        self._policy = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("decisions", self.decisions)
        writer.write_collection_of_object_values("definitions", self.definitions)
        writer.write_collection_of_object_values("historyDefinitions", self.history_definitions)
        writer.write_object_value("policy", self.policy)
    

