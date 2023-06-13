from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, print_usage_by_printer, print_usage_by_user

from . import entity

@dataclass
class PrintUsage(entity.Entity):
    # The blackAndWhitePageCount property
    black_and_white_page_count: Optional[int] = None
    # The colorPageCount property
    color_page_count: Optional[int] = None
    # The completedBlackAndWhiteJobCount property
    completed_black_and_white_job_count: Optional[int] = None
    # The completedColorJobCount property
    completed_color_job_count: Optional[int] = None
    # The completedJobCount property
    completed_job_count: Optional[int] = None
    # The doubleSidedSheetCount property
    double_sided_sheet_count: Optional[int] = None
    # The incompleteJobCount property
    incomplete_job_count: Optional[int] = None
    # The mediaSheetCount property
    media_sheet_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The pageCount property
    page_count: Optional[int] = None
    # The singleSidedSheetCount property
    single_sided_sheet_count: Optional[int] = None
    # The usageDate property
    usage_date: Optional[date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintUsage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.printUsageByPrinter":
                from . import print_usage_by_printer

                return print_usage_by_printer.PrintUsageByPrinter()
            if mapping_value == "#microsoft.graph.printUsageByUser":
                from . import print_usage_by_user

                return print_usage_by_user.PrintUsageByUser()
        return PrintUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, print_usage_by_printer, print_usage_by_user

        fields: Dict[str, Callable[[Any], None]] = {
            "blackAndWhitePageCount": lambda n : setattr(self, 'black_and_white_page_count', n.get_int_value()),
            "colorPageCount": lambda n : setattr(self, 'color_page_count', n.get_int_value()),
            "completedBlackAndWhiteJobCount": lambda n : setattr(self, 'completed_black_and_white_job_count', n.get_int_value()),
            "completedColorJobCount": lambda n : setattr(self, 'completed_color_job_count', n.get_int_value()),
            "completedJobCount": lambda n : setattr(self, 'completed_job_count', n.get_int_value()),
            "doubleSidedSheetCount": lambda n : setattr(self, 'double_sided_sheet_count', n.get_int_value()),
            "incompleteJobCount": lambda n : setattr(self, 'incomplete_job_count', n.get_int_value()),
            "mediaSheetCount": lambda n : setattr(self, 'media_sheet_count', n.get_int_value()),
            "pageCount": lambda n : setattr(self, 'page_count', n.get_int_value()),
            "singleSidedSheetCount": lambda n : setattr(self, 'single_sided_sheet_count', n.get_int_value()),
            "usageDate": lambda n : setattr(self, 'usage_date', n.get_date_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("blackAndWhitePageCount", self.black_and_white_page_count)
        writer.write_int_value("colorPageCount", self.color_page_count)
        writer.write_int_value("completedBlackAndWhiteJobCount", self.completed_black_and_white_job_count)
        writer.write_int_value("completedColorJobCount", self.completed_color_job_count)
        writer.write_int_value("completedJobCount", self.completed_job_count)
        writer.write_int_value("doubleSidedSheetCount", self.double_sided_sheet_count)
        writer.write_int_value("incompleteJobCount", self.incomplete_job_count)
        writer.write_int_value("mediaSheetCount", self.media_sheet_count)
        writer.write_int_value("pageCount", self.page_count)
        writer.write_int_value("singleSidedSheetCount", self.single_sided_sheet_count)
        writer.write_date_value("usageDate", self.usage_date)
    

