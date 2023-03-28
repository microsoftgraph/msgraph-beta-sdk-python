from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classification_error, entity, exact_match_lookup_job, exact_match_session, exact_match_session_base

from . import entity

class ExactMatchJobBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new exactMatchJobBase and sets the default values.
        """
        super().__init__()
        # The completionDateTime property
        self._completion_date_time: Optional[datetime] = None
        # The creationDateTime property
        self._creation_date_time: Optional[datetime] = None
        # The error property
        self._error: Optional[classification_error.ClassificationError] = None
        # The lastUpdatedDateTime property
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The startDateTime property
        self._start_date_time: Optional[datetime] = None
    
    @property
    def completion_date_time(self,) -> Optional[datetime]:
        """
        Gets the completionDateTime property value. The completionDateTime property
        Returns: Optional[datetime]
        """
        return self._completion_date_time
    
    @completion_date_time.setter
    def completion_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completionDateTime property value. The completionDateTime property
        Args:
            value: Value to set for the completion_date_time property.
        """
        self._completion_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchJobBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchJobBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.exactMatchLookupJob":
                from . import exact_match_lookup_job

                return exact_match_lookup_job.ExactMatchLookupJob()
            if mapping_value == "#microsoft.graph.exactMatchSession":
                from . import exact_match_session

                return exact_match_session.ExactMatchSession()
            if mapping_value == "#microsoft.graph.exactMatchSessionBase":
                from . import exact_match_session_base

                return exact_match_session_base.ExactMatchSessionBase()
        return ExactMatchJobBase()
    
    @property
    def creation_date_time(self,) -> Optional[datetime]:
        """
        Gets the creationDateTime property value. The creationDateTime property
        Returns: Optional[datetime]
        """
        return self._creation_date_time
    
    @creation_date_time.setter
    def creation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the creationDateTime property value. The creationDateTime property
        Args:
            value: Value to set for the creation_date_time property.
        """
        self._creation_date_time = value
    
    @property
    def error(self,) -> Optional[classification_error.ClassificationError]:
        """
        Gets the error property value. The error property
        Returns: Optional[classification_error.ClassificationError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[classification_error.ClassificationError] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classification_error, entity, exact_match_lookup_job, exact_match_session, exact_match_session_base

        fields: Dict[str, Callable[[Any], None]] = {
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(classification_error.ClassificationError)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The lastUpdatedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The lastUpdatedDateTime property
        Args:
            value: Value to set for the last_updated_date_time property.
        """
        self._last_updated_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    

