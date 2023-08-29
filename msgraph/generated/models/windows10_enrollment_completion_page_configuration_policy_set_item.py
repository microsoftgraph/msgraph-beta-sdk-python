from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_set_item import PolicySetItem

from .policy_set_item import PolicySetItem

@dataclass
class Windows10EnrollmentCompletionPageConfigurationPolicySetItem(PolicySetItem):
    """
    A class containing the properties used for Windows10EnrollmentCompletionPageConfiguration PolicySetItem.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10EnrollmentCompletionPageConfigurationPolicySetItem"
    # Priority of the Windows10EnrollmentCompletionPageConfigurationPolicySetItem.
    priority: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10EnrollmentCompletionPageConfigurationPolicySetItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10EnrollmentCompletionPageConfigurationPolicySetItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10EnrollmentCompletionPageConfigurationPolicySetItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .policy_set_item import PolicySetItem

        from .policy_set_item import PolicySetItem

        fields: Dict[str, Callable[[Any], None]] = {
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("priority", self.priority)
    

