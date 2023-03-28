from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_external_source, education_school, entity

from . import entity

class EducationOrganization(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new educationOrganization and sets the default values.
        """
        super().__init__()
        # Organization description.
        self._description: Optional[str] = None
        # Organization display name.
        self._display_name: Optional[str] = None
        # Where this user was created from. Possible values are: sis, lms, or manual.
        self._external_source: Optional[education_external_source.EducationExternalSource] = None
        # The externalSourceDetail property
        self._external_source_detail: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationOrganization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationOrganization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.educationSchool":
                from . import education_school

                return education_school.EducationSchool()
        return EducationOrganization()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Organization description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Organization description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Organization display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Organization display name.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def external_source(self,) -> Optional[education_external_source.EducationExternalSource]:
        """
        Gets the externalSource property value. Where this user was created from. Possible values are: sis, lms, or manual.
        Returns: Optional[education_external_source.EducationExternalSource]
        """
        return self._external_source
    
    @external_source.setter
    def external_source(self,value: Optional[education_external_source.EducationExternalSource] = None) -> None:
        """
        Sets the externalSource property value. Where this user was created from. Possible values are: sis, lms, or manual.
        Args:
            value: Value to set for the external_source property.
        """
        self._external_source = value
    
    @property
    def external_source_detail(self,) -> Optional[str]:
        """
        Gets the externalSourceDetail property value. The externalSourceDetail property
        Returns: Optional[str]
        """
        return self._external_source_detail
    
    @external_source_detail.setter
    def external_source_detail(self,value: Optional[str] = None) -> None:
        """
        Sets the externalSourceDetail property value. The externalSourceDetail property
        Args:
            value: Value to set for the external_source_detail property.
        """
        self._external_source_detail = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_external_source, education_school, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalSource": lambda n : setattr(self, 'external_source', n.get_enum_value(education_external_source.EducationExternalSource)),
            "externalSourceDetail": lambda n : setattr(self, 'external_source_detail', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("externalSource", self.external_source)
        writer.write_str_value("externalSourceDetail", self.external_source_detail)
    

