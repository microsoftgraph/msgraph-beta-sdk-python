from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

server_processed_content = lazy_import('msgraph.generated.models.server_processed_content')
title_area_layout_type = lazy_import('msgraph.generated.models.title_area_layout_type')
title_area_text_alignment_type = lazy_import('msgraph.generated.models.title_area_text_alignment_type')

class TitleArea(AdditionalDataHolder, Parsable):
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
    def alternative_text(self,) -> Optional[str]:
        """
        Gets the alternativeText property value. Alternative text on the title area.
        Returns: Optional[str]
        """
        return self._alternative_text
    
    @alternative_text.setter
    def alternative_text(self,value: Optional[str] = None) -> None:
        """
        Sets the alternativeText property value. Alternative text on the title area.
        Args:
            value: Value to set for the alternativeText property.
        """
        self._alternative_text = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new titleArea and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Alternative text on the title area.
        self._alternative_text: Optional[str] = None
        # Indicates whether the title area has a gradient effect enabled.
        self._enable_gradient_effect: Optional[bool] = None
        # URL of the image in the title area.
        self._image_web_url: Optional[str] = None
        # Enumeration value that indicates the layout of the title area. The possible values are: imageAndTitle, plain, colorBlock, overlap, unknownFutureValue.
        self._layout: Optional[title_area_layout_type.TitleAreaLayoutType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Contains collections of data that can be processed by server side services like search index and link fixup.
        self._server_processed_content: Optional[server_processed_content.ServerProcessedContent] = None
        # Indicates whether the author should be shown in title area.
        self._show_author: Optional[bool] = None
        # Indicates whether the published date should be shown in title area.
        self._show_published_date: Optional[bool] = None
        # Indicates whether the text block above title should be shown in title area.
        self._show_text_block_above_title: Optional[bool] = None
        # The text above title line.
        self._text_above_title: Optional[str] = None
        # Enumeration value that indicates the text alignment of the title area. The possible values are: left, center, unknownFutureValue.
        self._text_alignment: Optional[title_area_text_alignment_type.TitleAreaTextAlignmentType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TitleArea:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TitleArea
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TitleArea()
    
    @property
    def enable_gradient_effect(self,) -> Optional[bool]:
        """
        Gets the enableGradientEffect property value. Indicates whether the title area has a gradient effect enabled.
        Returns: Optional[bool]
        """
        return self._enable_gradient_effect
    
    @enable_gradient_effect.setter
    def enable_gradient_effect(self,value: Optional[bool] = None) -> None:
        """
        Sets the enableGradientEffect property value. Indicates whether the title area has a gradient effect enabled.
        Args:
            value: Value to set for the enableGradientEffect property.
        """
        self._enable_gradient_effect = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alternative_text": lambda n : setattr(self, 'alternative_text', n.get_str_value()),
            "enable_gradient_effect": lambda n : setattr(self, 'enable_gradient_effect', n.get_bool_value()),
            "image_web_url": lambda n : setattr(self, 'image_web_url', n.get_str_value()),
            "layout": lambda n : setattr(self, 'layout', n.get_enum_value(title_area_layout_type.TitleAreaLayoutType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "server_processed_content": lambda n : setattr(self, 'server_processed_content', n.get_object_value(server_processed_content.ServerProcessedContent)),
            "show_author": lambda n : setattr(self, 'show_author', n.get_bool_value()),
            "show_published_date": lambda n : setattr(self, 'show_published_date', n.get_bool_value()),
            "show_text_block_above_title": lambda n : setattr(self, 'show_text_block_above_title', n.get_bool_value()),
            "text_above_title": lambda n : setattr(self, 'text_above_title', n.get_str_value()),
            "text_alignment": lambda n : setattr(self, 'text_alignment', n.get_enum_value(title_area_text_alignment_type.TitleAreaTextAlignmentType)),
        }
        return fields
    
    @property
    def image_web_url(self,) -> Optional[str]:
        """
        Gets the imageWebUrl property value. URL of the image in the title area.
        Returns: Optional[str]
        """
        return self._image_web_url
    
    @image_web_url.setter
    def image_web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the imageWebUrl property value. URL of the image in the title area.
        Args:
            value: Value to set for the imageWebUrl property.
        """
        self._image_web_url = value
    
    @property
    def layout(self,) -> Optional[title_area_layout_type.TitleAreaLayoutType]:
        """
        Gets the layout property value. Enumeration value that indicates the layout of the title area. The possible values are: imageAndTitle, plain, colorBlock, overlap, unknownFutureValue.
        Returns: Optional[title_area_layout_type.TitleAreaLayoutType]
        """
        return self._layout
    
    @layout.setter
    def layout(self,value: Optional[title_area_layout_type.TitleAreaLayoutType] = None) -> None:
        """
        Sets the layout property value. Enumeration value that indicates the layout of the title area. The possible values are: imageAndTitle, plain, colorBlock, overlap, unknownFutureValue.
        Args:
            value: Value to set for the layout property.
        """
        self._layout = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("alternativeText", self.alternative_text)
        writer.write_bool_value("enableGradientEffect", self.enable_gradient_effect)
        writer.write_str_value("imageWebUrl", self.image_web_url)
        writer.write_enum_value("layout", self.layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("serverProcessedContent", self.server_processed_content)
        writer.write_bool_value("showAuthor", self.show_author)
        writer.write_bool_value("showPublishedDate", self.show_published_date)
        writer.write_bool_value("showTextBlockAboveTitle", self.show_text_block_above_title)
        writer.write_str_value("textAboveTitle", self.text_above_title)
        writer.write_enum_value("textAlignment", self.text_alignment)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def server_processed_content(self,) -> Optional[server_processed_content.ServerProcessedContent]:
        """
        Gets the serverProcessedContent property value. Contains collections of data that can be processed by server side services like search index and link fixup.
        Returns: Optional[server_processed_content.ServerProcessedContent]
        """
        return self._server_processed_content
    
    @server_processed_content.setter
    def server_processed_content(self,value: Optional[server_processed_content.ServerProcessedContent] = None) -> None:
        """
        Sets the serverProcessedContent property value. Contains collections of data that can be processed by server side services like search index and link fixup.
        Args:
            value: Value to set for the serverProcessedContent property.
        """
        self._server_processed_content = value
    
    @property
    def show_author(self,) -> Optional[bool]:
        """
        Gets the showAuthor property value. Indicates whether the author should be shown in title area.
        Returns: Optional[bool]
        """
        return self._show_author
    
    @show_author.setter
    def show_author(self,value: Optional[bool] = None) -> None:
        """
        Sets the showAuthor property value. Indicates whether the author should be shown in title area.
        Args:
            value: Value to set for the showAuthor property.
        """
        self._show_author = value
    
    @property
    def show_published_date(self,) -> Optional[bool]:
        """
        Gets the showPublishedDate property value. Indicates whether the published date should be shown in title area.
        Returns: Optional[bool]
        """
        return self._show_published_date
    
    @show_published_date.setter
    def show_published_date(self,value: Optional[bool] = None) -> None:
        """
        Sets the showPublishedDate property value. Indicates whether the published date should be shown in title area.
        Args:
            value: Value to set for the showPublishedDate property.
        """
        self._show_published_date = value
    
    @property
    def show_text_block_above_title(self,) -> Optional[bool]:
        """
        Gets the showTextBlockAboveTitle property value. Indicates whether the text block above title should be shown in title area.
        Returns: Optional[bool]
        """
        return self._show_text_block_above_title
    
    @show_text_block_above_title.setter
    def show_text_block_above_title(self,value: Optional[bool] = None) -> None:
        """
        Sets the showTextBlockAboveTitle property value. Indicates whether the text block above title should be shown in title area.
        Args:
            value: Value to set for the showTextBlockAboveTitle property.
        """
        self._show_text_block_above_title = value
    
    @property
    def text_above_title(self,) -> Optional[str]:
        """
        Gets the textAboveTitle property value. The text above title line.
        Returns: Optional[str]
        """
        return self._text_above_title
    
    @text_above_title.setter
    def text_above_title(self,value: Optional[str] = None) -> None:
        """
        Sets the textAboveTitle property value. The text above title line.
        Args:
            value: Value to set for the textAboveTitle property.
        """
        self._text_above_title = value
    
    @property
    def text_alignment(self,) -> Optional[title_area_text_alignment_type.TitleAreaTextAlignmentType]:
        """
        Gets the textAlignment property value. Enumeration value that indicates the text alignment of the title area. The possible values are: left, center, unknownFutureValue.
        Returns: Optional[title_area_text_alignment_type.TitleAreaTextAlignmentType]
        """
        return self._text_alignment
    
    @text_alignment.setter
    def text_alignment(self,value: Optional[title_area_text_alignment_type.TitleAreaTextAlignmentType] = None) -> None:
        """
        Sets the textAlignment property value. Enumeration value that indicates the text alignment of the title area. The possible values are: left, center, unknownFutureValue.
        Args:
            value: Value to set for the textAlignment property.
        """
        self._text_alignment = value
    

