from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.governance_schedule import GovernanceSchedule

@dataclass
class UpdateRequestPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The assignmentState property
    assignment_state: Optional[str] = None
    # The decision property
    decision: Optional[str] = None
    # The reason property
    reason: Optional[str] = None
    # The schedule property
    schedule: Optional[GovernanceSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateRequestPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateRequestPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateRequestPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......models.governance_schedule import GovernanceSchedule

        from ......models.governance_schedule import GovernanceSchedule

        fields: Dict[str, Callable[[Any], None]] = {
            "assignmentState": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(GovernanceSchedule)),
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
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("decision", self.decision)
        writer.write_str_value("reason", self.reason)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

