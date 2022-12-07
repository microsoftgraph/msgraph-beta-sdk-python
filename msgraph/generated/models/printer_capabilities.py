from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

integer_range = lazy_import('msgraph.generated.models.integer_range')
print_color_configuration = lazy_import('msgraph.generated.models.print_color_configuration')
print_color_mode = lazy_import('msgraph.generated.models.print_color_mode')
print_duplex_configuration = lazy_import('msgraph.generated.models.print_duplex_configuration')
print_duplex_mode = lazy_import('msgraph.generated.models.print_duplex_mode')
print_finishing = lazy_import('msgraph.generated.models.print_finishing')
print_media_type = lazy_import('msgraph.generated.models.print_media_type')
print_multipage_layout = lazy_import('msgraph.generated.models.print_multipage_layout')
print_orientation = lazy_import('msgraph.generated.models.print_orientation')
print_presentation_direction = lazy_import('msgraph.generated.models.print_presentation_direction')
print_quality = lazy_import('msgraph.generated.models.print_quality')
print_scaling = lazy_import('msgraph.generated.models.print_scaling')
printer_feed_direction = lazy_import('msgraph.generated.models.printer_feed_direction')
printer_feed_orientation = lazy_import('msgraph.generated.models.printer_feed_orientation')

class PrinterCapabilities(AdditionalDataHolder, Parsable):
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
    def bottom_margins(self,) -> Optional[List[int]]:
        """
        Gets the bottomMargins property value. A list of supported bottom margins(in microns) for the printer.
        Returns: Optional[List[int]]
        """
        return self._bottom_margins
    
    @bottom_margins.setter
    def bottom_margins(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the bottomMargins property value. A list of supported bottom margins(in microns) for the printer.
        Args:
            value: Value to set for the bottomMargins property.
        """
        self._bottom_margins = value
    
    @property
    def collation(self,) -> Optional[bool]:
        """
        Gets the collation property value. True if the printer supports collating when printing muliple copies of a multi-page document; false otherwise.
        Returns: Optional[bool]
        """
        return self._collation
    
    @collation.setter
    def collation(self,value: Optional[bool] = None) -> None:
        """
        Sets the collation property value. True if the printer supports collating when printing muliple copies of a multi-page document; false otherwise.
        Args:
            value: Value to set for the collation property.
        """
        self._collation = value
    
    @property
    def color_modes(self,) -> Optional[List[print_color_mode.PrintColorMode]]:
        """
        Gets the colorModes property value. The color modes supported by the printer. Valid values are described in the following table.
        Returns: Optional[List[print_color_mode.PrintColorMode]]
        """
        return self._color_modes
    
    @color_modes.setter
    def color_modes(self,value: Optional[List[print_color_mode.PrintColorMode]] = None) -> None:
        """
        Sets the colorModes property value. The color modes supported by the printer. Valid values are described in the following table.
        Args:
            value: Value to set for the colorModes property.
        """
        self._color_modes = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printerCapabilities and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of supported bottom margins(in microns) for the printer.
        self._bottom_margins: Optional[List[int]] = None
        # True if the printer supports collating when printing muliple copies of a multi-page document; false otherwise.
        self._collation: Optional[bool] = None
        # The color modes supported by the printer. Valid values are described in the following table.
        self._color_modes: Optional[List[print_color_mode.PrintColorMode]] = None
        # A list of supported content (MIME) types that the printer supports. It is not guaranteed that the Universal Print service supports printing all of these MIME types.
        self._content_types: Optional[List[str]] = None
        # The range of copies per job supported by the printer.
        self._copies_per_job: Optional[integer_range.IntegerRange] = None
        # The list of print resolutions in DPI that are supported by the printer.
        self._dpis: Optional[List[int]] = None
        # The list of duplex modes that are supported by the printer. Valid values are described in the following table.
        self._duplex_modes: Optional[List[print_duplex_mode.PrintDuplexMode]] = None
        # The feedDirections property
        self._feed_directions: Optional[List[printer_feed_direction.PrinterFeedDirection]] = None
        # The list of feed orientations that are supported by the printer.
        self._feed_orientations: Optional[List[printer_feed_orientation.PrinterFeedOrientation]] = None
        # Finishing processes the printer supports for a printed document.
        self._finishings: Optional[List[print_finishing.PrintFinishing]] = None
        # Supported input bins for the printer.
        self._input_bins: Optional[List[str]] = None
        # True if color printing is supported by the printer; false otherwise. Read-only.
        self._is_color_printing_supported: Optional[bool] = None
        # True if the printer supports printing by page ranges; false otherwise.
        self._is_page_range_supported: Optional[bool] = None
        # A list of supported left margins(in microns) for the printer.
        self._left_margins: Optional[List[int]] = None
        # The media (i.e., paper) colors supported by the printer.
        self._media_colors: Optional[List[str]] = None
        # The media sizes supported by the printer. Supports standard size names for ISO and ANSI media sizes. Valid values are in the following table.
        self._media_sizes: Optional[List[str]] = None
        # The media types supported by the printer.
        self._media_types: Optional[List[str]] = None
        # The presentation directions supported by the printer. Supported values are described in the following table.
        self._multipage_layouts: Optional[List[print_multipage_layout.PrintMultipageLayout]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The print orientations supported by the printer. Valid values are described in the following table.
        self._orientations: Optional[List[print_orientation.PrintOrientation]] = None
        # The printer's supported output bins (trays).
        self._output_bins: Optional[List[str]] = None
        # Supported number of Input Pages to impose upon a single Impression.
        self._pages_per_sheet: Optional[List[int]] = None
        # The print qualities supported by the printer.
        self._qualities: Optional[List[print_quality.PrintQuality]] = None
        # A list of supported right margins(in microns) for the printer.
        self._right_margins: Optional[List[int]] = None
        # Supported print scalings.
        self._scalings: Optional[List[print_scaling.PrintScaling]] = None
        # The supportedColorConfigurations property
        self._supported_color_configurations: Optional[List[print_color_configuration.PrintColorConfiguration]] = None
        # The supportedCopiesPerJob property
        self._supported_copies_per_job: Optional[integer_range.IntegerRange] = None
        # The supportedDocumentMimeTypes property
        self._supported_document_mime_types: Optional[List[str]] = None
        # The supportedDuplexConfigurations property
        self._supported_duplex_configurations: Optional[List[print_duplex_configuration.PrintDuplexConfiguration]] = None
        # The supportedFinishings property
        self._supported_finishings: Optional[List[print_finishing.PrintFinishing]] = None
        # The supportedMediaColors property
        self._supported_media_colors: Optional[List[str]] = None
        # The supportedMediaSizes property
        self._supported_media_sizes: Optional[List[str]] = None
        # The supportedMediaTypes property
        self._supported_media_types: Optional[List[print_media_type.PrintMediaType]] = None
        # The supportedOrientations property
        self._supported_orientations: Optional[List[print_orientation.PrintOrientation]] = None
        # The supportedOutputBins property
        self._supported_output_bins: Optional[List[str]] = None
        # The supportedPagesPerSheet property
        self._supported_pages_per_sheet: Optional[integer_range.IntegerRange] = None
        # The supportedPresentationDirections property
        self._supported_presentation_directions: Optional[List[print_presentation_direction.PrintPresentationDirection]] = None
        # The supportedPrintQualities property
        self._supported_print_qualities: Optional[List[print_quality.PrintQuality]] = None
        # True if the printer supports scaling PDF pages to match the print media size; false otherwise.
        self._supports_fit_pdf_to_page: Optional[bool] = None
        # A list of supported top margins(in microns) for the printer.
        self._top_margins: Optional[List[int]] = None
    
    @property
    def content_types(self,) -> Optional[List[str]]:
        """
        Gets the contentTypes property value. A list of supported content (MIME) types that the printer supports. It is not guaranteed that the Universal Print service supports printing all of these MIME types.
        Returns: Optional[List[str]]
        """
        return self._content_types
    
    @content_types.setter
    def content_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the contentTypes property value. A list of supported content (MIME) types that the printer supports. It is not guaranteed that the Universal Print service supports printing all of these MIME types.
        Args:
            value: Value to set for the contentTypes property.
        """
        self._content_types = value
    
    @property
    def copies_per_job(self,) -> Optional[integer_range.IntegerRange]:
        """
        Gets the copiesPerJob property value. The range of copies per job supported by the printer.
        Returns: Optional[integer_range.IntegerRange]
        """
        return self._copies_per_job
    
    @copies_per_job.setter
    def copies_per_job(self,value: Optional[integer_range.IntegerRange] = None) -> None:
        """
        Sets the copiesPerJob property value. The range of copies per job supported by the printer.
        Args:
            value: Value to set for the copiesPerJob property.
        """
        self._copies_per_job = value
    
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
    
    @property
    def dpis(self,) -> Optional[List[int]]:
        """
        Gets the dpis property value. The list of print resolutions in DPI that are supported by the printer.
        Returns: Optional[List[int]]
        """
        return self._dpis
    
    @dpis.setter
    def dpis(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the dpis property value. The list of print resolutions in DPI that are supported by the printer.
        Args:
            value: Value to set for the dpis property.
        """
        self._dpis = value
    
    @property
    def duplex_modes(self,) -> Optional[List[print_duplex_mode.PrintDuplexMode]]:
        """
        Gets the duplexModes property value. The list of duplex modes that are supported by the printer. Valid values are described in the following table.
        Returns: Optional[List[print_duplex_mode.PrintDuplexMode]]
        """
        return self._duplex_modes
    
    @duplex_modes.setter
    def duplex_modes(self,value: Optional[List[print_duplex_mode.PrintDuplexMode]] = None) -> None:
        """
        Sets the duplexModes property value. The list of duplex modes that are supported by the printer. Valid values are described in the following table.
        Args:
            value: Value to set for the duplexModes property.
        """
        self._duplex_modes = value
    
    @property
    def feed_directions(self,) -> Optional[List[printer_feed_direction.PrinterFeedDirection]]:
        """
        Gets the feedDirections property value. The feedDirections property
        Returns: Optional[List[printer_feed_direction.PrinterFeedDirection]]
        """
        return self._feed_directions
    
    @feed_directions.setter
    def feed_directions(self,value: Optional[List[printer_feed_direction.PrinterFeedDirection]] = None) -> None:
        """
        Sets the feedDirections property value. The feedDirections property
        Args:
            value: Value to set for the feedDirections property.
        """
        self._feed_directions = value
    
    @property
    def feed_orientations(self,) -> Optional[List[printer_feed_orientation.PrinterFeedOrientation]]:
        """
        Gets the feedOrientations property value. The list of feed orientations that are supported by the printer.
        Returns: Optional[List[printer_feed_orientation.PrinterFeedOrientation]]
        """
        return self._feed_orientations
    
    @feed_orientations.setter
    def feed_orientations(self,value: Optional[List[printer_feed_orientation.PrinterFeedOrientation]] = None) -> None:
        """
        Sets the feedOrientations property value. The list of feed orientations that are supported by the printer.
        Args:
            value: Value to set for the feedOrientations property.
        """
        self._feed_orientations = value
    
    @property
    def finishings(self,) -> Optional[List[print_finishing.PrintFinishing]]:
        """
        Gets the finishings property value. Finishing processes the printer supports for a printed document.
        Returns: Optional[List[print_finishing.PrintFinishing]]
        """
        return self._finishings
    
    @finishings.setter
    def finishings(self,value: Optional[List[print_finishing.PrintFinishing]] = None) -> None:
        """
        Sets the finishings property value. Finishing processes the printer supports for a printed document.
        Args:
            value: Value to set for the finishings property.
        """
        self._finishings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bottom_margins": lambda n : setattr(self, 'bottom_margins', n.get_collection_of_primitive_values(int)),
            "collation": lambda n : setattr(self, 'collation', n.get_bool_value()),
            "color_modes": lambda n : setattr(self, 'color_modes', n.get_collection_of_enum_values(print_color_mode.PrintColorMode)),
            "content_types": lambda n : setattr(self, 'content_types', n.get_collection_of_primitive_values(str)),
            "copies_per_job": lambda n : setattr(self, 'copies_per_job', n.get_object_value(integer_range.IntegerRange)),
            "dpis": lambda n : setattr(self, 'dpis', n.get_collection_of_primitive_values(int)),
            "duplex_modes": lambda n : setattr(self, 'duplex_modes', n.get_collection_of_enum_values(print_duplex_mode.PrintDuplexMode)),
            "feed_directions": lambda n : setattr(self, 'feed_directions', n.get_collection_of_enum_values(printer_feed_direction.PrinterFeedDirection)),
            "feed_orientations": lambda n : setattr(self, 'feed_orientations', n.get_collection_of_enum_values(printer_feed_orientation.PrinterFeedOrientation)),
            "finishings": lambda n : setattr(self, 'finishings', n.get_collection_of_enum_values(print_finishing.PrintFinishing)),
            "input_bins": lambda n : setattr(self, 'input_bins', n.get_collection_of_primitive_values(str)),
            "is_color_printing_supported": lambda n : setattr(self, 'is_color_printing_supported', n.get_bool_value()),
            "is_page_range_supported": lambda n : setattr(self, 'is_page_range_supported', n.get_bool_value()),
            "left_margins": lambda n : setattr(self, 'left_margins', n.get_collection_of_primitive_values(int)),
            "media_colors": lambda n : setattr(self, 'media_colors', n.get_collection_of_primitive_values(str)),
            "media_sizes": lambda n : setattr(self, 'media_sizes', n.get_collection_of_primitive_values(str)),
            "media_types": lambda n : setattr(self, 'media_types', n.get_collection_of_primitive_values(str)),
            "multipage_layouts": lambda n : setattr(self, 'multipage_layouts', n.get_collection_of_enum_values(print_multipage_layout.PrintMultipageLayout)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientations": lambda n : setattr(self, 'orientations', n.get_collection_of_enum_values(print_orientation.PrintOrientation)),
            "output_bins": lambda n : setattr(self, 'output_bins', n.get_collection_of_primitive_values(str)),
            "pages_per_sheet": lambda n : setattr(self, 'pages_per_sheet', n.get_collection_of_primitive_values(int)),
            "qualities": lambda n : setattr(self, 'qualities', n.get_collection_of_enum_values(print_quality.PrintQuality)),
            "right_margins": lambda n : setattr(self, 'right_margins', n.get_collection_of_primitive_values(int)),
            "scalings": lambda n : setattr(self, 'scalings', n.get_collection_of_enum_values(print_scaling.PrintScaling)),
            "supported_color_configurations": lambda n : setattr(self, 'supported_color_configurations', n.get_collection_of_enum_values(print_color_configuration.PrintColorConfiguration)),
            "supported_copies_per_job": lambda n : setattr(self, 'supported_copies_per_job', n.get_object_value(integer_range.IntegerRange)),
            "supported_document_mime_types": lambda n : setattr(self, 'supported_document_mime_types', n.get_collection_of_primitive_values(str)),
            "supported_duplex_configurations": lambda n : setattr(self, 'supported_duplex_configurations', n.get_collection_of_enum_values(print_duplex_configuration.PrintDuplexConfiguration)),
            "supported_finishings": lambda n : setattr(self, 'supported_finishings', n.get_collection_of_enum_values(print_finishing.PrintFinishing)),
            "supported_media_colors": lambda n : setattr(self, 'supported_media_colors', n.get_collection_of_primitive_values(str)),
            "supported_media_sizes": lambda n : setattr(self, 'supported_media_sizes', n.get_collection_of_primitive_values(str)),
            "supported_media_types": lambda n : setattr(self, 'supported_media_types', n.get_collection_of_enum_values(print_media_type.PrintMediaType)),
            "supported_orientations": lambda n : setattr(self, 'supported_orientations', n.get_collection_of_enum_values(print_orientation.PrintOrientation)),
            "supported_output_bins": lambda n : setattr(self, 'supported_output_bins', n.get_collection_of_primitive_values(str)),
            "supported_pages_per_sheet": lambda n : setattr(self, 'supported_pages_per_sheet', n.get_object_value(integer_range.IntegerRange)),
            "supported_presentation_directions": lambda n : setattr(self, 'supported_presentation_directions', n.get_collection_of_enum_values(print_presentation_direction.PrintPresentationDirection)),
            "supported_print_qualities": lambda n : setattr(self, 'supported_print_qualities', n.get_collection_of_enum_values(print_quality.PrintQuality)),
            "supports_fit_pdf_to_page": lambda n : setattr(self, 'supports_fit_pdf_to_page', n.get_bool_value()),
            "top_margins": lambda n : setattr(self, 'top_margins', n.get_collection_of_primitive_values(int)),
        }
        return fields
    
    @property
    def input_bins(self,) -> Optional[List[str]]:
        """
        Gets the inputBins property value. Supported input bins for the printer.
        Returns: Optional[List[str]]
        """
        return self._input_bins
    
    @input_bins.setter
    def input_bins(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the inputBins property value. Supported input bins for the printer.
        Args:
            value: Value to set for the inputBins property.
        """
        self._input_bins = value
    
    @property
    def is_color_printing_supported(self,) -> Optional[bool]:
        """
        Gets the isColorPrintingSupported property value. True if color printing is supported by the printer; false otherwise. Read-only.
        Returns: Optional[bool]
        """
        return self._is_color_printing_supported
    
    @is_color_printing_supported.setter
    def is_color_printing_supported(self,value: Optional[bool] = None) -> None:
        """
        Sets the isColorPrintingSupported property value. True if color printing is supported by the printer; false otherwise. Read-only.
        Args:
            value: Value to set for the isColorPrintingSupported property.
        """
        self._is_color_printing_supported = value
    
    @property
    def is_page_range_supported(self,) -> Optional[bool]:
        """
        Gets the isPageRangeSupported property value. True if the printer supports printing by page ranges; false otherwise.
        Returns: Optional[bool]
        """
        return self._is_page_range_supported
    
    @is_page_range_supported.setter
    def is_page_range_supported(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPageRangeSupported property value. True if the printer supports printing by page ranges; false otherwise.
        Args:
            value: Value to set for the isPageRangeSupported property.
        """
        self._is_page_range_supported = value
    
    @property
    def left_margins(self,) -> Optional[List[int]]:
        """
        Gets the leftMargins property value. A list of supported left margins(in microns) for the printer.
        Returns: Optional[List[int]]
        """
        return self._left_margins
    
    @left_margins.setter
    def left_margins(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the leftMargins property value. A list of supported left margins(in microns) for the printer.
        Args:
            value: Value to set for the leftMargins property.
        """
        self._left_margins = value
    
    @property
    def media_colors(self,) -> Optional[List[str]]:
        """
        Gets the mediaColors property value. The media (i.e., paper) colors supported by the printer.
        Returns: Optional[List[str]]
        """
        return self._media_colors
    
    @media_colors.setter
    def media_colors(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the mediaColors property value. The media (i.e., paper) colors supported by the printer.
        Args:
            value: Value to set for the mediaColors property.
        """
        self._media_colors = value
    
    @property
    def media_sizes(self,) -> Optional[List[str]]:
        """
        Gets the mediaSizes property value. The media sizes supported by the printer. Supports standard size names for ISO and ANSI media sizes. Valid values are in the following table.
        Returns: Optional[List[str]]
        """
        return self._media_sizes
    
    @media_sizes.setter
    def media_sizes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the mediaSizes property value. The media sizes supported by the printer. Supports standard size names for ISO and ANSI media sizes. Valid values are in the following table.
        Args:
            value: Value to set for the mediaSizes property.
        """
        self._media_sizes = value
    
    @property
    def media_types(self,) -> Optional[List[str]]:
        """
        Gets the mediaTypes property value. The media types supported by the printer.
        Returns: Optional[List[str]]
        """
        return self._media_types
    
    @media_types.setter
    def media_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the mediaTypes property value. The media types supported by the printer.
        Args:
            value: Value to set for the mediaTypes property.
        """
        self._media_types = value
    
    @property
    def multipage_layouts(self,) -> Optional[List[print_multipage_layout.PrintMultipageLayout]]:
        """
        Gets the multipageLayouts property value. The presentation directions supported by the printer. Supported values are described in the following table.
        Returns: Optional[List[print_multipage_layout.PrintMultipageLayout]]
        """
        return self._multipage_layouts
    
    @multipage_layouts.setter
    def multipage_layouts(self,value: Optional[List[print_multipage_layout.PrintMultipageLayout]] = None) -> None:
        """
        Sets the multipageLayouts property value. The presentation directions supported by the printer. Supported values are described in the following table.
        Args:
            value: Value to set for the multipageLayouts property.
        """
        self._multipage_layouts = value
    
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
    def orientations(self,) -> Optional[List[print_orientation.PrintOrientation]]:
        """
        Gets the orientations property value. The print orientations supported by the printer. Valid values are described in the following table.
        Returns: Optional[List[print_orientation.PrintOrientation]]
        """
        return self._orientations
    
    @orientations.setter
    def orientations(self,value: Optional[List[print_orientation.PrintOrientation]] = None) -> None:
        """
        Sets the orientations property value. The print orientations supported by the printer. Valid values are described in the following table.
        Args:
            value: Value to set for the orientations property.
        """
        self._orientations = value
    
    @property
    def output_bins(self,) -> Optional[List[str]]:
        """
        Gets the outputBins property value. The printer's supported output bins (trays).
        Returns: Optional[List[str]]
        """
        return self._output_bins
    
    @output_bins.setter
    def output_bins(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the outputBins property value. The printer's supported output bins (trays).
        Args:
            value: Value to set for the outputBins property.
        """
        self._output_bins = value
    
    @property
    def pages_per_sheet(self,) -> Optional[List[int]]:
        """
        Gets the pagesPerSheet property value. Supported number of Input Pages to impose upon a single Impression.
        Returns: Optional[List[int]]
        """
        return self._pages_per_sheet
    
    @pages_per_sheet.setter
    def pages_per_sheet(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the pagesPerSheet property value. Supported number of Input Pages to impose upon a single Impression.
        Args:
            value: Value to set for the pagesPerSheet property.
        """
        self._pages_per_sheet = value
    
    @property
    def qualities(self,) -> Optional[List[print_quality.PrintQuality]]:
        """
        Gets the qualities property value. The print qualities supported by the printer.
        Returns: Optional[List[print_quality.PrintQuality]]
        """
        return self._qualities
    
    @qualities.setter
    def qualities(self,value: Optional[List[print_quality.PrintQuality]] = None) -> None:
        """
        Sets the qualities property value. The print qualities supported by the printer.
        Args:
            value: Value to set for the qualities property.
        """
        self._qualities = value
    
    @property
    def right_margins(self,) -> Optional[List[int]]:
        """
        Gets the rightMargins property value. A list of supported right margins(in microns) for the printer.
        Returns: Optional[List[int]]
        """
        return self._right_margins
    
    @right_margins.setter
    def right_margins(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the rightMargins property value. A list of supported right margins(in microns) for the printer.
        Args:
            value: Value to set for the rightMargins property.
        """
        self._right_margins = value
    
    @property
    def scalings(self,) -> Optional[List[print_scaling.PrintScaling]]:
        """
        Gets the scalings property value. Supported print scalings.
        Returns: Optional[List[print_scaling.PrintScaling]]
        """
        return self._scalings
    
    @scalings.setter
    def scalings(self,value: Optional[List[print_scaling.PrintScaling]] = None) -> None:
        """
        Sets the scalings property value. Supported print scalings.
        Args:
            value: Value to set for the scalings property.
        """
        self._scalings = value
    
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
    
    @property
    def supported_color_configurations(self,) -> Optional[List[print_color_configuration.PrintColorConfiguration]]:
        """
        Gets the supportedColorConfigurations property value. The supportedColorConfigurations property
        Returns: Optional[List[print_color_configuration.PrintColorConfiguration]]
        """
        return self._supported_color_configurations
    
    @supported_color_configurations.setter
    def supported_color_configurations(self,value: Optional[List[print_color_configuration.PrintColorConfiguration]] = None) -> None:
        """
        Sets the supportedColorConfigurations property value. The supportedColorConfigurations property
        Args:
            value: Value to set for the supportedColorConfigurations property.
        """
        self._supported_color_configurations = value
    
    @property
    def supported_copies_per_job(self,) -> Optional[integer_range.IntegerRange]:
        """
        Gets the supportedCopiesPerJob property value. The supportedCopiesPerJob property
        Returns: Optional[integer_range.IntegerRange]
        """
        return self._supported_copies_per_job
    
    @supported_copies_per_job.setter
    def supported_copies_per_job(self,value: Optional[integer_range.IntegerRange] = None) -> None:
        """
        Sets the supportedCopiesPerJob property value. The supportedCopiesPerJob property
        Args:
            value: Value to set for the supportedCopiesPerJob property.
        """
        self._supported_copies_per_job = value
    
    @property
    def supported_document_mime_types(self,) -> Optional[List[str]]:
        """
        Gets the supportedDocumentMimeTypes property value. The supportedDocumentMimeTypes property
        Returns: Optional[List[str]]
        """
        return self._supported_document_mime_types
    
    @supported_document_mime_types.setter
    def supported_document_mime_types(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedDocumentMimeTypes property value. The supportedDocumentMimeTypes property
        Args:
            value: Value to set for the supportedDocumentMimeTypes property.
        """
        self._supported_document_mime_types = value
    
    @property
    def supported_duplex_configurations(self,) -> Optional[List[print_duplex_configuration.PrintDuplexConfiguration]]:
        """
        Gets the supportedDuplexConfigurations property value. The supportedDuplexConfigurations property
        Returns: Optional[List[print_duplex_configuration.PrintDuplexConfiguration]]
        """
        return self._supported_duplex_configurations
    
    @supported_duplex_configurations.setter
    def supported_duplex_configurations(self,value: Optional[List[print_duplex_configuration.PrintDuplexConfiguration]] = None) -> None:
        """
        Sets the supportedDuplexConfigurations property value. The supportedDuplexConfigurations property
        Args:
            value: Value to set for the supportedDuplexConfigurations property.
        """
        self._supported_duplex_configurations = value
    
    @property
    def supported_finishings(self,) -> Optional[List[print_finishing.PrintFinishing]]:
        """
        Gets the supportedFinishings property value. The supportedFinishings property
        Returns: Optional[List[print_finishing.PrintFinishing]]
        """
        return self._supported_finishings
    
    @supported_finishings.setter
    def supported_finishings(self,value: Optional[List[print_finishing.PrintFinishing]] = None) -> None:
        """
        Sets the supportedFinishings property value. The supportedFinishings property
        Args:
            value: Value to set for the supportedFinishings property.
        """
        self._supported_finishings = value
    
    @property
    def supported_media_colors(self,) -> Optional[List[str]]:
        """
        Gets the supportedMediaColors property value. The supportedMediaColors property
        Returns: Optional[List[str]]
        """
        return self._supported_media_colors
    
    @supported_media_colors.setter
    def supported_media_colors(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedMediaColors property value. The supportedMediaColors property
        Args:
            value: Value to set for the supportedMediaColors property.
        """
        self._supported_media_colors = value
    
    @property
    def supported_media_sizes(self,) -> Optional[List[str]]:
        """
        Gets the supportedMediaSizes property value. The supportedMediaSizes property
        Returns: Optional[List[str]]
        """
        return self._supported_media_sizes
    
    @supported_media_sizes.setter
    def supported_media_sizes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedMediaSizes property value. The supportedMediaSizes property
        Args:
            value: Value to set for the supportedMediaSizes property.
        """
        self._supported_media_sizes = value
    
    @property
    def supported_media_types(self,) -> Optional[List[print_media_type.PrintMediaType]]:
        """
        Gets the supportedMediaTypes property value. The supportedMediaTypes property
        Returns: Optional[List[print_media_type.PrintMediaType]]
        """
        return self._supported_media_types
    
    @supported_media_types.setter
    def supported_media_types(self,value: Optional[List[print_media_type.PrintMediaType]] = None) -> None:
        """
        Sets the supportedMediaTypes property value. The supportedMediaTypes property
        Args:
            value: Value to set for the supportedMediaTypes property.
        """
        self._supported_media_types = value
    
    @property
    def supported_orientations(self,) -> Optional[List[print_orientation.PrintOrientation]]:
        """
        Gets the supportedOrientations property value. The supportedOrientations property
        Returns: Optional[List[print_orientation.PrintOrientation]]
        """
        return self._supported_orientations
    
    @supported_orientations.setter
    def supported_orientations(self,value: Optional[List[print_orientation.PrintOrientation]] = None) -> None:
        """
        Sets the supportedOrientations property value. The supportedOrientations property
        Args:
            value: Value to set for the supportedOrientations property.
        """
        self._supported_orientations = value
    
    @property
    def supported_output_bins(self,) -> Optional[List[str]]:
        """
        Gets the supportedOutputBins property value. The supportedOutputBins property
        Returns: Optional[List[str]]
        """
        return self._supported_output_bins
    
    @supported_output_bins.setter
    def supported_output_bins(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the supportedOutputBins property value. The supportedOutputBins property
        Args:
            value: Value to set for the supportedOutputBins property.
        """
        self._supported_output_bins = value
    
    @property
    def supported_pages_per_sheet(self,) -> Optional[integer_range.IntegerRange]:
        """
        Gets the supportedPagesPerSheet property value. The supportedPagesPerSheet property
        Returns: Optional[integer_range.IntegerRange]
        """
        return self._supported_pages_per_sheet
    
    @supported_pages_per_sheet.setter
    def supported_pages_per_sheet(self,value: Optional[integer_range.IntegerRange] = None) -> None:
        """
        Sets the supportedPagesPerSheet property value. The supportedPagesPerSheet property
        Args:
            value: Value to set for the supportedPagesPerSheet property.
        """
        self._supported_pages_per_sheet = value
    
    @property
    def supported_presentation_directions(self,) -> Optional[List[print_presentation_direction.PrintPresentationDirection]]:
        """
        Gets the supportedPresentationDirections property value. The supportedPresentationDirections property
        Returns: Optional[List[print_presentation_direction.PrintPresentationDirection]]
        """
        return self._supported_presentation_directions
    
    @supported_presentation_directions.setter
    def supported_presentation_directions(self,value: Optional[List[print_presentation_direction.PrintPresentationDirection]] = None) -> None:
        """
        Sets the supportedPresentationDirections property value. The supportedPresentationDirections property
        Args:
            value: Value to set for the supportedPresentationDirections property.
        """
        self._supported_presentation_directions = value
    
    @property
    def supported_print_qualities(self,) -> Optional[List[print_quality.PrintQuality]]:
        """
        Gets the supportedPrintQualities property value. The supportedPrintQualities property
        Returns: Optional[List[print_quality.PrintQuality]]
        """
        return self._supported_print_qualities
    
    @supported_print_qualities.setter
    def supported_print_qualities(self,value: Optional[List[print_quality.PrintQuality]] = None) -> None:
        """
        Sets the supportedPrintQualities property value. The supportedPrintQualities property
        Args:
            value: Value to set for the supportedPrintQualities property.
        """
        self._supported_print_qualities = value
    
    @property
    def supports_fit_pdf_to_page(self,) -> Optional[bool]:
        """
        Gets the supportsFitPdfToPage property value. True if the printer supports scaling PDF pages to match the print media size; false otherwise.
        Returns: Optional[bool]
        """
        return self._supports_fit_pdf_to_page
    
    @supports_fit_pdf_to_page.setter
    def supports_fit_pdf_to_page(self,value: Optional[bool] = None) -> None:
        """
        Sets the supportsFitPdfToPage property value. True if the printer supports scaling PDF pages to match the print media size; false otherwise.
        Args:
            value: Value to set for the supportsFitPdfToPage property.
        """
        self._supports_fit_pdf_to_page = value
    
    @property
    def top_margins(self,) -> Optional[List[int]]:
        """
        Gets the topMargins property value. A list of supported top margins(in microns) for the printer.
        Returns: Optional[List[int]]
        """
        return self._top_margins
    
    @top_margins.setter
    def top_margins(self,value: Optional[List[int]] = None) -> None:
        """
        Sets the topMargins property value. A list of supported top margins(in microns) for the printer.
        Args:
            value: Value to set for the topMargins property.
        """
        self._top_margins = value
    

