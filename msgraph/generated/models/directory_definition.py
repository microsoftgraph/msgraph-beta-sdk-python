from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_definition_discoverabilities = lazy_import('msgraph.generated.models.directory_definition_discoverabilities')
entity = lazy_import('msgraph.generated.models.entity')
object_definition = lazy_import('msgraph.generated.models.object_definition')

class DirectoryDefinition(entity.Entity):
    """
    Casts the previous resource to application.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new directoryDefinition and sets the default values.
        """
        super().__init__()
        # The discoverabilities property
        self._discoverabilities: Optional[directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities] = None
        # Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._discovery_date_time: Optional[datetime] = None
        # Name of the directory. Must be unique within the synchronization schema. Not nullable.
        self._name: Optional[str] = None
        # Collection of objects supported by the directory.
        self._objects: Optional[List[object_definition.ObjectDefinition]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The readOnly property
        self._read_only: Optional[bool] = None
        # Read only value that indicates version discovered. null if discovery has not yet occurred.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DirectoryDefinition()
    
    @property
    def discoverabilities(self,) -> Optional[directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities]:
        """
        Gets the discoverabilities property value. The discoverabilities property
        Returns: Optional[directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities]
        """
        return self._discoverabilities
    
    @discoverabilities.setter
    def discoverabilities(self,value: Optional[directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities] = None) -> None:
        """
        Sets the discoverabilities property value. The discoverabilities property
        Args:
            value: Value to set for the discoverabilities property.
        """
        self._discoverabilities = value
    
    @property
    def discovery_date_time(self,) -> Optional[datetime]:
        """
        Gets the discoveryDateTime property value. Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._discovery_date_time
    
    @discovery_date_time.setter
    def discovery_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the discoveryDateTime property value. Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the discoveryDateTime property.
        """
        self._discovery_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "discoverabilities": lambda n : setattr(self, 'discoverabilities', n.get_enum_value(directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities)),
            "discovery_date_time": lambda n : setattr(self, 'discovery_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objects": lambda n : setattr(self, 'objects', n.get_collection_of_object_values(object_definition.ObjectDefinition)),
            "read_only": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the directory. Must be unique within the synchronization schema. Not nullable.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the directory. Must be unique within the synchronization schema. Not nullable.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def objects(self,) -> Optional[List[object_definition.ObjectDefinition]]:
        """
        Gets the objects property value. Collection of objects supported by the directory.
        Returns: Optional[List[object_definition.ObjectDefinition]]
        """
        return self._objects
    
    @objects.setter
    def objects(self,value: Optional[List[object_definition.ObjectDefinition]] = None) -> None:
        """
        Sets the objects property value. Collection of objects supported by the directory.
        Args:
            value: Value to set for the objects property.
        """
        self._objects = value
    
    @property
    def read_only(self,) -> Optional[bool]:
        """
        Gets the readOnly property value. The readOnly property
        Returns: Optional[bool]
        """
        return self._read_only
    
    @read_only.setter
    def read_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the readOnly property value. The readOnly property
        Args:
            value: Value to set for the readOnly property.
        """
        self._read_only = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("discoverabilities", self.discoverabilities)
        writer.write_datetime_value("discoveryDateTime", self.discovery_date_time)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objects", self.objects)
        writer.write_bool_value("readOnly", self.read_only)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Read only value that indicates version discovered. null if discovery has not yet occurred.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Read only value that indicates version discovered. null if discovery has not yet occurred.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

