from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
sign_in_status = lazy_import('msgraph.generated.models.sign_in_status')

class ApplicationSignInDetailedSummary(entity.Entity):
    @property
    def aggregated_event_date_time(self,) -> Optional[datetime]:
        """
        Gets the aggregatedEventDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._aggregated_event_date_time
    
    @aggregated_event_date_time.setter
    def aggregated_event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the aggregatedEventDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the aggregatedEventDateTime property.
        """
        self._aggregated_event_date_time = value
    
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. Name of the application that the user signed in to.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. Name of the application that the user signed in to.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_id(self,) -> Optional[str]:
        """
        Gets the appId property value. ID of the application that the user signed in to.
        Returns: Optional[str]
        """
        return self._app_id
    
    @app_id.setter
    def app_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appId property value. ID of the application that the user signed in to.
        Args:
            value: Value to set for the appId property.
        """
        self._app_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ApplicationSignInDetailedSummary and sets the default values.
        """
        super().__init__()
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._aggregated_event_date_time: Optional[datetime] = None
        # Name of the application that the user signed in to.
        self._app_display_name: Optional[str] = None
        # ID of the application that the user signed in to.
        self._app_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Count of sign-ins made by the application.
        self._sign_in_count: Optional[int] = None
        # Details of the sign-in status.
        self._status: Optional[sign_in_status.SignInStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ApplicationSignInDetailedSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationSignInDetailedSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ApplicationSignInDetailedSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aggregated_event_date_time": lambda n : setattr(self, 'aggregated_event_date_time', n.get_datetime_value()),
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_id": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "sign_in_count": lambda n : setattr(self, 'sign_in_count', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(sign_in_status.SignInStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("aggregatedEventDateTime", self.aggregated_event_date_time)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appId", self.app_id)
        writer.write_int_value("signInCount", self.sign_in_count)
        writer.write_object_value("status", self.status)
    
    @property
    def sign_in_count(self,) -> Optional[int]:
        """
        Gets the signInCount property value. Count of sign-ins made by the application.
        Returns: Optional[int]
        """
        return self._sign_in_count
    
    @sign_in_count.setter
    def sign_in_count(self,value: Optional[int] = None) -> None:
        """
        Sets the signInCount property value. Count of sign-ins made by the application.
        Args:
            value: Value to set for the signInCount property.
        """
        self._sign_in_count = value
    
    @property
    def status(self,) -> Optional[sign_in_status.SignInStatus]:
        """
        Gets the status property value. Details of the sign-in status.
        Returns: Optional[sign_in_status.SignInStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[sign_in_status.SignInStatus] = None) -> None:
        """
        Sets the status property value. Details of the sign-in status.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

