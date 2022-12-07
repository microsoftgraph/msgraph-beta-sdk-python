from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

education_identity_synchronization_configuration = lazy_import('msgraph.generated.models.education_identity_synchronization_configuration')
education_synchronization_data_provider = lazy_import('msgraph.generated.models.education_synchronization_data_provider')
education_synchronization_error = lazy_import('msgraph.generated.models.education_synchronization_error')
education_synchronization_license_assignment = lazy_import('msgraph.generated.models.education_synchronization_license_assignment')
education_synchronization_profile_state = lazy_import('msgraph.generated.models.education_synchronization_profile_state')
education_synchronization_profile_status = lazy_import('msgraph.generated.models.education_synchronization_profile_status')
entity = lazy_import('msgraph.generated.models.entity')

class EducationSynchronizationProfile(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationSynchronizationProfile and sets the default values.
        """
        super().__init__()
        # The dataProvider property
        self._data_provider: Optional[education_synchronization_data_provider.EducationSynchronizationDataProvider] = None
        # Name of the configuration profile for syncing identities.
        self._display_name: Optional[str] = None
        # All errors associated with this synchronization profile.
        self._errors: Optional[List[education_synchronization_error.EducationSynchronizationError]] = None
        # The date the profile should be considered expired and cease syncing. Provide the date in YYYY-MM-DD format, following ISO 8601. Maximum value is 18 months from profile creation.  (optional)
        self._expiration_date: Optional[Date] = None
        # Determines if School Data Sync should automatically replace unsupported special characters while syncing from source.
        self._handle_special_character_constraint: Optional[bool] = None
        # The identitySynchronizationConfiguration property
        self._identity_synchronization_configuration: Optional[education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration] = None
        # License setup configuration.
        self._licenses_to_assign: Optional[List[education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The synchronization status.
        self._profile_status: Optional[education_synchronization_profile_status.EducationSynchronizationProfileStatus] = None
        # The state of the profile. Possible values are: provisioning, provisioned, provisioningFailed, deleting, deletionFailed.
        self._state: Optional[education_synchronization_profile_state.EducationSynchronizationProfileState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationSynchronizationProfile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationSynchronizationProfile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationSynchronizationProfile()
    
    @property
    def data_provider(self,) -> Optional[education_synchronization_data_provider.EducationSynchronizationDataProvider]:
        """
        Gets the dataProvider property value. The dataProvider property
        Returns: Optional[education_synchronization_data_provider.EducationSynchronizationDataProvider]
        """
        return self._data_provider
    
    @data_provider.setter
    def data_provider(self,value: Optional[education_synchronization_data_provider.EducationSynchronizationDataProvider] = None) -> None:
        """
        Sets the dataProvider property value. The dataProvider property
        Args:
            value: Value to set for the dataProvider property.
        """
        self._data_provider = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the configuration profile for syncing identities.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the configuration profile for syncing identities.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def errors(self,) -> Optional[List[education_synchronization_error.EducationSynchronizationError]]:
        """
        Gets the errors property value. All errors associated with this synchronization profile.
        Returns: Optional[List[education_synchronization_error.EducationSynchronizationError]]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[List[education_synchronization_error.EducationSynchronizationError]] = None) -> None:
        """
        Sets the errors property value. All errors associated with this synchronization profile.
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
    @property
    def expiration_date(self,) -> Optional[Date]:
        """
        Gets the expirationDate property value. The date the profile should be considered expired and cease syncing. Provide the date in YYYY-MM-DD format, following ISO 8601. Maximum value is 18 months from profile creation.  (optional)
        Returns: Optional[Date]
        """
        return self._expiration_date
    
    @expiration_date.setter
    def expiration_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the expirationDate property value. The date the profile should be considered expired and cease syncing. Provide the date in YYYY-MM-DD format, following ISO 8601. Maximum value is 18 months from profile creation.  (optional)
        Args:
            value: Value to set for the expirationDate property.
        """
        self._expiration_date = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "data_provider": lambda n : setattr(self, 'data_provider', n.get_object_value(education_synchronization_data_provider.EducationSynchronizationDataProvider)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(education_synchronization_error.EducationSynchronizationError)),
            "expiration_date": lambda n : setattr(self, 'expiration_date', n.get_object_value(Date)),
            "handle_special_character_constraint": lambda n : setattr(self, 'handle_special_character_constraint', n.get_bool_value()),
            "identity_synchronization_configuration": lambda n : setattr(self, 'identity_synchronization_configuration', n.get_object_value(education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration)),
            "licenses_to_assign": lambda n : setattr(self, 'licenses_to_assign', n.get_collection_of_object_values(education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment)),
            "profile_status": lambda n : setattr(self, 'profile_status', n.get_object_value(education_synchronization_profile_status.EducationSynchronizationProfileStatus)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(education_synchronization_profile_state.EducationSynchronizationProfileState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def handle_special_character_constraint(self,) -> Optional[bool]:
        """
        Gets the handleSpecialCharacterConstraint property value. Determines if School Data Sync should automatically replace unsupported special characters while syncing from source.
        Returns: Optional[bool]
        """
        return self._handle_special_character_constraint
    
    @handle_special_character_constraint.setter
    def handle_special_character_constraint(self,value: Optional[bool] = None) -> None:
        """
        Sets the handleSpecialCharacterConstraint property value. Determines if School Data Sync should automatically replace unsupported special characters while syncing from source.
        Args:
            value: Value to set for the handleSpecialCharacterConstraint property.
        """
        self._handle_special_character_constraint = value
    
    @property
    def identity_synchronization_configuration(self,) -> Optional[education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration]:
        """
        Gets the identitySynchronizationConfiguration property value. The identitySynchronizationConfiguration property
        Returns: Optional[education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration]
        """
        return self._identity_synchronization_configuration
    
    @identity_synchronization_configuration.setter
    def identity_synchronization_configuration(self,value: Optional[education_identity_synchronization_configuration.EducationIdentitySynchronizationConfiguration] = None) -> None:
        """
        Sets the identitySynchronizationConfiguration property value. The identitySynchronizationConfiguration property
        Args:
            value: Value to set for the identitySynchronizationConfiguration property.
        """
        self._identity_synchronization_configuration = value
    
    @property
    def licenses_to_assign(self,) -> Optional[List[education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment]]:
        """
        Gets the licensesToAssign property value. License setup configuration.
        Returns: Optional[List[education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment]]
        """
        return self._licenses_to_assign
    
    @licenses_to_assign.setter
    def licenses_to_assign(self,value: Optional[List[education_synchronization_license_assignment.EducationSynchronizationLicenseAssignment]] = None) -> None:
        """
        Sets the licensesToAssign property value. License setup configuration.
        Args:
            value: Value to set for the licensesToAssign property.
        """
        self._licenses_to_assign = value
    
    @property
    def profile_status(self,) -> Optional[education_synchronization_profile_status.EducationSynchronizationProfileStatus]:
        """
        Gets the profileStatus property value. The synchronization status.
        Returns: Optional[education_synchronization_profile_status.EducationSynchronizationProfileStatus]
        """
        return self._profile_status
    
    @profile_status.setter
    def profile_status(self,value: Optional[education_synchronization_profile_status.EducationSynchronizationProfileStatus] = None) -> None:
        """
        Sets the profileStatus property value. The synchronization status.
        Args:
            value: Value to set for the profileStatus property.
        """
        self._profile_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("dataProvider", self.data_provider)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_object_value("expirationDate", self.expiration_date)
        writer.write_bool_value("handleSpecialCharacterConstraint", self.handle_special_character_constraint)
        writer.write_object_value("identitySynchronizationConfiguration", self.identity_synchronization_configuration)
        writer.write_collection_of_object_values("licensesToAssign", self.licenses_to_assign)
        writer.write_object_value("profileStatus", self.profile_status)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[education_synchronization_profile_state.EducationSynchronizationProfileState]:
        """
        Gets the state property value. The state of the profile. Possible values are: provisioning, provisioned, provisioningFailed, deleting, deletionFailed.
        Returns: Optional[education_synchronization_profile_state.EducationSynchronizationProfileState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[education_synchronization_profile_state.EducationSynchronizationProfileState] = None) -> None:
        """
        Sets the state property value. The state of the profile. Possible values are: provisioning, provisioned, provisioningFailed, deleting, deletionFailed.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

