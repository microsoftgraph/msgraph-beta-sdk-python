from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import information_protection_action

from . import information_protection_action

class RemoveContentFooterAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new RemoveContentFooterAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.removeContentFooterAction"
        # The name of the UI element of the footer to be removed.
        self._ui_element_names: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoveContentFooterAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoveContentFooterAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoveContentFooterAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import information_protection_action

        fields: Dict[str, Callable[[Any], None]] = {
            "uiElementNames": lambda n : setattr(self, 'ui_element_names', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("uiElementNames", self.ui_element_names)
    
    @property
    def ui_element_names(self,) -> Optional[List[str]]:
        """
        Gets the uiElementNames property value. The name of the UI element of the footer to be removed.
        Returns: Optional[List[str]]
        """
        return self._ui_element_names
    
    @ui_element_names.setter
    def ui_element_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the uiElementNames property value. The name of the UI element of the footer to be removed.
        Args:
            value: Value to set for the ui_element_names property.
        """
        self._ui_element_names = value
    

