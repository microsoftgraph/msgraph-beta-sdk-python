from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

admin_consent_state = lazy_import('msgraph.generated.models.admin_consent_state')

class AdminConsent(AdditionalDataHolder, Parsable):
    """
    Admin consent information.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new adminConsent and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Admin consent state.
        self._share_a_p_n_s_data: Optional[admin_consent_state.AdminConsentState] = None
        # Admin consent state.
        self._share_user_experience_analytics_data: Optional[admin_consent_state.AdminConsentState] = None
    
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
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "share_a_p_n_s_data": lambda n : setattr(self, 'share_a_p_n_s_data', n.get_enum_value(admin_consent_state.AdminConsentState)),
            "share_user_experience_analytics_data": lambda n : setattr(self, 'share_user_experience_analytics_data', n.get_enum_value(admin_consent_state.AdminConsentState)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
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
    
    @property
    def share_a_p_n_s_data(self,) -> Optional[admin_consent_state.AdminConsentState]:
        """
        Gets the shareAPNSData property value. Admin consent state.
        Returns: Optional[admin_consent_state.AdminConsentState]
        """
        return self._share_a_p_n_s_data
    
    @share_a_p_n_s_data.setter
    def share_a_p_n_s_data(self,value: Optional[admin_consent_state.AdminConsentState] = None) -> None:
        """
        Sets the shareAPNSData property value. Admin consent state.
        Args:
            value: Value to set for the shareAPNSData property.
        """
        self._share_a_p_n_s_data = value
    
    @property
    def share_user_experience_analytics_data(self,) -> Optional[admin_consent_state.AdminConsentState]:
        """
        Gets the shareUserExperienceAnalyticsData property value. Admin consent state.
        Returns: Optional[admin_consent_state.AdminConsentState]
        """
        return self._share_user_experience_analytics_data
    
    @share_user_experience_analytics_data.setter
    def share_user_experience_analytics_data(self,value: Optional[admin_consent_state.AdminConsentState] = None) -> None:
        """
        Sets the shareUserExperienceAnalyticsData property value. Admin consent state.
        Args:
            value: Value to set for the shareUserExperienceAnalyticsData property.
        """
        self._share_user_experience_analytics_data = value
    

