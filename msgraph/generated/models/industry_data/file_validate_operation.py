from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import validate_operation

from . import validate_operation

class FileValidateOperation(validate_operation.ValidateOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new FileValidateOperation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.industryData.fileValidateOperation"
        # Set of files validated by the validate operation.
        self._validated_files: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileValidateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileValidateOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FileValidateOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import validate_operation

        fields: Dict[str, Callable[[Any], None]] = {
            "validatedFiles": lambda n : setattr(self, 'validated_files', n.get_collection_of_primitive_values(str)),
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
    def validated_files(self,) -> Optional[List[str]]:
        """
        Gets the validatedFiles property value. Set of files validated by the validate operation.
        Returns: Optional[List[str]]
        """
        return self._validated_files
    
    @validated_files.setter
    def validated_files(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the validatedFiles property value. Set of files validated by the validate operation.
        Args:
            value: Value to set for the validated_files property.
        """
        self._validated_files = value
    

