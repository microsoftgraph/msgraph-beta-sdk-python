from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

information_protection_action = lazy_import('msgraph.generated.models.security.information_protection_action')

class RemoveWatermarkAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new RemoveWatermarkAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.removeWatermarkAction"
        # The name of the UI element of watermark to be removed.
        self._ui_element_names: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoveWatermarkAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoveWatermarkAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoveWatermarkAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ui_element_names": lambda n : setattr(self, 'ui_element_names', n.get_collection_of_primitive_values(str)),
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
        Gets the uiElementNames property value. The name of the UI element of watermark to be removed.
        Returns: Optional[List[str]]
        """
        return self._ui_element_names
    
    @ui_element_names.setter
    def ui_element_names(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the uiElementNames property value. The name of the UI element of watermark to be removed.
        Args:
            value: Value to set for the uiElementNames property.
        """
        self._ui_element_names = value
    

