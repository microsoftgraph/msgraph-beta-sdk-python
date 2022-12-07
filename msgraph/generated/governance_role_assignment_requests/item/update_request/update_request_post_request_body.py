from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

governance_schedule = lazy_import('msgraph.generated.models.governance_schedule')

class UpdateRequestPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the updateRequest method.
    """
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
    
    @property
    def assignment_state(self,) -> Optional[str]:
        """
        Gets the assignmentState property value. The assignmentState property
        Returns: Optional[str]
        """
        return self._assignment_state
    
    @assignment_state.setter
    def assignment_state(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentState property value. The assignmentState property
        Args:
            value: Value to set for the assignmentState property.
        """
        self._assignment_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new updateRequestPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The assignmentState property
        self._assignment_state: Optional[str] = None
        # The decision property
        self._decision: Optional[str] = None
        # The reason property
        self._reason: Optional[str] = None
        # The schedule property
        self._schedule: Optional[governance_schedule.GovernanceSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateRequestPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateRequestPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateRequestPostRequestBody()
    
    @property
    def decision(self,) -> Optional[str]:
        """
        Gets the decision property value. The decision property
        Returns: Optional[str]
        """
        return self._decision
    
    @decision.setter
    def decision(self,value: Optional[str] = None) -> None:
        """
        Sets the decision property value. The decision property
        Args:
            value: Value to set for the decision property.
        """
        self._decision = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_state": lambda n : setattr(self, 'assignment_state', n.get_str_value()),
            "decision": lambda n : setattr(self, 'decision', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(governance_schedule.GovernanceSchedule)),
        }
        return fields
    
    @property
    def reason(self,) -> Optional[str]:
        """
        Gets the reason property value. The reason property
        Returns: Optional[str]
        """
        return self._reason
    
    @reason.setter
    def reason(self,value: Optional[str] = None) -> None:
        """
        Sets the reason property value. The reason property
        Args:
            value: Value to set for the reason property.
        """
        self._reason = value
    
    @property
    def schedule(self,) -> Optional[governance_schedule.GovernanceSchedule]:
        """
        Gets the schedule property value. The schedule property
        Returns: Optional[governance_schedule.GovernanceSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[governance_schedule.GovernanceSchedule] = None) -> None:
        """
        Sets the schedule property value. The schedule property
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("assignmentState", self.assignment_state)
        writer.write_str_value("decision", self.decision)
        writer.write_str_value("reason", self.reason)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

