from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
program_control = lazy_import('msgraph.generated.models.program_control')

class Program(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Program and sets the default values.
        """
        super().__init__()
        # Controls associated with the program.
        self._controls: Optional[List[program_control.ProgramControl]] = None
        # The description of the program.
        self._description: Optional[str] = None
        # The name of the program.  Required on create.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def controls(self,) -> Optional[List[program_control.ProgramControl]]:
        """
        Gets the controls property value. Controls associated with the program.
        Returns: Optional[List[program_control.ProgramControl]]
        """
        return self._controls
    
    @controls.setter
    def controls(self,value: Optional[List[program_control.ProgramControl]] = None) -> None:
        """
        Sets the controls property value. Controls associated with the program.
        Args:
            value: Value to set for the controls property.
        """
        self._controls = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Program:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Program
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Program()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of the program.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of the program.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the program.  Required on create.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the program.  Required on create.
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
            "controls": lambda n : setattr(self, 'controls', n.get_collection_of_object_values(program_control.ProgramControl)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
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
        writer.write_collection_of_object_values("controls", self.controls)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

