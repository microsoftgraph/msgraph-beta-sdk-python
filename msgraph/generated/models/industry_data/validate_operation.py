from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import file_validate_operation
    from .. import long_running_operation, public_error

from .. import long_running_operation

class ValidateOperation(long_running_operation.LongRunningOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new ValidateOperation and sets the default values.
        """
        super().__init__()
        # Set of errors discovered through validation.
        self._errors: Optional[List[public_error.PublicError]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Set of warnings discovered through validation.
        self._warnings: Optional[List[public_error.PublicError]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ValidateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ValidateOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.industryData.fileValidateOperation":
                from . import file_validate_operation

                return file_validate_operation.FileValidateOperation()
        return ValidateOperation()
    
    @property
    def errors(self,) -> Optional[List[public_error.PublicError]]:
        """
        Gets the errors property value. Set of errors discovered through validation.
        Returns: Optional[List[public_error.PublicError]]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[List[public_error.PublicError]] = None) -> None:
        """
        Sets the errors property value. Set of errors discovered through validation.
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import file_validate_operation
        from .. import long_running_operation, public_error

        fields: Dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(public_error.PublicError)),
            "warnings": lambda n : setattr(self, 'warnings', n.get_collection_of_object_values(public_error.PublicError)),
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
    
    @property
    def warnings(self,) -> Optional[List[public_error.PublicError]]:
        """
        Gets the warnings property value. Set of warnings discovered through validation.
        Returns: Optional[List[public_error.PublicError]]
        """
        return self._warnings
    
    @warnings.setter
    def warnings(self,value: Optional[List[public_error.PublicError]] = None) -> None:
        """
        Sets the warnings property value. Set of warnings discovered through validation.
        Args:
            value: Value to set for the warnings property.
        """
        self._warnings = value
    

