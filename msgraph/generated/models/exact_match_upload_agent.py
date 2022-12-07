from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ExactMatchUploadAgent(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new exactMatchUploadAgent and sets the default values.
        """
        super().__init__()
        # The creationDateTime property
        self._creation_date_time: Optional[datetime] = None
        # The description property
        self._description: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchUploadAgent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchUploadAgent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ExactMatchUploadAgent()
    
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
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "creation_date_time": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
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
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_str_value("description", self.description)
    

