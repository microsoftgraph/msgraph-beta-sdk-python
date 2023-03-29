from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import article_indicator, formatted_content
    from .. import entity

from .. import entity

class Article(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new article and sets the default values.
        """
        super().__init__()
        # The body property
        self._body: Optional[formatted_content.FormattedContent] = None
        # The date and time when this article was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # URL of the header image for this article, used for display purposes.
        self._image_url: Optional[str] = None
        # Indicators related to this article.
        self._indicators: Optional[List[article_indicator.ArticleIndicator]] = None
        # Indicates whether this article is currently featured by Microsoft.
        self._is_featured: Optional[bool] = None
        # The most recent date and time when this article was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The summary property
        self._summary: Optional[formatted_content.FormattedContent] = None
        # Tags for this article, communicating keywords, or key concepts.
        self._tags: Optional[List[str]] = None
        # The title of this article.
        self._title: Optional[str] = None
    
    @property
    def body(self,) -> Optional[formatted_content.FormattedContent]:
        """
        Gets the body property value. The body property
        Returns: Optional[formatted_content.FormattedContent]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[formatted_content.FormattedContent] = None) -> None:
        """
        Sets the body property value. The body property
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when this article was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when this article was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Article:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Article
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Article()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import article_indicator, formatted_content
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_object_value(formatted_content.FormattedContent)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "indicators": lambda n : setattr(self, 'indicators', n.get_collection_of_object_values(article_indicator.ArticleIndicator)),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_object_value(formatted_content.FormattedContent)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def image_url(self,) -> Optional[str]:
        """
        Gets the imageUrl property value. URL of the header image for this article, used for display purposes.
        Returns: Optional[str]
        """
        return self._image_url
    
    @image_url.setter
    def image_url(self,value: Optional[str] = None) -> None:
        """
        Sets the imageUrl property value. URL of the header image for this article, used for display purposes.
        Args:
            value: Value to set for the image_url property.
        """
        self._image_url = value
    
    @property
    def indicators(self,) -> Optional[List[article_indicator.ArticleIndicator]]:
        """
        Gets the indicators property value. Indicators related to this article.
        Returns: Optional[List[article_indicator.ArticleIndicator]]
        """
        return self._indicators
    
    @indicators.setter
    def indicators(self,value: Optional[List[article_indicator.ArticleIndicator]] = None) -> None:
        """
        Sets the indicators property value. Indicators related to this article.
        Args:
            value: Value to set for the indicators property.
        """
        self._indicators = value
    
    @property
    def is_featured(self,) -> Optional[bool]:
        """
        Gets the isFeatured property value. Indicates whether this article is currently featured by Microsoft.
        Returns: Optional[bool]
        """
        return self._is_featured
    
    @is_featured.setter
    def is_featured(self,value: Optional[bool] = None) -> None:
        """
        Sets the isFeatured property value. Indicates whether this article is currently featured by Microsoft.
        Args:
            value: Value to set for the is_featured property.
        """
        self._is_featured = value
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The most recent date and time when this article was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The most recent date and time when this article was updated. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the last_updated_date_time property.
        """
        self._last_updated_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("body", self.body)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_collection_of_object_values("indicators", self.indicators)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_object_value("summary", self.summary)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
    
    @property
    def summary(self,) -> Optional[formatted_content.FormattedContent]:
        """
        Gets the summary property value. The summary property
        Returns: Optional[formatted_content.FormattedContent]
        """
        return self._summary
    
    @summary.setter
    def summary(self,value: Optional[formatted_content.FormattedContent] = None) -> None:
        """
        Sets the summary property value. The summary property
        Args:
            value: Value to set for the summary property.
        """
        self._summary = value
    
    @property
    def tags(self,) -> Optional[List[str]]:
        """
        Gets the tags property value. Tags for this article, communicating keywords, or key concepts.
        Returns: Optional[List[str]]
        """
        return self._tags
    
    @tags.setter
    def tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tags property value. Tags for this article, communicating keywords, or key concepts.
        Args:
            value: Value to set for the tags property.
        """
        self._tags = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of this article.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of this article.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

