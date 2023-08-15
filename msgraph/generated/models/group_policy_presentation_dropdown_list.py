from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group_policy_presentation_dropdown_list_item import GroupPolicyPresentationDropdownListItem
    from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

@dataclass
class GroupPolicyPresentationDropdownList(GroupPolicyUploadedPresentation):
    """
    Represents an ADMX dropdownList element and an ADMX enum element.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupPolicyPresentationDropdownList"
    # Localized string value identifying the default choice of the list of items.
    default_item: Optional[GroupPolicyPresentationDropdownListItem] = None
    # Represents a set of localized display names and their associated values.
    items: Optional[List[GroupPolicyPresentationDropdownListItem]] = None
    # Requirement to enter a value in the parameter box. The default value is false.
    required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationDropdownList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationDropdownList
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return GroupPolicyPresentationDropdownList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group_policy_presentation_dropdown_list_item import GroupPolicyPresentationDropdownListItem
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        from .group_policy_presentation_dropdown_list_item import GroupPolicyPresentationDropdownListItem
        from .group_policy_uploaded_presentation import GroupPolicyUploadedPresentation

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultItem": lambda n : setattr(self, 'default_item', n.get_object_value(GroupPolicyPresentationDropdownListItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(GroupPolicyPresentationDropdownListItem)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
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
        writer.write_object_value("defaultItem", self.default_item)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_bool_value("required", self.required)
    

