from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

custom_authentication_extension = lazy_import('msgraph.generated.models.custom_authentication_extension')
on_token_issuance_start_return_claim = lazy_import('msgraph.generated.models.on_token_issuance_start_return_claim')

class OnTokenIssuanceStartCustomExtension(custom_authentication_extension.CustomAuthenticationExtension):
    @property
    def claims_for_token_configuration(self,) -> Optional[List[on_token_issuance_start_return_claim.OnTokenIssuanceStartReturnClaim]]:
        """
        Gets the claimsForTokenConfiguration property value. The claimsForTokenConfiguration property
        Returns: Optional[List[on_token_issuance_start_return_claim.OnTokenIssuanceStartReturnClaim]]
        """
        return self._claims_for_token_configuration
    
    @claims_for_token_configuration.setter
    def claims_for_token_configuration(self,value: Optional[List[on_token_issuance_start_return_claim.OnTokenIssuanceStartReturnClaim]] = None) -> None:
        """
        Sets the claimsForTokenConfiguration property value. The claimsForTokenConfiguration property
        Args:
            value: Value to set for the claimsForTokenConfiguration property.
        """
        self._claims_for_token_configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new OnTokenIssuanceStartCustomExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.onTokenIssuanceStartCustomExtension"
        # The claimsForTokenConfiguration property
        self._claims_for_token_configuration: Optional[List[on_token_issuance_start_return_claim.OnTokenIssuanceStartReturnClaim]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnTokenIssuanceStartCustomExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnTokenIssuanceStartCustomExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnTokenIssuanceStartCustomExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "claims_for_token_configuration": lambda n : setattr(self, 'claims_for_token_configuration', n.get_collection_of_object_values(on_token_issuance_start_return_claim.OnTokenIssuanceStartReturnClaim)),
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
        writer.write_collection_of_object_values("claimsForTokenConfiguration", self.claims_for_token_configuration)
    

