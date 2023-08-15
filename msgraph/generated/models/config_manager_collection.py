from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ConfigManagerCollection(Entity):
    """
    A ConfigManager defined collection of devices or users.
    """
    # The collection identifier in SCCM.
    collection_identifier: Optional[str] = None
    # The created date.
    created_date_time: Optional[datetime.datetime] = None
    # The DisplayName.
    display_name: Optional[str] = None
    # The Hierarchy Identifier.
    hierarchy_identifier: Optional[str] = None
    # The HierarchyName.
    hierarchy_name: Optional[str] = None
    # The last modified date.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigManagerCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigManagerCollection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConfigManagerCollection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "collectionIdentifier": lambda n : setattr(self, 'collection_identifier', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hierarchyIdentifier": lambda n : setattr(self, 'hierarchy_identifier', n.get_str_value()),
            "hierarchyName": lambda n : setattr(self, 'hierarchy_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("collectionIdentifier", self.collection_identifier)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("hierarchyIdentifier", self.hierarchy_identifier)
        writer.write_str_value("hierarchyName", self.hierarchy_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

