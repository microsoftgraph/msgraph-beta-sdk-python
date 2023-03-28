from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_strength_result

class AuthenticationStrength(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationStrength and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identifier of the authentication strength.
        self._authentication_strength_id: Optional[str] = None
        # The result of the authentication strength. The possible values are: notSet, skippedForProofUp, satisfied, singleChallengeRequired, multipleChallengesRequired, singleRegistrationRequired, multipleRegistrationsRequired, cannotSatisfyDueToCombinationConfiguration, cannotSatisfy, unknownFutureValue.
        self._authentication_strength_result: Optional[authentication_strength_result.AuthenticationStrengthResult] = None
        # The name of the authentication strength.
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def authentication_strength_id(self,) -> Optional[str]:
        """
        Gets the authenticationStrengthId property value. Identifier of the authentication strength.
        Returns: Optional[str]
        """
        return self._authentication_strength_id
    
    @authentication_strength_id.setter
    def authentication_strength_id(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationStrengthId property value. Identifier of the authentication strength.
        Args:
            value: Value to set for the authentication_strength_id property.
        """
        self._authentication_strength_id = value
    
    @property
    def authentication_strength_result(self,) -> Optional[authentication_strength_result.AuthenticationStrengthResult]:
        """
        Gets the authenticationStrengthResult property value. The result of the authentication strength. The possible values are: notSet, skippedForProofUp, satisfied, singleChallengeRequired, multipleChallengesRequired, singleRegistrationRequired, multipleRegistrationsRequired, cannotSatisfyDueToCombinationConfiguration, cannotSatisfy, unknownFutureValue.
        Returns: Optional[authentication_strength_result.AuthenticationStrengthResult]
        """
        return self._authentication_strength_result
    
    @authentication_strength_result.setter
    def authentication_strength_result(self,value: Optional[authentication_strength_result.AuthenticationStrengthResult] = None) -> None:
        """
        Sets the authenticationStrengthResult property value. The result of the authentication strength. The possible values are: notSet, skippedForProofUp, satisfied, singleChallengeRequired, multipleChallengesRequired, singleRegistrationRequired, multipleRegistrationsRequired, cannotSatisfyDueToCombinationConfiguration, cannotSatisfy, unknownFutureValue.
        Args:
            value: Value to set for the authentication_strength_result property.
        """
        self._authentication_strength_result = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrength:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrength
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationStrength()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the authentication strength.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the authentication strength.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_strength_result

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationStrengthId": lambda n : setattr(self, 'authentication_strength_id', n.get_str_value()),
            "authenticationStrengthResult": lambda n : setattr(self, 'authentication_strength_result', n.get_enum_value(authentication_strength_result.AuthenticationStrengthResult)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("authenticationStrengthId", self.authentication_strength_id)
        writer.write_enum_value("authenticationStrengthResult", self.authentication_strength_result)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

