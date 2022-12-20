from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
feature_type = lazy_import('msgraph.generated.models.feature_type')
usage_auth_method = lazy_import('msgraph.generated.models.usage_auth_method')

class UserCredentialUsageDetails(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def auth_method(self,) -> Optional[usage_auth_method.UsageAuthMethod]:
        """
        Gets the authMethod property value. The authMethod property
        Returns: Optional[usage_auth_method.UsageAuthMethod]
        """
        return self._auth_method
    
    @auth_method.setter
    def auth_method(self,value: Optional[usage_auth_method.UsageAuthMethod] = None) -> None:
        """
        Sets the authMethod property value. The authMethod property
        Args:
            value: Value to set for the authMethod property.
        """
        self._auth_method = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userCredentialUsageDetails and sets the default values.
        """
        super().__init__()
        # The authMethod property
        self._auth_method: Optional[usage_auth_method.UsageAuthMethod] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._event_date_time: Optional[datetime] = None
        # Provides the failure reason for the corresponding reset or registration workflow.
        self._failure_reason: Optional[str] = None
        # The feature property
        self._feature: Optional[feature_type.FeatureType] = None
        # Indicates success or failure of the workflow.
        self._is_success: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # User name of the user performing the reset or registration workflow.
        self._user_display_name: Optional[str] = None
        # User principal name of the user performing the reset or registration workflow.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserCredentialUsageDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserCredentialUsageDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserCredentialUsageDetails()
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the eventDateTime property.
        """
        self._event_date_time = value
    
    @property
    def failure_reason(self,) -> Optional[str]:
        """
        Gets the failureReason property value. Provides the failure reason for the corresponding reset or registration workflow.
        Returns: Optional[str]
        """
        return self._failure_reason
    
    @failure_reason.setter
    def failure_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the failureReason property value. Provides the failure reason for the corresponding reset or registration workflow.
        Args:
            value: Value to set for the failureReason property.
        """
        self._failure_reason = value
    
    @property
    def feature(self,) -> Optional[feature_type.FeatureType]:
        """
        Gets the feature property value. The feature property
        Returns: Optional[feature_type.FeatureType]
        """
        return self._feature
    
    @feature.setter
    def feature(self,value: Optional[feature_type.FeatureType] = None) -> None:
        """
        Sets the feature property value. The feature property
        Args:
            value: Value to set for the feature property.
        """
        self._feature = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "auth_method": lambda n : setattr(self, 'auth_method', n.get_enum_value(usage_auth_method.UsageAuthMethod)),
            "event_date_time": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "failure_reason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(feature_type.FeatureType)),
            "is_success": lambda n : setattr(self, 'is_success', n.get_bool_value()),
            "user_display_name": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_success(self,) -> Optional[bool]:
        """
        Gets the isSuccess property value. Indicates success or failure of the workflow.
        Returns: Optional[bool]
        """
        return self._is_success
    
    @is_success.setter
    def is_success(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSuccess property value. Indicates success or failure of the workflow.
        Args:
            value: Value to set for the isSuccess property.
        """
        self._is_success = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("authMethod", self.auth_method)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_enum_value("feature", self.feature)
        writer.write_bool_value("isSuccess", self.is_success)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. User name of the user performing the reset or registration workflow.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. User name of the user performing the reset or registration workflow.
        Args:
            value: Value to set for the userDisplayName property.
        """
        self._user_display_name = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User principal name of the user performing the reset or registration workflow.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User principal name of the user performing the reset or registration workflow.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

