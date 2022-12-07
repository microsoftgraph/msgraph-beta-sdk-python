from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_audit_actor_type = lazy_import('msgraph.generated.models.cloud_pc_audit_actor_type')
cloud_pc_user_role_scope_tag_info = lazy_import('msgraph.generated.models.cloud_pc_user_role_scope_tag_info')

class CloudPcAuditActor(AdditionalDataHolder, Parsable):
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
        Gets the applicationDisplayName property value. Name of the application.
        Returns: Optional[str]
        """
        return self._application_display_name
    
    @application_display_name.setter
    def application_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationDisplayName property value. Name of the application.
        Args:
            value: Value to set for the applicationDisplayName property.
        """
        self._application_display_name = value
    
    @property
    def application_id(self,) -> Optional[str]:
        """
        Gets the applicationId property value. Azure AD application ID.
        Returns: Optional[str]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationId property value. Azure AD application ID.
        Args:
            value: Value to set for the applicationId property.
        """
        self._application_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcAuditActor and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of the application.
        self._application_display_name: Optional[str] = None
        # Azure AD application ID.
        self._application_id: Optional[str] = None
        # IP address.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The delegated partner tenant ID.
        self._remote_tenant_id: Optional[str] = None
        # The delegated partner user ID.
        self._remote_user_id: Optional[str] = None
        # Service Principal Name (SPN).
        self._service_principal_name: Optional[str] = None
        # The type property
        self._type: Optional[cloud_pc_audit_actor_type.CloudPcAuditActorType] = None
        # Azure AD user ID.
        self._user_id: Optional[str] = None
        # List of user permissions and application permissions when the audit event was performed.
        self._user_permissions: Optional[List[str]] = None
        # User Principal Name (UPN).
        self._user_principal_name: Optional[str] = None
        # List of role scope tags.
        self._user_role_scope_tags: Optional[List[cloud_pc_user_role_scope_tag_info.CloudPcUserRoleScopeTagInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcAuditActor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAuditActor
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcAuditActor()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_display_name": lambda n : setattr(self, 'application_display_name', n.get_str_value()),
            "application_id": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remote_tenant_id": lambda n : setattr(self, 'remote_tenant_id', n.get_str_value()),
            "remote_user_id": lambda n : setattr(self, 'remote_user_id', n.get_str_value()),
            "service_principal_name": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(cloud_pc_audit_actor_type.CloudPcAuditActorType)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "user_permissions": lambda n : setattr(self, 'user_permissions', n.get_collection_of_primitive_values(str)),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "user_role_scope_tags": lambda n : setattr(self, 'user_role_scope_tags', n.get_collection_of_object_values(cloud_pc_user_role_scope_tag_info.CloudPcUserRoleScopeTagInfo)),
        }
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. IP address.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IP address.
        Args:
            value: Value to set for the ipAddress property.
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
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def remote_tenant_id(self,) -> Optional[str]:
        """
        Gets the remoteTenantId property value. The delegated partner tenant ID.
        Returns: Optional[str]
        """
        return self._remote_tenant_id
    
    @remote_tenant_id.setter
    def remote_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteTenantId property value. The delegated partner tenant ID.
        Args:
            value: Value to set for the remoteTenantId property.
        """
        self._remote_tenant_id = value
    
    @property
    def remote_user_id(self,) -> Optional[str]:
        """
        Gets the remoteUserId property value. The delegated partner user ID.
        Returns: Optional[str]
        """
        return self._remote_user_id
    
    @remote_user_id.setter
    def remote_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteUserId property value. The delegated partner user ID.
        Args:
            value: Value to set for the remoteUserId property.
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
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("remoteTenantId", self.remote_tenant_id)
        writer.write_str_value("remoteUserId", self.remote_user_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_enum_value("type", self.type)
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
            value: Value to set for the servicePrincipalName property.
        """
        self._service_principal_name = value
    
    @property
    def type(self,) -> Optional[cloud_pc_audit_actor_type.CloudPcAuditActorType]:
        """
        Gets the type property value. The type property
        Returns: Optional[cloud_pc_audit_actor_type.CloudPcAuditActorType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[cloud_pc_audit_actor_type.CloudPcAuditActorType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Azure AD user ID.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Azure AD user ID.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    
    @property
    def user_permissions(self,) -> Optional[List[str]]:
        """
        Gets the userPermissions property value. List of user permissions and application permissions when the audit event was performed.
        Returns: Optional[List[str]]
        """
        return self._user_permissions
    
    @user_permissions.setter
    def user_permissions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the userPermissions property value. List of user permissions and application permissions when the audit event was performed.
        Args:
            value: Value to set for the userPermissions property.
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
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    
    @property
    def user_role_scope_tags(self,) -> Optional[List[cloud_pc_user_role_scope_tag_info.CloudPcUserRoleScopeTagInfo]]:
        """
        Gets the userRoleScopeTags property value. List of role scope tags.
        Returns: Optional[List[cloud_pc_user_role_scope_tag_info.CloudPcUserRoleScopeTagInfo]]
        """
        return self._user_role_scope_tags
    
    @user_role_scope_tags.setter
    def user_role_scope_tags(self,value: Optional[List[cloud_pc_user_role_scope_tag_info.CloudPcUserRoleScopeTagInfo]] = None) -> None:
        """
        Sets the userRoleScopeTags property value. List of role scope tags.
        Args:
            value: Value to set for the userRoleScopeTags property.
        """
        self._user_role_scope_tags = value
    

