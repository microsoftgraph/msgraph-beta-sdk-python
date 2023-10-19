from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meta_data_key_string_pair import MetaDataKeyStringPair
    from .meta_data_key_value_pair import MetaDataKeyValuePair

@dataclass
class ServerProcessedContent(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A key-value map where keys are string identifiers and values are component ids. SharePoint servers might decide to use this hint to preload the script for corresponding components for performance boost.
    component_dependencies: Optional[List[MetaDataKeyStringPair]] = None
    # A key-value map where keys are string identifier and values are object of custom key-value pair.
    custom_metadata: Optional[List[MetaDataKeyValuePair]] = None
    # A key-value map where keys are string identifiers and values are rich text with HTML format. SharePoint servers treat the values as HTML content and run services like safety checks, search index and link fixup on them.
    html_strings: Optional[List[MetaDataKeyStringPair]] = None
    # A key-value map where keys are string identifiers and values are image sources. SharePoint servers treat the values as image sources and run services like search index and link fixup on them.
    image_sources: Optional[List[MetaDataKeyStringPair]] = None
    # A key-value map where keys are string identifiers and values are links. SharePoint servers treat the values as links and run services like link fixup on them.
    links: Optional[List[MetaDataKeyStringPair]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A key-value map where keys are string identifiers and values are strings that should be search indexed.
    searchable_plain_texts: Optional[List[MetaDataKeyStringPair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServerProcessedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServerProcessedContent
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServerProcessedContent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .meta_data_key_string_pair import MetaDataKeyStringPair
        from .meta_data_key_value_pair import MetaDataKeyValuePair

        from .meta_data_key_string_pair import MetaDataKeyStringPair
        from .meta_data_key_value_pair import MetaDataKeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "componentDependencies": lambda n : setattr(self, 'component_dependencies', n.get_collection_of_object_values(MetaDataKeyStringPair)),
            "customMetadata": lambda n : setattr(self, 'custom_metadata', n.get_collection_of_object_values(MetaDataKeyValuePair)),
            "htmlStrings": lambda n : setattr(self, 'html_strings', n.get_collection_of_object_values(MetaDataKeyStringPair)),
            "imageSources": lambda n : setattr(self, 'image_sources', n.get_collection_of_object_values(MetaDataKeyStringPair)),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(MetaDataKeyStringPair)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "searchablePlainTexts": lambda n : setattr(self, 'searchable_plain_texts', n.get_collection_of_object_values(MetaDataKeyStringPair)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("componentDependencies", self.component_dependencies)
        writer.write_collection_of_object_values("customMetadata", self.custom_metadata)
        writer.write_collection_of_object_values("htmlStrings", self.html_strings)
        writer.write_collection_of_object_values("imageSources", self.image_sources)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_object_values("searchablePlainTexts", self.searchable_plain_texts)
        writer.write_additional_data_value(self.additional_data)
    

