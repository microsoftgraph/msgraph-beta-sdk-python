from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_definition = lazy_import('msgraph.generated.models.directory_definition')
entity = lazy_import('msgraph.generated.models.entity')
synchronization_rule = lazy_import('msgraph.generated.models.synchronization_rule')

class SynchronizationSchema(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationSchema and sets the default values.
        """
        super().__init__()
        # Contains the collection of directories and all of their objects.
        self._directories: Optional[List[directory_definition.DirectoryDefinition]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of synchronization rules configured for the synchronizationJob or synchronizationTemplate.
        self._synchronization_rules: Optional[List[synchronization_rule.SynchronizationRule]] = None
        # The version of the schema, updated automatically with every schema change.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationSchema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationSchema()
    
    @property
    def directories(self,) -> Optional[List[directory_definition.DirectoryDefinition]]:
        """
        Gets the directories property value. Contains the collection of directories and all of their objects.
        Returns: Optional[List[directory_definition.DirectoryDefinition]]
        """
        return self._directories
    
    @directories.setter
    def directories(self,value: Optional[List[directory_definition.DirectoryDefinition]] = None) -> None:
        """
        Sets the directories property value. Contains the collection of directories and all of their objects.
        Args:
            value: Value to set for the directories property.
        """
        self._directories = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "directories": lambda n : setattr(self, 'directories', n.get_collection_of_object_values(directory_definition.DirectoryDefinition)),
            "synchronization_rules": lambda n : setattr(self, 'synchronization_rules', n.get_collection_of_object_values(synchronization_rule.SynchronizationRule)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_collection_of_object_values("directories", self.directories)
        writer.write_collection_of_object_values("synchronizationRules", self.synchronization_rules)
        writer.write_str_value("version", self.version)
    
    @property
    def synchronization_rules(self,) -> Optional[List[synchronization_rule.SynchronizationRule]]:
        """
        Gets the synchronizationRules property value. A collection of synchronization rules configured for the synchronizationJob or synchronizationTemplate.
        Returns: Optional[List[synchronization_rule.SynchronizationRule]]
        """
        return self._synchronization_rules
    
    @synchronization_rules.setter
    def synchronization_rules(self,value: Optional[List[synchronization_rule.SynchronizationRule]] = None) -> None:
        """
        Sets the synchronizationRules property value. A collection of synchronization rules configured for the synchronizationJob or synchronizationTemplate.
        Args:
            value: Value to set for the synchronizationRules property.
        """
        self._synchronization_rules = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version of the schema, updated automatically with every schema change.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version of the schema, updated automatically with every schema change.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

