from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

classification_error = lazy_import('msgraph.generated.models.classification_error')
entity = lazy_import('msgraph.generated.models.entity')

class ExactMatchJobBase(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
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
            value: Value to set for the completionDateTime property.
        """
        self._completion_date_time = value
    
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
            value: Value to set for the creationDateTime property.
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
        fields = {
            "completion_date_time": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(classification_error.ClassificationError)),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
            value: Value to set for the lastUpdatedDateTime property.
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
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    

