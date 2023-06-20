from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_resource_role, access_package_resource_scope, entity

from . import entity

@dataclass
class AccessPackageResourceRoleScope(entity.Entity):
    # Read-only. Nullable. Supports $expand.
    access_package_resource_role: Optional[access_package_resource_role.AccessPackageResourceRole] = None
    # The accessPackageResourceScope property
    access_package_resource_scope: Optional[access_package_resource_scope.AccessPackageResourceScope] = None
    # The createdBy property
    created_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime] = None
    # The modifiedBy property
    modified_by: Optional[str] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceRoleScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRoleScope
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceRoleScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_resource_role, access_package_resource_scope, entity

        from . import access_package_resource_role, access_package_resource_scope, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "accessPackageResourceRole": lambda n : setattr(self, 'access_package_resource_role', n.get_object_value(access_package_resource_role.AccessPackageResourceRole)),
            "accessPackageResourceScope": lambda n : setattr(self, 'access_package_resource_scope', n.get_object_value(access_package_resource_scope.AccessPackageResourceScope)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "modifiedBy": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("accessPackageResourceRole", self.access_package_resource_role)
        writer.write_object_value("accessPackageResourceScope", self.access_package_resource_scope)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

