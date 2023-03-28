from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer_base, printer_share, print_connector, print_task_trigger

from . import printer_base

class Printer(printer_base.PrinterBase):
    def __init__(self,) -> None:
        """
        Instantiates a new printer and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.printer"
        # The acceptingJobs property
        self._accepting_jobs: Optional[bool] = None
        # The connectors that are associated with the printer.
        self._connectors: Optional[List[print_connector.PrintConnector]] = None
        # True if the printer has a physical device for printing. Read-only.
        self._has_physical_device: Optional[bool] = None
        # True if the printer is shared; false otherwise. Read-only.
        self._is_shared: Optional[bool] = None
        # The most recent dateTimeOffset when a printer interacted with Universal Print. Read-only.
        self._last_seen_date_time: Optional[datetime] = None
        # The DateTimeOffset when the printer was registered. Read-only.
        self._registered_date_time: Optional[datetime] = None
        # The share property
        self._share: Optional[printer_share.PrinterShare] = None
        # The list of printerShares that are associated with the printer. Currently, only one printerShare can be associated with the printer. Read-only. Nullable.
        self._shares: Optional[List[printer_share.PrinterShare]] = None
        # A list of task triggers that are associated with the printer.
        self._task_triggers: Optional[List[print_task_trigger.PrintTaskTrigger]] = None
    
    @property
    def accepting_jobs(self,) -> Optional[bool]:
        """
        Gets the acceptingJobs property value. The acceptingJobs property
        Returns: Optional[bool]
        """
        return self._accepting_jobs
    
    @accepting_jobs.setter
    def accepting_jobs(self,value: Optional[bool] = None) -> None:
        """
        Sets the acceptingJobs property value. The acceptingJobs property
        Args:
            value: Value to set for the accepting_jobs property.
        """
        self._accepting_jobs = value
    
    @property
    def connectors(self,) -> Optional[List[print_connector.PrintConnector]]:
        """
        Gets the connectors property value. The connectors that are associated with the printer.
        Returns: Optional[List[print_connector.PrintConnector]]
        """
        return self._connectors
    
    @connectors.setter
    def connectors(self,value: Optional[List[print_connector.PrintConnector]] = None) -> None:
        """
        Sets the connectors property value. The connectors that are associated with the printer.
        Args:
            value: Value to set for the connectors property.
        """
        self._connectors = value
    
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
    
    @property
    def has_physical_device(self,) -> Optional[bool]:
        """
        Gets the hasPhysicalDevice property value. True if the printer has a physical device for printing. Read-only.
        Returns: Optional[bool]
        """
        return self._has_physical_device
    
    @has_physical_device.setter
    def has_physical_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasPhysicalDevice property value. True if the printer has a physical device for printing. Read-only.
        Args:
            value: Value to set for the has_physical_device property.
        """
        self._has_physical_device = value
    
    @property
    def is_shared(self,) -> Optional[bool]:
        """
        Gets the isShared property value. True if the printer is shared; false otherwise. Read-only.
        Returns: Optional[bool]
        """
        return self._is_shared
    
    @is_shared.setter
    def is_shared(self,value: Optional[bool] = None) -> None:
        """
        Sets the isShared property value. True if the printer is shared; false otherwise. Read-only.
        Args:
            value: Value to set for the is_shared property.
        """
        self._is_shared = value
    
    @property
    def last_seen_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSeenDateTime property value. The most recent dateTimeOffset when a printer interacted with Universal Print. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_seen_date_time
    
    @last_seen_date_time.setter
    def last_seen_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSeenDateTime property value. The most recent dateTimeOffset when a printer interacted with Universal Print. Read-only.
        Args:
            value: Value to set for the last_seen_date_time property.
        """
        self._last_seen_date_time = value
    
    @property
    def registered_date_time(self,) -> Optional[datetime]:
        """
        Gets the registeredDateTime property value. The DateTimeOffset when the printer was registered. Read-only.
        Returns: Optional[datetime]
        """
        return self._registered_date_time
    
    @registered_date_time.setter
    def registered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the registeredDateTime property value. The DateTimeOffset when the printer was registered. Read-only.
        Args:
            value: Value to set for the registered_date_time property.
        """
        self._registered_date_time = value
    
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
    
    @property
    def share(self,) -> Optional[printer_share.PrinterShare]:
        """
        Gets the share property value. The share property
        Returns: Optional[printer_share.PrinterShare]
        """
        return self._share
    
    @share.setter
    def share(self,value: Optional[printer_share.PrinterShare] = None) -> None:
        """
        Sets the share property value. The share property
        Args:
            value: Value to set for the share property.
        """
        self._share = value
    
    @property
    def shares(self,) -> Optional[List[printer_share.PrinterShare]]:
        """
        Gets the shares property value. The list of printerShares that are associated with the printer. Currently, only one printerShare can be associated with the printer. Read-only. Nullable.
        Returns: Optional[List[printer_share.PrinterShare]]
        """
        return self._shares
    
    @shares.setter
    def shares(self,value: Optional[List[printer_share.PrinterShare]] = None) -> None:
        """
        Sets the shares property value. The list of printerShares that are associated with the printer. Currently, only one printerShare can be associated with the printer. Read-only. Nullable.
        Args:
            value: Value to set for the shares property.
        """
        self._shares = value
    
    @property
    def task_triggers(self,) -> Optional[List[print_task_trigger.PrintTaskTrigger]]:
        """
        Gets the taskTriggers property value. A list of task triggers that are associated with the printer.
        Returns: Optional[List[print_task_trigger.PrintTaskTrigger]]
        """
        return self._task_triggers
    
    @task_triggers.setter
    def task_triggers(self,value: Optional[List[print_task_trigger.PrintTaskTrigger]] = None) -> None:
        """
        Sets the taskTriggers property value. A list of task triggers that are associated with the printer.
        Args:
            value: Value to set for the task_triggers property.
        """
        self._task_triggers = value
    

