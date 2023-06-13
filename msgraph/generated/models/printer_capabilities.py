from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import integer_range, printer_feed_direction, printer_feed_orientation, print_color_configuration, print_color_mode, print_duplex_configuration, print_duplex_mode, print_finishing, print_media_type, print_multipage_layout, print_orientation, print_presentation_direction, print_quality, print_scaling

@dataclass
class PrinterCapabilities(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A list of supported bottom margins(in microns) for the printer.
    bottom_margins: Optional[List[int]] = None
    # True if the printer supports collating when printing muliple copies of a multi-page document; false otherwise.
    collation: Optional[bool] = None
    # The color modes supported by the printer. Valid values are described in the following table.
    color_modes: Optional[List[print_color_mode.PrintColorMode]] = None
    # A list of supported content (MIME) types that the printer supports. It is not guaranteed that the Universal Print service supports printing all of these MIME types.
    content_types: Optional[List[str]] = None
    # The range of copies per job supported by the printer.
    copies_per_job: Optional[integer_range.IntegerRange] = None
    # The list of print resolutions in DPI that are supported by the printer.
    dpis: Optional[List[int]] = None
    # The list of duplex modes that are supported by the printer. Valid values are described in the following table.
    duplex_modes: Optional[List[print_duplex_mode.PrintDuplexMode]] = None
    # The feedDirections property
    feed_directions: Optional[List[printer_feed_direction.PrinterFeedDirection]] = None
    # The list of feed orientations that are supported by the printer.
    feed_orientations: Optional[List[printer_feed_orientation.PrinterFeedOrientation]] = None
    # Finishing processes the printer supports for a printed document.
    finishings: Optional[List[print_finishing.PrintFinishing]] = None
    # Supported input bins for the printer.
    input_bins: Optional[List[str]] = None
    # True if color printing is supported by the printer; false otherwise. Read-only.
    is_color_printing_supported: Optional[bool] = None
    # True if the printer supports printing by page ranges; false otherwise.
    is_page_range_supported: Optional[bool] = None
    # A list of supported left margins(in microns) for the printer.
    left_margins: Optional[List[int]] = None
    # The media (i.e., paper) colors supported by the printer.
    media_colors: Optional[List[str]] = None
    # The media sizes supported by the printer. Supports standard size names for ISO and ANSI media sizes. Valid values are in the following table.
    media_sizes: Optional[List[str]] = None
    # The media types supported by the printer.
    media_types: Optional[List[str]] = None
    # The presentation directions supported by the printer. Supported values are described in the following table.
    multipage_layouts: Optional[List[print_multipage_layout.PrintMultipageLayout]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The print orientations supported by the printer. Valid values are described in the following table.
    orientations: Optional[List[print_orientation.PrintOrientation]] = None
    # The printer's supported output bins (trays).
    output_bins: Optional[List[str]] = None
    # Supported number of Input Pages to impose upon a single Impression.
    pages_per_sheet: Optional[List[int]] = None
    # The print qualities supported by the printer.
    qualities: Optional[List[print_quality.PrintQuality]] = None
    # A list of supported right margins(in microns) for the printer.
    right_margins: Optional[List[int]] = None
    # Supported print scalings.
    scalings: Optional[List[print_scaling.PrintScaling]] = None
    # The supportedColorConfigurations property
    supported_color_configurations: Optional[List[print_color_configuration.PrintColorConfiguration]] = None
    # The supportedCopiesPerJob property
    supported_copies_per_job: Optional[integer_range.IntegerRange] = None
    # The supportedDocumentMimeTypes property
    supported_document_mime_types: Optional[List[str]] = None
    # The supportedDuplexConfigurations property
    supported_duplex_configurations: Optional[List[print_duplex_configuration.PrintDuplexConfiguration]] = None
    # The supportedFinishings property
    supported_finishings: Optional[List[print_finishing.PrintFinishing]] = None
    # The supportedMediaColors property
    supported_media_colors: Optional[List[str]] = None
    # The supportedMediaSizes property
    supported_media_sizes: Optional[List[str]] = None
    # The supportedMediaTypes property
    supported_media_types: Optional[List[print_media_type.PrintMediaType]] = None
    # The supportedOrientations property
    supported_orientations: Optional[List[print_orientation.PrintOrientation]] = None
    # The supportedOutputBins property
    supported_output_bins: Optional[List[str]] = None
    # The supportedPagesPerSheet property
    supported_pages_per_sheet: Optional[integer_range.IntegerRange] = None
    # The supportedPresentationDirections property
    supported_presentation_directions: Optional[List[print_presentation_direction.PrintPresentationDirection]] = None
    # The supportedPrintQualities property
    supported_print_qualities: Optional[List[print_quality.PrintQuality]] = None
    # True if the printer supports scaling PDF pages to match the print media size; false otherwise.
    supports_fit_pdf_to_page: Optional[bool] = None
    # A list of supported top margins(in microns) for the printer.
    top_margins: Optional[List[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterCapabilities:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterCapabilities
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterCapabilities()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import integer_range, printer_feed_direction, printer_feed_orientation, print_color_configuration, print_color_mode, print_duplex_configuration, print_duplex_mode, print_finishing, print_media_type, print_multipage_layout, print_orientation, print_presentation_direction, print_quality, print_scaling

        fields: Dict[str, Callable[[Any], None]] = {
            "bottomMargins": lambda n : setattr(self, 'bottom_margins', n.get_collection_of_primitive_values(int)),
            "collation": lambda n : setattr(self, 'collation', n.get_bool_value()),
            "colorModes": lambda n : setattr(self, 'color_modes', n.get_collection_of_enum_values(print_color_mode.PrintColorMode)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_primitive_values(str)),
            "copiesPerJob": lambda n : setattr(self, 'copies_per_job', n.get_object_value(integer_range.IntegerRange)),
            "dpis": lambda n : setattr(self, 'dpis', n.get_collection_of_primitive_values(int)),
            "duplexModes": lambda n : setattr(self, 'duplex_modes', n.get_collection_of_enum_values(print_duplex_mode.PrintDuplexMode)),
            "feedDirections": lambda n : setattr(self, 'feed_directions', n.get_collection_of_enum_values(printer_feed_direction.PrinterFeedDirection)),
            "feedOrientations": lambda n : setattr(self, 'feed_orientations', n.get_collection_of_enum_values(printer_feed_orientation.PrinterFeedOrientation)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(print_finishing.PrintFinishing)),
            "inputBins": lambda n : setattr(self, 'input_bins', n.get_collection_of_primitive_values(str)),
            "isColorPrintingSupported": lambda n : setattr(self, 'is_color_printing_supported', n.get_bool_value()),
            "isPageRangeSupported": lambda n : setattr(self, 'is_page_range_supported', n.get_bool_value()),
            "leftMargins": lambda n : setattr(self, 'left_margins', n.get_collection_of_primitive_values(int)),
            "mediaColors": lambda n : setattr(self, 'media_colors', n.get_collection_of_primitive_values(str)),
            "mediaSizes": lambda n : setattr(self, 'media_sizes', n.get_collection_of_primitive_values(str)),
            "mediaTypes": lambda n : setattr(self, 'media_types', n.get_collection_of_primitive_values(str)),
            "multipageLayouts": lambda n : setattr(self, 'multipage_layouts', n.get_collection_of_enum_values(print_multipage_layout.PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientations": lambda n : setattr(self, 'orientations', n.get_collection_of_enum_values(print_orientation.PrintOrientation)),
            "outputBins": lambda n : setattr(self, 'output_bins', n.get_collection_of_primitive_values(str)),
            "pagesPerSheet": lambda n : setattr(self, 'pages_per_sheet', n.get_collection_of_primitive_values(int)),
            "qualities": lambda n : setattr(self, 'qualities', n.get_collection_of_enum_values(print_quality.PrintQuality)),
            "rightMargins": lambda n : setattr(self, 'right_margins', n.get_collection_of_primitive_values(int)),
            "scalings": lambda n : setattr(self, 'scalings', n.get_collection_of_enum_values(print_scaling.PrintScaling)),
            "supportedColorConfigurations": lambda n : setattr(self, 'supported_color_configurations', n.get_collection_of_enum_values(print_color_configuration.PrintColorConfiguration)),
            "supportedCopiesPerJob": lambda n : setattr(self, 'supported_copies_per_job', n.get_object_value(integer_range.IntegerRange)),
            "supportedDocumentMimeTypes": lambda n : setattr(self, 'supported_document_mime_types', n.get_collection_of_primitive_values(str)),
            "supportedDuplexConfigurations": lambda n : setattr(self, 'supported_duplex_configurations', n.get_collection_of_enum_values(print_duplex_configuration.PrintDuplexConfiguration)),
            "supportedFinishings": lambda n : setattr(self, 'supported_finishings', n.get_collection_of_enum_values(print_finishing.PrintFinishing)),
            "supportedMediaColors": lambda n : setattr(self, 'supported_media_colors', n.get_collection_of_primitive_values(str)),
            "supportedMediaSizes": lambda n : setattr(self, 'supported_media_sizes', n.get_collection_of_primitive_values(str)),
            "supportedMediaTypes": lambda n : setattr(self, 'supported_media_types', n.get_collection_of_enum_values(print_media_type.PrintMediaType)),
            "supportedOrientations": lambda n : setattr(self, 'supported_orientations', n.get_collection_of_enum_values(print_orientation.PrintOrientation)),
            "supportedOutputBins": lambda n : setattr(self, 'supported_output_bins', n.get_collection_of_primitive_values(str)),
            "supportedPagesPerSheet": lambda n : setattr(self, 'supported_pages_per_sheet', n.get_object_value(integer_range.IntegerRange)),
            "supportedPresentationDirections": lambda n : setattr(self, 'supported_presentation_directions', n.get_collection_of_enum_values(print_presentation_direction.PrintPresentationDirection)),
            "supportedPrintQualities": lambda n : setattr(self, 'supported_print_qualities', n.get_collection_of_enum_values(print_quality.PrintQuality)),
            "supportsFitPdfToPage": lambda n : setattr(self, 'supports_fit_pdf_to_page', n.get_bool_value()),
            "topMargins": lambda n : setattr(self, 'top_margins', n.get_collection_of_primitive_values(int)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_primitive_values("bottomMargins", self.bottom_margins)
        writer.write_bool_value("collation", self.collation)
        writer.write_enum_value("colorModes", self.color_modes)
        writer.write_collection_of_primitive_values("contentTypes", self.content_types)
        writer.write_object_value("copiesPerJob", self.copies_per_job)
        writer.write_collection_of_primitive_values("dpis", self.dpis)
        writer.write_enum_value("duplexModes", self.duplex_modes)
        writer.write_enum_value("feedDirections", self.feed_directions)
        writer.write_enum_value("feedOrientations", self.feed_orientations)
        writer.write_enum_value("finishings", self.finishings)
        writer.write_collection_of_primitive_values("inputBins", self.input_bins)
        writer.write_bool_value("isColorPrintingSupported", self.is_color_printing_supported)
        writer.write_bool_value("isPageRangeSupported", self.is_page_range_supported)
        writer.write_collection_of_primitive_values("leftMargins", self.left_margins)
        writer.write_collection_of_primitive_values("mediaColors", self.media_colors)
        writer.write_collection_of_primitive_values("mediaSizes", self.media_sizes)
        writer.write_collection_of_primitive_values("mediaTypes", self.media_types)
        writer.write_enum_value("multipageLayouts", self.multipage_layouts)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("orientations", self.orientations)
        writer.write_collection_of_primitive_values("outputBins", self.output_bins)
        writer.write_collection_of_primitive_values("pagesPerSheet", self.pages_per_sheet)
        writer.write_enum_value("qualities", self.qualities)
        writer.write_collection_of_primitive_values("rightMargins", self.right_margins)
        writer.write_enum_value("scalings", self.scalings)
        writer.write_enum_value("supportedColorConfigurations", self.supported_color_configurations)
        writer.write_object_value("supportedCopiesPerJob", self.supported_copies_per_job)
        writer.write_collection_of_primitive_values("supportedDocumentMimeTypes", self.supported_document_mime_types)
        writer.write_enum_value("supportedDuplexConfigurations", self.supported_duplex_configurations)
        writer.write_enum_value("supportedFinishings", self.supported_finishings)
        writer.write_collection_of_primitive_values("supportedMediaColors", self.supported_media_colors)
        writer.write_collection_of_primitive_values("supportedMediaSizes", self.supported_media_sizes)
        writer.write_enum_value("supportedMediaTypes", self.supported_media_types)
        writer.write_enum_value("supportedOrientations", self.supported_orientations)
        writer.write_collection_of_primitive_values("supportedOutputBins", self.supported_output_bins)
        writer.write_object_value("supportedPagesPerSheet", self.supported_pages_per_sheet)
        writer.write_enum_value("supportedPresentationDirections", self.supported_presentation_directions)
        writer.write_enum_value("supportedPrintQualities", self.supported_print_qualities)
        writer.write_bool_value("supportsFitPdfToPage", self.supports_fit_pdf_to_page)
        writer.write_collection_of_primitive_values("topMargins", self.top_margins)
        writer.write_additional_data_value(self.additional_data)
    

