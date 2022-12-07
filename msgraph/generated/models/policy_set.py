from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
error_code = lazy_import('msgraph.generated.models.error_code')
policy_set_assignment = lazy_import('msgraph.generated.models.policy_set_assignment')
policy_set_item = lazy_import('msgraph.generated.models.policy_set_item')
policy_set_status = lazy_import('msgraph.generated.models.policy_set_status')

class PolicySet(entity.Entity):
    """
    A class containing the properties used for PolicySet.
    """
    @property
    def assignments(self,) -> Optional[List[policy_set_assignment.PolicySetAssignment]]:
        """
        Gets the assignments property value. Assignments of the PolicySet.
        Returns: Optional[List[policy_set_assignment.PolicySetAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[policy_set_assignment.PolicySetAssignment]] = None) -> None:
        """
        Sets the assignments property value. Assignments of the PolicySet.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new policySet and sets the default values.
        """
        super().__init__()
        # Assignments of the PolicySet.
        self._assignments: Optional[List[policy_set_assignment.PolicySetAssignment]] = None
        # Creation time of the PolicySet.
        self._created_date_time: Optional[datetime] = None
        # Description of the PolicySet.
        self._description: Optional[str] = None
        # DisplayName of the PolicySet.
        self._display_name: Optional[str] = None
        # The errorCode property
        self._error_code: Optional[error_code.ErrorCode] = None
        # Tags of the guided deployment
        self._guided_deployment_tags: Optional[List[str]] = None
        # Items of the PolicySet with maximum count 100.
        self._items: Optional[List[policy_set_item.PolicySetItem]] = None
        # Last modified time of the PolicySet.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # RoleScopeTags of the PolicySet
        self._role_scope_tags: Optional[List[str]] = None
        # The enum to specify the status of PolicySet.
        self._status: Optional[policy_set_status.PolicySetStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Creation time of the PolicySet.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Creation time of the PolicySet.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PolicySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PolicySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PolicySet()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description of the PolicySet.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description of the PolicySet.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. DisplayName of the PolicySet.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. DisplayName of the PolicySet.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def error_code(self,) -> Optional[error_code.ErrorCode]:
        """
        Gets the errorCode property value. The errorCode property
        Returns: Optional[error_code.ErrorCode]
        """
        return self._error_code
    
    @error_code.setter
    def error_code(self,value: Optional[error_code.ErrorCode] = None) -> None:
        """
        Sets the errorCode property value. The errorCode property
        Args:
            value: Value to set for the errorCode property.
        """
        self._error_code = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(policy_set_assignment.PolicySetAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "error_code": lambda n : setattr(self, 'error_code', n.get_enum_value(error_code.ErrorCode)),
            "guided_deployment_tags": lambda n : setattr(self, 'guided_deployment_tags', n.get_collection_of_primitive_values(str)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(policy_set_item.PolicySetItem)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "role_scope_tags": lambda n : setattr(self, 'role_scope_tags', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(policy_set_status.PolicySetStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def guided_deployment_tags(self,) -> Optional[List[str]]:
        """
        Gets the guidedDeploymentTags property value. Tags of the guided deployment
        Returns: Optional[List[str]]
        """
        return self._guided_deployment_tags
    
    @guided_deployment_tags.setter
    def guided_deployment_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the guidedDeploymentTags property value. Tags of the guided deployment
        Args:
            value: Value to set for the guidedDeploymentTags property.
        """
        self._guided_deployment_tags = value
    
    @property
    def items(self,) -> Optional[List[policy_set_item.PolicySetItem]]:
        """
        Gets the items property value. Items of the PolicySet with maximum count 100.
        Returns: Optional[List[policy_set_item.PolicySetItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[policy_set_item.PolicySetItem]] = None) -> None:
        """
        Sets the items property value. Items of the PolicySet with maximum count 100.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified time of the PolicySet.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified time of the PolicySet.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def role_scope_tags(self,) -> Optional[List[str]]:
        """
        Gets the roleScopeTags property value. RoleScopeTags of the PolicySet
        Returns: Optional[List[str]]
        """
        return self._role_scope_tags
    
    @role_scope_tags.setter
    def role_scope_tags(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roleScopeTags property value. RoleScopeTags of the PolicySet
        Args:
            value: Value to set for the roleScopeTags property.
        """
        self._role_scope_tags = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_collection_of_primitive_values("guidedDeploymentTags", self.guided_deployment_tags)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("roleScopeTags", self.role_scope_tags)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[policy_set_status.PolicySetStatus]:
        """
        Gets the status property value. The enum to specify the status of PolicySet.
        Returns: Optional[policy_set_status.PolicySetStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[policy_set_status.PolicySetStatus] = None) -> None:
        """
        Sets the status property value. The enum to specify the status of PolicySet.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

