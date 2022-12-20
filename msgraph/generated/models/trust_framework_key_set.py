from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
trust_framework_key = lazy_import('msgraph.generated.models.trust_framework_key')

class TrustFrameworkKeySet(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new trustFrameworkKeySet and sets the default values.
        """
        super().__init__()
        # A collection of the keys.
        self._keys: Optional[List[trust_framework_key.TrustFrameworkKey]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrustFrameworkKeySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TrustFrameworkKeySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TrustFrameworkKeySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "keys": lambda n : setattr(self, 'keys', n.get_collection_of_object_values(trust_framework_key.TrustFrameworkKey)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def keys(self,) -> Optional[List[trust_framework_key.TrustFrameworkKey]]:
        """
        Gets the keys property value. A collection of the keys.
        Returns: Optional[List[trust_framework_key.TrustFrameworkKey]]
        """
        return self._keys
    
    @keys.setter
    def keys(self,value: Optional[List[trust_framework_key.TrustFrameworkKey]] = None) -> None:
        """
        Sets the keys property value. A collection of the keys.
        Args:
            value: Value to set for the keys property.
        """
        self._keys = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("keys", self.keys)
    

