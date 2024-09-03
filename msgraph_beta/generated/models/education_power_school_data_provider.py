from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_synchronization_customizations import EducationSynchronizationCustomizations
    from .education_synchronization_data_provider import EducationSynchronizationDataProvider

from .education_synchronization_data_provider import EducationSynchronizationDataProvider

@dataclass
class EducationPowerSchoolDataProvider(EducationSynchronizationDataProvider):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationPowerSchoolDataProvider"
    # Indicates whether the source has multiple identifiers for a single student or teacher.
    allow_teachers_in_multiple_schools: Optional[bool] = None
    # The client ID used to connect to PowerSchool.
    client_id: Optional[str] = None
    # The client secret to authenticate the connection to the PowerSchool instance.
    client_secret: Optional[str] = None
    # The connection URL to the PowerSchool instance.
    connection_url: Optional[str] = None
    # Optional customization to be applied to the synchronization profile.
    customizations: Optional[EducationSynchronizationCustomizations] = None
    # The school year to sync.
    school_year: Optional[str] = None
    # The list of schools to sync.
    schools_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationPowerSchoolDataProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationPowerSchoolDataProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationPowerSchoolDataProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_synchronization_customizations import EducationSynchronizationCustomizations
        from .education_synchronization_data_provider import EducationSynchronizationDataProvider

        from .education_synchronization_customizations import EducationSynchronizationCustomizations
        from .education_synchronization_data_provider import EducationSynchronizationDataProvider

        fields: Dict[str, Callable[[Any], None]] = {
            "allowTeachersInMultipleSchools": lambda n : setattr(self, 'allow_teachers_in_multiple_schools', n.get_bool_value()),
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "connectionUrl": lambda n : setattr(self, 'connection_url', n.get_str_value()),
            "customizations": lambda n : setattr(self, 'customizations', n.get_object_value(EducationSynchronizationCustomizations)),
            "schoolYear": lambda n : setattr(self, 'school_year', n.get_str_value()),
            "schoolsIds": lambda n : setattr(self, 'schools_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("allowTeachersInMultipleSchools", self.allow_teachers_in_multiple_schools)
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("connectionUrl", self.connection_url)
        writer.write_object_value("customizations", self.customizations)
        writer.write_str_value("schoolYear", self.school_year)
        writer.write_collection_of_primitive_values("schoolsIds", self.schools_ids)
    

