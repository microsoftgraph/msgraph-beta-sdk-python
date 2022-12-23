from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_resource_role = lazy_import('msgraph.generated.models.access_package_resource_role')
access_package_resource_scope = lazy_import('msgraph.generated.models.access_package_resource_scope')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageResourceRoleScope(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def access_package_resource_role(self,) -> Optional[access_package_resource_role.AccessPackageResourceRole]:
        """
        Gets the accessPackageResourceRole property value. Read-only. Nullable. Supports $expand.
        Returns: Optional[access_package_resource_role.AccessPackageResourceRole]
        """
        return self._access_package_resource_role
    
    @access_package_resource_role.setter
    def access_package_resource_role(self,value: Optional[access_package_resource_role.AccessPackageResourceRole] = None) -> None:
        """
        Sets the accessPackageResourceRole property value. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the accessPackageResourceRole property.
        """
        self._access_package_resource_role = value
    
    @property
    def access_package_resource_scope(self,) -> Optional[access_package_resource_scope.AccessPackageResourceScope]:
        """
        Gets the accessPackageResourceScope property value. The accessPackageResourceScope property
        Returns: Optional[access_package_resource_scope.AccessPackageResourceScope]
        """
        return self._access_package_resource_scope
    
    @access_package_resource_scope.setter
    def access_package_resource_scope(self,value: Optional[access_package_resource_scope.AccessPackageResourceScope] = None) -> None:
        """
        Sets the accessPackageResourceScope property value. The accessPackageResourceScope property
        Args:
            value: Value to set for the accessPackageResourceScope property.
        """
        self._access_package_resource_scope = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageResourceRoleScope and sets the default values.
        """
        super().__init__()
        # Read-only. Nullable. Supports $expand.
        self._access_package_resource_role: Optional[access_package_resource_role.AccessPackageResourceRole] = None
        # The accessPackageResourceScope property
        self._access_package_resource_scope: Optional[access_package_resource_scope.AccessPackageResourceScope] = None
        # The createdBy property
        self._created_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # The modifiedBy property
        self._modified_by: Optional[str] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceRoleScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceRoleScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResourceRoleScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "access_package_resource_role": lambda n : setattr(self, 'access_package_resource_role', n.get_object_value(access_package_resource_role.AccessPackageResourceRole)),
            "access_package_resource_scope": lambda n : setattr(self, 'access_package_resource_scope', n.get_object_value(access_package_resource_scope.AccessPackageResourceScope)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "modified_by": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modified_by(self,) -> Optional[str]:
        """
        Gets the modifiedBy property value. The modifiedBy property
        Returns: Optional[str]
        """
        return self._modified_by
    
    @modified_by.setter
    def modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the modifiedBy property value. The modifiedBy property
        Args:
            value: Value to set for the modifiedBy property.
        """
        self._modified_by = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("accessPackageResourceRole", self.access_package_resource_role)
        writer.write_object_value("accessPackageResourceScope", self.access_package_resource_scope)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

