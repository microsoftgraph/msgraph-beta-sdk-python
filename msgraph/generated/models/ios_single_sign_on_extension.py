from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import ios_azure_ad_single_sign_on_extension, ios_credential_single_sign_on_extension, ios_kerberos_single_sign_on_extension, ios_redirect_single_sign_on_extension, single_sign_on_extension

from . import single_sign_on_extension

@dataclass
class IosSingleSignOnExtension(single_sign_on_extension.SingleSignOnExtension):
    odata_type = "#microsoft.graph.iosSingleSignOnExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosSingleSignOnExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosAzureAdSingleSignOnExtension".casefold():
            from . import ios_azure_ad_single_sign_on_extension

            return ios_azure_ad_single_sign_on_extension.IosAzureAdSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCredentialSingleSignOnExtension".casefold():
            from . import ios_credential_single_sign_on_extension

            return ios_credential_single_sign_on_extension.IosCredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosKerberosSingleSignOnExtension".casefold():
            from . import ios_kerberos_single_sign_on_extension

            return ios_kerberos_single_sign_on_extension.IosKerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosRedirectSingleSignOnExtension".casefold():
            from . import ios_redirect_single_sign_on_extension

            return ios_redirect_single_sign_on_extension.IosRedirectSingleSignOnExtension()
        return IosSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import ios_azure_ad_single_sign_on_extension, ios_credential_single_sign_on_extension, ios_kerberos_single_sign_on_extension, ios_redirect_single_sign_on_extension, single_sign_on_extension

        from . import ios_azure_ad_single_sign_on_extension, ios_credential_single_sign_on_extension, ios_kerberos_single_sign_on_extension, ios_redirect_single_sign_on_extension, single_sign_on_extension

        fields: Dict[str, Callable[[Any], None]] = {
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
    

