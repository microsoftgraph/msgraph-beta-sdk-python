from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_policy_presentation_dropdown_list_item = lazy_import('msgraph.generated.models.group_policy_presentation_dropdown_list_item')
group_policy_uploaded_presentation = lazy_import('msgraph.generated.models.group_policy_uploaded_presentation')

class GroupPolicyPresentationDropdownList(group_policy_uploaded_presentation.GroupPolicyUploadedPresentation):
    def __init__(self,) -> None:
        """
        Instantiates a new GroupPolicyPresentationDropdownList and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.groupPolicyPresentationDropdownList"
        # Localized string value identifying the default choice of the list of items.
        self._default_item: Optional[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem] = None
        # Represents a set of localized display names and their associated values.
        self._items: Optional[List[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem]] = None
        # Requirement to enter a value in the parameter box. The default value is false.
        self._required: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyPresentationDropdownList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyPresentationDropdownList
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyPresentationDropdownList()
    
    @property
    def default_item(self,) -> Optional[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem]:
        """
        Gets the defaultItem property value. Localized string value identifying the default choice of the list of items.
        Returns: Optional[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem]
        """
        return self._default_item
    
    @default_item.setter
    def default_item(self,value: Optional[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem] = None) -> None:
        """
        Sets the defaultItem property value. Localized string value identifying the default choice of the list of items.
        Args:
            value: Value to set for the defaultItem property.
        """
        self._default_item = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_item": lambda n : setattr(self, 'default_item', n.get_object_value(group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def items(self,) -> Optional[List[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem]]:
        """
        Gets the items property value. Represents a set of localized display names and their associated values.
        Returns: Optional[List[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[group_policy_presentation_dropdown_list_item.GroupPolicyPresentationDropdownListItem]] = None) -> None:
        """
        Sets the items property value. Represents a set of localized display names and their associated values.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def required(self,) -> Optional[bool]:
        """
        Gets the required property value. Requirement to enter a value in the parameter box. The default value is false.
        Returns: Optional[bool]
        """
        return self._required
    
    @required.setter
    def required(self,value: Optional[bool] = None) -> None:
        """
        Sets the required property value. Requirement to enter a value in the parameter box. The default value is false.
        Args:
            value: Value to set for the required property.
        """
        self._required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("defaultItem", self.default_item)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_bool_value("required", self.required)
    

