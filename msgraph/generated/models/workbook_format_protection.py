from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity

from . import entity

class WorkbookFormatProtection(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new WorkbookFormatProtection and sets the default values.
        """
        super().__init__()
        # The formulaHidden property
        self._formula_hidden: Optional[bool] = None
        # The locked property
        self._locked: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkbookFormatProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookFormatProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkbookFormatProtection()
    
    @property
    def formula_hidden(self,) -> Optional[bool]:
        """
        Gets the formulaHidden property value. The formulaHidden property
        Returns: Optional[bool]
        """
        return self._formula_hidden
    
    @formula_hidden.setter
    def formula_hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the formulaHidden property value. The formulaHidden property
        Args:
            value: Value to set for the formula_hidden property.
        """
        self._formula_hidden = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "formulaHidden": lambda n : setattr(self, 'formula_hidden', n.get_bool_value()),
            "locked": lambda n : setattr(self, 'locked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def locked(self,) -> Optional[bool]:
        """
        Gets the locked property value. The locked property
        Returns: Optional[bool]
        """
        return self._locked
    
    @locked.setter
    def locked(self,value: Optional[bool] = None) -> None:
        """
        Sets the locked property value. The locked property
        Args:
            value: Value to set for the locked property.
        """
        self._locked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("formulaHidden", self.formula_hidden)
        writer.write_bool_value("locked", self.locked)
    

