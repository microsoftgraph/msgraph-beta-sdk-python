from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .printer_defaults_color_mode import PrinterDefaults_colorMode
    from .printer_defaults_duplex_configuration import PrinterDefaults_duplexConfiguration
    from .printer_defaults_duplex_mode import PrinterDefaults_duplexMode
    from .printer_defaults_finishings import PrinterDefaults_finishings
    from .printer_defaults_multipage_layout import PrinterDefaults_multipageLayout
    from .printer_defaults_orientation import PrinterDefaults_orientation
    from .printer_defaults_presentation_direction import PrinterDefaults_presentationDirection
    from .printer_defaults_print_color_configuration import PrinterDefaults_printColorConfiguration
    from .printer_defaults_print_quality import PrinterDefaults_printQuality
    from .printer_defaults_quality import PrinterDefaults_quality
    from .printer_defaults_scaling import PrinterDefaults_scaling

@dataclass
class PrinterDefaults(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The default color mode to use when printing the document. Valid values are described in the following table.
    color_mode: Optional[PrinterDefaults_colorMode] = None
    # The default content (MIME) type to use when processing documents.
    content_type: Optional[str] = None
    # The default number of copies printed per job.
    copies_per_job: Optional[int] = None
    # The documentMimeType property
    document_mime_type: Optional[str] = None
    # The default resolution in DPI to use when printing the job.
    dpi: Optional[int] = None
    # The duplexConfiguration property
    duplex_configuration: Optional[PrinterDefaults_duplexConfiguration] = None
    # The default duplex (double-sided) configuration to use when printing a document. Valid values are described in the following table.
    duplex_mode: Optional[PrinterDefaults_duplexMode] = None
    # The default set of finishings to apply to print jobs. Valid values are described in the following table.
    finishings: Optional[List[PrinterDefaults_finishings]] = None
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
    multipage_layout: Optional[PrinterDefaults_multipageLayout] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The default orientation to use when printing the document. Valid values are described in the following table.
    orientation: Optional[PrinterDefaults_orientation] = None
    # The default output bin to place completed prints into. See the printer's capabilities for a list of supported output bins.
    output_bin: Optional[str] = None
    # The default number of document pages to print on each sheet.
    pages_per_sheet: Optional[int] = None
    # The pdfFitToPage property
    pdf_fit_to_page: Optional[bool] = None
    # The presentationDirection property
    presentation_direction: Optional[PrinterDefaults_presentationDirection] = None
    # The printColorConfiguration property
    print_color_configuration: Optional[PrinterDefaults_printColorConfiguration] = None
    # The printQuality property
    print_quality: Optional[PrinterDefaults_printQuality] = None
    # The default quality to use when printing the document. Valid values are described in the following table.
    quality: Optional[PrinterDefaults_quality] = None
    # Specifies how the printer scales the document data to fit the requested media. Valid values are described in the following table.
    scaling: Optional[PrinterDefaults_scaling] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterDefaults:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
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
        from .printer_defaults_color_mode import PrinterDefaults_colorMode
        from .printer_defaults_duplex_configuration import PrinterDefaults_duplexConfiguration
        from .printer_defaults_duplex_mode import PrinterDefaults_duplexMode
        from .printer_defaults_finishings import PrinterDefaults_finishings
        from .printer_defaults_multipage_layout import PrinterDefaults_multipageLayout
        from .printer_defaults_orientation import PrinterDefaults_orientation
        from .printer_defaults_presentation_direction import PrinterDefaults_presentationDirection
        from .printer_defaults_print_color_configuration import PrinterDefaults_printColorConfiguration
        from .printer_defaults_print_quality import PrinterDefaults_printQuality
        from .printer_defaults_quality import PrinterDefaults_quality
        from .printer_defaults_scaling import PrinterDefaults_scaling

        from .printer_defaults_color_mode import PrinterDefaults_colorMode
        from .printer_defaults_duplex_configuration import PrinterDefaults_duplexConfiguration
        from .printer_defaults_duplex_mode import PrinterDefaults_duplexMode
        from .printer_defaults_finishings import PrinterDefaults_finishings
        from .printer_defaults_multipage_layout import PrinterDefaults_multipageLayout
        from .printer_defaults_orientation import PrinterDefaults_orientation
        from .printer_defaults_presentation_direction import PrinterDefaults_presentationDirection
        from .printer_defaults_print_color_configuration import PrinterDefaults_printColorConfiguration
        from .printer_defaults_print_quality import PrinterDefaults_printQuality
        from .printer_defaults_quality import PrinterDefaults_quality
        from .printer_defaults_scaling import PrinterDefaults_scaling

        fields: Dict[str, Callable[[Any], None]] = {
            "colorMode": lambda n : setattr(self, 'color_mode', n.get_enum_value(PrinterDefaults_colorMode)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "copiesPerJob": lambda n : setattr(self, 'copies_per_job', n.get_int_value()),
            "documentMimeType": lambda n : setattr(self, 'document_mime_type', n.get_str_value()),
            "dpi": lambda n : setattr(self, 'dpi', n.get_int_value()),
            "duplexConfiguration": lambda n : setattr(self, 'duplex_configuration', n.get_enum_value(PrinterDefaults_duplexConfiguration)),
            "duplexMode": lambda n : setattr(self, 'duplex_mode', n.get_enum_value(PrinterDefaults_duplexMode)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(PrinterDefaults_finishings)),
            "fitPdfToPage": lambda n : setattr(self, 'fit_pdf_to_page', n.get_bool_value()),
            "inputBin": lambda n : setattr(self, 'input_bin', n.get_str_value()),
            "mediaColor": lambda n : setattr(self, 'media_color', n.get_str_value()),
            "mediaSize": lambda n : setattr(self, 'media_size', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "multipageLayout": lambda n : setattr(self, 'multipage_layout', n.get_enum_value(PrinterDefaults_multipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientation": lambda n : setattr(self, 'orientation', n.get_enum_value(PrinterDefaults_orientation)),
            "outputBin": lambda n : setattr(self, 'output_bin', n.get_str_value()),
            "pagesPerSheet": lambda n : setattr(self, 'pages_per_sheet', n.get_int_value()),
            "pdfFitToPage": lambda n : setattr(self, 'pdf_fit_to_page', n.get_bool_value()),
            "presentationDirection": lambda n : setattr(self, 'presentation_direction', n.get_enum_value(PrinterDefaults_presentationDirection)),
            "printColorConfiguration": lambda n : setattr(self, 'print_color_configuration', n.get_enum_value(PrinterDefaults_printColorConfiguration)),
            "printQuality": lambda n : setattr(self, 'print_quality', n.get_enum_value(PrinterDefaults_printQuality)),
            "quality": lambda n : setattr(self, 'quality', n.get_enum_value(PrinterDefaults_quality)),
            "scaling": lambda n : setattr(self, 'scaling', n.get_enum_value(PrinterDefaults_scaling)),
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
    

