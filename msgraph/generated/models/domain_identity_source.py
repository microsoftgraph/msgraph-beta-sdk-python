from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_source

from . import identity_source

class DomainIdentitySource(identity_source.IdentitySource):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainIdentitySource and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.domainIdentitySource"
        # The name of the identity source, typically also the domain name. Read only.
        self._display_name: Optional[str] = None
        # The domain name. Read only.
        self._domain_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainIdentitySource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainIdentitySource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainIdentitySource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the identity source, typically also the domain name. Read only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the identity source, typically also the domain name. Read only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def domain_name(self,) -> Optional[str]:
        """
        Gets the domainName property value. The domain name. Read only.
        Returns: Optional[str]
        """
        return self._domain_name
    
    @domain_name.setter
    def domain_name(self,value: Optional[str] = None) -> None:
        """
        Sets the domainName property value. The domain name. Read only.
        Args:
            value: Value to set for the domain_name property.
        """
        self._domain_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_source

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
    

