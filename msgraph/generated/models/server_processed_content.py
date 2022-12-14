from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

meta_data_key_string_pair = lazy_import('msgraph.generated.models.meta_data_key_string_pair')
meta_data_key_value_pair = lazy_import('msgraph.generated.models.meta_data_key_value_pair')

class ServerProcessedContent(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def component_dependencies(self,) -> Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]:
        """
        Gets the componentDependencies property value. A key-value map where keys are string identifiers and values are component ids. SharePoint servers might decide to use this hint to preload the script for corresponding components for performance boost.
        Returns: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]
        """
        return self._component_dependencies
    
    @component_dependencies.setter
    def component_dependencies(self,value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None) -> None:
        """
        Sets the componentDependencies property value. A key-value map where keys are string identifiers and values are component ids. SharePoint servers might decide to use this hint to preload the script for corresponding components for performance boost.
        Args:
            value: Value to set for the componentDependencies property.
        """
        self._component_dependencies = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new serverProcessedContent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A key-value map where keys are string identifiers and values are component ids. SharePoint servers might decide to use this hint to preload the script for corresponding components for performance boost.
        self._component_dependencies: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None
        # A key-value map where keys are string identifier and values are object of custom key-value pair.
        self._custom_metadata: Optional[List[meta_data_key_value_pair.MetaDataKeyValuePair]] = None
        # A key-value map where keys are string identifiers and values are rich text with HTML format. SharePoint servers treat the values as HTML content and run services like safety checks, search index and link fixup on them.
        self._html_strings: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None
        # A key-value map where keys are string identifiers and values are image sources. SharePoint servers treat the values as image sources and run services like search index and link fixup on them.
        self._image_sources: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None
        # A key-value map where keys are string identifiers and values are links. SharePoint servers treat the values as links and run services like link fixup on them.
        self._links: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # A key-value map where keys are string identifiers and values are strings that should be search indexed.
        self._searchable_plain_texts: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServerProcessedContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServerProcessedContent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServerProcessedContent()
    
    @property
    def custom_metadata(self,) -> Optional[List[meta_data_key_value_pair.MetaDataKeyValuePair]]:
        """
        Gets the customMetadata property value. A key-value map where keys are string identifier and values are object of custom key-value pair.
        Returns: Optional[List[meta_data_key_value_pair.MetaDataKeyValuePair]]
        """
        return self._custom_metadata
    
    @custom_metadata.setter
    def custom_metadata(self,value: Optional[List[meta_data_key_value_pair.MetaDataKeyValuePair]] = None) -> None:
        """
        Sets the customMetadata property value. A key-value map where keys are string identifier and values are object of custom key-value pair.
        Args:
            value: Value to set for the customMetadata property.
        """
        self._custom_metadata = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "component_dependencies": lambda n : setattr(self, 'component_dependencies', n.get_collection_of_object_values(meta_data_key_string_pair.MetaDataKeyStringPair)),
            "custom_metadata": lambda n : setattr(self, 'custom_metadata', n.get_collection_of_object_values(meta_data_key_value_pair.MetaDataKeyValuePair)),
            "html_strings": lambda n : setattr(self, 'html_strings', n.get_collection_of_object_values(meta_data_key_string_pair.MetaDataKeyStringPair)),
            "image_sources": lambda n : setattr(self, 'image_sources', n.get_collection_of_object_values(meta_data_key_string_pair.MetaDataKeyStringPair)),
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(meta_data_key_string_pair.MetaDataKeyStringPair)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "searchable_plain_texts": lambda n : setattr(self, 'searchable_plain_texts', n.get_collection_of_object_values(meta_data_key_string_pair.MetaDataKeyStringPair)),
        }
        return fields
    
    @property
    def html_strings(self,) -> Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]:
        """
        Gets the htmlStrings property value. A key-value map where keys are string identifiers and values are rich text with HTML format. SharePoint servers treat the values as HTML content and run services like safety checks, search index and link fixup on them.
        Returns: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]
        """
        return self._html_strings
    
    @html_strings.setter
    def html_strings(self,value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None) -> None:
        """
        Sets the htmlStrings property value. A key-value map where keys are string identifiers and values are rich text with HTML format. SharePoint servers treat the values as HTML content and run services like safety checks, search index and link fixup on them.
        Args:
            value: Value to set for the htmlStrings property.
        """
        self._html_strings = value
    
    @property
    def image_sources(self,) -> Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]:
        """
        Gets the imageSources property value. A key-value map where keys are string identifiers and values are image sources. SharePoint servers treat the values as image sources and run services like search index and link fixup on them.
        Returns: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]
        """
        return self._image_sources
    
    @image_sources.setter
    def image_sources(self,value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None) -> None:
        """
        Sets the imageSources property value. A key-value map where keys are string identifiers and values are image sources. SharePoint servers treat the values as image sources and run services like search index and link fixup on them.
        Args:
            value: Value to set for the imageSources property.
        """
        self._image_sources = value
    
    @property
    def links(self,) -> Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]:
        """
        Gets the links property value. A key-value map where keys are string identifiers and values are links. SharePoint servers treat the values as links and run services like link fixup on them.
        Returns: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]
        """
        return self._links
    
    @links.setter
    def links(self,value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None) -> None:
        """
        Sets the links property value. A key-value map where keys are string identifiers and values are links. SharePoint servers treat the values as links and run services like link fixup on them.
        Args:
            value: Value to set for the links property.
        """
        self._links = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def searchable_plain_texts(self,) -> Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]:
        """
        Gets the searchablePlainTexts property value. A key-value map where keys are string identifiers and values are strings that should be search indexed.
        Returns: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]]
        """
        return self._searchable_plain_texts
    
    @searchable_plain_texts.setter
    def searchable_plain_texts(self,value: Optional[List[meta_data_key_string_pair.MetaDataKeyStringPair]] = None) -> None:
        """
        Sets the searchablePlainTexts property value. A key-value map where keys are string identifiers and values are strings that should be search indexed.
        Args:
            value: Value to set for the searchablePlainTexts property.
        """
        self._searchable_plain_texts = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("componentDependencies", self.component_dependencies)
        writer.write_collection_of_object_values("customMetadata", self.custom_metadata)
        writer.write_collection_of_object_values("htmlStrings", self.html_strings)
        writer.write_collection_of_object_values("imageSources", self.image_sources)
        writer.write_collection_of_object_values("links", self.links)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("searchablePlainTexts", self.searchable_plain_texts)
        writer.write_additional_data_value(self.additional_data)
    

