from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_identity_synchronization_configuration, education_synchronization_data_provider, education_synchronization_error, education_synchronization_license_assignment, education_synchronization_profile_state, education_synchronization_profile_status, entity

from . import entity

@dataclass
class EducationSynchronizationProfile(entity.Entity):
    # The dataProvider property
    data_provider: Optional[education_synchronization_data_provider.EducationSynchronizationDataProvider] = None
    # Name of the configuration profile for syncing identities.
    display_name: Optional[str] = None
    # All errors associated with this synchronization profile.
    errors: Optional[List[education_synchronization_error.EducationSynchronizationError]] = None
    # The date the profile should be considered expired and cease syncing. Provide the date in YYYY-MM-DD format, following ISO 8601. Maximum value is 18 months from profile creation.  (optional)
    expiration_date: Optional[date] = None
    # Determines if School Data Sync should automatically replace unsupported special characters while syncing from source.
    handle_special_character_constraint: Optional[bool] = None
    # The identitySynchronizationConfiguration property
    identity_synchronization_configuration: Optional[education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration] = None
    # License setup configuration.
    licenses_to_assign: Optional[List[education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The synchronization status.
    profile_status: Optional[education_synchronization_profile_status.EducationSynchronizationProfileStatus] = None
    # The state of the profile. Possible values are: provisioning, provisioned, provisioningFailed, deleting, deletionFailed.
    state: Optional[education_synchronization_profile_state.EducationSynchronizationProfileState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationProfile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_identity_synchronization_configuration, education_synchronization_data_provider, education_synchronization_error, education_synchronization_license_assignment, education_synchronization_profile_state, education_synchronization_profile_status, entity

        from . import education_identity_synchronization_configuration, education_synchronization_data_provider, education_synchronization_error, education_synchronization_license_assignment, education_synchronization_profile_state, education_synchronization_profile_status, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "dataProvider": lambda n : setattr(self, 'data_provider', n.get_object_value(education_synchronization_data_provider.EducationSynchronizationDataProvider)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(education_synchronization_error.EducationSynchronizationError)),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "handleSpecialCharacterConstraint": lambda n : setattr(self, 'handle_special_character_constraint', n.get_bool_value()),
            "identitySynchronizationConfiguration": lambda n : setattr(self, 'identity_synchronization_configuration', n.get_object_value(education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration)),
            "licensesToAssign": lambda n : setattr(self, 'licenses_to_assign', n.get_collection_of_object_values(education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment)),
            "profileStatus": lambda n : setattr(self, 'profile_status', n.get_object_value(education_synchronization_profile_status.EducationSynchronizationProfileStatus)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(education_synchronization_profile_state.EducationSynchronizationProfileState)),
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
        writer.write_object_value("dataProvider", self.data_provider)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_bool_value("handleSpecialCharacterConstraint", self.handle_special_character_constraint)
        writer.write_object_value("identitySynchronizationConfiguration", self.identity_synchronization_configuration)
        writer.write_collection_of_object_values("licensesToAssign", self.licenses_to_assign)
        writer.write_object_value("profileStatus", self.profile_status)
        writer.write_enum_value("state", self.state)
    

