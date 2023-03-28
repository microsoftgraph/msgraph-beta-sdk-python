from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import print_usage

from . import print_usage

class PrintUsageByPrinter(print_usage.PrintUsage):
    def __init__(self,) -> None:
        """
        Instantiates a new PrintUsageByPrinter and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The printerId property
        self._printer_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintUsageByPrinter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintUsageByPrinter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintUsageByPrinter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import print_usage

        fields: Dict[str, Callable[[Any], None]] = {
            "printerId": lambda n : setattr(self, 'printer_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def printer_id(self,) -> Optional[str]:
        """
        Gets the printerId property value. The printerId property
        Returns: Optional[str]
        """
        return self._printer_id
    
    @printer_id.setter
    def printer_id(self,value: Optional[str] = None) -> None:
        """
        Sets the printerId property value. The printerId property
        Args:
            value: Value to set for the printer_id property.
        """
        self._printer_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("printerId", self.printer_id)
    

