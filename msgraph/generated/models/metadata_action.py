from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import information_protection_action, key_value_pair

from . import information_protection_action

class MetadataAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new MetadataAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.metadataAction"
        # A collection of key value pairs that should be added to the file.
        self._metadata_to_add: Optional[List[key_value_pair.KeyValuePair]] = None
        # A collection of strings that indicate which keys to remove from the file metadata.
        self._metadata_to_remove: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MetadataAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MetadataAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MetadataAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import information_protection_action, key_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "metadataToAdd": lambda n : setattr(self, 'metadata_to_add', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "metadataToRemove": lambda n : setattr(self, 'metadata_to_remove', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def metadata_to_add(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the metadataToAdd property value. A collection of key value pairs that should be added to the file.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._metadata_to_add
    
    @metadata_to_add.setter
    def metadata_to_add(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the metadataToAdd property value. A collection of key value pairs that should be added to the file.
        Args:
            value: Value to set for the metadata_to_add property.
        """
        self._metadata_to_add = value
    
    @property
    def metadata_to_remove(self,) -> Optional[List[str]]:
        """
        Gets the metadataToRemove property value. A collection of strings that indicate which keys to remove from the file metadata.
        Returns: Optional[List[str]]
        """
        return self._metadata_to_remove
    
    @metadata_to_remove.setter
    def metadata_to_remove(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the metadataToRemove property value. A collection of strings that indicate which keys to remove from the file metadata.
        Args:
            value: Value to set for the metadata_to_remove property.
        """
        self._metadata_to_remove = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("metadataToAdd", self.metadata_to_add)
        writer.write_collection_of_primitive_values("metadataToRemove", self.metadata_to_remove)
    

