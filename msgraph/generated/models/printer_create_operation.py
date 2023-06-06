from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer, print_operation

from . import print_operation

@dataclass
class PrinterCreateOperation(print_operation.PrintOperation):
    odata_type = "#microsoft.graph.printerCreateOperation"
    # The signed certificate created during the registration process. Read-only.
    certificate: Optional[str] = None
    # The printer property
    printer: Optional[printer.Printer] = None
    
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
    

