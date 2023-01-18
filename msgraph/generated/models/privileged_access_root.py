from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
privileged_access_group = lazy_import('msgraph.generated.models.privileged_access_group')

class PrivilegedAccessRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PrivilegedAccessRoot and sets the default values.
        """
        super().__init__()
        # The group property
        self._group: Optional[privileged_access_group.PrivilegedAccessGroup] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrivilegedAccessRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "group": lambda n : setattr(self, 'group', n.get_object_value(privileged_access_group.PrivilegedAccessGroup)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group(self,) -> Optional[privileged_access_group.PrivilegedAccessGroup]:
        """
        Gets the group property value. The group property
        Returns: Optional[privileged_access_group.PrivilegedAccessGroup]
        """
        return self._group
    
    @group.setter
    def group(self,value: Optional[privileged_access_group.PrivilegedAccessGroup] = None) -> None:
        """
        Sets the group property value. The group property
        Args:
            value: Value to set for the group property.
        """
        self._group = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("group", self.group)
    

