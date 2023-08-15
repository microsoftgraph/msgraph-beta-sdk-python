from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
    from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
    from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
    from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
    from .single_sign_on_extension import SingleSignOnExtension

from .single_sign_on_extension import SingleSignOnExtension

@dataclass
class MacOSSingleSignOnExtension(SingleSignOnExtension):
    """
    An abstract base class for all macOS-specific single sign-on extension types.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSSingleSignOnExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSingleSignOnExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSAzureAdSingleSignOnExtension".casefold():
            from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension

            return MacOSAzureAdSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCredentialSingleSignOnExtension".casefold():
            from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension

            return MacOSCredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSKerberosSingleSignOnExtension".casefold():
            from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension

            return MacOSKerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSRedirectSingleSignOnExtension".casefold():
            from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension

            return MacOSRedirectSingleSignOnExtension()
        return MacOSSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
        from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
        from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
        from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
        from .single_sign_on_extension import SingleSignOnExtension

        from .mac_o_s_azure_ad_single_sign_on_extension import MacOSAzureAdSingleSignOnExtension
        from .mac_o_s_credential_single_sign_on_extension import MacOSCredentialSingleSignOnExtension
        from .mac_o_s_kerberos_single_sign_on_extension import MacOSKerberosSingleSignOnExtension
        from .mac_o_s_redirect_single_sign_on_extension import MacOSRedirectSingleSignOnExtension
        from .single_sign_on_extension import SingleSignOnExtension

        fields: Dict[str, Callable[[Any], None]] = {
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

