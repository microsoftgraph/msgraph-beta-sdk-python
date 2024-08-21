from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings
    from .education_synchronization_customizations import EducationSynchronizationCustomizations
    from .education_synchronization_data_provider import EducationSynchronizationDataProvider

from .education_synchronization_data_provider import EducationSynchronizationDataProvider

@dataclass
class EducationOneRosterApiDataProvider(EducationSynchronizationDataProvider):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.educationOneRosterApiDataProvider"
    # The connectionSettings property
    connection_settings: Optional[EducationSynchronizationConnectionSettings] = None
    # The connection URL to the OneRoster instance.
    connection_url: Optional[str] = None
    # Optional customization to be applied to the synchronization profile.
    customizations: Optional[EducationSynchronizationCustomizations] = None
    # The OneRoster Service Provider name as defined by the OneRoster specification.
    provider_name: Optional[str] = None
    # The list of School/Org sourcedId to sync.
    schools_ids: Optional[List[str]] = None
    # The list of academic sessions to sync.
    term_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationOneRosterApiDataProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationOneRosterApiDataProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationOneRosterApiDataProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings
        from .education_synchronization_customizations import EducationSynchronizationCustomizations
        from .education_synchronization_data_provider import EducationSynchronizationDataProvider

        from .education_synchronization_connection_settings import EducationSynchronizationConnectionSettings
        from .education_synchronization_customizations import EducationSynchronizationCustomizations
        from .education_synchronization_data_provider import EducationSynchronizationDataProvider

        fields: Dict[str, Callable[[Any], None]] = {
            "connectionSettings": lambda n : setattr(self, 'connection_settings', n.get_object_value(EducationSynchronizationConnectionSettings)),
            "connectionUrl": lambda n : setattr(self, 'connection_url', n.get_str_value()),
            "customizations": lambda n : setattr(self, 'customizations', n.get_object_value(EducationSynchronizationCustomizations)),
            "providerName": lambda n : setattr(self, 'provider_name', n.get_str_value()),
            "schoolsIds": lambda n : setattr(self, 'schools_ids', n.get_collection_of_primitive_values(str)),
            "termIds": lambda n : setattr(self, 'term_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("connectionSettings", self.connection_settings)
        writer.write_str_value("connectionUrl", self.connection_url)
        writer.write_object_value("customizations", self.customizations)
        writer.write_str_value("providerName", self.provider_name)
        writer.write_collection_of_primitive_values("schoolsIds", self.schools_ids)
        writer.write_collection_of_primitive_values("termIds", self.term_ids)
    

