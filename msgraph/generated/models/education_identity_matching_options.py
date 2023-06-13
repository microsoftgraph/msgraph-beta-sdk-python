from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import education_user_role

@dataclass
class EducationIdentityMatchingOptions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The appliesTo property
    applies_to: Optional[education_user_role.EducationUserRole] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the source property, which should be a field name in the source data. This property is case-sensitive.
    source_property_name: Optional[str] = None
    # The domain to suffix with the source property to match on the target. If provided as null, the source property will be used to match with the target property.
    target_domain: Optional[str] = None
    # The name of the target property, which should be a valid property in Azure AD. This property is case-sensitive.
    target_property_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EducationIdentityMatchingOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityMatchingOptions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EducationIdentityMatchingOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import education_user_role

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_enum_value(education_user_role.EducationUserRole)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourcePropertyName": lambda n : setattr(self, 'source_property_name', n.get_str_value()),
            "targetDomain": lambda n : setattr(self, 'target_domain', n.get_str_value()),
            "targetPropertyName": lambda n : setattr(self, 'target_property_name', n.get_str_value()),
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
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourcePropertyName", self.source_property_name)
        writer.write_str_value("targetDomain", self.target_domain)
        writer.write_str_value("targetPropertyName", self.target_property_name)
        writer.write_additional_data_value(self.additional_data)
    

