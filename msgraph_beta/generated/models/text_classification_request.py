from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .classification_request_content_meta_data import ClassificationRequestContentMetaData
    from .entity import Entity
    from .ml_classification_match_tolerance import MlClassificationMatchTolerance
    from .sensitive_type_scope import SensitiveTypeScope

from .entity import Entity

@dataclass
class TextClassificationRequest(Entity):
    # The contentMetaData property
    content_meta_data: Optional[ClassificationRequestContentMetaData] = None
    # The fileExtension property
    file_extension: Optional[str] = None
    # The matchTolerancesToInclude property
    match_tolerances_to_include: Optional[MlClassificationMatchTolerance] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scopesToRun property
    scopes_to_run: Optional[SensitiveTypeScope] = None
    # The sensitiveTypeIds property
    sensitive_type_ids: Optional[List[str]] = None
    # The text property
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TextClassificationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TextClassificationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TextClassificationRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .classification_request_content_meta_data import ClassificationRequestContentMetaData
        from .entity import Entity
        from .ml_classification_match_tolerance import MlClassificationMatchTolerance
        from .sensitive_type_scope import SensitiveTypeScope

        from .classification_request_content_meta_data import ClassificationRequestContentMetaData
        from .entity import Entity
        from .ml_classification_match_tolerance import MlClassificationMatchTolerance
        from .sensitive_type_scope import SensitiveTypeScope

        fields: Dict[str, Callable[[Any], None]] = {
            "contentMetaData": lambda n : setattr(self, 'content_meta_data', n.get_object_value(ClassificationRequestContentMetaData)),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "matchTolerancesToInclude": lambda n : setattr(self, 'match_tolerances_to_include', n.get_collection_of_enum_values(MlClassificationMatchTolerance)),
            "scopesToRun": lambda n : setattr(self, 'scopes_to_run', n.get_collection_of_enum_values(SensitiveTypeScope)),
            "sensitiveTypeIds": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("contentMetaData", self.content_meta_data)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_enum_value("matchTolerancesToInclude", self.match_tolerances_to_include)
        writer.write_enum_value("scopesToRun", self.scopes_to_run)
        writer.write_collection_of_primitive_values("sensitiveTypeIds", self.sensitive_type_ids)
        writer.write_str_value("text", self.text)
    

