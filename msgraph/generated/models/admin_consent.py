from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import admin_consent_state

@dataclass
class AdminConsent(AdditionalDataHolder, Parsable):
    """
    Admin consent information.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Admin consent state.
    share_a_p_n_s_data: Optional[admin_consent_state.AdminConsentState] = None
    # Admin consent state.
    share_user_experience_analytics_data: Optional[admin_consent_state.AdminConsentState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AdminConsent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AdminConsent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AdminConsent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import admin_consent_state

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "shareAPNSData": lambda n : setattr(self, 'share_a_p_n_s_data', n.get_enum_value(admin_consent_state.AdminConsentState)),
            "shareUserExperienceAnalyticsData": lambda n : setattr(self, 'share_user_experience_analytics_data', n.get_enum_value(admin_consent_state.AdminConsentState)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("shareAPNSData", self.share_a_p_n_s_data)
        writer.write_enum_value("shareUserExperienceAnalyticsData", self.share_user_experience_analytics_data)
        writer.write_additional_data_value(self.additional_data)
    

