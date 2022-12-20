from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item = lazy_import('msgraph.generated.models.base_item')
canvas_layout = lazy_import('msgraph.generated.models.canvas_layout')
content_type_info = lazy_import('msgraph.generated.models.content_type_info')
page_layout_type = lazy_import('msgraph.generated.models.page_layout_type')
page_promotion_type = lazy_import('msgraph.generated.models.page_promotion_type')
publication_facet = lazy_import('msgraph.generated.models.publication_facet')
reactions_facet = lazy_import('msgraph.generated.models.reactions_facet')
title_area = lazy_import('msgraph.generated.models.title_area')
web_part = lazy_import('msgraph.generated.models.web_part')

class SitePage(base_item.BaseItem):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def canvas_layout(self,) -> Optional[canvas_layout.CanvasLayout]:
        """
        Gets the canvasLayout property value. Indicates the layout of the content in a given SharePoint page, including horizontal sections and vertical section
        Returns: Optional[canvas_layout.CanvasLayout]
        """
        return self._canvas_layout
    
    @canvas_layout.setter
    def canvas_layout(self,value: Optional[canvas_layout.CanvasLayout] = None) -> None:
        """
        Sets the canvasLayout property value. Indicates the layout of the content in a given SharePoint page, including horizontal sections and vertical section
        Args:
            value: Value to set for the canvasLayout property.
        """
        self._canvas_layout = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sitePage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sitePage"
        # Indicates the layout of the content in a given SharePoint page, including horizontal sections and vertical section
        self._canvas_layout: Optional[canvas_layout.CanvasLayout] = None
        # Inherited from baseItem.
        self._content_type: Optional[content_type_info.ContentTypeInfo] = None
        # The name of the page layout of the page. The possible values are: microsoftReserved, article, home, unknownFutureValue.
        self._page_layout: Optional[page_layout_type.PageLayoutType] = None
        # Indicates the promotion kind of the sitePage. The possible values are: microsoftReserved, page, newsPost, unknownFutureValue.
        self._promotion_kind: Optional[page_promotion_type.PagePromotionType] = None
        # The publishing status and the MM.mm version of the page.
        self._publishing_state: Optional[publication_facet.PublicationFacet] = None
        # Reactions information for the page.
        self._reactions: Optional[reactions_facet.ReactionsFacet] = None
        # Determines whether or not to show comments at the bottom of the page.
        self._show_comments: Optional[bool] = None
        # Determines whether or not to show recommended pages at the bottom of the page.
        self._show_recommended_pages: Optional[bool] = None
        # Url of the sitePage's thumbnail image
        self._thumbnail_web_url: Optional[str] = None
        # Title of the sitePage.
        self._title: Optional[str] = None
        # Title area on the SharePoint page.
        self._title_area: Optional[title_area.TitleArea] = None
        # Collection of webparts on the SharePoint page
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
            "canvas_layout": lambda n : setattr(self, 'canvas_layout', n.get_object_value(canvas_layout.CanvasLayout)),
            "content_type": lambda n : setattr(self, 'content_type', n.get_object_value(content_type_info.ContentTypeInfo)),
            "page_layout": lambda n : setattr(self, 'page_layout', n.get_enum_value(page_layout_type.PageLayoutType)),
            "promotion_kind": lambda n : setattr(self, 'promotion_kind', n.get_enum_value(page_promotion_type.PagePromotionType)),
            "publishing_state": lambda n : setattr(self, 'publishing_state', n.get_object_value(publication_facet.PublicationFacet)),
            "reactions": lambda n : setattr(self, 'reactions', n.get_object_value(reactions_facet.ReactionsFacet)),
            "show_comments": lambda n : setattr(self, 'show_comments', n.get_bool_value()),
            "show_recommended_pages": lambda n : setattr(self, 'show_recommended_pages', n.get_bool_value()),
            "thumbnail_web_url": lambda n : setattr(self, 'thumbnail_web_url', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "title_area": lambda n : setattr(self, 'title_area', n.get_object_value(title_area.TitleArea)),
            "web_parts": lambda n : setattr(self, 'web_parts', n.get_collection_of_object_values(web_part.WebPart)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def page_layout(self,) -> Optional[page_layout_type.PageLayoutType]:
        """
        Gets the pageLayout property value. The name of the page layout of the page. The possible values are: microsoftReserved, article, home, unknownFutureValue.
        Returns: Optional[page_layout_type.PageLayoutType]
        """
        return self._page_layout
    
    @page_layout.setter
    def page_layout(self,value: Optional[page_layout_type.PageLayoutType] = None) -> None:
        """
        Sets the pageLayout property value. The name of the page layout of the page. The possible values are: microsoftReserved, article, home, unknownFutureValue.
        Args:
            value: Value to set for the pageLayout property.
        """
        self._page_layout = value
    
    @property
    def promotion_kind(self,) -> Optional[page_promotion_type.PagePromotionType]:
        """
        Gets the promotionKind property value. Indicates the promotion kind of the sitePage. The possible values are: microsoftReserved, page, newsPost, unknownFutureValue.
        Returns: Optional[page_promotion_type.PagePromotionType]
        """
        return self._promotion_kind
    
    @promotion_kind.setter
    def promotion_kind(self,value: Optional[page_promotion_type.PagePromotionType] = None) -> None:
        """
        Sets the promotionKind property value. Indicates the promotion kind of the sitePage. The possible values are: microsoftReserved, page, newsPost, unknownFutureValue.
        Args:
            value: Value to set for the promotionKind property.
        """
        self._promotion_kind = value
    
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
    
    @property
    def reactions(self,) -> Optional[reactions_facet.ReactionsFacet]:
        """
        Gets the reactions property value. Reactions information for the page.
        Returns: Optional[reactions_facet.ReactionsFacet]
        """
        return self._reactions
    
    @reactions.setter
    def reactions(self,value: Optional[reactions_facet.ReactionsFacet] = None) -> None:
        """
        Sets the reactions property value. Reactions information for the page.
        Args:
            value: Value to set for the reactions property.
        """
        self._reactions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("canvasLayout", self.canvas_layout)
        writer.write_object_value("contentType", self.content_type)
        writer.write_enum_value("pageLayout", self.page_layout)
        writer.write_enum_value("promotionKind", self.promotion_kind)
        writer.write_object_value("publishingState", self.publishing_state)
        writer.write_object_value("reactions", self.reactions)
        writer.write_bool_value("showComments", self.show_comments)
        writer.write_bool_value("showRecommendedPages", self.show_recommended_pages)
        writer.write_str_value("thumbnailWebUrl", self.thumbnail_web_url)
        writer.write_str_value("title", self.title)
        writer.write_object_value("titleArea", self.title_area)
        writer.write_collection_of_object_values("webParts", self.web_parts)
    
    @property
    def show_comments(self,) -> Optional[bool]:
        """
        Gets the showComments property value. Determines whether or not to show comments at the bottom of the page.
        Returns: Optional[bool]
        """
        return self._show_comments
    
    @show_comments.setter
    def show_comments(self,value: Optional[bool] = None) -> None:
        """
        Sets the showComments property value. Determines whether or not to show comments at the bottom of the page.
        Args:
            value: Value to set for the showComments property.
        """
        self._show_comments = value
    
    @property
    def show_recommended_pages(self,) -> Optional[bool]:
        """
        Gets the showRecommendedPages property value. Determines whether or not to show recommended pages at the bottom of the page.
        Returns: Optional[bool]
        """
        return self._show_recommended_pages
    
    @show_recommended_pages.setter
    def show_recommended_pages(self,value: Optional[bool] = None) -> None:
        """
        Sets the showRecommendedPages property value. Determines whether or not to show recommended pages at the bottom of the page.
        Args:
            value: Value to set for the showRecommendedPages property.
        """
        self._show_recommended_pages = value
    
    @property
    def thumbnail_web_url(self,) -> Optional[str]:
        """
        Gets the thumbnailWebUrl property value. Url of the sitePage's thumbnail image
        Returns: Optional[str]
        """
        return self._thumbnail_web_url
    
    @thumbnail_web_url.setter
    def thumbnail_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the thumbnailWebUrl property value. Url of the sitePage's thumbnail image
        Args:
            value: Value to set for the thumbnailWebUrl property.
        """
        self._thumbnail_web_url = value
    
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
    def title_area(self,) -> Optional[title_area.TitleArea]:
        """
        Gets the titleArea property value. Title area on the SharePoint page.
        Returns: Optional[title_area.TitleArea]
        """
        return self._title_area
    
    @title_area.setter
    def title_area(self,value: Optional[title_area.TitleArea] = None) -> None:
        """
        Sets the titleArea property value. Title area on the SharePoint page.
        Args:
            value: Value to set for the titleArea property.
        """
        self._title_area = value
    
    @property
    def web_parts(self,) -> Optional[List[web_part.WebPart]]:
        """
        Gets the webParts property value. Collection of webparts on the SharePoint page
        Returns: Optional[List[web_part.WebPart]]
        """
        return self._web_parts
    
    @web_parts.setter
    def web_parts(self,value: Optional[List[web_part.WebPart]] = None) -> None:
        """
        Sets the webParts property value. Collection of webparts on the SharePoint page
        Args:
            value: Value to set for the webParts property.
        """
        self._web_parts = value
    

