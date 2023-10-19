from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .label import Label
    from .property_type import PropertyType

@dataclass
class Property_(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The aliases property
    aliases: Optional[List[str]] = None
    # The isQueryable property
    is_queryable: Optional[bool] = None
    # The isRefinable property
    is_refinable: Optional[bool] = None
    # The isRetrievable property
    is_retrievable: Optional[bool] = None
    # The isSearchable property
    is_searchable: Optional[bool] = None
    # The labels property
    labels: Optional[List[Label]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type property
    type: Optional[PropertyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Property_:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Property_
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Property_()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .label import Label
        from .property_type import PropertyType

        from .label import Label
        from .property_type import PropertyType

        fields: Dict[str, Callable[[Any], None]] = {
            "aliases": lambda n : setattr(self, 'aliases', n.get_collection_of_primitive_values(str)),
            "isQueryable": lambda n : setattr(self, 'is_queryable', n.get_bool_value()),
            "isRefinable": lambda n : setattr(self, 'is_refinable', n.get_bool_value()),
            "isRetrievable": lambda n : setattr(self, 'is_retrievable', n.get_bool_value()),
            "isSearchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_enum_values(Label)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PropertyType)),
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
        writer.write_collection_of_primitive_values("aliases", self.aliases)
        writer.write_bool_value("isQueryable", self.is_queryable)
        writer.write_bool_value("isRefinable", self.is_refinable)
        writer.write_bool_value("isRetrievable", self.is_retrievable)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_collection_of_enum_values("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

