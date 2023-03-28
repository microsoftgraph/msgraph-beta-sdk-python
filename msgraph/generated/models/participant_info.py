from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import endpoint_type, identity_set

class ParticipantInfo(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new participantInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.
        self._country_code: Optional[str] = None
        # The type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue. Read-only.
        self._endpoint_type: Optional[endpoint_type.EndpointType] = None
        # The identity property
        self._identity: Optional[identity_set.IdentitySet] = None
        # The language culture string. Read-only.
        self._language_id: Optional[str] = None
        # The nonAnonymizedIdentity property
        self._non_anonymized_identity: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The participant ID of the participant. Read-only.
        self._participant_id: Optional[str] = None
        # The client platform ID of the participant. Read-only.
        self._platform_id: Optional[str] = None
        # The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location, unlike countryCode. Read-only.
        self._region: Optional[str] = None
    
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
    
    @property
    def country_code(self,) -> Optional[str]:
        """
        Gets the countryCode property value. The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.
        Returns: Optional[str]
        """
        return self._country_code
    
    @country_code.setter
    def country_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryCode property value. The ISO 3166-1 Alpha-2 country code of the participant's best estimated physical location at the start of the call. Read-only.
        Args:
            value: Value to set for the country_code property.
        """
        self._country_code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParticipantInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParticipantInfo()
    
    @property
    def endpoint_type(self,) -> Optional[endpoint_type.EndpointType]:
        """
        Gets the endpointType property value. The type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue. Read-only.
        Returns: Optional[endpoint_type.EndpointType]
        """
        return self._endpoint_type
    
    @endpoint_type.setter
    def endpoint_type(self,value: Optional[endpoint_type.EndpointType] = None) -> None:
        """
        Sets the endpointType property value. The type of endpoint the participant is using. Possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone and unknownFutureValue. Read-only.
        Args:
            value: Value to set for the endpoint_type property.
        """
        self._endpoint_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import endpoint_type, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "endpointType": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(endpoint_type.EndpointType)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity_set.IdentitySet)),
            "languageId": lambda n : setattr(self, 'language_id', n.get_str_value()),
            "nonAnonymizedIdentity": lambda n : setattr(self, 'non_anonymized_identity', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "participantId": lambda n : setattr(self, 'participant_id', n.get_str_value()),
            "platformId": lambda n : setattr(self, 'platform_id', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
        }
        return fields
    
    @property
    def identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the identity property value. The identity property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the identity property value. The identity property
        Args:
            value: Value to set for the identity property.
        """
        self._identity = value
    
    @property
    def language_id(self,) -> Optional[str]:
        """
        Gets the languageId property value. The language culture string. Read-only.
        Returns: Optional[str]
        """
        return self._language_id
    
    @language_id.setter
    def language_id(self,value: Optional[str] = None) -> None:
        """
        Sets the languageId property value. The language culture string. Read-only.
        Args:
            value: Value to set for the language_id property.
        """
        self._language_id = value
    
    @property
    def non_anonymized_identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the nonAnonymizedIdentity property value. The nonAnonymizedIdentity property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._non_anonymized_identity
    
    @non_anonymized_identity.setter
    def non_anonymized_identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the nonAnonymizedIdentity property value. The nonAnonymizedIdentity property
        Args:
            value: Value to set for the non_anonymized_identity property.
        """
        self._non_anonymized_identity = value
    
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
    def participant_id(self,) -> Optional[str]:
        """
        Gets the participantId property value. The participant ID of the participant. Read-only.
        Returns: Optional[str]
        """
        return self._participant_id
    
    @participant_id.setter
    def participant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the participantId property value. The participant ID of the participant. Read-only.
        Args:
            value: Value to set for the participant_id property.
        """
        self._participant_id = value
    
    @property
    def platform_id(self,) -> Optional[str]:
        """
        Gets the platformId property value. The client platform ID of the participant. Read-only.
        Returns: Optional[str]
        """
        return self._platform_id
    
    @platform_id.setter
    def platform_id(self,value: Optional[str] = None) -> None:
        """
        Sets the platformId property value. The client platform ID of the participant. Read-only.
        Args:
            value: Value to set for the platform_id property.
        """
        self._platform_id = value
    
    @property
    def region(self,) -> Optional[str]:
        """
        Gets the region property value. The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location, unlike countryCode. Read-only.
        Returns: Optional[str]
        """
        return self._region
    
    @region.setter
    def region(self,value: Optional[str] = None) -> None:
        """
        Sets the region property value. The home region of the participant. This can be a country, a continent, or a larger geographic region. This does not change based on the participant's current physical location, unlike countryCode. Read-only.
        Args:
            value: Value to set for the region property.
        """
        self._region = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("countryCode", self.country_code)
        writer.write_enum_value("endpointType", self.endpoint_type)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("languageId", self.language_id)
        writer.write_object_value("nonAnonymizedIdentity", self.non_anonymized_identity)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("participantId", self.participant_id)
        writer.write_str_value("platformId", self.platform_id)
        writer.write_str_value("region", self.region)
        writer.write_additional_data_value(self.additional_data)
    

