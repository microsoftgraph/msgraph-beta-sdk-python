from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
unified_role_permission = lazy_import('msgraph.generated.models.unified_role_permission')

class DefaultUserRoleOverride(entity.Entity):
    """
    Casts the previous resource to application.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new defaultUserRoleOverride and sets the default values.
        """
        super().__init__()
        # The isDefault property
        self._is_default: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The rolePermissions property
        self._role_permissions: Optional[List[unified_role_permission.UnifiedRolePermission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DefaultUserRoleOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DefaultUserRoleOverride
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DefaultUserRoleOverride()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_default": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "role_permissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(unified_role_permission.UnifiedRolePermission)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default(self,) -> Optional[bool]:
        """
        Gets the isDefault property value. The isDefault property
        Returns: Optional[bool]
        """
        return self._is_default
    
    @is_default.setter
    def is_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefault property value. The isDefault property
        Args:
            value: Value to set for the isDefault property.
        """
        self._is_default = value
    
    @property
    def role_permissions(self,) -> Optional[List[unified_role_permission.UnifiedRolePermission]]:
        """
        Gets the rolePermissions property value. The rolePermissions property
        Returns: Optional[List[unified_role_permission.UnifiedRolePermission]]
        """
        return self._role_permissions
    
    @role_permissions.setter
    def role_permissions(self,value: Optional[List[unified_role_permission.UnifiedRolePermission]] = None) -> None:
        """
        Sets the rolePermissions property value. The rolePermissions property
        Args:
            value: Value to set for the rolePermissions property.
        """
        self._role_permissions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
    

