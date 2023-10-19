from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EducationalActivityDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Shortened name of the degree or program (example: PhD, MBA)
    abbreviation: Optional[str] = None
    # Extracurricular activities undertaken alongside the program.
    activities: Optional[List[str]] = None
    # Any awards or honors associated with the program.
    awards: Optional[List[str]] = None
    # Short description of the program provided by the user.
    description: Optional[str] = None
    # Long-form name of the program that the user has provided.
    display_name: Optional[str] = None
    # Majors and minors associated with the program. (if applicable)
    fields_of_study: Optional[List[str]] = None
    # The final grade, class, GPA or score.
    grade: Optional[str] = None
    # Additional notes the user has provided.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Link to the degree or program page.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationalActivityDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationalActivityDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EducationalActivityDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "abbreviation": lambda n : setattr(self, 'abbreviation', n.get_str_value()),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_primitive_values(str)),
            "awards": lambda n : setattr(self, 'awards', n.get_collection_of_primitive_values(str)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fieldsOfStudy": lambda n : setattr(self, 'fields_of_study', n.get_collection_of_primitive_values(str)),
            "grade": lambda n : setattr(self, 'grade', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("abbreviation", self.abbreviation)
        writer.write_collection_of_primitive_values("activities", self.activities)
        writer.write_collection_of_primitive_values("awards", self.awards)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("fieldsOfStudy", self.fields_of_study)
        writer.write_str_value("grade", self.grade)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    

