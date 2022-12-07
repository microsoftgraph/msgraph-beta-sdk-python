from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
ml_classification_match_tolerance = lazy_import('msgraph.generated.models.ml_classification_match_tolerance')
sensitive_type_scope = lazy_import('msgraph.generated.models.sensitive_type_scope')

class TextClassificationRequest(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new TextClassificationRequest and sets the default values.
        """
        super().__init__()
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
            value: Value to set for the fileExtension property.
        """
        self._file_extension = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "file_extension": lambda n : setattr(self, 'file_extension', n.get_str_value()),
            "match_tolerances_to_include": lambda n : setattr(self, 'match_tolerances_to_include', n.get_enum_value(ml_classification_match_tolerance.MlClassificationMatchTolerance)),
            "scopes_to_run": lambda n : setattr(self, 'scopes_to_run', n.get_enum_value(sensitive_type_scope.SensitiveTypeScope)),
            "sensitive_type_ids": lambda n : setattr(self, 'sensitive_type_ids', n.get_collection_of_primitive_values(str)),
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
            value: Value to set for the matchTolerancesToInclude property.
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
            value: Value to set for the scopesToRun property.
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
            value: Value to set for the sensitiveTypeIds property.
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
    

