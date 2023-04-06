from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import classification_request_content_meta_data, entity, ml_classification_match_tolerance, sensitive_type_scope

from . import entity

class TextClassificationRequest(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new TextClassificationRequest and sets the default values.
        """
        super().__init__()
        # The contentMetaData property
        self._content_meta_data: Optional[classification_request_content_meta_data.ClassificationRequestContentMetaData] = None
        # The fileExtension property
        self._file_extension: Optional[str] = None
        # The matchTolerancesToInclude property
        self._match_tolerances_to_include: Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The scopesToRun property
        self._scopes_to_run: Optional[sensitive_type_scope.SensitiveTypeScope] = None
        # The sensitiveTypeIds property
        self._sensitive_type_ids: Optional[List[str]] = None
        # The text property
        self._text: Optional[str] = None
    
    @property
    def content_meta_data(self,) -> Optional[classification_request_content_meta_data.ClassificationRequestContentMetaData]:
        """
        Gets the contentMetaData property value. The contentMetaData property
        Returns: Optional[classification_request_content_meta_data.ClassificationRequestContentMetaData]
        """
        return self._content_meta_data
    
    @content_meta_data.setter
    def content_meta_data(self,value: Optional[classification_request_content_meta_data.ClassificationRequestContentMetaData] = None) -> None:
        """
        Sets the contentMetaData property value. The contentMetaData property
        Args:
            value: Value to set for the content_meta_data property.
        """
        self._content_meta_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TextClassificationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TextClassificationRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TextClassificationRequest()
    
    @property
    def file_extension(self,) -> Optional[str]:
        """
        Gets the fileExtension property value. The fileExtension property
        Returns: Optional[str]
        """
        return self._file_extension
    
    @file_extension.setter
    def file_extension(self,value: Optional[str] = None) -> None:
        """
        Sets the fileExtension property value. The fileExtension property
        Args:
            value: Value to set for the file_extension property.
        """
        self._file_extension = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import classification_request_content_meta_data, entity, ml_classification_match_tolerance, sensitive_type_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "contentMetaData": lambda n : setattr(self, 'content_meta_data', n.get_object_value(classification_request_content_meta_data.ClassificationRequestContentMetaData)),
            "fileExtension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "matchTolerancesToInclude": lambda n : setattr(self, 'match_tolerances_to_include', n.get_enum_value(ml_classification_match_tolerance.MlClassificationMatchTolerance)),
            "scopesToRun": lambda n : setattr(self, 'scopes_to_run', n.get_enum_value(sensitive_type_scope.SensitiveTypeScope)),
            "sensitiveTypeIds": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def match_tolerances_to_include(self,) -> Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance]:
        """
        Gets the matchTolerancesToInclude property value. The matchTolerancesToInclude property
        Returns: Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance]
        """
        return self._match_tolerances_to_include
    
    @match_tolerances_to_include.setter
    def match_tolerances_to_include(self,value: Optional[ml_classification_match_tolerance.MlClassificationMatchTolerance] = None) -> None:
        """
        Sets the matchTolerancesToInclude property value. The matchTolerancesToInclude property
        Args:
            value: Value to set for the match_tolerances_to_include property.
        """
        self._match_tolerances_to_include = value
    
    @property
    def scopes_to_run(self,) -> Optional[sensitive_type_scope.SensitiveTypeScope]:
        """
        Gets the scopesToRun property value. The scopesToRun property
        Returns: Optional[sensitive_type_scope.SensitiveTypeScope]
        """
        return self._scopes_to_run
    
    @scopes_to_run.setter
    def scopes_to_run(self,value: Optional[sensitive_type_scope.SensitiveTypeScope] = None) -> None:
        """
        Sets the scopesToRun property value. The scopesToRun property
        Args:
            value: Value to set for the scopes_to_run property.
        """
        self._scopes_to_run = value
    
    @property
    def sensitive_type_ids(self,) -> Optional[List[str]]:
        """
        Gets the sensitiveTypeIds property value. The sensitiveTypeIds property
        Returns: Optional[List[str]]
        """
        return self._sensitive_type_ids
    
    @sensitive_type_ids.setter
    def sensitive_type_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the sensitiveTypeIds property value. The sensitiveTypeIds property
        Args:
            value: Value to set for the sensitive_type_ids property.
        """
        self._sensitive_type_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("contentMetaData", self.content_meta_data)
        writer.write_str_value("fileExtension", self.file_extension)
        writer.write_enum_value("matchTolerancesToInclude", self.match_tolerances_to_include)
        writer.write_enum_value("scopesToRun", self.scopes_to_run)
        writer.write_collection_of_primitive_values("sensitiveTypeIds", self.sensitive_type_ids)
        writer.write_str_value("text", self.text)
    
    @property
    def text(self,) -> Optional[str]:
        """
        Gets the text property value. The text property
        Returns: Optional[str]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[str] = None) -> None:
        """
        Sets the text property value. The text property
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

