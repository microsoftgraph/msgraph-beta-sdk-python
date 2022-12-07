from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

user_identity = lazy_import('msgraph.generated.models.user_identity')

class AuditUserIdentity(user_identity.UserIdentity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuditUserIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.auditUserIdentity"
        # For user sign ins, the identifier of the tenant that the user is a member of.
        self._home_tenant_id: Optional[str] = None
        # For user sign ins, the name of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Azure AD to show the tenant content.
        self._home_tenant_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditUserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditUserIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditUserIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "home_tenant_id": lambda n : setattr(self, 'home_tenant_id', n.get_str_value()),
            "home_tenant_name": lambda n : setattr(self, 'home_tenant_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_tenant_id(self,) -> Optional[str]:
        """
        Gets the homeTenantId property value. For user sign ins, the identifier of the tenant that the user is a member of.
        Returns: Optional[str]
        """
        return self._home_tenant_id
    
    @home_tenant_id.setter
    def home_tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the homeTenantId property value. For user sign ins, the identifier of the tenant that the user is a member of.
        Args:
            value: Value to set for the homeTenantId property.
        """
        self._home_tenant_id = value
    
    @property
    def home_tenant_name(self,) -> Optional[str]:
        """
        Gets the homeTenantName property value. For user sign ins, the name of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Azure AD to show the tenant content.
        Returns: Optional[str]
        """
        return self._home_tenant_name
    
    @home_tenant_name.setter
    def home_tenant_name(self,value: Optional[str] = None) -> None:
        """
        Sets the homeTenantName property value. For user sign ins, the name of the tenant that the user is a member of. Only populated in cases where the home tenant has provided affirmative consent to Azure AD to show the tenant content.
        Args:
            value: Value to set for the homeTenantName property.
        """
        self._home_tenant_name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("homeTenantId", self.home_tenant_id)
        writer.write_str_value("homeTenantName", self.home_tenant_name)
    

