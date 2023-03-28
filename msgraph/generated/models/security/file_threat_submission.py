from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import file_content_threat_submission, file_url_threat_submission, threat_submission

from . import threat_submission

class FileThreatSubmission(threat_submission.ThreatSubmission):
    def __init__(self,) -> None:
        """
        Instantiates a new FileThreatSubmission and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.fileThreatSubmission"
        # It specifies the file name to be submitted.
        self._file_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileThreatSubmission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FileThreatSubmission
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.security.fileContentThreatSubmission":
                from . import file_content_threat_submission

                return file_content_threat_submission.FileContentThreatSubmission()
            if mapping_value == "#microsoft.graph.security.fileUrlThreatSubmission":
                from . import file_url_threat_submission

                return file_url_threat_submission.FileUrlThreatSubmission()
        return FileThreatSubmission()
    
    @property
    def file_name(self,) -> Optional[str]:
        """
        Gets the fileName property value. It specifies the file name to be submitted.
        Returns: Optional[str]
        """
        return self._file_name
    
    @file_name.setter
    def file_name(self,value: Optional[str] = None) -> None:
        """
        Sets the fileName property value. It specifies the file name to be submitted.
        Args:
            value: Value to set for the file_name property.
        """
        self._file_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import file_content_threat_submission, file_url_threat_submission, threat_submission

        fields: Dict[str, Callable[[Any], None]] = {
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
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
        writer.write_str_value("fileName", self.file_name)
    

