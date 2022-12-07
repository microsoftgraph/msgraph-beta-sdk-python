from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item = lazy_import('msgraph.generated.models.base_item')
content_type_info = lazy_import('msgraph.generated.models.content_type_info')
publication_facet = lazy_import('msgraph.generated.models.publication_facet')
web_part = lazy_import('msgraph.generated.models.web_part')

class SitePage(base_item.BaseItem):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new sitePage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sitePage"
        # Inherited from baseItem.
        self._content_type: Optional[content_type_info.ContentTypeInfo] = None
        # The pageLayoutType property
        self._page_layout_type: Optional[str] = None
        # The publishing status and the MM.mm version of the page.
        self._publishing_state: Optional[publication_facet.PublicationFacet] = None
        # Title of the sitePage.
        self._title: Optional[str] = None
        # The webParts property
        self._web_parts: Optional[List[web_part.WebPart]] = None
    
    @property
    def content_type(self,) -> Optional[content_type_info.ContentTypeInfo]:
        """
        Gets the contentType property value. Inherited from baseItem.
        Returns: Optional[content_type_info.ContentTypeInfo]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[content_type_info.ContentTypeInfo] = None) -> None:
        """
        Sets the contentType property value. Inherited from baseItem.
        Args:
            value: Value to set for the contentType property.
        """
        self._content_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SitePage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SitePage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SitePage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_type": lambda n : setattr(self, 'content_type', n.get_object_value(content_type_info.ContentTypeInfo)),
            "page_layout_type": lambda n : setattr(self, 'page_layout_type', n.get_str_value()),
            "publishing_state": lambda n : setattr(self, 'publishing_state', n.get_object_value(publication_facet.PublicationFacet)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "web_parts": lambda n : setattr(self, 'web_parts', n.get_collection_of_object_values(web_part.WebPart)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def page_layout_type(self,) -> Optional[str]:
        """
        Gets the pageLayoutType property value. The pageLayoutType property
        Returns: Optional[str]
        """
        return self._page_layout_type
    
    @page_layout_type.setter
    def page_layout_type(self,value: Optional[str] = None) -> None:
        """
        Sets the pageLayoutType property value. The pageLayoutType property
        Args:
            value: Value to set for the pageLayoutType property.
        """
        self._page_layout_type = value
    
    @property
    def publishing_state(self,) -> Optional[publication_facet.PublicationFacet]:
        """
        Gets the publishingState property value. The publishing status and the MM.mm version of the page.
        Returns: Optional[publication_facet.PublicationFacet]
        """
        return self._publishing_state
    
    @publishing_state.setter
    def publishing_state(self,value: Optional[publication_facet.PublicationFacet] = None) -> None:
        """
        Sets the publishingState property value. The publishing status and the MM.mm version of the page.
        Args:
            value: Value to set for the publishingState property.
        """
        self._publishing_state = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("contentType", self.content_type)
        writer.write_str_value("pageLayoutType", self.page_layout_type)
        writer.write_object_value("publishingState", self.publishing_state)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_object_values("webParts", self.web_parts)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Title of the sitePage.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Title of the sitePage.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def web_parts(self,) -> Optional[List[web_part.WebPart]]:
        """
        Gets the webParts property value. The webParts property
        Returns: Optional[List[web_part.WebPart]]
        """
        return self._web_parts
    
    @web_parts.setter
    def web_parts(self,value: Optional[List[web_part.WebPart]] = None) -> None:
        """
        Sets the webParts property value. The webParts property
        Args:
            value: Value to set for the webParts property.
        """
        self._web_parts = value
    

