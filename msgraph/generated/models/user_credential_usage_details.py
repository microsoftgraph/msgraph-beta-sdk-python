from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, feature_type, usage_auth_method

from . import entity

@dataclass
class UserCredentialUsageDetails(entity.Entity):
    # The authMethod property
    auth_method: Optional[usage_auth_method.UsageAuthMethod] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    event_date_time: Optional[datetime] = None
    # Provides the failure reason for the corresponding reset or registration workflow.
    failure_reason: Optional[str] = None
    # The feature property
    feature: Optional[feature_type.FeatureType] = None
    # Indicates success or failure of the workflow.
    is_success: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # User name of the user performing the reset or registration workflow.
    user_display_name: Optional[str] = None
    # User principal name of the user performing the reset or registration workflow.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserCredentialUsageDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserCredentialUsageDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserCredentialUsageDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, feature_type, usage_auth_method

        from . import entity, feature_type, usage_auth_method

        fields: Dict[str, Callable[[Any], None]] = {
            "authMethod": lambda n : setattr(self, 'auth_method', n.get_enum_value(usage_auth_method.UsageAuthMethod)),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(feature_type.FeatureType)),
            "isSuccess": lambda n : setattr(self, 'is_success', n.get_bool_value()),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("authMethod", self.auth_method)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_enum_value("feature", self.feature)
        writer.write_bool_value("isSuccess", self.is_success)
        writer.write_str_value("userDisplayName", self.user_display_name)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
    

