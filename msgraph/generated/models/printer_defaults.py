from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import print_color_configuration, print_color_mode, print_duplex_configuration, print_duplex_mode, print_finishing, print_multipage_layout, print_orientation, print_presentation_direction, print_quality, print_scaling

@dataclass
class PrinterDefaults(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The default color mode to use when printing the document. Valid values are described in the following table.
    color_mode: Optional[print_color_mode.PrintColorMode] = None
    # The default content (MIME) type to use when processing documents.
    content_type: Optional[str] = None
    # The default number of copies printed per job.
    copies_per_job: Optional[int] = None
    # The documentMimeType property
    document_mime_type: Optional[str] = None
    # The default resolution in DPI to use when printing the job.
    dpi: Optional[int] = None
    # The duplexConfiguration property
    duplex_configuration: Optional[print_duplex_configuration.PrintDuplexConfiguration] = None
    # The default duplex (double-sided) configuration to use when printing a document. Valid values are described in the following table.
    duplex_mode: Optional[print_duplex_mode.PrintDuplexMode] = None
    # The default set of finishings to apply to print jobs. Valid values are described in the following table.
    finishings: Optional[List[print_finishing.PrintFinishing]] = None
    # The default fitPdfToPage setting. True to fit each page of a PDF document to a physical sheet of media; false to let the printer decide how to lay out impressions.
    fit_pdf_to_page: Optional[bool] = None
    # The default input bin that serves as the paper source.
    input_bin: Optional[str] = None
    # The default media (such as paper) color to print the document on.
    media_color: Optional[str] = None
    # The default media size to use. Supports standard size names for ISO and ANSI media sizes. Valid values are listed in the printerCapabilities topic.
    media_size: Optional[str] = None
    # The default media (such as paper) type to print the document on.
    media_type: Optional[str] = None
    # The default direction to lay out pages when multiple pages are being printed per sheet. Valid values are described in the following table.
    multipage_layout: Optional[print_multipage_layout.PrintMultipageLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The default orientation to use when printing the document. Valid values are described in the following table.
    orientation: Optional[print_orientation.PrintOrientation] = None
    # The default output bin to place completed prints into. See the printer's capabilities for a list of supported output bins.
    output_bin: Optional[str] = None
    # The default number of document pages to print on each sheet.
    pages_per_sheet: Optional[int] = None
    # The pdfFitToPage property
    pdf_fit_to_page: Optional[bool] = None
    # The presentationDirection property
    presentation_direction: Optional[print_presentation_direction.PrintPresentationDirection] = None
    # The printColorConfiguration property
    print_color_configuration: Optional[print_color_configuration.PrintColorConfiguration] = None
    # The printQuality property
    print_quality: Optional[print_quality.PrintQuality] = None
    # The default quality to use when printing the document. Valid values are described in the following table.
    quality: Optional[print_quality.PrintQuality] = None
    # Specifies how the printer scales the document data to fit the requested media. Valid values are described in the following table.
    scaling: Optional[print_scaling.PrintScaling] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterDefaults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterDefaults
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrinterDefaults()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import print_color_configuration, print_color_mode, print_duplex_configuration, print_duplex_mode, print_finishing, print_multipage_layout, print_orientation, print_presentation_direction, print_quality, print_scaling

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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("colorMode", self.color_mode)
        writer.write_str_value("contentType", self.content_type)
        writer.write_int_value("copiesPerJob", self.copies_per_job)
        writer.write_str_value("documentMimeType", self.document_mime_type)
        writer.write_int_value("dpi", self.dpi)
        writer.write_enum_value("duplexConfiguration", self.duplex_configuration)
        writer.write_enum_value("duplexMode", self.duplex_mode)
        writer.write_collection_of_enum_values("finishings", self.finishings)
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
    

