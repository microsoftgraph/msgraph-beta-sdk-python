from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer, print_operation

from . import print_operation

class PrinterCreateOperation(print_operation.PrintOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new PrinterCreateOperation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.printerCreateOperation"
        # The signed certificate created during the registration process. Read-only.
        self._certificate: Optional[str] = None
        # The printer property
        self._printer: Optional[printer.Printer] = None
    
    @property
    def certificate(self,) -> Optional[str]:
        """
        Gets the certificate property value. The signed certificate created during the registration process. Read-only.
        Returns: Optional[str]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the certificate property value. The signed certificate created during the registration process. Read-only.
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterCreateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterCreateOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterCreateOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import printer, print_operation

        fields: Dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(printer.Printer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def printer(self,) -> Optional[printer.Printer]:
        """
        Gets the printer property value. The printer property
        Returns: Optional[printer.Printer]
        """
        return self._printer
    
    @printer.setter
    def printer(self,value: Optional[printer.Printer] = None) -> None:
        """
        Sets the printer property value. The printer property
        Args:
            value: Value to set for the printer property.
        """
        self._printer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("certificate", self.certificate)
        writer.write_object_value("printer", self.printer)
    

