from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class ProgramResource(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new ProgramResource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.programResource"
        # Type of the resource, indicating whether it is a group or an app.
        self._type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProgramResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProgramResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProgramResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("type", self.type)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Type of the resource, indicating whether it is a group or an app.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Type of the resource, indicating whether it is a group or an app.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

