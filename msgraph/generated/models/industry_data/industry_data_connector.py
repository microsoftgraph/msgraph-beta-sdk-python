from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .azure_data_lake_connector import AzureDataLakeConnector
    from .file_data_connector import FileDataConnector
    from .source_system_definition import SourceSystemDefinition

from ..entity import Entity

@dataclass
class IndustryDataConnector(Entity):
    # The name of the data connector. Maximum supported length is 100 characters.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sourceSystem property
    source_system: Optional[SourceSystemDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataConnector
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.azureDataLakeConnector".casefold():
            from .azure_data_lake_connector import AzureDataLakeConnector

            return AzureDataLakeConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.industryData.fileDataConnector".casefold():
            from .file_data_connector import FileDataConnector

            return FileDataConnector()
        return IndustryDataConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .azure_data_lake_connector import AzureDataLakeConnector
        from .file_data_connector import FileDataConnector
        from .source_system_definition import SourceSystemDefinition

        from ..entity import Entity
        from .azure_data_lake_connector import AzureDataLakeConnector
        from .file_data_connector import FileDataConnector
        from .source_system_definition import SourceSystemDefinition

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "sourceSystem": lambda n : setattr(self, 'source_system', n.get_object_value(SourceSystemDefinition)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("sourceSystem", self.source_system)
    

