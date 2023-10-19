from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_feedback import AlertFeedback
    from .alert_status import AlertStatus

@dataclass
class AlertHistoryState(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Application ID of the calling application that submitted an update (PATCH) to the alert. The appId should be extracted from the auth token and not entered manually by the calling application.
    app_id: Optional[str] = None
    # UPN of user the alert was assigned to (note: alert.assignedTo only stores the last value/UPN).
    assigned_to: Optional[str] = None
    # Comment entered by signed-in user.
    comments: Optional[List[str]] = None
    # Analyst feedback on the alert in this update. Possible values are: unknown, truePositive, falsePositive, benignPositive.
    feedback: Optional[AlertFeedback] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Alert status value (if updated). Possible values are: unknown, newAlert, inProgress, resolved, dismissed.
    status: Optional[AlertStatus] = None
    # Date and time of the alert update. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    updated_date_time: Optional[datetime.datetime] = None
    # UPN of the signed-in user that updated the alert (taken from the bearer token - if in user/delegated auth mode).
    user: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertHistoryState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertHistoryState
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AlertHistoryState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_feedback import AlertFeedback
        from .alert_status import AlertStatus

        from .alert_feedback import AlertFeedback
        from .alert_status import AlertStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_primitive_values(str)),
            "feedback": lambda n : setattr(self, 'feedback', n.get_enum_value(AlertFeedback)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AlertStatus)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_collection_of_primitive_values("comments", self.comments)
        writer.write_enum_value("feedback", self.feedback)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_str_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

