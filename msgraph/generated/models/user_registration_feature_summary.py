from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import included_user_roles, included_user_types, user_registration_feature_count

@dataclass
class UserRegistrationFeatureSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Total number of users accounts, excluding those that are blocked
    total_user_count: Optional[int] = None
    # Number of users registered or capable for Multi-Factor Authentication, Self-Service Password Reset and Passwordless Authentication.
    user_registration_feature_counts: Optional[List[user_registration_feature_count.UserRegistrationFeatureCount]] = None
    # User role type. Possible values are: all, privilegedAdmin, admin, user.
    user_roles: Optional[included_user_roles.IncludedUserRoles] = None
    # User type. Possible values are: all, member, guest.
    user_types: Optional[included_user_types.IncludedUserTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserRegistrationFeatureSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserRegistrationFeatureSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserRegistrationFeatureSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import included_user_roles, included_user_types, user_registration_feature_count

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalUserCount": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
            "userRegistrationFeatureCounts": lambda n : setattr(self, 'user_registration_feature_counts', n.get_collection_of_object_values(user_registration_feature_count.UserRegistrationFeatureCount)),
            "userRoles": lambda n : setattr(self, 'user_roles', n.get_enum_value(included_user_roles.IncludedUserRoles)),
            "userTypes": lambda n : setattr(self, 'user_types', n.get_enum_value(included_user_types.IncludedUserTypes)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalUserCount", self.total_user_count)
        writer.write_collection_of_object_values("userRegistrationFeatureCounts", self.user_registration_feature_counts)
        writer.write_enum_value("userRoles", self.user_roles)
        writer.write_enum_value("userTypes", self.user_types)
        writer.write_additional_data_value(self.additional_data)
    

