from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, continuous_access_evaluation_session_control, persistent_browser_session_control, secure_sign_in_session_control, sign_in_frequency_session_control

class ConditionalAccessSessionControls(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new conditionalAccessSessionControls and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
        self._application_enforced_restrictions: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl] = None
        # Session control to apply cloud app security.
        self._cloud_app_security: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl] = None
        # Session control for continuous access evaluation settings.
        self._continuous_access_evaluation: Optional[continuous_access_evaluation_session_control.ContinuousAccessEvaluationSessionControl] = None
        # Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
        self._disable_resilience_defaults: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
        self._persistent_browser: Optional[persistent_browser_session_control.PersistentBrowserSessionControl] = None
        # The secureSignInSession property
        self._secure_sign_in_session: Optional[secure_sign_in_session_control.SecureSignInSessionControl] = None
        # Session control to enforce signin frequency.
        self._sign_in_frequency: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl] = None
    
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
    def application_enforced_restrictions(self,) -> Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl]:
        """
        Gets the applicationEnforcedRestrictions property value. Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
        Returns: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl]
        """
        return self._application_enforced_restrictions
    
    @application_enforced_restrictions.setter
    def application_enforced_restrictions(self,value: Optional[application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl] = None) -> None:
        """
        Sets the applicationEnforcedRestrictions property value. Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control.
        Args:
            value: Value to set for the application_enforced_restrictions property.
        """
        self._application_enforced_restrictions = value
    
    @property
    def cloud_app_security(self,) -> Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl]:
        """
        Gets the cloudAppSecurity property value. Session control to apply cloud app security.
        Returns: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl]
        """
        return self._cloud_app_security
    
    @cloud_app_security.setter
    def cloud_app_security(self,value: Optional[cloud_app_security_session_control.CloudAppSecuritySessionControl] = None) -> None:
        """
        Sets the cloudAppSecurity property value. Session control to apply cloud app security.
        Args:
            value: Value to set for the cloud_app_security property.
        """
        self._cloud_app_security = value
    
    @property
    def continuous_access_evaluation(self,) -> Optional[continuous_access_evaluation_session_control.ContinuousAccessEvaluationSessionControl]:
        """
        Gets the continuousAccessEvaluation property value. Session control for continuous access evaluation settings.
        Returns: Optional[continuous_access_evaluation_session_control.ContinuousAccessEvaluationSessionControl]
        """
        return self._continuous_access_evaluation
    
    @continuous_access_evaluation.setter
    def continuous_access_evaluation(self,value: Optional[continuous_access_evaluation_session_control.ContinuousAccessEvaluationSessionControl] = None) -> None:
        """
        Sets the continuousAccessEvaluation property value. Session control for continuous access evaluation settings.
        Args:
            value: Value to set for the continuous_access_evaluation property.
        """
        self._continuous_access_evaluation = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessSessionControls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessSessionControls
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConditionalAccessSessionControls()
    
    @property
    def disable_resilience_defaults(self,) -> Optional[bool]:
        """
        Gets the disableResilienceDefaults property value. Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
        Returns: Optional[bool]
        """
        return self._disable_resilience_defaults
    
    @disable_resilience_defaults.setter
    def disable_resilience_defaults(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableResilienceDefaults property value. Session control that determines whether it is acceptable for Azure AD to extend existing sessions based on information collected prior to an outage or not.
        Args:
            value: Value to set for the disable_resilience_defaults property.
        """
        self._disable_resilience_defaults = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import application_enforced_restrictions_session_control, cloud_app_security_session_control, continuous_access_evaluation_session_control, persistent_browser_session_control, secure_sign_in_session_control, sign_in_frequency_session_control

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationEnforcedRestrictions": lambda n : setattr(self, 'application_enforced_restrictions', n.get_object_value(application_enforced_restrictions_session_control.ApplicationEnforcedRestrictionsSessionControl)),
            "cloudAppSecurity": lambda n : setattr(self, 'cloud_app_security', n.get_object_value(cloud_app_security_session_control.CloudAppSecuritySessionControl)),
            "continuousAccessEvaluation": lambda n : setattr(self, 'continuous_access_evaluation', n.get_object_value(continuous_access_evaluation_session_control.ContinuousAccessEvaluationSessionControl)),
            "disableResilienceDefaults": lambda n : setattr(self, 'disable_resilience_defaults', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "persistentBrowser": lambda n : setattr(self, 'persistent_browser', n.get_object_value(persistent_browser_session_control.PersistentBrowserSessionControl)),
            "secureSignInSession": lambda n : setattr(self, 'secure_sign_in_session', n.get_object_value(secure_sign_in_session_control.SecureSignInSessionControl)),
            "signInFrequency": lambda n : setattr(self, 'sign_in_frequency', n.get_object_value(sign_in_frequency_session_control.SignInFrequencySessionControl)),
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
    def persistent_browser(self,) -> Optional[persistent_browser_session_control.PersistentBrowserSessionControl]:
        """
        Gets the persistentBrowser property value. Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
        Returns: Optional[persistent_browser_session_control.PersistentBrowserSessionControl]
        """
        return self._persistent_browser
    
    @persistent_browser.setter
    def persistent_browser(self,value: Optional[persistent_browser_session_control.PersistentBrowserSessionControl] = None) -> None:
        """
        Sets the persistentBrowser property value. Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly.
        Args:
            value: Value to set for the persistent_browser property.
        """
        self._persistent_browser = value
    
    @property
    def secure_sign_in_session(self,) -> Optional[secure_sign_in_session_control.SecureSignInSessionControl]:
        """
        Gets the secureSignInSession property value. The secureSignInSession property
        Returns: Optional[secure_sign_in_session_control.SecureSignInSessionControl]
        """
        return self._secure_sign_in_session
    
    @secure_sign_in_session.setter
    def secure_sign_in_session(self,value: Optional[secure_sign_in_session_control.SecureSignInSessionControl] = None) -> None:
        """
        Sets the secureSignInSession property value. The secureSignInSession property
        Args:
            value: Value to set for the secure_sign_in_session property.
        """
        self._secure_sign_in_session = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("applicationEnforcedRestrictions", self.application_enforced_restrictions)
        writer.write_object_value("cloudAppSecurity", self.cloud_app_security)
        writer.write_object_value("continuousAccessEvaluation", self.continuous_access_evaluation)
        writer.write_bool_value("disableResilienceDefaults", self.disable_resilience_defaults)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("persistentBrowser", self.persistent_browser)
        writer.write_object_value("secureSignInSession", self.secure_sign_in_session)
        writer.write_object_value("signInFrequency", self.sign_in_frequency)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sign_in_frequency(self,) -> Optional[sign_in_frequency_session_control.SignInFrequencySessionControl]:
        """
        Gets the signInFrequency property value. Session control to enforce signin frequency.
        Returns: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl]
        """
        return self._sign_in_frequency
    
    @sign_in_frequency.setter
    def sign_in_frequency(self,value: Optional[sign_in_frequency_session_control.SignInFrequencySessionControl] = None) -> None:
        """
        Sets the signInFrequency property value. Session control to enforce signin frequency.
        Args:
            value: Value to set for the sign_in_frequency property.
        """
        self._sign_in_frequency = value
    

