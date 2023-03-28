from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_feature_configuration

class MicrosoftAuthenticatorFeatureSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new microsoftAuthenticatorFeatureSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Determines whether users will be able to approve push notifications on other Microsoft applications such as Outlook Mobile.
        self._companion_app_allowed_state: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None
        # Determines whether the user's Authenticator app will show them the client app they are signing into.
        self._display_app_information_required_state: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None
        # Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
        self._display_location_information_required_state: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None
        # Specifies whether the user needs to enter a number in the Authenticator app from the login screen to complete their login. Value is ignored for phone sign-in notifications.
        self._number_matching_required_state: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None
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
    def companion_app_allowed_state(self,) -> Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]:
        """
        Gets the companionAppAllowedState property value. Determines whether users will be able to approve push notifications on other Microsoft applications such as Outlook Mobile.
        Returns: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]
        """
        return self._companion_app_allowed_state
    
    @companion_app_allowed_state.setter
    def companion_app_allowed_state(self,value: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None) -> None:
        """
        Sets the companionAppAllowedState property value. Determines whether users will be able to approve push notifications on other Microsoft applications such as Outlook Mobile.
        Args:
            value: Value to set for the companion_app_allowed_state property.
        """
        self._companion_app_allowed_state = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorFeatureSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorFeatureSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftAuthenticatorFeatureSettings()
    
    @property
    def display_app_information_required_state(self,) -> Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]:
        """
        Gets the displayAppInformationRequiredState property value. Determines whether the user's Authenticator app will show them the client app they are signing into.
        Returns: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]
        """
        return self._display_app_information_required_state
    
    @display_app_information_required_state.setter
    def display_app_information_required_state(self,value: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None) -> None:
        """
        Sets the displayAppInformationRequiredState property value. Determines whether the user's Authenticator app will show them the client app they are signing into.
        Args:
            value: Value to set for the display_app_information_required_state property.
        """
        self._display_app_information_required_state = value
    
    @property
    def display_location_information_required_state(self,) -> Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]:
        """
        Gets the displayLocationInformationRequiredState property value. Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
        Returns: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]
        """
        return self._display_location_information_required_state
    
    @display_location_information_required_state.setter
    def display_location_information_required_state(self,value: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None) -> None:
        """
        Sets the displayLocationInformationRequiredState property value. Determines whether the user's Authenticator app will show them the geographic location of where the authentication request originated from.
        Args:
            value: Value to set for the display_location_information_required_state property.
        """
        self._display_location_information_required_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_feature_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "companionAppAllowedState": lambda n : setattr(self, 'companion_app_allowed_state', n.get_object_value(authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration)),
            "displayAppInformationRequiredState": lambda n : setattr(self, 'display_app_information_required_state', n.get_object_value(authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration)),
            "displayLocationInformationRequiredState": lambda n : setattr(self, 'display_location_information_required_state', n.get_object_value(authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration)),
            "numberMatchingRequiredState": lambda n : setattr(self, 'number_matching_required_state', n.get_object_value(authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def number_matching_required_state(self,) -> Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]:
        """
        Gets the numberMatchingRequiredState property value. Specifies whether the user needs to enter a number in the Authenticator app from the login screen to complete their login. Value is ignored for phone sign-in notifications.
        Returns: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration]
        """
        return self._number_matching_required_state
    
    @number_matching_required_state.setter
    def number_matching_required_state(self,value: Optional[authentication_method_feature_configuration.AuthenticationMethodFeatureConfiguration] = None) -> None:
        """
        Sets the numberMatchingRequiredState property value. Specifies whether the user needs to enter a number in the Authenticator app from the login screen to complete their login. Value is ignored for phone sign-in notifications.
        Args:
            value: Value to set for the number_matching_required_state property.
        """
        self._number_matching_required_state = value
    
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
        writer.write_object_value("companionAppAllowedState", self.companion_app_allowed_state)
        writer.write_object_value("displayAppInformationRequiredState", self.display_app_information_required_state)
        writer.write_object_value("displayLocationInformationRequiredState", self.display_location_information_required_state)
        writer.write_object_value("numberMatchingRequiredState", self.number_matching_required_state)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

