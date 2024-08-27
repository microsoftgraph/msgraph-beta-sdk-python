from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .information_protection_action import InformationProtectionAction
    from .key_value_pair import KeyValuePair

from .information_protection_action import InformationProtectionAction

@dataclass
class MetadataAction(InformationProtectionAction):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.metadataAction"
    # A collection of key-value pairs that should be added to the file.
    metadata_to_add: Optional[List[KeyValuePair]] = None
    # A collection of strings that indicate which keys to remove from the file metadata.
    metadata_to_remove: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MetadataAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MetadataAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MetadataAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .information_protection_action import InformationProtectionAction
        from .key_value_pair import KeyValuePair

        from .information_protection_action import InformationProtectionAction
        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "metadataToAdd": lambda n : setattr(self, 'metadata_to_add', n.get_collection_of_object_values(KeyValuePair)),
            "metadataToRemove": lambda n : setattr(self, 'metadata_to_remove', n.get_collection_of_primitive_values(str)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("metadataToAdd", self.metadata_to_add)
        writer.write_collection_of_primitive_values("metadataToRemove", self.metadata_to_remove)
    

