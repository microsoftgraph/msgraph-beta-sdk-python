from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserConfiguration(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def binary_data(self,) -> Optional[bytes]:
        """
        Gets the binaryData property value. The binaryData property
        Returns: Optional[bytes]
        """
        return self._binary_data
    
    @binary_data.setter
    def binary_data(self,value: Optional[bytes] = None) -> None:
        """
        Sets the binaryData property value. The binaryData property
        Args:
            value: Value to set for the binaryData property.
        """
        self._binary_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userConfiguration and sets the default values.
        """
        super().__init__()
        # The binaryData property
        self._binary_data: Optional[bytes] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "binary_data": lambda n : setattr(self, 'binary_data', n.get_bytes_value()),
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
        writer.write_object_value("binaryData", self.binary_data)
    

