from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity

from . import identity

class SharePointIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new SharePointIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.sharePointIdentity"
        # The sign in name of the SharePoint identity.
        self._login_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharePointIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharePointIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharePointIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity

        fields: Dict[str, Callable[[Any], None]] = {
            "loginName": lambda n : setattr(self, 'login_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def login_name(self,) -> Optional[str]:
        """
        Gets the loginName property value. The sign in name of the SharePoint identity.
        Returns: Optional[str]
        """
        return self._login_name
    
    @login_name.setter
    def login_name(self,value: Optional[str] = None) -> None:
        """
        Sets the loginName property value. The sign in name of the SharePoint identity.
        Args:
            value: Value to set for the login_name property.
        """
        self._login_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("loginName", self.login_name)
    

