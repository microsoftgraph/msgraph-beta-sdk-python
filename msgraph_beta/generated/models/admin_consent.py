from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .admin_consent_state import AdminConsentState

@dataclass
class AdminConsent(AdditionalDataHolder, BackedModel, Parsable):
    """
    Admin consent information.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Admin consent state.
    share_a_p_n_s_data: Optional[AdminConsentState] = None
    # Admin consent state.
    share_user_experience_analytics_data: Optional[AdminConsentState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdminConsent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdminConsent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdminConsent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .admin_consent_state import AdminConsentState

        from .admin_consent_state import AdminConsentState

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "shareAPNSData": lambda n : setattr(self, 'share_a_p_n_s_data', n.get_enum_value(AdminConsentState)),
            "shareUserExperienceAnalyticsData": lambda n : setattr(self, 'share_user_experience_analytics_data', n.get_enum_value(AdminConsentState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("shareAPNSData", self.share_a_p_n_s_data)
        writer.write_enum_value("shareUserExperienceAnalyticsData", self.share_user_experience_analytics_data)
        writer.write_additional_data_value(self.additional_data)
    

