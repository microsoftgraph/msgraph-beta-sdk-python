from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class AccessReviewPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewPolicy and sets the default values.
        """
        super().__init__()
        # Description for this policy. Read-only.
        self._description: Optional[str] = None
        # Display name for this policy. Read-only.
        self._display_name: Optional[str] = None
        # If true, group owners can create and manage access reviews on groups they own.
        self._is_group_owner_management_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for this policy. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for this policy. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for this policy. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for this policy. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_group_owner_management_enabled": lambda n : setattr(self, 'is_group_owner_management_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_group_owner_management_enabled(self,) -> Optional[bool]:
        """
        Gets the isGroupOwnerManagementEnabled property value. If true, group owners can create and manage access reviews on groups they own.
        Returns: Optional[bool]
        """
        return self._is_group_owner_management_enabled
    
    @is_group_owner_management_enabled.setter
    def is_group_owner_management_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isGroupOwnerManagementEnabled property value. If true, group owners can create and manage access reviews on groups they own.
        Args:
            value: Value to set for the isGroupOwnerManagementEnabled property.
        """
        self._is_group_owner_management_enabled = value
    
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isGroupOwnerManagementEnabled", self.is_group_owner_management_enabled)
    

