from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import azure_data_lake_connector, file_data_connector, source_system_definition
    from .. import entity

from .. import entity

class IndustryDataConnector(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new industryDataConnector and sets the default values.
        """
        super().__init__()
        # The name of the data connector. Maximum supported length is 100 characters.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The sourceSystem property
        self._source_system: Optional[source_system_definition.SourceSystemDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IndustryDataConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IndustryDataConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.industryData.azureDataLakeConnector":
                from . import azure_data_lake_connector

                return azure_data_lake_connector.AzureDataLakeConnector()
            if mapping_value == "#microsoft.graph.industryData.fileDataConnector":
                from . import file_data_connector

                return file_data_connector.FileDataConnector()
        return IndustryDataConnector()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the data connector. Maximum supported length is 100 characters.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the data connector. Maximum supported length is 100 characters.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import azure_data_lake_connector, file_data_connector, source_system_definition
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "sourceSystem": lambda n : setattr(self, 'source_system', n.get_object_value(source_system_definition.SourceSystemDefinition)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("sourceSystem", self.source_system)
    
    @property
    def source_system(self,) -> Optional[source_system_definition.SourceSystemDefinition]:
        """
        Gets the sourceSystem property value. The sourceSystem property
        Returns: Optional[source_system_definition.SourceSystemDefinition]
        """
        return self._source_system
    
    @source_system.setter
    def source_system(self,value: Optional[source_system_definition.SourceSystemDefinition] = None) -> None:
        """
        Sets the sourceSystem property value. The sourceSystem property
        Args:
            value: Value to set for the source_system property.
        """
        self._source_system = value
    

