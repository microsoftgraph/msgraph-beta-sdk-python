from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_body = lazy_import('msgraph.generated.models.item_body')

class EndBreakPostRequestBody(AdditionalDataHolder, Parsable):
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
    def at_approved_location(self,) -> Optional[bool]:
        """
        Gets the atApprovedLocation property value. The atApprovedLocation property
        Returns: Optional[bool]
        """
        return self._at_approved_location
    
    @at_approved_location.setter
    def at_approved_location(self,value: Optional[bool] = None) -> None:
        """
        Sets the atApprovedLocation property value. The atApprovedLocation property
        Args:
            value: Value to set for the atApprovedLocation property.
        """
        self._at_approved_location = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new endBreakPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The atApprovedLocation property
        self._at_approved_location: Optional[bool] = None
        # The notes property
        self._notes: Optional[item_body.ItemBody] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EndBreakPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EndBreakPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EndBreakPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "at_approved_location": lambda n : setattr(self, 'at_approved_location', n.get_bool_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(item_body.ItemBody)),
        }
        return fields
    
    @property
    def notes(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the notes property value. The notes property
        Returns: Optional[item_body.ItemBody]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the notes property value. The notes property
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("atApprovedLocation", self.at_approved_location)
        writer.write_object_value("notes", self.notes)
        writer.write_additional_data_value(self.additional_data)
    

