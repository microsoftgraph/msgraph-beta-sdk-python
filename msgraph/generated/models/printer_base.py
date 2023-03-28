from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, printer, printer_capabilities, printer_defaults, printer_location, printer_share, printer_status, print_job

from . import entity

class PrinterBase(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new printerBase and sets the default values.
        """
        super().__init__()
        # The capabilities property
        self._capabilities: Optional[printer_capabilities.PrinterCapabilities] = None
        # The defaults property
        self._defaults: Optional[printer_defaults.PrinterDefaults] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The isAcceptingJobs property
        self._is_accepting_jobs: Optional[bool] = None
        # The jobs property
        self._jobs: Optional[List[print_job.PrintJob]] = None
        # The location property
        self._location: Optional[printer_location.PrinterLocation] = None
        # The manufacturer property
        self._manufacturer: Optional[str] = None
        # The model property
        self._model: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The status property
        self._status: Optional[printer_status.PrinterStatus] = None
    
    @property
    def capabilities(self,) -> Optional[printer_capabilities.PrinterCapabilities]:
        """
        Gets the capabilities property value. The capabilities property
        Returns: Optional[printer_capabilities.PrinterCapabilities]
        """
        return self._capabilities
    
    @capabilities.setter
    def capabilities(self,value: Optional[printer_capabilities.PrinterCapabilities] = None) -> None:
        """
        Sets the capabilities property value. The capabilities property
        Args:
            value: Value to set for the capabilities property.
        """
        self._capabilities = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.printer":
                from . import printer

                return printer.Printer()
            if mapping_value == "#microsoft.graph.printerShare":
                from . import printer_share

                return printer_share.PrinterShare()
        return PrinterBase()
    
    @property
    def defaults(self,) -> Optional[printer_defaults.PrinterDefaults]:
        """
        Gets the defaults property value. The defaults property
        Returns: Optional[printer_defaults.PrinterDefaults]
        """
        return self._defaults
    
    @defaults.setter
    def defaults(self,value: Optional[printer_defaults.PrinterDefaults] = None) -> None:
        """
        Sets the defaults property value. The defaults property
        Args:
            value: Value to set for the defaults property.
        """
        self._defaults = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, printer, printer_capabilities, printer_defaults, printer_location, printer_share, printer_status, print_job

        fields: Dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(printer_capabilities.PrinterCapabilities)),
            "defaults": lambda n : setattr(self, 'defaults', n.get_object_value(printer_defaults.PrinterDefaults)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAcceptingJobs": lambda n : setattr(self, 'is_accepting_jobs', n.get_bool_value()),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(print_job.PrintJob)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(printer_location.PrinterLocation)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(printer_status.PrinterStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_accepting_jobs(self,) -> Optional[bool]:
        """
        Gets the isAcceptingJobs property value. The isAcceptingJobs property
        Returns: Optional[bool]
        """
        return self._is_accepting_jobs
    
    @is_accepting_jobs.setter
    def is_accepting_jobs(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAcceptingJobs property value. The isAcceptingJobs property
        Args:
            value: Value to set for the is_accepting_jobs property.
        """
        self._is_accepting_jobs = value
    
    @property
    def jobs(self,) -> Optional[List[print_job.PrintJob]]:
        """
        Gets the jobs property value. The jobs property
        Returns: Optional[List[print_job.PrintJob]]
        """
        return self._jobs
    
    @jobs.setter
    def jobs(self,value: Optional[List[print_job.PrintJob]] = None) -> None:
        """
        Sets the jobs property value. The jobs property
        Args:
            value: Value to set for the jobs property.
        """
        self._jobs = value
    
    @property
    def location(self,) -> Optional[printer_location.PrinterLocation]:
        """
        Gets the location property value. The location property
        Returns: Optional[printer_location.PrinterLocation]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[printer_location.PrinterLocation] = None) -> None:
        """
        Sets the location property value. The location property
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. The manufacturer property
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. The manufacturer property
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. The model property
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. The model property
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("capabilities", self.capabilities)
        writer.write_object_value("defaults", self.defaults)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAcceptingJobs", self.is_accepting_jobs)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_object_value("location", self.location)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_str_value("name", self.name)
        writer.write_object_value("status", self.status)
    
    @property
    def status(self,) -> Optional[printer_status.PrinterStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[printer_status.PrinterStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[printer_status.PrinterStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

