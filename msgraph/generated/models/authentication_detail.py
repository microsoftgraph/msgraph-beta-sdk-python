from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AuthenticationDetail(AdditionalDataHolder, Parsable):
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
    def authentication_method(self,) -> Optional[str]:
        """
        Gets the authenticationMethod property value. The type of authentication method used to perform this step of authentication. Possible values: Password, SMS, Voice, Authenticator App, Software OATH token, Satisfied by token, Previously satisfied.
        Returns: Optional[str]
        """
        return self._authentication_method
    
    @authentication_method.setter
    def authentication_method(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationMethod property value. The type of authentication method used to perform this step of authentication. Possible values: Password, SMS, Voice, Authenticator App, Software OATH token, Satisfied by token, Previously satisfied.
        Args:
            value: Value to set for the authenticationMethod property.
        """
        self._authentication_method = value
    
    @property
    def authentication_method_detail(self,) -> Optional[str]:
        """
        Gets the authenticationMethodDetail property value. Details about the authentication method used to perform this authentication step. For example, phone number (for SMS and voice), device name (for Authenticator app), and password source (e.g. cloud, AD FS, PTA, PHS).
        Returns: Optional[str]
        """
        return self._authentication_method_detail
    
    @authentication_method_detail.setter
    def authentication_method_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationMethodDetail property value. Details about the authentication method used to perform this authentication step. For example, phone number (for SMS and voice), device name (for Authenticator app), and password source (e.g. cloud, AD FS, PTA, PHS).
        Args:
            value: Value to set for the authenticationMethodDetail property.
        """
        self._authentication_method_detail = value
    
    @property
    def authentication_step_date_time(self,) -> Optional[datetime]:
        """
        Gets the authenticationStepDateTime property value. Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._authentication_step_date_time
    
    @authentication_step_date_time.setter
    def authentication_step_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the authenticationStepDateTime property value. Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the authenticationStepDateTime property.
        """
        self._authentication_step_date_time = value
    
    @property
    def authentication_step_requirement(self,) -> Optional[str]:
        """
        Gets the authenticationStepRequirement property value. The step of authentication that this satisfied. For example, primary authentication, or multi-factor authentication.
        Returns: Optional[str]
        """
        return self._authentication_step_requirement
    
    @authentication_step_requirement.setter
    def authentication_step_requirement(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationStepRequirement property value. The step of authentication that this satisfied. For example, primary authentication, or multi-factor authentication.
        Args:
            value: Value to set for the authenticationStepRequirement property.
        """
        self._authentication_step_requirement = value
    
    @property
    def authentication_step_result_detail(self,) -> Optional[str]:
        """
        Gets the authenticationStepResultDetail property value. Details about why the step succeeded or failed. For examples, user is blocked, fraud code entered, no phone input - timed out, phone unreachable, or claim in token.
        Returns: Optional[str]
        """
        return self._authentication_step_result_detail
    
    @authentication_step_result_detail.setter
    def authentication_step_result_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the authenticationStepResultDetail property value. Details about why the step succeeded or failed. For examples, user is blocked, fraud code entered, no phone input - timed out, phone unreachable, or claim in token.
        Args:
            value: Value to set for the authenticationStepResultDetail property.
        """
        self._authentication_step_result_detail = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of authentication method used to perform this step of authentication. Possible values: Password, SMS, Voice, Authenticator App, Software OATH token, Satisfied by token, Previously satisfied.
        self._authentication_method: Optional[str] = None
        # Details about the authentication method used to perform this authentication step. For example, phone number (for SMS and voice), device name (for Authenticator app), and password source (e.g. cloud, AD FS, PTA, PHS).
        self._authentication_method_detail: Optional[str] = None
        # Represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._authentication_step_date_time: Optional[datetime] = None
        # The step of authentication that this satisfied. For example, primary authentication, or multi-factor authentication.
        self._authentication_step_requirement: Optional[str] = None
        # Details about why the step succeeded or failed. For examples, user is blocked, fraud code entered, no phone input - timed out, phone unreachable, or claim in token.
        self._authentication_step_result_detail: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates the status of the authentication step. Possible values: succeeded, failed.
        self._succeeded: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method": lambda n : setattr(self, 'authentication_method', n.get_str_value()),
            "authentication_method_detail": lambda n : setattr(self, 'authentication_method_detail', n.get_str_value()),
            "authentication_step_date_time": lambda n : setattr(self, 'authentication_step_date_time', n.get_datetime_value()),
            "authentication_step_requirement": lambda n : setattr(self, 'authentication_step_requirement', n.get_str_value()),
            "authentication_step_result_detail": lambda n : setattr(self, 'authentication_step_result_detail', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "succeeded": lambda n : setattr(self, 'succeeded', n.get_bool_value()),
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
        writer.write_str_value("authenticationMethod", self.authentication_method)
        writer.write_str_value("authenticationMethodDetail", self.authentication_method_detail)
        writer.write_datetime_value("authenticationStepDateTime", self.authentication_step_date_time)
        writer.write_str_value("authenticationStepRequirement", self.authentication_step_requirement)
        writer.write_str_value("authenticationStepResultDetail", self.authentication_step_result_detail)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("succeeded", self.succeeded)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def succeeded(self,) -> Optional[bool]:
        """
        Gets the succeeded property value. Indicates the status of the authentication step. Possible values: succeeded, failed.
        Returns: Optional[bool]
        """
        return self._succeeded
    
    @succeeded.setter
    def succeeded(self,value: Optional[bool] = None) -> None:
        """
        Sets the succeeded property value. Indicates the status of the authentication step. Possible values: succeeded, failed.
        Args:
            value: Value to set for the succeeded property.
        """
        self._succeeded = value
    

