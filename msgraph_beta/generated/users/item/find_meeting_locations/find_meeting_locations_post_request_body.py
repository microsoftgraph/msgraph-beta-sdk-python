from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.attendee_base import AttendeeBase
    from ....models.time_constraint import TimeConstraint

@dataclass
class FindMeetingLocationsPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The allowFreeOnly property
    allow_free_only: Optional[bool] = None
    # The attendees property
    attendees: Optional[list[AttendeeBase]] = None
    # The maxCandidates property
    max_candidates: Optional[int] = None
    # The meetingDuration property
    meeting_duration: Optional[datetime.timedelta] = None
    # The query property
    query: Optional[str] = None
    # The timeConstraint property
    time_constraint: Optional[TimeConstraint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FindMeetingLocationsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FindMeetingLocationsPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FindMeetingLocationsPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.attendee_base import AttendeeBase
        from ....models.time_constraint import TimeConstraint

        from ....models.attendee_base import AttendeeBase
        from ....models.time_constraint import TimeConstraint

        fields: dict[str, Callable[[Any], None]] = {
            "allowFreeOnly": lambda n : setattr(self, 'allow_free_only', n.get_bool_value()),
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(AttendeeBase)),
            "maxCandidates": lambda n : setattr(self, 'max_candidates', n.get_int_value()),
            "meetingDuration": lambda n : setattr(self, 'meeting_duration', n.get_timedelta_value()),
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "timeConstraint": lambda n : setattr(self, 'time_constraint', n.get_object_value(TimeConstraint)),
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
        writer.write_bool_value("allowFreeOnly", self.allow_free_only)
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_int_value("maxCandidates", self.max_candidates)
        writer.write_timedelta_value("meetingDuration", self.meeting_duration)
        writer.write_str_value("query", self.query)
        writer.write_object_value("timeConstraint", self.time_constraint)
        writer.write_additional_data_value(self.additional_data)
    

