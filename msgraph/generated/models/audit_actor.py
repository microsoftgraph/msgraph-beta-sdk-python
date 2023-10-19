from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .role_scope_tag_info import RoleScopeTagInfo

@dataclass
class AuditActor(AdditionalDataHolder, BackedModel, Parsable):
    """
    A class containing the properties for Audit Actor.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Name of the Application.
    application_display_name: Optional[str] = None
    # AAD Application Id.
    application_id: Optional[str] = None
    # Actor Type.
    audit_actor_type: Optional[str] = None
    # IPAddress.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Remote Tenant Id
    remote_tenant_id: Optional[str] = None
    # Remote User Id
    remote_user_id: Optional[str] = None
    # Service Principal Name (SPN).
    service_principal_name: Optional[str] = None
    # Actor Type.
    type: Optional[str] = None
    # User Id.
    user_id: Optional[str] = None
    # List of user permissions when the audit was performed.
    user_permissions: Optional[List[str]] = None
    # User Principal Name (UPN).
    user_principal_name: Optional[str] = None
    # List of user scope tags when the audit was performed.
    user_role_scope_tags: Optional[List[RoleScopeTagInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditActor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditActor
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuditActor()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .role_scope_tag_info import RoleScopeTagInfo

        from .role_scope_tag_info import RoleScopeTagInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationDisplayName": lambda n : setattr(self, 'application_display_name', n.get_str_value()),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "auditActorType": lambda n : setattr(self, 'audit_actor_type', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remoteTenantId": lambda n : setattr(self, 'remote_tenant_id', n.get_str_value()),
            "remoteUserId": lambda n : setattr(self, 'remote_user_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPermissions": lambda n : setattr(self, 'user_permissions', n.get_collection_of_primitive_values(str)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userRoleScopeTags": lambda n : setattr(self, 'user_role_scope_tags', n.get_collection_of_object_values(RoleScopeTagInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("applicationDisplayName", self.application_display_name)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("auditActorType", self.audit_actor_type)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_str_value("remoteTenantId", self.remote_tenant_id)
        writer.write_str_value("remoteUserId", self.remote_user_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
        writer.write_collection_of_primitive_values("userPermissions", self.user_permissions)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_collection_of_object_values("userRoleScopeTags", self.user_role_scope_tags)
        writer.write_additional_data_value(self.additional_data)
    

