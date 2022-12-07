from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AttributeSet(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new attributeSet and sets the default values.
        """
        super().__init__()
        # Description of the attribute set. Can be up to 128 characters long and include Unicode characters. Can be changed later.
        self._description: Optional[str] = None
        # Maximum number of custom security attributes that can be defined in this attribute set. Default value is null. If not specified, the administrator can add up to the maximum of 500 active attributes per tenant. Can be changed later.
        self._max_attributes_per_set: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeSet()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the attribute set. Can be up to 128 characters long and include Unicode characters. Can be changed later.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the attribute set. Can be up to 128 characters long and include Unicode characters. Can be changed later.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "max_attributes_per_set": lambda n : setattr(self, 'max_attributes_per_set', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def max_attributes_per_set(self,) -> Optional[int]:
        """
        Gets the maxAttributesPerSet property value. Maximum number of custom security attributes that can be defined in this attribute set. Default value is null. If not specified, the administrator can add up to the maximum of 500 active attributes per tenant. Can be changed later.
        Returns: Optional[int]
        """
        return self._max_attributes_per_set
    
    @max_attributes_per_set.setter
    def max_attributes_per_set(self,value: Optional[int] = None) -> None:
        """
        Sets the maxAttributesPerSet property value. Maximum number of custom security attributes that can be defined in this attribute set. Default value is null. If not specified, the administrator can add up to the maximum of 500 active attributes per tenant. Can be changed later.
        Args:
            value: Value to set for the maxAttributesPerSet property.
        """
        self._max_attributes_per_set = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_int_value("maxAttributesPerSet", self.max_attributes_per_set)
    

