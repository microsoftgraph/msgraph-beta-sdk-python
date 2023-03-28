from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import host

from . import host

class Hostname(host.Host):
    def __init__(self,) -> None:
        """
        Instantiates a new Hostname and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.hostname"
        # The company or individual who registered this hostname, from WHOIS data.
        self._registrant: Optional[str] = None
        # The registrar for this hostname, from WHOIS data.
        self._registrar: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Hostname:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Hostname
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Hostname()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import host

        fields: Dict[str, Callable[[Any], None]] = {
            "registrant": lambda n : setattr(self, 'registrant', n.get_str_value()),
            "registrar": lambda n : setattr(self, 'registrar', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def registrant(self,) -> Optional[str]:
        """
        Gets the registrant property value. The company or individual who registered this hostname, from WHOIS data.
        Returns: Optional[str]
        """
        return self._registrant
    
    @registrant.setter
    def registrant(self,value: Optional[str] = None) -> None:
        """
        Sets the registrant property value. The company or individual who registered this hostname, from WHOIS data.
        Args:
            value: Value to set for the registrant property.
        """
        self._registrant = value
    
    @property
    def registrar(self,) -> Optional[str]:
        """
        Gets the registrar property value. The registrar for this hostname, from WHOIS data.
        Returns: Optional[str]
        """
        return self._registrar
    
    @registrar.setter
    def registrar(self,value: Optional[str] = None) -> None:
        """
        Sets the registrar property value. The registrar for this hostname, from WHOIS data.
        Args:
            value: Value to set for the registrar property.
        """
        self._registrar = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("registrant", self.registrant)
        writer.write_str_value("registrar", self.registrar)
    

