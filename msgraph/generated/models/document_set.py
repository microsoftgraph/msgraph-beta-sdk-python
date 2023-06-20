from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import column_definition, content_type_info, document_set_content

@dataclass
class DocumentSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Content types allowed in document set.
    allowed_content_types: Optional[List[content_type_info.ContentTypeInfo]] = None
    # Default contents of document set.
    default_contents: Optional[List[document_set_content.DocumentSetContent]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether to add the name of the document set to each file name.
    propagate_welcome_page_changes: Optional[bool] = None
    # The sharedColumns property
    shared_columns: Optional[List[column_definition.ColumnDefinition]] = None
    # Add the name of the Document Set to each file name.
    should_prefix_name_to_file: Optional[bool] = None
    # The welcomePageColumns property
    welcome_page_columns: Optional[List[column_definition.ColumnDefinition]] = None
    # Welcome page absolute URL.
    welcome_page_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DocumentSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DocumentSet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DocumentSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import column_definition, content_type_info, document_set_content

        from . import column_definition, content_type_info, document_set_content

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedContentTypes": lambda n : setattr(self, 'allowed_content_types', n.get_collection_of_object_values(content_type_info.ContentTypeInfo)),
            "defaultContents": lambda n : setattr(self, 'default_contents', n.get_collection_of_object_values(document_set_content.DocumentSetContent)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "propagateWelcomePageChanges": lambda n : setattr(self, 'propagate_welcome_page_changes', n.get_bool_value()),
            "sharedColumns": lambda n : setattr(self, 'shared_columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "shouldPrefixNameToFile": lambda n : setattr(self, 'should_prefix_name_to_file', n.get_bool_value()),
            "welcomePageColumns": lambda n : setattr(self, 'welcome_page_columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "welcomePageUrl": lambda n : setattr(self, 'welcome_page_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("allowedContentTypes", self.allowed_content_types)
        writer.write_collection_of_object_values("defaultContents", self.default_contents)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("propagateWelcomePageChanges", self.propagate_welcome_page_changes)
        writer.write_collection_of_object_values("sharedColumns", self.shared_columns)
        writer.write_bool_value("shouldPrefixNameToFile", self.should_prefix_name_to_file)
        writer.write_collection_of_object_values("welcomePageColumns", self.welcome_page_columns)
        writer.write_str_value("welcomePageUrl", self.welcome_page_url)
        writer.write_additional_data_value(self.additional_data)
    

