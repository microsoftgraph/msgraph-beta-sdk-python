from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, exact_data_match_store_column, exact_match_data_store

from . import entity

@dataclass
class ExactMatchDataStoreBase(entity.Entity):
    # The columns property
    columns: Optional[List[exact_data_match_store_column.ExactDataMatchStoreColumn]] = None
    # The dataLastUpdatedDateTime property
    data_last_updated_date_time: Optional[datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExactMatchDataStoreBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchDataStoreBase
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.exactMatchDataStore":
                from . import exact_match_data_store

                return exact_match_data_store.ExactMatchDataStore()
        return ExactMatchDataStoreBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, exact_data_match_store_column, exact_match_data_store

        fields: Dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(exact_data_match_store_column.ExactDataMatchStoreColumn)),
            "dataLastUpdatedDateTime": lambda n : setattr(self, 'data_last_updated_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_datetime_value("dataLastUpdatedDateTime", self.data_last_updated_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

