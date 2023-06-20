from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import credential_single_sign_on_extension, ios_azure_ad_single_sign_on_extension, ios_credential_single_sign_on_extension, ios_kerberos_single_sign_on_extension, ios_redirect_single_sign_on_extension, ios_single_sign_on_extension, kerberos_single_sign_on_extension, mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, mac_o_s_single_sign_on_extension, redirect_single_sign_on_extension

@dataclass
class SingleSignOnExtension(AdditionalDataHolder, Parsable):
    """
    Represents an Apple Single Sign-On Extension.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SingleSignOnExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SingleSignOnExtension
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.credentialSingleSignOnExtension".casefold():
            from . import credential_single_sign_on_extension

            return credential_single_sign_on_extension.CredentialSingleSignOnExtension()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosSingleSignOnExtension".casefold():
            from . import ios_single_sign_on_extension

            return ios_single_sign_on_extension.IosSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.kerberosSingleSignOnExtension".casefold():
            from . import kerberos_single_sign_on_extension

            return kerberos_single_sign_on_extension.KerberosSingleSignOnExtension()
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSSingleSignOnExtension".casefold():
            from . import mac_o_s_single_sign_on_extension

            return mac_o_s_single_sign_on_extension.MacOSSingleSignOnExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.redirectSingleSignOnExtension".casefold():
            from . import redirect_single_sign_on_extension

            return redirect_single_sign_on_extension.RedirectSingleSignOnExtension()
        return SingleSignOnExtension()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import credential_single_sign_on_extension, ios_azure_ad_single_sign_on_extension, ios_credential_single_sign_on_extension, ios_kerberos_single_sign_on_extension, ios_redirect_single_sign_on_extension, ios_single_sign_on_extension, kerberos_single_sign_on_extension, mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, mac_o_s_single_sign_on_extension, redirect_single_sign_on_extension

        from . import credential_single_sign_on_extension, ios_azure_ad_single_sign_on_extension, ios_credential_single_sign_on_extension, ios_kerberos_single_sign_on_extension, ios_redirect_single_sign_on_extension, ios_single_sign_on_extension, kerberos_single_sign_on_extension, mac_o_s_azure_ad_single_sign_on_extension, mac_o_s_credential_single_sign_on_extension, mac_o_s_kerberos_single_sign_on_extension, mac_o_s_redirect_single_sign_on_extension, mac_o_s_single_sign_on_extension, redirect_single_sign_on_extension

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

