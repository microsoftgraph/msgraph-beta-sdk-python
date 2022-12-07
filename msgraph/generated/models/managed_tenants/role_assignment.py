from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delegated_privilege_status = lazy_import('msgraph.generated.models.managed_tenants.delegated_privilege_status')
role_definition = lazy_import('msgraph.generated.models.managed_tenants.role_definition')

class RoleAssignment(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def assignment_type(self,) -> Optional[delegated_privilege_status.DelegatedPrivilegeStatus]:
        """
        Gets the assignmentType property value. The type of the admin relationship(s) associated with the role assignment. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges.
        Returns: Optional[delegated_privilege_status.DelegatedPrivilegeStatus]
        """
        return self._assignment_type
    
    @assignment_type.setter
    def assignment_type(self,value: Optional[delegated_privilege_status.DelegatedPrivilegeStatus] = None) -> None:
        """
        Sets the assignmentType property value. The type of the admin relationship(s) associated with the role assignment. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges.
        Args:
            value: Value to set for the assignmentType property.
        """
        self._assignment_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new roleAssignment and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The type of the admin relationship(s) associated with the role assignment. Possible values are: none, delegatedAdminPrivileges, unknownFutureValue, granularDelegatedAdminPrivileges, delegatedAndGranularDelegetedAdminPrivileges. Note that you must use the Prefer: include-unknown-enum-members request header to get the following values from this evolvable enum: granularDelegatedAdminPrivileges , delegatedAndGranularDelegetedAdminPrivileges.
        self._assignment_type: Optional[delegated_privilege_status.DelegatedPrivilegeStatus] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The collection of roles assigned.
        self._roles: Optional[List[role_definition.RoleDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignment_type": lambda n : setattr(self, 'assignment_type', n.get_enum_value(delegated_privilege_status.DelegatedPrivilegeStatus)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_object_values(role_definition.RoleDefinition)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def roles(self,) -> Optional[List[role_definition.RoleDefinition]]:
        """
        Gets the roles property value. The collection of roles assigned.
        Returns: Optional[List[role_definition.RoleDefinition]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[role_definition.RoleDefinition]] = None) -> None:
        """
        Sets the roles property value. The collection of roles assigned.
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("assignmentType", self.assignment_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("roles", self.roles)
        writer.write_additional_data_value(self.additional_data)
    

