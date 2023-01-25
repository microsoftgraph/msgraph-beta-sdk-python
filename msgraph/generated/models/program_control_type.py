from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ProgramControlType(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ProgramControlType and sets the default values.
        """
        super().__init__()
        # The controlTypeGroupId property
        self._control_type_group_id: Optional[str] = None
        # The name of the program control type
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def control_type_group_id(self,) -> Optional[str]:
        """
        Gets the controlTypeGroupId property value. The controlTypeGroupId property
        Returns: Optional[str]
        """
        return self._control_type_group_id
    
    @control_type_group_id.setter
    def control_type_group_id(self,value: Optional[str] = None) -> None:
        """
        Sets the controlTypeGroupId property value. The controlTypeGroupId property
        Args:
            value: Value to set for the controlTypeGroupId property.
        """
        self._control_type_group_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProgramControlType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProgramControlType
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProgramControlType()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the program control type
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the program control type
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "control_type_group_id": lambda n : setattr(self, 'control_type_group_id', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_str_value("controlTypeGroupId", self.control_type_group_id)
        writer.write_str_value("displayName", self.display_name)
    

