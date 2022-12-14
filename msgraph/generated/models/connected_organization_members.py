from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user_set = lazy_import('msgraph.generated.models.user_set')

class ConnectedOrganizationMembers(user_set.UserSet):
    def __init__(self,) -> None:
        """
        Instantiates a new ConnectedOrganizationMembers and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.connectedOrganizationMembers"
        # The name of the connected organization. Read only.
        self._description: Optional[str] = None
        # The ID of the connected organization in entitlement management.
        self._id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConnectedOrganizationMembers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConnectedOrganizationMembers
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConnectedOrganizationMembers()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The name of the connected organization. Read only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The name of the connected organization. Read only.
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
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. The ID of the connected organization in entitlement management.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. The ID of the connected organization in entitlement management.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
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
        writer.write_str_value("id", self.id)
    

