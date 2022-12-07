from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
external_activity_type = lazy_import('msgraph.generated.models.external_connectors.external_activity_type')
identity = lazy_import('msgraph.generated.models.external_connectors.identity')

class ExternalActivity(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new externalActivity and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents an identity used to identify who is responsible for the activity.
        self._performed_by: Optional[identity.Identity] = None
        # When the particular activity occurred.
        self._start_date_time: Optional[datetime] = None
        # The type property
        self._type: Optional[external_activity_type.ExternalActivityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExternalActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "performed_by": lambda n : setattr(self, 'performed_by', n.get_object_value(identity.Identity)),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(external_activity_type.ExternalActivityType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def performed_by(self,) -> Optional[identity.Identity]:
        """
        Gets the performedBy property value. Represents an identity used to identify who is responsible for the activity.
        Returns: Optional[identity.Identity]
        """
        return self._performed_by
    
    @performed_by.setter
    def performed_by(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the performedBy property value. Represents an identity used to identify who is responsible for the activity.
        Args:
            value: Value to set for the performedBy property.
        """
        self._performed_by = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("performedBy", self.performed_by)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. When the particular activity occurred.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. When the particular activity occurred.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def type(self,) -> Optional[external_activity_type.ExternalActivityType]:
        """
        Gets the type property value. The type property
        Returns: Optional[external_activity_type.ExternalActivityType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[external_activity_type.ExternalActivityType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

