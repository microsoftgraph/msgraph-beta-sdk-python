from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import role_scope_tag_info

class AuditActor(AdditionalDataHolder, Parsable):
    """
    A class containing the properties for Audit Actor.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new auditActor and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of the Application.
        self._application_display_name: Optional[str] = None
        # AAD Application Id.
        self._application_id: Optional[str] = None
        # Actor Type.
        self._audit_actor_type: Optional[str] = None
        # IPAddress.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Remote Tenant Id
        self._remote_tenant_id: Optional[str] = None
        # Remote User Id
        self._remote_user_id: Optional[str] = None
        # Service Principal Name (SPN).
        self._service_principal_name: Optional[str] = None
        # Actor Type.
        self._type: Optional[str] = None
        # User Id.
        self._user_id: Optional[str] = None
        # List of user permissions when the audit was performed.
        self._user_permissions: Optional[List[str]] = None
        # User Principal Name (UPN).
        self._user_principal_name: Optional[str] = None
        # List of user scope tags when the audit was performed.
        self._user_role_scope_tags: Optional[List[role_scope_tag_info.RoleScopeTagInfo]] = None
    
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
    def application_display_name(self,) -> Optional[str]:
        """
        Gets the applicationDisplayName property value. Name of the Application.
        Returns: Optional[str]
        """
        return self._application_display_name
    
    @application_display_name.setter
    def application_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationDisplayName property value. Name of the Application.
        Args:
            value: Value to set for the application_display_name property.
        """
        self._application_display_name = value
    
    @property
    def application_id(self,) -> Optional[str]:
        """
        Gets the applicationId property value. AAD Application Id.
        Returns: Optional[str]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationId property value. AAD Application Id.
        Args:
            value: Value to set for the application_id property.
        """
        self._application_id = value
    
    @property
    def audit_actor_type(self,) -> Optional[str]:
        """
        Gets the auditActorType property value. Actor Type.
        Returns: Optional[str]
        """
        return self._audit_actor_type
    
    @audit_actor_type.setter
    def audit_actor_type(self,value: Optional[str] = None) -> None:
        """
        Sets the auditActorType property value. Actor Type.
        Args:
            value: Value to set for the audit_actor_type property.
        """
        self._audit_actor_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditActor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditActor
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditActor()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import role_scope_tag_info

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationDisplayName": lambda n : setattr(self, 'application_display_name', n.get_str_value()),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "auditActorType": lambda n : setattr(self, 'audit_actor_type', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remoteTenantId": lambda n : setattr(self, 'remote_tenant_id', n.get_str_value()),
            "remoteUserId": lambda n : setattr(self, 'remote_user_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPermissions": lambda n : setattr(self, 'user_permissions', n.get_collection_of_primitive_values(str)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userRoleScopeTags": lambda n : setattr(self, 'user_role_scope_tags', n.get_collection_of_object_values(role_scope_tag_info.RoleScopeTagInfo)),
        }
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. IPAddress.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IPAddress.
        Args:
            value: Value to set for the ip_address property.
        """
        self._ip_address = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def remote_tenant_id(self,) -> Optional[str]:
        """
        Gets the remoteTenantId property value. Remote Tenant Id
        Returns: Optional[str]
        """
        return self._remote_tenant_id
    
    @remote_tenant_id.setter
    def remote_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteTenantId property value. Remote Tenant Id
        Args:
            value: Value to set for the remote_tenant_id property.
        """
        self._remote_tenant_id = value
    
    @property
    def remote_user_id(self,) -> Optional[str]:
        """
        Gets the remoteUserId property value. Remote User Id
        Returns: Optional[str]
        """
        return self._remote_user_id
    
    @remote_user_id.setter
    def remote_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteUserId property value. Remote User Id
        Args:
            value: Value to set for the remote_user_id property.
        """
        self._remote_user_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("applicationDisplayName", self.application_display_name)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("auditActorType", self.audit_actor_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("remoteTenantId", self.remote_tenant_id)
        writer.write_str_value("remoteUserId", self.remote_user_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
        writer.write_collection_of_primitive_values("userPermissions", self.user_permissions)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_collection_of_object_values("userRoleScopeTags", self.user_role_scope_tags)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service_principal_name(self,) -> Optional[str]:
        """
        Gets the servicePrincipalName property value. Service Principal Name (SPN).
        Returns: Optional[str]
        """
        return self._service_principal_name
    
    @service_principal_name.setter
    def service_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the servicePrincipalName property value. Service Principal Name (SPN).
        Args:
            value: Value to set for the service_principal_name property.
        """
        self._service_principal_name = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Actor Type.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Actor Type.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. User Id.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. User Id.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_permissions(self,) -> Optional[List[str]]:
        """
        Gets the userPermissions property value. List of user permissions when the audit was performed.
        Returns: Optional[List[str]]
        """
        return self._user_permissions
    
    @user_permissions.setter
    def user_permissions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the userPermissions property value. List of user permissions when the audit was performed.
        Args:
            value: Value to set for the user_permissions property.
        """
        self._user_permissions = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. User Principal Name (UPN).
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. User Principal Name (UPN).
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def user_role_scope_tags(self,) -> Optional[List[role_scope_tag_info.RoleScopeTagInfo]]:
        """
        Gets the userRoleScopeTags property value. List of user scope tags when the audit was performed.
        Returns: Optional[List[role_scope_tag_info.RoleScopeTagInfo]]
        """
        return self._user_role_scope_tags
    
    @user_role_scope_tags.setter
    def user_role_scope_tags(self,value: Optional[List[role_scope_tag_info.RoleScopeTagInfo]] = None) -> None:
        """
        Sets the userRoleScopeTags property value. List of user scope tags when the audit was performed.
        Args:
            value: Value to set for the user_role_scope_tags property.
        """
        self._user_role_scope_tags = value
    

