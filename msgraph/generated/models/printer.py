from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer_base, printer_share, print_connector, print_task_trigger

from . import printer_base

@dataclass
class Printer(printer_base.PrinterBase):
    odata_type = "#microsoft.graph.printer"
    # The acceptingJobs property
    accepting_jobs: Optional[bool] = None
    # The connectors that are associated with the printer.
    connectors: Optional[List[print_connector.PrintConnector]] = None
    # True if the printer has a physical device for printing. Read-only.
    has_physical_device: Optional[bool] = None
    # True if the printer is shared; false otherwise. Read-only.
    is_shared: Optional[bool] = None
    # The most recent dateTimeOffset when a printer interacted with Universal Print. Read-only.
    last_seen_date_time: Optional[datetime] = None
    # The DateTimeOffset when the printer was registered. Read-only.
    registered_date_time: Optional[datetime] = None
    # The share property
    share: Optional[printer_share.PrinterShare] = None
    # The list of printerShares that are associated with the printer. Currently, only one printerShare can be associated with the printer. Read-only. Nullable.
    shares: Optional[List[printer_share.PrinterShare]] = None
    # A list of task triggers that are associated with the printer.
    task_triggers: Optional[List[print_task_trigger.PrintTaskTrigger]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Printer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Printer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Printer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import printer_base, printer_share, print_connector, print_task_trigger

        fields: Dict[str, Callable[[Any], None]] = {
            "acceptingJobs": lambda n : setattr(self, 'accepting_jobs', n.get_bool_value()),
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(print_connector.PrintConnector)),
            "hasPhysicalDevice": lambda n : setattr(self, 'has_physical_device', n.get_bool_value()),
            "isShared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "registeredDateTime": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
            "share": lambda n : setattr(self, 'share', n.get_object_value(printer_share.PrinterShare)),
            "shares": lambda n : setattr(self, 'shares', n.get_collection_of_object_values(printer_share.PrinterShare)),
            "taskTriggers": lambda n : setattr(self, 'task_triggers', n.get_collection_of_object_values(print_task_trigger.PrintTaskTrigger)),
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
        writer.write_bool_value("acceptingJobs", self.accepting_jobs)
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_bool_value("hasPhysicalDevice", self.has_physical_device)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
        writer.write_object_value("share", self.share)
        writer.write_collection_of_object_values("shares", self.shares)
        writer.write_collection_of_object_values("taskTriggers", self.task_triggers)
    

