from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, json, workbook_worksheet

from . import entity

@dataclass
class WorkbookNamedItem(entity.Entity):
    # Represents the comment associated with this name.
    comment: Optional[str] = None
    # The name of the object. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the name is scoped to the workbook or to a specific worksheet. Read-only.
    scope: Optional[str] = None
    # Indicates what type of reference is associated with the name. Possible values are: String, Integer, Double, Boolean, Range. Read-only.
    type: Optional[str] = None
    # Represents the formula that the name is defined to refer to. For example, =Sheet14!$B$2:$H$12 and =4.75. Read-only.
    value: Optional[json.Json] = None
    # Specifies whether the object is visible or not.
    visible: Optional[bool] = None
    # Returns the worksheet on which the named item is scoped to. Available only if the item is scoped to the worksheet. Read-only.
    worksheet: Optional[workbook_worksheet.WorkbookWorksheet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookNamedItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookNamedItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookNamedItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, json, workbook_worksheet

        fields: Dict[str, Callable[[Any], None]] = {
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(json.Json)),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
            "worksheet": lambda n : setattr(self, 'worksheet', n.get_object_value(workbook_worksheet.WorkbookWorksheet)),
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
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("name", self.name)
        writer.write_str_value("scope", self.scope)
        writer.write_str_value("type", self.type)
        writer.write_object_value("value", self.value)
        writer.write_bool_value("visible", self.visible)
        writer.write_object_value("worksheet", self.worksheet)
    

