from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
    from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
    from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
    from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
    from .single_sign_on_extension import SingleSignOnExtension

from .single_sign_on_extension import SingleSignOnExtension

@dataclass
class IosSingleSignOnExtension(SingleSignOnExtension):
    """
    An abstract base class for all iOS-specific single sign-on extension types.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosSingleSignOnExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosSingleSignOnExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosAzureAdSingleSignOnExtension".casefold():
            from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension

            return IosAzureAdSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCredentialSingleSignOnExtension".casefold():
            from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension

            return IosCredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosKerberosSingleSignOnExtension".casefold():
            from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension

            return IosKerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosRedirectSingleSignOnExtension".casefold():
            from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension

            return IosRedirectSingleSignOnExtension()
        return IosSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
        from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
        from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
        from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
        from .single_sign_on_extension import SingleSignOnExtension

        from .ios_azure_ad_single_sign_on_extension import IosAzureAdSingleSignOnExtension
        from .ios_credential_single_sign_on_extension import IosCredentialSingleSignOnExtension
        from .ios_kerberos_single_sign_on_extension import IosKerberosSingleSignOnExtension
        from .ios_redirect_single_sign_on_extension import IosRedirectSingleSignOnExtension
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
    

