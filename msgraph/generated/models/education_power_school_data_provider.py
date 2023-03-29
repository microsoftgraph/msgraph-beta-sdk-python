from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_synchronization_customizations, education_synchronization_data_provider

from . import education_synchronization_data_provider

class EducationPowerSchoolDataProvider(education_synchronization_data_provider.EducationSynchronizationDataProvider):
    def __init__(self,) -> None:
        """
        Instantiates a new EducationPowerSchoolDataProvider and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.educationPowerSchoolDataProvider"
        # Indicates whether the source has multiple identifiers for a single student or teacher.
        self._allow_teachers_in_multiple_schools: Optional[bool] = None
        # The client ID used to connect to PowerSchool.
        self._client_id: Optional[str] = None
        # The client secret to authenticate the connection to the PowerSchool instance.
        self._client_secret: Optional[str] = None
        # The connection URL to the PowerSchool instance.
        self._connection_url: Optional[str] = None
        # Optional customization to be applied to the synchronization profile.
        self._customizations: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations] = None
        # The school year to sync.
        self._school_year: Optional[str] = None
        # The list of schools to sync.
        self._schools_ids: Optional[List[str]] = None
    
    @property
    def allow_teachers_in_multiple_schools(self,) -> Optional[bool]:
        """
        Gets the allowTeachersInMultipleSchools property value. Indicates whether the source has multiple identifiers for a single student or teacher.
        Returns: Optional[bool]
        """
        return self._allow_teachers_in_multiple_schools
    
    @allow_teachers_in_multiple_schools.setter
    def allow_teachers_in_multiple_schools(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowTeachersInMultipleSchools property value. Indicates whether the source has multiple identifiers for a single student or teacher.
        Args:
            value: Value to set for the allow_teachers_in_multiple_schools property.
        """
        self._allow_teachers_in_multiple_schools = value
    
    @property
    def client_id(self,) -> Optional[str]:
        """
        Gets the clientId property value. The client ID used to connect to PowerSchool.
        Returns: Optional[str]
        """
        return self._client_id
    
    @client_id.setter
    def client_id(self,value: Optional[str] = None) -> None:
        """
        Sets the clientId property value. The client ID used to connect to PowerSchool.
        Args:
            value: Value to set for the client_id property.
        """
        self._client_id = value
    
    @property
    def client_secret(self,) -> Optional[str]:
        """
        Gets the clientSecret property value. The client secret to authenticate the connection to the PowerSchool instance.
        Returns: Optional[str]
        """
        return self._client_secret
    
    @client_secret.setter
    def client_secret(self,value: Optional[str] = None) -> None:
        """
        Sets the clientSecret property value. The client secret to authenticate the connection to the PowerSchool instance.
        Args:
            value: Value to set for the client_secret property.
        """
        self._client_secret = value
    
    @property
    def connection_url(self,) -> Optional[str]:
        """
        Gets the connectionUrl property value. The connection URL to the PowerSchool instance.
        Returns: Optional[str]
        """
        return self._connection_url
    
    @connection_url.setter
    def connection_url(self,value: Optional[str] = None) -> None:
        """
        Sets the connectionUrl property value. The connection URL to the PowerSchool instance.
        Args:
            value: Value to set for the connection_url property.
        """
        self._connection_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationPowerSchoolDataProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationPowerSchoolDataProvider
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationPowerSchoolDataProvider()
    
    @property
    def customizations(self,) -> Optional[education_synchronization_customizations.EducationSynchronizationCustomizations]:
        """
        Gets the customizations property value. Optional customization to be applied to the synchronization profile.
        Returns: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations]
        """
        return self._customizations
    
    @customizations.setter
    def customizations(self,value: Optional[education_synchronization_customizations.EducationSynchronizationCustomizations] = None) -> None:
        """
        Sets the customizations property value. Optional customization to be applied to the synchronization profile.
        Args:
            value: Value to set for the customizations property.
        """
        self._customizations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_synchronization_customizations, education_synchronization_data_provider

        fields: Dict[str, Callable[[Any], None]] = {
            "allowTeachersInMultipleSchools": lambda n : setattr(self, 'allow_teachers_in_multiple_schools', n.get_bool_value()),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "connectionUrl": lambda n : setattr(self, 'connection_url', n.get_str_value()),
            "customizations": lambda n : setattr(self, 'customizations', n.get_object_value(education_synchronization_customizations.EducationSynchronizationCustomizations)),
            "schoolsIds": lambda n : setattr(self, 'schools_ids', n.get_collection_of_primitive_values(str)),
            "schoolYear": lambda n : setattr(self, 'school_year', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def school_year(self,) -> Optional[str]:
        """
        Gets the schoolYear property value. The school year to sync.
        Returns: Optional[str]
        """
        return self._school_year
    
    @school_year.setter
    def school_year(self,value: Optional[str] = None) -> None:
        """
        Sets the schoolYear property value. The school year to sync.
        Args:
            value: Value to set for the school_year property.
        """
        self._school_year = value
    
    @property
    def schools_ids(self,) -> Optional[List[str]]:
        """
        Gets the schoolsIds property value. The list of schools to sync.
        Returns: Optional[List[str]]
        """
        return self._schools_ids
    
    @schools_ids.setter
    def schools_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the schoolsIds property value. The list of schools to sync.
        Args:
            value: Value to set for the schools_ids property.
        """
        self._schools_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowTeachersInMultipleSchools", self.allow_teachers_in_multiple_schools)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("connectionUrl", self.connection_url)
        writer.write_object_value("customizations", self.customizations)
        writer.write_collection_of_primitive_values("schoolsIds", self.schools_ids)
        writer.write_str_value("schoolYear", self.school_year)
    

