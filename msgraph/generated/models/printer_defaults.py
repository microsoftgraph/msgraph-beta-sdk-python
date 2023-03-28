from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import print_color_configuration, print_color_mode, print_duplex_configuration, print_duplex_mode, print_finishing, print_multipage_layout, print_orientation, print_presentation_direction, print_quality, print_scaling

class PrinterDefaults(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new printerDefaults and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The default color mode to use when printing the document. Valid values are described in the following table.
        self._color_mode: Optional[print_color_mode.PrintColorMode] = None
        # The default content (MIME) type to use when processing documents.
        self._content_type: Optional[str] = None
        # The default number of copies printed per job.
        self._copies_per_job: Optional[int] = None
        # The documentMimeType property
        self._document_mime_type: Optional[str] = None
        # The default resolution in DPI to use when printing the job.
        self._dpi: Optional[int] = None
        # The duplexConfiguration property
        self._duplex_configuration: Optional[print_duplex_configuration.PrintDuplexConfiguration] = None
        # The default duplex (double-sided) configuration to use when printing a document. Valid values are described in the following table.
        self._duplex_mode: Optional[print_duplex_mode.PrintDuplexMode] = None
        # The default set of finishings to apply to print jobs. Valid values are described in the following table.
        self._finishings: Optional[List[print_finishing.PrintFinishing]] = None
        # The default fitPdfToPage setting. True to fit each page of a PDF document to a physical sheet of media; false to let the printer decide how to lay out impressions.
        self._fit_pdf_to_page: Optional[bool] = None
        # The default input bin that serves as the paper source.
        self._input_bin: Optional[str] = None
        # The default media (such as paper) color to print the document on.
        self._media_color: Optional[str] = None
        # The default media size to use. Supports standard size names for ISO and ANSI media sizes. Valid values are listed in the printerCapabilities topic.
        self._media_size: Optional[str] = None
        # The default media (such as paper) type to print the document on.
        self._media_type: Optional[str] = None
        # The default direction to lay out pages when multiple pages are being printed per sheet. Valid values are described in the following table.
        self._multipage_layout: Optional[print_multipage_layout.PrintMultipageLayout] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The default orientation to use when printing the document. Valid values are described in the following table.
        self._orientation: Optional[print_orientation.PrintOrientation] = None
        # The default output bin to place completed prints into. See the printer's capabilities for a list of supported output bins.
        self._output_bin: Optional[str] = None
        # The default number of document pages to print on each sheet.
        self._pages_per_sheet: Optional[int] = None
        # The pdfFitToPage property
        self._pdf_fit_to_page: Optional[bool] = None
        # The presentationDirection property
        self._presentation_direction: Optional[print_presentation_direction.PrintPresentationDirection] = None
        # The printColorConfiguration property
        self._print_color_configuration: Optional[print_color_configuration.PrintColorConfiguration] = None
        # The printQuality property
        self._print_quality: Optional[print_quality.PrintQuality] = None
        # The default quality to use when printing the document. Valid values are described in the following table.
        self._quality: Optional[print_quality.PrintQuality] = None
        # Specifies how the printer scales the document data to fit the requested media. Valid values are described in the following table.
        self._scaling: Optional[print_scaling.PrintScaling] = None
    
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
    def color_mode(self,) -> Optional[print_color_mode.PrintColorMode]:
        """
        Gets the colorMode property value. The default color mode to use when printing the document. Valid values are described in the following table.
        Returns: Optional[print_color_mode.PrintColorMode]
        """
        return self._color_mode
    
    @color_mode.setter
    def color_mode(self,value: Optional[print_color_mode.PrintColorMode] = None) -> None:
        """
        Sets the colorMode property value. The default color mode to use when printing the document. Valid values are described in the following table.
        Args:
            value: Value to set for the color_mode property.
        """
        self._color_mode = value
    
    @property
    def content_type(self,) -> Optional[str]:
        """
        Gets the contentType property value. The default content (MIME) type to use when processing documents.
        Returns: Optional[str]
        """
        return self._content_type
    
    @content_type.setter
    def content_type(self,value: Optional[str] = None) -> None:
        """
        Sets the contentType property value. The default content (MIME) type to use when processing documents.
        Args:
            value: Value to set for the content_type property.
        """
        self._content_type = value
    
    @property
    def copies_per_job(self,) -> Optional[int]:
        """
        Gets the copiesPerJob property value. The default number of copies printed per job.
        Returns: Optional[int]
        """
        return self._copies_per_job
    
    @copies_per_job.setter
    def copies_per_job(self,value: Optional[int] = None) -> None:
        """
        Sets the copiesPerJob property value. The default number of copies printed per job.
        Args:
            value: Value to set for the copies_per_job property.
        """
        self._copies_per_job = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterDefaults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterDefaults
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterDefaults()
    
    @property
    def document_mime_type(self,) -> Optional[str]:
        """
        Gets the documentMimeType property value. The documentMimeType property
        Returns: Optional[str]
        """
        return self._document_mime_type
    
    @document_mime_type.setter
    def document_mime_type(self,value: Optional[str] = None) -> None:
        """
        Sets the documentMimeType property value. The documentMimeType property
        Args:
            value: Value to set for the document_mime_type property.
        """
        self._document_mime_type = value
    
    @property
    def dpi(self,) -> Optional[int]:
        """
        Gets the dpi property value. The default resolution in DPI to use when printing the job.
        Returns: Optional[int]
        """
        return self._dpi
    
    @dpi.setter
    def dpi(self,value: Optional[int] = None) -> None:
        """
        Sets the dpi property value. The default resolution in DPI to use when printing the job.
        Args:
            value: Value to set for the dpi property.
        """
        self._dpi = value
    
    @property
    def duplex_configuration(self,) -> Optional[print_duplex_configuration.PrintDuplexConfiguration]:
        """
        Gets the duplexConfiguration property value. The duplexConfiguration property
        Returns: Optional[print_duplex_configuration.PrintDuplexConfiguration]
        """
        return self._duplex_configuration
    
    @duplex_configuration.setter
    def duplex_configuration(self,value: Optional[print_duplex_configuration.PrintDuplexConfiguration] = None) -> None:
        """
        Sets the duplexConfiguration property value. The duplexConfiguration property
        Args:
            value: Value to set for the duplex_configuration property.
        """
        self._duplex_configuration = value
    
    @property
    def duplex_mode(self,) -> Optional[print_duplex_mode.PrintDuplexMode]:
        """
        Gets the duplexMode property value. The default duplex (double-sided) configuration to use when printing a document. Valid values are described in the following table.
        Returns: Optional[print_duplex_mode.PrintDuplexMode]
        """
        return self._duplex_mode
    
    @duplex_mode.setter
    def duplex_mode(self,value: Optional[print_duplex_mode.PrintDuplexMode] = None) -> None:
        """
        Sets the duplexMode property value. The default duplex (double-sided) configuration to use when printing a document. Valid values are described in the following table.
        Args:
            value: Value to set for the duplex_mode property.
        """
        self._duplex_mode = value
    
    @property
    def finishings(self,) -> Optional[List[print_finishing.PrintFinishing]]:
        """
        Gets the finishings property value. The default set of finishings to apply to print jobs. Valid values are described in the following table.
        Returns: Optional[List[print_finishing.PrintFinishing]]
        """
        return self._finishings
    
    @finishings.setter
    def finishings(self,value: Optional[List[print_finishing.PrintFinishing]] = None) -> None:
        """
        Sets the finishings property value. The default set of finishings to apply to print jobs. Valid values are described in the following table.
        Args:
            value: Value to set for the finishings property.
        """
        self._finishings = value
    
    @property
    def fit_pdf_to_page(self,) -> Optional[bool]:
        """
        Gets the fitPdfToPage property value. The default fitPdfToPage setting. True to fit each page of a PDF document to a physical sheet of media; false to let the printer decide how to lay out impressions.
        Returns: Optional[bool]
        """
        return self._fit_pdf_to_page
    
    @fit_pdf_to_page.setter
    def fit_pdf_to_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the fitPdfToPage property value. The default fitPdfToPage setting. True to fit each page of a PDF document to a physical sheet of media; false to let the printer decide how to lay out impressions.
        Args:
            value: Value to set for the fit_pdf_to_page property.
        """
        self._fit_pdf_to_page = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import print_color_configuration, print_color_mode, print_duplex_configuration, print_duplex_mode, print_finishing, print_multipage_layout, print_orientation, print_presentation_direction, print_quality, print_scaling

        fields: Dict[str, Callable[[Any], None]] = {
            "colorMode": lambda n : setattr(self, 'color_mode', n.get_enum_value(print_color_mode.PrintColorMode)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "copiesPerJob": lambda n : setattr(self, 'copies_per_job', n.get_int_value()),
            "documentMimeType": lambda n : setattr(self, 'document_mime_type', n.get_str_value()),
            "dpi": lambda n : setattr(self, 'dpi', n.get_int_value()),
            "duplexConfiguration": lambda n : setattr(self, 'duplex_configuration', n.get_enum_value(print_duplex_configuration.PrintDuplexConfiguration)),
            "duplexMode": lambda n : setattr(self, 'duplex_mode', n.get_enum_value(print_duplex_mode.PrintDuplexMode)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(print_finishing.PrintFinishing)),
            "fitPdfToPage": lambda n : setattr(self, 'fit_pdf_to_page', n.get_bool_value()),
            "inputBin": lambda n : setattr(self, 'input_bin', n.get_str_value()),
            "mediaColor": lambda n : setattr(self, 'media_color', n.get_str_value()),
            "mediaSize": lambda n : setattr(self, 'media_size', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "multipageLayout": lambda n : setattr(self, 'multipage_layout', n.get_enum_value(print_multipage_layout.PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(print_orientation.PrintOrientation)),
            "outputBin": lambda n : setattr(self, 'output_bin', n.get_str_value()),
            "pagesPerSheet": lambda n : setattr(self, 'pages_per_sheet', n.get_int_value()),
            "pdfFitToPage": lambda n : setattr(self, 'pdf_fit_to_page', n.get_bool_value()),
            "presentationDirection": lambda n : setattr(self, 'presentation_direction', n.get_enum_value(print_presentation_direction.PrintPresentationDirection)),
            "printColorConfiguration": lambda n : setattr(self, 'print_color_configuration', n.get_enum_value(print_color_configuration.PrintColorConfiguration)),
            "printQuality": lambda n : setattr(self, 'print_quality', n.get_enum_value(print_quality.PrintQuality)),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(print_quality.PrintQuality)),
            "scaling": lambda n : setattr(self, 'scaling', n.get_enum_value(print_scaling.PrintScaling)),
        }
        return fields
    
    @property
    def input_bin(self,) -> Optional[str]:
        """
        Gets the inputBin property value. The default input bin that serves as the paper source.
        Returns: Optional[str]
        """
        return self._input_bin
    
    @input_bin.setter
    def input_bin(self,value: Optional[str] = None) -> None:
        """
        Sets the inputBin property value. The default input bin that serves as the paper source.
        Args:
            value: Value to set for the input_bin property.
        """
        self._input_bin = value
    
    @property
    def media_color(self,) -> Optional[str]:
        """
        Gets the mediaColor property value. The default media (such as paper) color to print the document on.
        Returns: Optional[str]
        """
        return self._media_color
    
    @media_color.setter
    def media_color(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaColor property value. The default media (such as paper) color to print the document on.
        Args:
            value: Value to set for the media_color property.
        """
        self._media_color = value
    
    @property
    def media_size(self,) -> Optional[str]:
        """
        Gets the mediaSize property value. The default media size to use. Supports standard size names for ISO and ANSI media sizes. Valid values are listed in the printerCapabilities topic.
        Returns: Optional[str]
        """
        return self._media_size
    
    @media_size.setter
    def media_size(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaSize property value. The default media size to use. Supports standard size names for ISO and ANSI media sizes. Valid values are listed in the printerCapabilities topic.
        Args:
            value: Value to set for the media_size property.
        """
        self._media_size = value
    
    @property
    def media_type(self,) -> Optional[str]:
        """
        Gets the mediaType property value. The default media (such as paper) type to print the document on.
        Returns: Optional[str]
        """
        return self._media_type
    
    @media_type.setter
    def media_type(self,value: Optional[str] = None) -> None:
        """
        Sets the mediaType property value. The default media (such as paper) type to print the document on.
        Args:
            value: Value to set for the media_type property.
        """
        self._media_type = value
    
    @property
    def multipage_layout(self,) -> Optional[print_multipage_layout.PrintMultipageLayout]:
        """
        Gets the multipageLayout property value. The default direction to lay out pages when multiple pages are being printed per sheet. Valid values are described in the following table.
        Returns: Optional[print_multipage_layout.PrintMultipageLayout]
        """
        return self._multipage_layout
    
    @multipage_layout.setter
    def multipage_layout(self,value: Optional[print_multipage_layout.PrintMultipageLayout] = None) -> None:
        """
        Sets the multipageLayout property value. The default direction to lay out pages when multiple pages are being printed per sheet. Valid values are described in the following table.
        Args:
            value: Value to set for the multipage_layout property.
        """
        self._multipage_layout = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def orientation(self,) -> Optional[print_orientation.PrintOrientation]:
        """
        Gets the orientation property value. The default orientation to use when printing the document. Valid values are described in the following table.
        Returns: Optional[print_orientation.PrintOrientation]
        """
        return self._orientation
    
    @orientation.setter
    def orientation(self,value: Optional[print_orientation.PrintOrientation] = None) -> None:
        """
        Sets the orientation property value. The default orientation to use when printing the document. Valid values are described in the following table.
        Args:
            value: Value to set for the orientation property.
        """
        self._orientation = value
    
    @property
    def output_bin(self,) -> Optional[str]:
        """
        Gets the outputBin property value. The default output bin to place completed prints into. See the printer's capabilities for a list of supported output bins.
        Returns: Optional[str]
        """
        return self._output_bin
    
    @output_bin.setter
    def output_bin(self,value: Optional[str] = None) -> None:
        """
        Sets the outputBin property value. The default output bin to place completed prints into. See the printer's capabilities for a list of supported output bins.
        Args:
            value: Value to set for the output_bin property.
        """
        self._output_bin = value
    
    @property
    def pages_per_sheet(self,) -> Optional[int]:
        """
        Gets the pagesPerSheet property value. The default number of document pages to print on each sheet.
        Returns: Optional[int]
        """
        return self._pages_per_sheet
    
    @pages_per_sheet.setter
    def pages_per_sheet(self,value: Optional[int] = None) -> None:
        """
        Sets the pagesPerSheet property value. The default number of document pages to print on each sheet.
        Args:
            value: Value to set for the pages_per_sheet property.
        """
        self._pages_per_sheet = value
    
    @property
    def pdf_fit_to_page(self,) -> Optional[bool]:
        """
        Gets the pdfFitToPage property value. The pdfFitToPage property
        Returns: Optional[bool]
        """
        return self._pdf_fit_to_page
    
    @pdf_fit_to_page.setter
    def pdf_fit_to_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the pdfFitToPage property value. The pdfFitToPage property
        Args:
            value: Value to set for the pdf_fit_to_page property.
        """
        self._pdf_fit_to_page = value
    
    @property
    def presentation_direction(self,) -> Optional[print_presentation_direction.PrintPresentationDirection]:
        """
        Gets the presentationDirection property value. The presentationDirection property
        Returns: Optional[print_presentation_direction.PrintPresentationDirection]
        """
        return self._presentation_direction
    
    @presentation_direction.setter
    def presentation_direction(self,value: Optional[print_presentation_direction.PrintPresentationDirection] = None) -> None:
        """
        Sets the presentationDirection property value. The presentationDirection property
        Args:
            value: Value to set for the presentation_direction property.
        """
        self._presentation_direction = value
    
    @property
    def print_color_configuration(self,) -> Optional[print_color_configuration.PrintColorConfiguration]:
        """
        Gets the printColorConfiguration property value. The printColorConfiguration property
        Returns: Optional[print_color_configuration.PrintColorConfiguration]
        """
        return self._print_color_configuration
    
    @print_color_configuration.setter
    def print_color_configuration(self,value: Optional[print_color_configuration.PrintColorConfiguration] = None) -> None:
        """
        Sets the printColorConfiguration property value. The printColorConfiguration property
        Args:
            value: Value to set for the print_color_configuration property.
        """
        self._print_color_configuration = value
    
    @property
    def print_quality(self,) -> Optional[print_quality.PrintQuality]:
        """
        Gets the printQuality property value. The printQuality property
        Returns: Optional[print_quality.PrintQuality]
        """
        return self._print_quality
    
    @print_quality.setter
    def print_quality(self,value: Optional[print_quality.PrintQuality] = None) -> None:
        """
        Sets the printQuality property value. The printQuality property
        Args:
            value: Value to set for the print_quality property.
        """
        self._print_quality = value
    
    @property
    def quality(self,) -> Optional[print_quality.PrintQuality]:
        """
        Gets the quality property value. The default quality to use when printing the document. Valid values are described in the following table.
        Returns: Optional[print_quality.PrintQuality]
        """
        return self._quality
    
    @quality.setter
    def quality(self,value: Optional[print_quality.PrintQuality] = None) -> None:
        """
        Sets the quality property value. The default quality to use when printing the document. Valid values are described in the following table.
        Args:
            value: Value to set for the quality property.
        """
        self._quality = value
    
    @property
    def scaling(self,) -> Optional[print_scaling.PrintScaling]:
        """
        Gets the scaling property value. Specifies how the printer scales the document data to fit the requested media. Valid values are described in the following table.
        Returns: Optional[print_scaling.PrintScaling]
        """
        return self._scaling
    
    @scaling.setter
    def scaling(self,value: Optional[print_scaling.PrintScaling] = None) -> None:
        """
        Sets the scaling property value. Specifies how the printer scales the document data to fit the requested media. Valid values are described in the following table.
        Args:
            value: Value to set for the scaling property.
        """
        self._scaling = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("colorMode", self.color_mode)
        writer.write_str_value("contentType", self.content_type)
        writer.write_int_value("copiesPerJob", self.copies_per_job)
        writer.write_str_value("documentMimeType", self.document_mime_type)
        writer.write_int_value("dpi", self.dpi)
        writer.write_enum_value("duplexConfiguration", self.duplex_configuration)
        writer.write_enum_value("duplexMode", self.duplex_mode)
        writer.write_enum_value("finishings", self.finishings)
        writer.write_bool_value("fitPdfToPage", self.fit_pdf_to_page)
        writer.write_str_value("inputBin", self.input_bin)
        writer.write_str_value("mediaColor", self.media_color)
        writer.write_str_value("mediaSize", self.media_size)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_enum_value("multipageLayout", self.multipage_layout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("orientation", self.orientation)
        writer.write_str_value("outputBin", self.output_bin)
        writer.write_int_value("pagesPerSheet", self.pages_per_sheet)
        writer.write_bool_value("pdfFitToPage", self.pdf_fit_to_page)
        writer.write_enum_value("presentationDirection", self.presentation_direction)
        writer.write_enum_value("printColorConfiguration", self.print_color_configuration)
        writer.write_enum_value("printQuality", self.print_quality)
        writer.write_enum_value("quality", self.quality)
        writer.write_enum_value("scaling", self.scaling)
        writer.write_additional_data_value(self.additional_data)
    

