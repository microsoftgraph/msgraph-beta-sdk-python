from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_configuration = lazy_import('msgraph.generated.models.device_configuration')
secure_assessment_account_type = lazy_import('msgraph.generated.models.secure_assessment_account_type')

class Windows10SecureAssessmentConfiguration(device_configuration.DeviceConfiguration):
    @property
    def allow_printing(self,) -> Optional[bool]:
        """
        Gets the allowPrinting property value. Indicates whether or not to allow the app from printing during the test.
        Returns: Optional[bool]
        """
        return self._allow_printing
    
    @allow_printing.setter
    def allow_printing(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowPrinting property value. Indicates whether or not to allow the app from printing during the test.
        Args:
            value: Value to set for the allowPrinting property.
        """
        self._allow_printing = value
    
    @property
    def allow_screen_capture(self,) -> Optional[bool]:
        """
        Gets the allowScreenCapture property value. Indicates whether or not to allow screen capture capability during a test.
        Returns: Optional[bool]
        """
        return self._allow_screen_capture
    
    @allow_screen_capture.setter
    def allow_screen_capture(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowScreenCapture property value. Indicates whether or not to allow screen capture capability during a test.
        Args:
            value: Value to set for the allowScreenCapture property.
        """
        self._allow_screen_capture = value
    
    @property
    def allow_text_suggestion(self,) -> Optional[bool]:
        """
        Gets the allowTextSuggestion property value. Indicates whether or not to allow text suggestions during the test.
        Returns: Optional[bool]
        """
        return self._allow_text_suggestion
    
    @allow_text_suggestion.setter
    def allow_text_suggestion(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowTextSuggestion property value. Indicates whether or not to allow text suggestions during the test.
        Args:
            value: Value to set for the allowTextSuggestion property.
        """
        self._allow_text_suggestion = value
    
    @property
    def assessment_app_user_model_id(self,) -> Optional[str]:
        """
        Gets the assessmentAppUserModelId property value. Specifies the application user model ID of the assessment app launched when a user signs in to a secure assessment with a local guest account. Important notice: this property must be set with localGuestAccountName in order to make the local guest account sign-in experience work properly for secure assessments.
        Returns: Optional[str]
        """
        return self._assessment_app_user_model_id
    
    @assessment_app_user_model_id.setter
    def assessment_app_user_model_id(self,value: Optional[str] = None) -> None:
        """
        Sets the assessmentAppUserModelId property value. Specifies the application user model ID of the assessment app launched when a user signs in to a secure assessment with a local guest account. Important notice: this property must be set with localGuestAccountName in order to make the local guest account sign-in experience work properly for secure assessments.
        Args:
            value: Value to set for the assessmentAppUserModelId property.
        """
        self._assessment_app_user_model_id = value
    
    @property
    def configuration_account(self,) -> Optional[str]:
        """
        Gets the configurationAccount property value. The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
        Returns: Optional[str]
        """
        return self._configuration_account
    
    @configuration_account.setter
    def configuration_account(self,value: Optional[str] = None) -> None:
        """
        Sets the configurationAccount property value. The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
        Args:
            value: Value to set for the configurationAccount property.
        """
        self._configuration_account = value
    
    @property
    def configuration_account_type(self,) -> Optional[secure_assessment_account_type.SecureAssessmentAccountType]:
        """
        Gets the configurationAccountType property value. Type of accounts that are allowed for Windows10SecureAssessment ConfigurationAccount.
        Returns: Optional[secure_assessment_account_type.SecureAssessmentAccountType]
        """
        return self._configuration_account_type
    
    @configuration_account_type.setter
    def configuration_account_type(self,value: Optional[secure_assessment_account_type.SecureAssessmentAccountType] = None) -> None:
        """
        Sets the configurationAccountType property value. Type of accounts that are allowed for Windows10SecureAssessment ConfigurationAccount.
        Args:
            value: Value to set for the configurationAccountType property.
        """
        self._configuration_account_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10SecureAssessmentConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10SecureAssessmentConfiguration"
        # Indicates whether or not to allow the app from printing during the test.
        self._allow_printing: Optional[bool] = None
        # Indicates whether or not to allow screen capture capability during a test.
        self._allow_screen_capture: Optional[bool] = None
        # Indicates whether or not to allow text suggestions during the test.
        self._allow_text_suggestion: Optional[bool] = None
        # Specifies the application user model ID of the assessment app launched when a user signs in to a secure assessment with a local guest account. Important notice: this property must be set with localGuestAccountName in order to make the local guest account sign-in experience work properly for secure assessments.
        self._assessment_app_user_model_id: Optional[str] = None
        # The account used to configure the Windows device for taking the test. The user can be a domain account (domain/user), an AAD account (username@tenant.com) or a local account (username).
        self._configuration_account: Optional[str] = None
        # Type of accounts that are allowed for Windows10SecureAssessment ConfigurationAccount.
        self._configuration_account_type: Optional[secure_assessment_account_type.SecureAssessmentAccountType] = None
        # Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
        self._launch_uri: Optional[str] = None
        # Specifies the display text for the local guest account shown on the sign-in screen. Typically is the name of an assessment. When the user clicks the local guest account on the sign-in screen, an assessment app is launched with a specified assessment URL. Secure assessments can only be configured with local guest account sign-in on devices running Windows 10, version 1903 or later. Important notice: this property must be set with assessmentAppUserModelID in order to make the local guest account sign-in experience work properly for secure assessments.
        self._local_guest_account_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10SecureAssessmentConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10SecureAssessmentConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10SecureAssessmentConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_printing": lambda n : setattr(self, 'allow_printing', n.get_bool_value()),
            "allow_screen_capture": lambda n : setattr(self, 'allow_screen_capture', n.get_bool_value()),
            "allow_text_suggestion": lambda n : setattr(self, 'allow_text_suggestion', n.get_bool_value()),
            "assessment_app_user_model_id": lambda n : setattr(self, 'assessment_app_user_model_id', n.get_str_value()),
            "configuration_account": lambda n : setattr(self, 'configuration_account', n.get_str_value()),
            "configuration_account_type": lambda n : setattr(self, 'configuration_account_type', n.get_enum_value(secure_assessment_account_type.SecureAssessmentAccountType)),
            "launch_uri": lambda n : setattr(self, 'launch_uri', n.get_str_value()),
            "local_guest_account_name": lambda n : setattr(self, 'local_guest_account_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def launch_uri(self,) -> Optional[str]:
        """
        Gets the launchUri property value. Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
        Returns: Optional[str]
        """
        return self._launch_uri
    
    @launch_uri.setter
    def launch_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the launchUri property value. Url link to an assessment that's automatically loaded when the secure assessment browser is launched. It has to be a valid Url (http[s]://msdn.microsoft.com/).
        Args:
            value: Value to set for the launchUri property.
        """
        self._launch_uri = value
    
    @property
    def local_guest_account_name(self,) -> Optional[str]:
        """
        Gets the localGuestAccountName property value. Specifies the display text for the local guest account shown on the sign-in screen. Typically is the name of an assessment. When the user clicks the local guest account on the sign-in screen, an assessment app is launched with a specified assessment URL. Secure assessments can only be configured with local guest account sign-in on devices running Windows 10, version 1903 or later. Important notice: this property must be set with assessmentAppUserModelID in order to make the local guest account sign-in experience work properly for secure assessments.
        Returns: Optional[str]
        """
        return self._local_guest_account_name
    
    @local_guest_account_name.setter
    def local_guest_account_name(self,value: Optional[str] = None) -> None:
        """
        Sets the localGuestAccountName property value. Specifies the display text for the local guest account shown on the sign-in screen. Typically is the name of an assessment. When the user clicks the local guest account on the sign-in screen, an assessment app is launched with a specified assessment URL. Secure assessments can only be configured with local guest account sign-in on devices running Windows 10, version 1903 or later. Important notice: this property must be set with assessmentAppUserModelID in order to make the local guest account sign-in experience work properly for secure assessments.
        Args:
            value: Value to set for the localGuestAccountName property.
        """
        self._local_guest_account_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowPrinting", self.allow_printing)
        writer.write_bool_value("allowScreenCapture", self.allow_screen_capture)
        writer.write_bool_value("allowTextSuggestion", self.allow_text_suggestion)
        writer.write_str_value("assessmentAppUserModelId", self.assessment_app_user_model_id)
        writer.write_str_value("configurationAccount", self.configuration_account)
        writer.write_enum_value("configurationAccountType", self.configuration_account_type)
        writer.write_str_value("launchUri", self.launch_uri)
        writer.write_str_value("localGuestAccountName", self.local_guest_account_name)
    

