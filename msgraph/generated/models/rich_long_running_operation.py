from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import long_running_operation, public_error

from . import long_running_operation

class RichLongRunningOperation(long_running_operation.LongRunningOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new RichLongRunningOperation and sets the default values.
        """
        super().__init__()
        # Error due to which the operation failed.
        self._error: Optional[public_error.PublicError] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A value between 0 and 100 that indicates the progress of the operation.
        self._percentage_complete: Optional[int] = None
        # A unique identifier for the result.
        self._resource_id: Optional[str] = None
        # Type of the operation.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RichLongRunningOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RichLongRunningOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RichLongRunningOperation()
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. Error due to which the operation failed.
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. Error due to which the operation failed.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import long_running_operation, public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "percentageComplete": lambda n : setattr(self, 'percentage_complete', n.get_int_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def percentage_complete(self,) -> Optional[int]:
        """
        Gets the percentageComplete property value. A value between 0 and 100 that indicates the progress of the operation.
        Returns: Optional[int]
        """
        return self._percentage_complete
    
    @percentage_complete.setter
    def percentage_complete(self,value: Optional[int] = None) -> None:
        """
        Sets the percentageComplete property value. A value between 0 and 100 that indicates the progress of the operation.
        Args:
            value: Value to set for the percentage_complete property.
        """
        self._percentage_complete = value
    
    @property
    def resource_id(self,) -> Optional[str]:
        """
        Gets the resourceId property value. A unique identifier for the result.
        Returns: Optional[str]
        """
        return self._resource_id
    
    @resource_id.setter
    def resource_id(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceId property value. A unique identifier for the result.
        Args:
            value: Value to set for the resource_id property.
        """
        self._resource_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("error", self.error)
        writer.write_int_value("percentageComplete", self.percentage_complete)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("type", self.type)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Type of the operation.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Type of the operation.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

