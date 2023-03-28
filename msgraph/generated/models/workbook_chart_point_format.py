from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, workbook_chart_fill

from . import entity

class WorkbookChartPointFormat(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new workbookChartPointFormat and sets the default values.
        """
        super().__init__()
        # Represents the fill format of a chart, which includes background formating information. Read-only.
        self._fill: Optional[workbook_chart_fill.WorkbookChartFill] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookChartPointFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookChartPointFormat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookChartPointFormat()
    
    @property
    def fill(self,) -> Optional[workbook_chart_fill.WorkbookChartFill]:
        """
        Gets the fill property value. Represents the fill format of a chart, which includes background formating information. Read-only.
        Returns: Optional[workbook_chart_fill.WorkbookChartFill]
        """
        return self._fill
    
    @fill.setter
    def fill(self,value: Optional[workbook_chart_fill.WorkbookChartFill] = None) -> None:
        """
        Sets the fill property value. Represents the fill format of a chart, which includes background formating information. Read-only.
        Args:
            value: Value to set for the fill property.
        """
        self._fill = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, workbook_chart_fill

        fields: Dict[str, Callable[[Any], None]] = {
            "fill": lambda n : setattr(self, 'fill', n.get_object_value(workbook_chart_fill.WorkbookChartFill)),
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
        writer.write_object_value("fill", self.fill)
    

