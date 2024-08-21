from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_user_role import EducationUserRole

@dataclass
class EducationIdentityMatchingOptions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The appliesTo property
    applies_to: Optional[EducationUserRole] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the source property, which should be a field name in the source data. This property is case-sensitive.
    source_property_name: Optional[str] = None
    # The domain to suffix with the source property to match on the target. If provided as null, the source property will be used to match with the target property.
    target_domain: Optional[str] = None
    # The name of the target property, which should be a valid property in Microsoft Entra ID. This property is case-sensitive.
    target_property_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationIdentityMatchingOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationIdentityMatchingOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationIdentityMatchingOptions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .education_user_role import EducationUserRole

        from .education_user_role import EducationUserRole

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_enum_value(EducationUserRole)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourcePropertyName": lambda n : setattr(self, 'source_property_name', n.get_str_value()),
            "targetDomain": lambda n : setattr(self, 'target_domain', n.get_str_value()),
            "targetPropertyName": lambda n : setattr(self, 'target_property_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("appliesTo", self.applies_to)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourcePropertyName", self.source_property_name)
        writer.write_str_value("targetDomain", self.target_domain)
        writer.write_str_value("targetPropertyName", self.target_property_name)
        writer.write_additional_data_value(self.additional_data)
    

