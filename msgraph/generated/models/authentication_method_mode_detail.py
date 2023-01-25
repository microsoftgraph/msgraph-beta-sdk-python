from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_authentication_method = lazy_import('msgraph.generated.models.base_authentication_method')
entity = lazy_import('msgraph.generated.models.entity')

class AuthenticationMethodModeDetail(entity.Entity):
    @property
    def authentication_method(self,) -> Optional[base_authentication_method.BaseAuthenticationMethod]:
        """
        Gets the authenticationMethod property value. The authenticationMethod property
        Returns: Optional[base_authentication_method.BaseAuthenticationMethod]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[base_authentication_method.BaseAuthenticationMethod] = None) -> None:
        """
        Sets the authenticationMethod property value. The authenticationMethod property
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationMethodModeDetail and sets the default values.
        """
        super().__init__()
        # The authenticationMethod property
        self._authentication_method: Optional[base_authentication_method.BaseAuthenticationMethod] = None
        # The display name of this mode
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodModeDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodModeDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodModeDetail()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of this mode
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of this mode
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
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_enum_value(base_authentication_method.BaseAuthenticationMethod)),
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
        writer.write_enum_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("displayName", self.display_name)
    

