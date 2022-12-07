from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_platform_type = lazy_import('msgraph.generated.models.device_platform_type')
entity = lazy_import('msgraph.generated.models.entity')
payload_by_filter = lazy_import('msgraph.generated.models.payload_by_filter')

class DeviceAndAppManagementAssignmentFilter(entity.Entity):
    """
    A class containing the properties used for Assignment Filter.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceAndAppManagementAssignmentFilter and sets the default values.
        """
        super().__init__()
        # Creation time of the Assignment Filter.
        self._created_date_time: Optional[datetime] = None
        # Description of the Assignment Filter.
        self._description: Optional[str] = None
        # DisplayName of the Assignment Filter.
        self._display_name: Optional[str] = None
        # Last modified time of the Assignment Filter.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Associated assignments for a specific filter
        self._payloads: Optional[List[payload_by_filter.PayloadByFilter]] = None
        # Supported platform types.
        self._platform: Optional[device_platform_type.DevicePlatformType] = None
        # RoleScopeTags of the Assignment Filter.
        self._role_scope_tags: Optional[List[str]] = None
        # Rule definition of the Assignment Filter.
        self._rule: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Creation time of the Assignment Filter.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Creation time of the Assignment Filter.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceAndAppManagementAssignmentFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceAndAppManagementAssignmentFilter
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceAndAppManagementAssignmentFilter()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the Assignment Filter.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the Assignment Filter.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. DisplayName of the Assignment Filter.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. DisplayName of the Assignment Filter.
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
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloads": lambda n : setattr(self, 'payloads', n.get_collection_of_object_values(payload_by_filter.PayloadByFilter)),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(device_platform_type.DevicePlatformType)),
            "role_scope_tags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_primitive_values(str)),
            "rule": lambda n : setattr(self, 'rule', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified time of the Assignment Filter.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified time of the Assignment Filter.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def payloads(self,) -> Optional[List[payload_by_filter.PayloadByFilter]]:
        """
        Gets the payloads property value. Associated assignments for a specific filter
        Returns: Optional[List[payload_by_filter.PayloadByFilter]]
        """
        return self._payloads
    
    @payloads.setter
    def payloads(self,value: Optional[List[payload_by_filter.PayloadByFilter]] = None) -> None:
        """
        Sets the payloads property value. Associated assignments for a specific filter
        Args:
            value: Value to set for the payloads property.
        """
        self._payloads = value
    
    @property
    def platform(self,) -> Optional[device_platform_type.DevicePlatformType]:
        """
        Gets the platform property value. Supported platform types.
        Returns: Optional[device_platform_type.DevicePlatformType]
        """
        return self._platform
    
    @platform.setter
    def platform(self,value: Optional[device_platform_type.DevicePlatformType] = None) -> None:
        """
        Sets the platform property value. Supported platform types.
        Args:
            value: Value to set for the platform property.
        """
        self._platform = value
    
    @property
    def role_scope_tags(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTags property value. RoleScopeTags of the Assignment Filter.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tags
    
    @role_scope_tags.setter
    def role_scope_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTags property value. RoleScopeTags of the Assignment Filter.
        Args:
            value: Value to set for the roleScopeTags property.
        """
        self._role_scope_tags = value
    
    @property
    def rule(self,) -> Optional[str]:
        """
        Gets the rule property value. Rule definition of the Assignment Filter.
        Returns: Optional[str]
        """
        return self._rule
    
    @rule.setter
    def rule(self,value: Optional[str] = None) -> None:
        """
        Sets the rule property value. Rule definition of the Assignment Filter.
        Args:
            value: Value to set for the rule property.
        """
        self._rule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("payloads", self.payloads)
        writer.write_enum_value("platform", self.platform)
        writer.write_collection_of_primitive_values("roleScopeTags", self.role_scope_tags)
        writer.write_str_value("rule", self.rule)
    

