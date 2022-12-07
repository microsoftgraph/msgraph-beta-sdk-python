from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

information_protection_action = lazy_import('msgraph.generated.models.security.information_protection_action')

class ProtectByTemplateAction(information_protection_action.InformationProtectionAction):
    def __init__(self,) -> None:
        """
        Instantiates a new ProtectByTemplateAction and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.protectByTemplateAction"
        # The unique identifier for a protection template in Microsoft Purview Information Protection to apply to the content.
        self._template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProtectByTemplateAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProtectByTemplateAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProtectByTemplateAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        writer.write_str_value("templateId", self.template_id)
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. The unique identifier for a protection template in Microsoft Purview Information Protection to apply to the content.
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. The unique identifier for a protection template in Microsoft Purview Information Protection to apply to the content.
        Args:
            value: Value to set for the templateId property.
        """
        self._template_id = value
    

