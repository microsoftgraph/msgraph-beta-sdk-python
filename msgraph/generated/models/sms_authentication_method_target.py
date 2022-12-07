from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_target = lazy_import('msgraph.generated.models.authentication_method_target')

class SmsAuthenticationMethodTarget(authentication_method_target.AuthenticationMethodTarget):
    def __init__(self,) -> None:
        """
        Instantiates a new SmsAuthenticationMethodTarget and sets the default values.
        """
        super().__init__()
        # Determines if the users or groups can use this authentication method to sign in to Azure AD. The value is always true.
        self._is_usable_for_sign_in: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SmsAuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SmsAuthenticationMethodTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SmsAuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_usable_for_sign_in": lambda n : setattr(self, 'is_usable_for_sign_in', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_usable_for_sign_in(self,) -> Optional[bool]:
        """
        Gets the isUsableForSignIn property value. Determines if the users or groups can use this authentication method to sign in to Azure AD. The value is always true.
        Returns: Optional[bool]
        """
        return self._is_usable_for_sign_in
    
    @is_usable_for_sign_in.setter
    def is_usable_for_sign_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUsableForSignIn property value. Determines if the users or groups can use this authentication method to sign in to Azure AD. The value is always true.
        Args:
            value: Value to set for the isUsableForSignIn property.
        """
        self._is_usable_for_sign_in = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isUsableForSignIn", self.is_usable_for_sign_in)
    

