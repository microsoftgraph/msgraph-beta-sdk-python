from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration
    from .education_synchronization_data_provider import EducationSynchronizationDataProvider
    from .education_synchronization_error import EducationSynchronizationError
    from .education_synchronization_license_assignment import EducationSynchronizationLicenseAssignment
    from .education_synchronization_profile_state import EducationSynchronizationProfileState
    from .education_synchronization_profile_status import EducationSynchronizationProfileStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class EducationSynchronizationProfile(Entity):
    # The dataProvider property
    data_provider: Optional[EducationSynchronizationDataProvider] = None
    # Name of the configuration profile for syncing identities.
    display_name: Optional[str] = None
    # All errors associated with this synchronization profile.
    errors: Optional[List[EducationSynchronizationError]] = None
    # The date the profile should be considered expired and cease syncing. Provide the date in YYYY-MM-DD format, following ISO 8601. Maximum value is 18 months from profile creation.  (optional)
    expiration_date: Optional[datetime.date] = None
    # Determines if School Data Sync should automatically replace unsupported special characters while syncing from source.
    handle_special_character_constraint: Optional[bool] = None
    # The identitySynchronizationConfiguration property
    identity_synchronization_configuration: Optional[EducationIdentitySynchronizationConfiguration] = None
    # License setup configuration.
    licenses_to_assign: Optional[List[EducationSynchronizationLicenseAssignment]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The synchronization status.
    profile_status: Optional[EducationSynchronizationProfileStatus] = None
    # The state of the profile. Possible values are: provisioning, provisioned, provisioningFailed, deleting, deletionFailed.
    state: Optional[EducationSynchronizationProfileState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationSynchronizationProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationProfile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationSynchronizationProfile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration
        from .education_synchronization_data_provider import EducationSynchronizationDataProvider
        from .education_synchronization_error import EducationSynchronizationError
        from .education_synchronization_license_assignment import EducationSynchronizationLicenseAssignment
        from .education_synchronization_profile_state import EducationSynchronizationProfileState
        from .education_synchronization_profile_status import EducationSynchronizationProfileStatus
        from .entity import Entity

        from .education_identity_synchronization_configuration import EducationIdentitySynchronizationConfiguration
        from .education_synchronization_data_provider import EducationSynchronizationDataProvider
        from .education_synchronization_error import EducationSynchronizationError
        from .education_synchronization_license_assignment import EducationSynchronizationLicenseAssignment
        from .education_synchronization_profile_state import EducationSynchronizationProfileState
        from .education_synchronization_profile_status import EducationSynchronizationProfileStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "dataProvider": lambda n : setattr(self, 'data_provider', n.get_object_value(EducationSynchronizationDataProvider)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(EducationSynchronizationError)),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "handleSpecialCharacterConstraint": lambda n : setattr(self, 'handle_special_character_constraint', n.get_bool_value()),
            "identitySynchronizationConfiguration": lambda n : setattr(self, 'identity_synchronization_configuration', n.get_object_value(EducationIdentitySynchronizationConfiguration)),
            "licensesToAssign": lambda n : setattr(self, 'licenses_to_assign', n.get_collection_of_object_values(EducationSynchronizationLicenseAssignment)),
            "profileStatus": lambda n : setattr(self, 'profile_status', n.get_object_value(EducationSynchronizationProfileStatus)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(EducationSynchronizationProfileState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
    

