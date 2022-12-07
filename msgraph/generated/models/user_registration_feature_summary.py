from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

included_user_roles = lazy_import('msgraph.generated.models.included_user_roles')
included_user_types = lazy_import('msgraph.generated.models.included_user_types')
user_registration_feature_count = lazy_import('msgraph.generated.models.user_registration_feature_count')

class UserRegistrationFeatureSummary(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new UserRegistrationFeatureSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total number of users accounts, excluding those that are blocked
        self._total_user_count: Optional[int] = None
        # Number of users registered or capable for Multi-Factor Authentication, Self-Service Password Reset and Passwordless Authentication.
        self._user_registration_feature_counts: Optional[List[user_registration_feature_count.UserRegistrationFeatureCount]] = None
        # User role type. Possible values are: all, privilegedAdmin, admin, user.
        self._user_roles: Optional[included_user_roles.IncludedUserRoles] = None
        # User type. Possible values are: all, member, guest.
        self._user_types: Optional[included_user_types.IncludedUserTypes] = None
    
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
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "total_user_count": lambda n : setattr(self, 'total_user_count', n.get_int_value()),
            "user_registration_feature_counts": lambda n : setattr(self, 'user_registration_feature_counts', n.get_collection_of_object_values(user_registration_feature_count.UserRegistrationFeatureCount)),
            "user_roles": lambda n : setattr(self, 'user_roles', n.get_enum_value(included_user_roles.IncludedUserRoles)),
            "user_types": lambda n : setattr(self, 'user_types', n.get_enum_value(included_user_types.IncludedUserTypes)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("totalUserCount", self.total_user_count)
        writer.write_collection_of_object_values("userRegistrationFeatureCounts", self.user_registration_feature_counts)
        writer.write_enum_value("userRoles", self.user_roles)
        writer.write_enum_value("userTypes", self.user_types)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_user_count(self,) -> Optional[int]:
        """
        Gets the totalUserCount property value. Total number of users accounts, excluding those that are blocked
        Returns: Optional[int]
        """
        return self._total_user_count
    
    @total_user_count.setter
    def total_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUserCount property value. Total number of users accounts, excluding those that are blocked
        Args:
            value: Value to set for the totalUserCount property.
        """
        self._total_user_count = value
    
    @property
    def user_registration_feature_counts(self,) -> Optional[List[user_registration_feature_count.UserRegistrationFeatureCount]]:
        """
        Gets the userRegistrationFeatureCounts property value. Number of users registered or capable for Multi-Factor Authentication, Self-Service Password Reset and Passwordless Authentication.
        Returns: Optional[List[user_registration_feature_count.UserRegistrationFeatureCount]]
        """
        return self._user_registration_feature_counts
    
    @user_registration_feature_counts.setter
    def user_registration_feature_counts(self,value: Optional[List[user_registration_feature_count.UserRegistrationFeatureCount]] = None) -> None:
        """
        Sets the userRegistrationFeatureCounts property value. Number of users registered or capable for Multi-Factor Authentication, Self-Service Password Reset and Passwordless Authentication.
        Args:
            value: Value to set for the userRegistrationFeatureCounts property.
        """
        self._user_registration_feature_counts = value
    
    @property
    def user_roles(self,) -> Optional[included_user_roles.IncludedUserRoles]:
        """
        Gets the userRoles property value. User role type. Possible values are: all, privilegedAdmin, admin, user.
        Returns: Optional[included_user_roles.IncludedUserRoles]
        """
        return self._user_roles
    
    @user_roles.setter
    def user_roles(self,value: Optional[included_user_roles.IncludedUserRoles] = None) -> None:
        """
        Sets the userRoles property value. User role type. Possible values are: all, privilegedAdmin, admin, user.
        Args:
            value: Value to set for the userRoles property.
        """
        self._user_roles = value
    
    @property
    def user_types(self,) -> Optional[included_user_types.IncludedUserTypes]:
        """
        Gets the userTypes property value. User type. Possible values are: all, member, guest.
        Returns: Optional[included_user_types.IncludedUserTypes]
        """
        return self._user_types
    
    @user_types.setter
    def user_types(self,value: Optional[included_user_types.IncludedUserTypes] = None) -> None:
        """
        Sets the userTypes property value. User type. Possible values are: all, member, guest.
        Args:
            value: Value to set for the userTypes property.
        """
        self._user_types = value
    

