from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .expiration_requirement import ExpirationRequirement

@dataclass
class SessionLifetimePolicy(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The human-readable details of the conditional access session management policy applied to the sign-in.
    detail: Optional[str] = None
    # If a conditional access session management policy required the user to authenticate in this sign-in event, this field describes the policy type that required authentication. The possible values are: rememberMultifactorAuthenticationOnTrustedDevices, tenantTokenLifetimePolicy, audienceTokenLifetimePolicy, signInFrequencyPeriodicReauthentication, ngcMfa, signInFrequencyEveryTime, unknownFutureValue.
    expiration_requirement: Optional[ExpirationRequirement] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SessionLifetimePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SessionLifetimePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SessionLifetimePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .expiration_requirement import ExpirationRequirement

        from .expiration_requirement import ExpirationRequirement

        fields: Dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "expirationRequirement": lambda n : setattr(self, 'expiration_requirement', n.get_enum_value(ExpirationRequirement)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("detail", self.detail)
        writer.write_enum_value("expirationRequirement", self.expiration_requirement)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

