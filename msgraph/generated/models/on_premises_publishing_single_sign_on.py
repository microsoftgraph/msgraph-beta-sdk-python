from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .kerberos_sign_on_settings import KerberosSignOnSettings
    from .single_sign_on_mode import SingleSignOnMode

@dataclass
class OnPremisesPublishingSingleSignOn(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The Kerberos Constrained Delegation settings for applications that use Integrated Window Authentication.
    kerberos_sign_on_settings: Optional[KerberosSignOnSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The preferred single-sign on mode for the application. Possible values are: none, onPremisesKerberos, aadHeaderBased,pingHeaderBased, oAuthToken.
    single_sign_on_mode: Optional[SingleSignOnMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesPublishingSingleSignOn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesPublishingSingleSignOn
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesPublishingSingleSignOn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .kerberos_sign_on_settings import KerberosSignOnSettings
        from .single_sign_on_mode import SingleSignOnMode

        from .kerberos_sign_on_settings import KerberosSignOnSettings
        from .single_sign_on_mode import SingleSignOnMode

        fields: Dict[str, Callable[[Any], None]] = {
            "kerberosSignOnSettings": lambda n : setattr(self, 'kerberos_sign_on_settings', n.get_object_value(KerberosSignOnSettings)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "singleSignOnMode": lambda n : setattr(self, 'single_sign_on_mode', n.get_enum_value(SingleSignOnMode)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("kerberosSignOnSettings", self.kerberos_sign_on_settings)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("singleSignOnMode", self.single_sign_on_mode)
        writer.write_additional_data_value(self.additional_data)
    

