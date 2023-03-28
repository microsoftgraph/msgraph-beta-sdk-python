from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, identity

from . import entity

class ApprovalStep(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new approvalStep and sets the default values.
        """
        super().__init__()
        # Indicates whether the step is assigned to the calling user to review. Read-only.
        self._assigned_to_me: Optional[bool] = None
        # The label provided by the policy creator to identify an approval step. Read-only.
        self._display_name: Optional[str] = None
        # The justification associated with the approval step decision.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The result of this approval record. Possible values include: NotReviewed, Approved, Denied.
        self._review_result: Optional[str] = None
        # The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.
        self._reviewed_by: Optional[identity.Identity] = None
        # The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._reviewed_date_time: Optional[datetime] = None
        # The step status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.
        self._status: Optional[str] = None
    
    @property
    def assigned_to_me(self,) -> Optional[bool]:
        """
        Gets the assignedToMe property value. Indicates whether the step is assigned to the calling user to review. Read-only.
        Returns: Optional[bool]
        """
        return self._assigned_to_me
    
    @assigned_to_me.setter
    def assigned_to_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the assignedToMe property value. Indicates whether the step is assigned to the calling user to review. Read-only.
        Args:
            value: Value to set for the assigned_to_me property.
        """
        self._assigned_to_me = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApprovalStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApprovalStep
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApprovalStep()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The label provided by the policy creator to identify an approval step. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The label provided by the policy creator to identify an approval step. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, identity

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedToMe": lambda n : setattr(self, 'assigned_to_me', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "reviewedBy": lambda n : setattr(self, 'reviewed_by', n.get_object_value(identity.Identity)),
            "reviewedDateTime": lambda n : setattr(self, 'reviewed_date_time', n.get_datetime_value()),
            "reviewResult": lambda n : setattr(self, 'review_result', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. The justification associated with the approval step decision.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. The justification associated with the approval step decision.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def review_result(self,) -> Optional[str]:
        """
        Gets the reviewResult property value. The result of this approval record. Possible values include: NotReviewed, Approved, Denied.
        Returns: Optional[str]
        """
        return self._review_result
    
    @review_result.setter
    def review_result(self,value: Optional[str] = None) -> None:
        """
        Sets the reviewResult property value. The result of this approval record. Possible values include: NotReviewed, Approved, Denied.
        Args:
            value: Value to set for the review_result property.
        """
        self._review_result = value
    
    @property
    def reviewed_by(self,) -> Optional[identity.Identity]:
        """
        Gets the reviewedBy property value. The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.
        Returns: Optional[identity.Identity]
        """
        return self._reviewed_by
    
    @reviewed_by.setter
    def reviewed_by(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the reviewedBy property value. The identifier of the reviewer. 00000000-0000-0000-0000-000000000000 if the assigned reviewer hasn't reviewed. Read-only.
        Args:
            value: Value to set for the reviewed_by property.
        """
        self._reviewed_by = value
    
    @property
    def reviewed_date_time(self,) -> Optional[datetime]:
        """
        Gets the reviewedDateTime property value. The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._reviewed_date_time
    
    @reviewed_date_time.setter
    def reviewed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the reviewedDateTime property value. The date and time when a decision was recorded. The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the reviewed_date_time property.
        """
        self._reviewed_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("assignedToMe", self.assigned_to_me)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("reviewedBy", self.reviewed_by)
        writer.write_datetime_value("reviewedDateTime", self.reviewed_date_time)
        writer.write_str_value("reviewResult", self.review_result)
        writer.write_str_value("status", self.status)
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. The step status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. The step status. Possible values: InProgress, Initializing, Completed, Expired. Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

