from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class GroupPolicyObjectFile(entity.Entity):
    """
    The Group Policy Object file uploaded by admin.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new groupPolicyObjectFile and sets the default values.
        """
        super().__init__()
        # The Group Policy Object file content.
        self._content: Optional[str] = None
        # The date and time at which the GroupPolicy was first uploaded.
        self._created_date_time: Optional[datetime] = None
        # The Group Policy Object GUID from GPO Xml content
        self._group_policy_object_id: Optional[Guid] = None
        # The date and time at which the GroupPolicyObjectFile was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The distinguished name of the OU.
        self._ou_distinguished_name: Optional[str] = None
        # The list of scope tags for the configuration.
        self._role_scope_tag_ids: Optional[List[str]] = None
    
    @property
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. The Group Policy Object file content.
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. The Group Policy Object file content.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time at which the GroupPolicy was first uploaded.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time at which the GroupPolicy was first uploaded.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> GroupPolicyObjectFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: GroupPolicyObjectFile
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return GroupPolicyObjectFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "group_policy_object_id": lambda n : setattr(self, 'group_policy_object_id', n.get_object_value(Guid)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "ou_distinguished_name": lambda n : setattr(self, 'ou_distinguished_name', n.get_str_value()),
            "role_scope_tag_ids": lambda n : setattr(self, 'role_scope_tag_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def group_policy_object_id(self,) -> Optional[Guid]:
        """
        Gets the groupPolicyObjectId property value. The Group Policy Object GUID from GPO Xml content
        Returns: Optional[Guid]
        """
        return self._group_policy_object_id
    
    @group_policy_object_id.setter
    def group_policy_object_id(self,value: Optional[Guid] = None) -> None:
        """
        Sets the groupPolicyObjectId property value. The Group Policy Object GUID from GPO Xml content
        Args:
            value: Value to set for the groupPolicyObjectId property.
        """
        self._group_policy_object_id = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time at which the GroupPolicyObjectFile was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time at which the GroupPolicyObjectFile was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def ou_distinguished_name(self,) -> Optional[str]:
        """
        Gets the ouDistinguishedName property value. The distinguished name of the OU.
        Returns: Optional[str]
        """
        return self._ou_distinguished_name
    
    @ou_distinguished_name.setter
    def ou_distinguished_name(self,value: Optional[str] = None) -> None:
        """
        Sets the ouDistinguishedName property value. The distinguished name of the OU.
        Args:
            value: Value to set for the ouDistinguishedName property.
        """
        self._ou_distinguished_name = value
    
    @property
    def role_scope_tag_ids(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTagIds property value. The list of scope tags for the configuration.
        Returns: Optional[List[str]]
        """
        return self._role_scope_tag_ids
    
    @role_scope_tag_ids.setter
    def role_scope_tag_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTagIds property value. The list of scope tags for the configuration.
        Args:
            value: Value to set for the roleScopeTagIds property.
        """
        self._role_scope_tag_ids = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("groupPolicyObjectId", self.group_policy_object_id)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("ouDistinguishedName", self.ou_distinguished_name)
        writer.write_collection_of_primitive_values("roleScopeTagIds", self.role_scope_tag_ids)
    

