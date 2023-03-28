from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, single_sign_on_extension

from . import single_sign_on_extension

class MacOSSingleSignOnExtension(single_sign_on_extension.SingleSignOnExtension):
    def __init__(self,) -> None:
        """
        Instantiates a new MacOSSingleSignOnExtension and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.macOSSingleSignOnExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOSSingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOSSingleSignOnExtension
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.macOSAzureAdSingleSignOnExtension":
                from . import mac_o_s_azure_ad_single_sign_on_extension

                return mac_o_s_azure_ad_single_sign_on_extension.MacOSAzureAdSingleSignOnExtension()
            if mapping_value == "#microsoft.graph.macOSCredentialSingleSignOnExtension":
                from . import mac_o_s_credential_single_sign_on_extension

                return mac_o_s_credential_single_sign_on_extension.MacOSCredentialSingleSignOnExtension()
            if mapping_value == "#microsoft.graph.macOSKerberosSingleSignOnExtension":
                from . import mac_o_s_kerberos_single_sign_on_extension

                return mac_o_s_kerberos_single_sign_on_extension.MacOSKerberosSingleSignOnExtension()
            if mapping_value == "#microsoft.graph.macOSRedirectSingleSignOnExtension":
                from . import mac_o_s_redirect_single_sign_on_extension

                return mac_o_s_redirect_single_sign_on_extension.MacOSRedirectSingleSignOnExtension()
        return MacOSSingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

