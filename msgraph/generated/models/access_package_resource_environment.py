from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_package_resource = lazy_import('msgraph.generated.models.access_package_resource')
connection_info = lazy_import('msgraph.generated.models.connection_info')
entity = lazy_import('msgraph.generated.models.entity')

class AccessPackageResourceEnvironment(entity.Entity):
    @property
    def access_package_resources(self,) -> Optional[List[access_package_resource.AccessPackageResource]]:
        """
        Gets the accessPackageResources property value. Read-only. Required.
        Returns: Optional[List[access_package_resource.AccessPackageResource]]
        """
        return self._access_package_resources
    
    @access_package_resources.setter
    def access_package_resources(self,value: Optional[List[access_package_resource.AccessPackageResource]] = None) -> None:
        """
        Sets the accessPackageResources property value. Read-only. Required.
        Args:
            value: Value to set for the accessPackageResources property.
        """
        self._access_package_resources = value
    
    @property
    def connection_info(self,) -> Optional[connection_info.ConnectionInfo]:
        """
        Gets the connectionInfo property value. Connection information of an environment used to connect to a resource.
        Returns: Optional[connection_info.ConnectionInfo]
        """
        return self._connection_info
    
    @connection_info.setter
    def connection_info(self,value: Optional[connection_info.ConnectionInfo] = None) -> None:
        """
        Sets the connectionInfo property value. Connection information of an environment used to connect to a resource.
        Args:
            value: Value to set for the connectionInfo property.
        """
        self._connection_info = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageResourceEnvironment and sets the default values.
        """
        super().__init__()
        # Read-only. Required.
        self._access_package_resources: Optional[List[access_package_resource.AccessPackageResource]] = None
        # Connection information of an environment used to connect to a resource.
        self._connection_info: Optional[connection_info.ConnectionInfo] = None
        # The display name of the user that created this object.
        self._created_by: Optional[str] = None
        # The date and time that this object was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._created_date_time: Optional[datetime] = None
        # The description of this object.
        self._description: Optional[str] = None
        # The display name of this object.
        self._display_name: Optional[str] = None
        # Determines whether this is default environment or not. It is set to true for all static origin systems, such as Azure AD groups and Azure AD Applications.
        self._is_default_environment: Optional[bool] = None
        # The display name of the entity that last modified this object.
        self._modified_by: Optional[str] = None
        # The date and time that this object was last modified. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The unique identifier of this environment in the origin system.
        self._origin_id: Optional[str] = None
        # The type of the resource in the origin system, that is, SharePointOnline. Requires $filter (eq).
        self._origin_system: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[str]:
        """
        Gets the createdBy property value. The display name of the user that created this object.
        Returns: Optional[str]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[str] = None) -> None:
        """
        Sets the createdBy property value. The display name of the user that created this object.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time that this object was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time that this object was created. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageResourceEnvironment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceEnvironment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageResourceEnvironment()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description of this object.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description of this object.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of this object.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of this object.
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
            "access_package_resources": lambda n : setattr(self, 'access_package_resources', n.get_collection_of_object_values(access_package_resource.AccessPackageResource)),
            "connection_info": lambda n : setattr(self, 'connection_info', n.get_object_value(connection_info.ConnectionInfo)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_default_environment": lambda n : setattr(self, 'is_default_environment', n.get_bool_value()),
            "modified_by": lambda n : setattr(self, 'modified_by', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "origin_id": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "origin_system": lambda n : setattr(self, 'origin_system', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default_environment(self,) -> Optional[bool]:
        """
        Gets the isDefaultEnvironment property value. Determines whether this is default environment or not. It is set to true for all static origin systems, such as Azure AD groups and Azure AD Applications.
        Returns: Optional[bool]
        """
        return self._is_default_environment
    
    @is_default_environment.setter
    def is_default_environment(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultEnvironment property value. Determines whether this is default environment or not. It is set to true for all static origin systems, such as Azure AD groups and Azure AD Applications.
        Args:
            value: Value to set for the isDefaultEnvironment property.
        """
        self._is_default_environment = value
    
    @property
    def modified_by(self,) -> Optional[str]:
        """
        Gets the modifiedBy property value. The display name of the entity that last modified this object.
        Returns: Optional[str]
        """
        return self._modified_by
    
    @modified_by.setter
    def modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the modifiedBy property value. The display name of the entity that last modified this object.
        Args:
            value: Value to set for the modifiedBy property.
        """
        self._modified_by = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The date and time that this object was last modified. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The date and time that this object was last modified. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    @property
    def origin_id(self,) -> Optional[str]:
        """
        Gets the originId property value. The unique identifier of this environment in the origin system.
        Returns: Optional[str]
        """
        return self._origin_id
    
    @origin_id.setter
    def origin_id(self,value: Optional[str] = None) -> None:
        """
        Sets the originId property value. The unique identifier of this environment in the origin system.
        Args:
            value: Value to set for the originId property.
        """
        self._origin_id = value
    
    @property
    def origin_system(self,) -> Optional[str]:
        """
        Gets the originSystem property value. The type of the resource in the origin system, that is, SharePointOnline. Requires $filter (eq).
        Returns: Optional[str]
        """
        return self._origin_system
    
    @origin_system.setter
    def origin_system(self,value: Optional[str] = None) -> None:
        """
        Sets the originSystem property value. The type of the resource in the origin system, that is, SharePointOnline. Requires $filter (eq).
        Args:
            value: Value to set for the originSystem property.
        """
        self._origin_system = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("accessPackageResources", self.access_package_resources)
        writer.write_object_value("connectionInfo", self.connection_info)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isDefaultEnvironment", self.is_default_environment)
        writer.write_str_value("modifiedBy", self.modified_by)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originSystem", self.origin_system)
    

