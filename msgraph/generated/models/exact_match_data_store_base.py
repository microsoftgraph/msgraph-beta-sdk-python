from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exact_data_match_store_column import ExactDataMatchStoreColumn
    from .exact_match_data_store import ExactMatchDataStore

from .entity import Entity

@dataclass
class ExactMatchDataStoreBase(Entity):
    # The columns property
    columns: Optional[List[ExactDataMatchStoreColumn]] = None
    # The dataLastUpdatedDateTime property
    data_last_updated_date_time: Optional[datetime.datetime] = None
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
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExactMatchDataStoreBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exactMatchDataStore".casefold():
            from .exact_match_data_store import ExactMatchDataStore

            return ExactMatchDataStore()
        return ExactMatchDataStoreBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exact_data_match_store_column import ExactDataMatchStoreColumn
        from .exact_match_data_store import ExactMatchDataStore

        from .entity import Entity
        from .exact_data_match_store_column import ExactDataMatchStoreColumn
        from .exact_match_data_store import ExactMatchDataStore

        fields: Dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(ExactDataMatchStoreColumn)),
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_datetime_value("dataLastUpdatedDateTime", self.data_last_updated_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
    

