from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

@dataclass
class GroupPolicyPresentationListBox(GroupPolicyUploadedPresentation):
    """
    Represents an ADMX listBox element and an ADMX list element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyPresentationListBox"
    # If this option is specified true the user must specify the registry subkey value and the registry subkey name. The list box shows two columns, one for the name and one for the data. The default value is false.
    explicit_value: Optional[bool] = None
    # Not yet documented
    value_prefix: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationListBox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationListBox
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationListBox()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: Dict[str, Callable[[Any], None]] = {
            "explicitValue": lambda n : setattr(self, 'explicit_value', n.get_bool_value()),
            "valuePrefix": lambda n : setattr(self, 'value_prefix', n.get_str_value()),
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
        writer.write_bool_value("explicitValue", self.explicit_value)
        writer.write_str_value("valuePrefix", self.value_prefix)
    

