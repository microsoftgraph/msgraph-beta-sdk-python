from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

classifcation_error_base = lazy_import('msgraph.generated.models.classifcation_error_base')

class ClassificationError(classifcation_error_base.ClassifcationErrorBase):
    def __init__(self,) -> None:
        """
        Instantiates a new ClassificationError and sets the default values.
        """
        super().__init__()
        # The details property
        self._details: Optional[List[classifcation_error_base.ClassifcationErrorBase]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClassificationError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClassificationError
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClassificationError()
    
    @property
    def details(self,) -> Optional[List[classifcation_error_base.ClassifcationErrorBase]]:
        """
        Gets the details property value. The details property
        Returns: Optional[List[classifcation_error_base.ClassifcationErrorBase]]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[List[classifcation_error_base.ClassifcationErrorBase]] = None) -> None:
        """
        Sets the details property value. The details property
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(classifcation_error_base.ClassifcationErrorBase)),
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
        writer.write_collection_of_object_values("details", self.details)
    

