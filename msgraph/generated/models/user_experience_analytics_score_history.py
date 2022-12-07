from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsScoreHistory(entity.Entity):
    """
    The user experience analytics device startup score history.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsScoreHistory and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user experience analytics device startup date time.
        self._startup_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsScoreHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsScoreHistory
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsScoreHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "startup_date_time": lambda n : setattr(self, 'startup_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("startupDateTime", self.startup_date_time)
    
    @property
    def startup_date_time(self,) -> Optional[datetime]:
        """
        Gets the startupDateTime property value. The user experience analytics device startup date time.
        Returns: Optional[datetime]
        """
        return self._startup_date_time
    
    @startup_date_time.setter
    def startup_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startupDateTime property value. The user experience analytics device startup date time.
        Args:
            value: Value to set for the startupDateTime property.
        """
        self._startup_date_time = value
    

