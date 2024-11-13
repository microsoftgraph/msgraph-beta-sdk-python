from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .accounts_with_access import AccountsWithAccess
    from .authorization_system import AuthorizationSystem

from .accounts_with_access import AccountsWithAccess

@dataclass
class EnumeratedAccountsWithAccess(AccountsWithAccess, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.enumeratedAccountsWithAccess"
    # The accounts property
    accounts: Optional[List[AuthorizationSystem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EnumeratedAccountsWithAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EnumeratedAccountsWithAccess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EnumeratedAccountsWithAccess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .accounts_with_access import AccountsWithAccess
        from .authorization_system import AuthorizationSystem

        from .accounts_with_access import AccountsWithAccess
        from .authorization_system import AuthorizationSystem

        fields: Dict[str, Callable[[Any], None]] = {
            "accounts": lambda n : setattr(self, 'accounts', n.get_collection_of_object_values(AuthorizationSystem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .accounts_with_access import AccountsWithAccess
        from .authorization_system import AuthorizationSystem

        writer.write_collection_of_object_values("accounts", self.accounts)
    

