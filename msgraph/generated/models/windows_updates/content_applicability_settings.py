from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import safeguard_settings

class ContentApplicabilitySettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new contentApplicabilitySettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Offer if the update is recommended by a vendor in the list, otherwise withhold the offer.
        self._offer_while_recommended_by: Optional[List[str]] = None
        # Settings for governing safeguard holds on offering content.
        self._safeguard: Optional[safeguard_settings.SafeguardSettings] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContentApplicabilitySettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContentApplicabilitySettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContentApplicabilitySettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import safeguard_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offerWhileRecommendedBy": lambda n : setattr(self, 'offer_while_recommended_by', n.get_collection_of_primitive_values(str)),
            "safeguard": lambda n : setattr(self, 'safeguard', n.get_object_value(safeguard_settings.SafeguardSettings)),
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def offer_while_recommended_by(self,) -> Optional[List[str]]:
        """
        Gets the offerWhileRecommendedBy property value. Offer if the update is recommended by a vendor in the list, otherwise withhold the offer.
        Returns: Optional[List[str]]
        """
        return self._offer_while_recommended_by
    
    @offer_while_recommended_by.setter
    def offer_while_recommended_by(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the offerWhileRecommendedBy property value. Offer if the update is recommended by a vendor in the list, otherwise withhold the offer.
        Args:
            value: Value to set for the offer_while_recommended_by property.
        """
        self._offer_while_recommended_by = value
    
    @property
    def safeguard(self,) -> Optional[safeguard_settings.SafeguardSettings]:
        """
        Gets the safeguard property value. Settings for governing safeguard holds on offering content.
        Returns: Optional[safeguard_settings.SafeguardSettings]
        """
        return self._safeguard
    
    @safeguard.setter
    def safeguard(self,value: Optional[safeguard_settings.SafeguardSettings] = None) -> None:
        """
        Sets the safeguard property value. Settings for governing safeguard holds on offering content.
        Args:
            value: Value to set for the safeguard property.
        """
        self._safeguard = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("offerWhileRecommendedBy", self.offer_while_recommended_by)
        writer.write_object_value("safeguard", self.safeguard)
        writer.write_additional_data_value(self.additional_data)
    

