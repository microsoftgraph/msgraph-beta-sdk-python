from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import alert_feedback, alert_status

class AlertHistoryState(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new alertHistoryState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Application ID of the calling application that submitted an update (PATCH) to the alert. The appId should be extracted from the auth token and not entered manually by the calling application.
        self._app_id: Optional[str] = None
        # UPN of user the alert was assigned to (note: alert.assignedTo only stores the last value/UPN).
        self._assigned_to: Optional[str] = None
        # Comment entered by signed-in user.
        self._comments: Optional[List[str]] = None
        # Analyst feedback on the alert in this update. Possible values are: unknown, truePositive, falsePositive, benignPositive.
        self._feedback: Optional[alert_feedback.AlertFeedback] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Alert status value (if updated). Possible values are: unknown, newAlert, inProgress, resolved, dismissed.
        self._status: Optional[alert_status.AlertStatus] = None
        # Date and time of the alert update. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._updated_date_time: Optional[datetime] = None
        # UPN of the signed-in user that updated the alert (taken from the bearer token - if in user/delegated auth mode).
        self._user: Optional[str] = None
    
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
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. The Application ID of the calling application that submitted an update (PATCH) to the alert. The appId should be extracted from the auth token and not entered manually by the calling application.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. The Application ID of the calling application that submitted an update (PATCH) to the alert. The appId should be extracted from the auth token and not entered manually by the calling application.
        Args:
            value: Value to set for the app_id property.
        """
        self._app_id = value
    
    @property
    def assigned_to(self,) -> Optional[str]:
        """
        Gets the assignedTo property value. UPN of user the alert was assigned to (note: alert.assignedTo only stores the last value/UPN).
        Returns: Optional[str]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[str] = None) -> None:
        """
        Sets the assignedTo property value. UPN of user the alert was assigned to (note: alert.assignedTo only stores the last value/UPN).
        Args:
            value: Value to set for the assigned_to property.
        """
        self._assigned_to = value
    
    @property
    def comments(self,) -> Optional[List[str]]:
        """
        Gets the comments property value. Comment entered by signed-in user.
        Returns: Optional[List[str]]
        """
        return self._comments
    
    @comments.setter
    def comments(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the comments property value. Comment entered by signed-in user.
        Args:
            value: Value to set for the comments property.
        """
        self._comments = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlertHistoryState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlertHistoryState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlertHistoryState()
    
    @property
    def feedback(self,) -> Optional[alert_feedback.AlertFeedback]:
        """
        Gets the feedback property value. Analyst feedback on the alert in this update. Possible values are: unknown, truePositive, falsePositive, benignPositive.
        Returns: Optional[alert_feedback.AlertFeedback]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[alert_feedback.AlertFeedback] = None) -> None:
        """
        Sets the feedback property value. Analyst feedback on the alert in this update. Possible values are: unknown, truePositive, falsePositive, benignPositive.
        Args:
            value: Value to set for the feedback property.
        """
        self._feedback = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import alert_feedback, alert_status

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comments": lambda n : setattr(self, 'comments', n.get_collection_of_primitive_values(str)),
            "feedback": lambda n : setattr(self, 'feedback', n.get_enum_value(alert_feedback.AlertFeedback)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(alert_status.AlertStatus)),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
        }
        return fields
    
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_collection_of_primitive_values("comments", self.comments)
        writer.write_enum_value("feedback", self.feedback)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_str_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def status(self,) -> Optional[alert_status.AlertStatus]:
        """
        Gets the status property value. Alert status value (if updated). Possible values are: unknown, newAlert, inProgress, resolved, dismissed.
        Returns: Optional[alert_status.AlertStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[alert_status.AlertStatus] = None) -> None:
        """
        Sets the status property value. Alert status value (if updated). Possible values are: unknown, newAlert, inProgress, resolved, dismissed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the updatedDateTime property value. Date and time of the alert update. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._updated_date_time
    
    @updated_date_time.setter
    def updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the updatedDateTime property value. Date and time of the alert update. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the updated_date_time property.
        """
        self._updated_date_time = value
    
    @property
    def user(self,) -> Optional[str]:
        """
        Gets the user property value. UPN of the signed-in user that updated the alert (taken from the bearer token - if in user/delegated auth mode).
        Returns: Optional[str]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[str] = None) -> None:
        """
        Sets the user property value. UPN of the signed-in user that updated the alert (taken from the bearer token - if in user/delegated auth mode).
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

