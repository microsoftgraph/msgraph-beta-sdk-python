from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AllowedValue(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new allowedValue and sets the default values.
        """
        super().__init__()
        # Indicates whether the predefined value is active or deactivated. If set to false, this predefined value cannot be assigned to any additional supported directory objects.
        self._is_active: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AllowedValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AllowedValue
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AllowedValue()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_active": lambda n : setattr(self, 'is_active', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_active(self,) -> Optional[bool]:
        """
        Gets the isActive property value. Indicates whether the predefined value is active or deactivated. If set to false, this predefined value cannot be assigned to any additional supported directory objects.
        Returns: Optional[bool]
        """
        return self._is_active
    
    @is_active.setter
    def is_active(self,value: Optional[bool] = None) -> None:
        """
        Sets the isActive property value. Indicates whether the predefined value is active or deactivated. If set to false, this predefined value cannot be assigned to any additional supported directory objects.
        Args:
            value: Value to set for the isActive property.
        """
        self._is_active = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isActive", self.is_active)
    

