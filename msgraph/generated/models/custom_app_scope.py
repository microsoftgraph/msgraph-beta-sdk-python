from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_scope, custom_app_scope_attributes_dictionary

from . import app_scope

class CustomAppScope(app_scope.AppScope):
    def __init__(self,) -> None:
        """
        Instantiates a new CustomAppScope and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.customAppScope"
        # The customAttributes property
        self._custom_attributes: Optional[custom_app_scope_attributes_dictionary.CustomAppScopeAttributesDictionary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CustomAppScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CustomAppScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CustomAppScope()
    
    @property
    def custom_attributes(self,) -> Optional[custom_app_scope_attributes_dictionary.CustomAppScopeAttributesDictionary]:
        """
        Gets the customAttributes property value. The customAttributes property
        Returns: Optional[custom_app_scope_attributes_dictionary.CustomAppScopeAttributesDictionary]
        """
        return self._custom_attributes
    
    @custom_attributes.setter
    def custom_attributes(self,value: Optional[custom_app_scope_attributes_dictionary.CustomAppScopeAttributesDictionary] = None) -> None:
        """
        Sets the customAttributes property value. The customAttributes property
        Args:
            value: Value to set for the custom_attributes property.
        """
        self._custom_attributes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_scope, custom_app_scope_attributes_dictionary

        fields: Dict[str, Callable[[Any], None]] = {
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_object_value(custom_app_scope_attributes_dictionary.CustomAppScopeAttributesDictionary)),
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
        writer.write_object_value("customAttributes", self.custom_attributes)
    

