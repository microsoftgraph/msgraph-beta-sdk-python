from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, single_sign_on_extension

from . import single_sign_on_extension

@dataclass
class MacOSSingleSignOnExtension(single_sign_on_extension.SingleSignOnExtension):
    odata_type = "#microsoft.graph.macOSSingleSignOnExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSingleSignOnExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSAzureAdSingleSignOnExtension".casefold():
            from . import mac_o_s_azure_ad_single_sign_on_extension

            return mac_o_s_azure_ad_single_sign_on_extension.MacOSAzureAdSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCredentialSingleSignOnExtension".casefold():
            from . import mac_o_s_credential_single_sign_on_extension

            return mac_o_s_credential_single_sign_on_extension.MacOSCredentialSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSKerberosSingleSignOnExtension".casefold():
            from . import mac_o_s_kerberos_single_sign_on_extension

            return mac_o_s_kerberos_single_sign_on_extension.MacOSKerberosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSRedirectSingleSignOnExtension".casefold():
            from . import mac_o_s_redirect_single_sign_on_extension

            return mac_o_s_redirect_single_sign_on_extension.MacOSRedirectSingleSignOnExtension()
        return MacOSSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, single_sign_on_extension

        from . import mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, single_sign_on_extension

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
    

