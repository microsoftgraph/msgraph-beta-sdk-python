from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')

class CommunicationsApplicationIdentity(identity.Identity):
    @property
    def application_type(self,) -> Optional[str]:
        """
        Gets the applicationType property value. First party Microsoft application presenting this identity.
        Returns: Optional[str]
        """
        return self._application_type
    
    @application_type.setter
    def application_type(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationType property value. First party Microsoft application presenting this identity.
        Args:
            value: Value to set for the applicationType property.
        """
        self._application_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CommunicationsApplicationIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.communicationsApplicationIdentity"
        # First party Microsoft application presenting this identity.
        self._application_type: Optional[str] = None
        # True if the participant would not like to be shown in other participants' rosters.
        self._hidden: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommunicationsApplicationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsApplicationIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CommunicationsApplicationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_type": lambda n : setattr(self, 'application_type', n.get_str_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hidden(self,) -> Optional[bool]:
        """
        Gets the hidden property value. True if the participant would not like to be shown in other participants' rosters.
        Returns: Optional[bool]
        """
        return self._hidden
    
    @hidden.setter
    def hidden(self,value: Optional[bool] = None) -> None:
        """
        Sets the hidden property value. True if the participant would not like to be shown in other participants' rosters.
        Args:
            value: Value to set for the hidden property.
        """
        self._hidden = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("applicationType", self.application_type)
        writer.write_bool_value("hidden", self.hidden)
    

