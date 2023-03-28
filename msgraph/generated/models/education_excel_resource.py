from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_resource

from . import education_resource

class EducationExcelResource(education_resource.EducationResource):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationExcelResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationExcelResource"
        # Pointer to the Excel file object.
        self._file_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationExcelResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationExcelResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationExcelResource()
    
    @property
    def file_url(self,) -> Optional[str]:
        """
        Gets the fileUrl property value. Pointer to the Excel file object.
        Returns: Optional[str]
        """
        return self._file_url
    
    @file_url.setter
    def file_url(self,value: Optional[str] = None) -> None:
        """
        Sets the fileUrl property value. Pointer to the Excel file object.
        Args:
            value: Value to set for the file_url property.
        """
        self._file_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_resource

        fields: Dict[str, Callable[[Any], None]] = {
            "fileUrl": lambda n : setattr(self, 'file_url', n.get_str_value()),
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
        writer.write_str_value("fileUrl", self.file_url)
    

