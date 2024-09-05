from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .print_job_processing_state import PrintJobProcessingState
    from .user_identity import UserIdentity

@dataclass
class ArchivedPrintJob(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # True if the job was acquired by a printer; false otherwise. Read-only.
    acquired_by_printer: Optional[bool] = None
    # The dateTimeOffset when the job was acquired by the printer, if any. Read-only.
    acquired_date_time: Optional[datetime.datetime] = None
    # The number of black and white pages that were printed. Read-only.
    black_and_white_page_count: Optional[int] = None
    # The number of color pages that were printed. Read-only.
    color_page_count: Optional[int] = None
    # The dateTimeOffset when the job was completed, canceled, or aborted. Read-only.
    completion_date_time: Optional[datetime.datetime] = None
    # The number of copies that were printed. Read-only.
    copies_printed: Optional[int] = None
    # The user who created the print job. Read-only.
    created_by: Optional[UserIdentity] = None
    # The dateTimeOffset when the job was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The number of duplex (double-sided) pages that were printed. Read-only.
    duplex_page_count: Optional[int] = None
    # The archived print job's GUID. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of pages that were printed. Read-only.
    page_count: Optional[int] = None
    # The printer ID that the job was queued for. Read-only.
    printer_id: Optional[str] = None
    # The printer name that the job was queued for. Read-only.
    printer_name: Optional[str] = None
    # The processingState property
    processing_state: Optional[PrintJobProcessingState] = None
    # The number of simplex (single-sided) pages that were printed. Read-only.
    simplex_page_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ArchivedPrintJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArchivedPrintJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ArchivedPrintJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .print_job_processing_state import PrintJobProcessingState
        from .user_identity import UserIdentity

        from .print_job_processing_state import PrintJobProcessingState
        from .user_identity import UserIdentity

        fields: Dict[str, Callable[[Any], None]] = {
            "acquiredByPrinter": lambda n : setattr(self, 'acquired_by_printer', n.get_bool_value()),
            "acquiredDateTime": lambda n : setattr(self, 'acquired_date_time', n.get_datetime_value()),
            "blackAndWhitePageCount": lambda n : setattr(self, 'black_and_white_page_count', n.get_int_value()),
            "colorPageCount": lambda n : setattr(self, 'color_page_count', n.get_int_value()),
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "copiesPrinted": lambda n : setattr(self, 'copies_printed', n.get_int_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "duplexPageCount": lambda n : setattr(self, 'duplex_page_count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pageCount": lambda n : setattr(self, 'page_count', n.get_int_value()),
            "printerId": lambda n : setattr(self, 'printer_id', n.get_str_value()),
            "printerName": lambda n : setattr(self, 'printer_name', n.get_str_value()),
            "processingState": lambda n : setattr(self, 'processing_state', n.get_enum_value(PrintJobProcessingState)),
            "simplexPageCount": lambda n : setattr(self, 'simplex_page_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_bool_value("acquiredByPrinter", self.acquired_by_printer)
        writer.write_datetime_value("acquiredDateTime", self.acquired_date_time)
        writer.write_int_value("blackAndWhitePageCount", self.black_and_white_page_count)
        writer.write_int_value("colorPageCount", self.color_page_count)
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_int_value("copiesPrinted", self.copies_printed)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("duplexPageCount", self.duplex_page_count)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("pageCount", self.page_count)
        writer.write_str_value("printerId", self.printer_id)
        writer.write_str_value("printerName", self.printer_name)
        writer.write_enum_value("processingState", self.processing_state)
        writer.write_int_value("simplexPageCount", self.simplex_page_count)
        writer.write_additional_data_value(self.additional_data)
    

