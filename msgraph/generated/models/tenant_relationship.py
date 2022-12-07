from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

delegated_admin_customer = lazy_import('msgraph.generated.models.delegated_admin_customer')
delegated_admin_relationship = lazy_import('msgraph.generated.models.delegated_admin_relationship')
entity = lazy_import('msgraph.generated.models.entity')
managed_tenant = lazy_import('msgraph.generated.models.managed_tenants.managed_tenant')

class TenantRelationship(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new TenantRelationship and sets the default values.
        """
        super().__init__()
        # The customer who has a delegated admin relationship with a Microsoft partner.
        self._delegated_admin_customers: Optional[List[delegated_admin_customer.DelegatedAdminCustomer]] = None
        # The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
        self._delegated_admin_relationships: Optional[List[delegated_admin_relationship.DelegatedAdminRelationship]] = None
        # The operations available to interact with the multi-tenant management platform.
        self._managed_tenants: Optional[managed_tenant.ManagedTenant] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantRelationship:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantRelationship
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantRelationship()
    
    @property
    def delegated_admin_customers(self,) -> Optional[List[delegated_admin_customer.DelegatedAdminCustomer]]:
        """
        Gets the delegatedAdminCustomers property value. The customer who has a delegated admin relationship with a Microsoft partner.
        Returns: Optional[List[delegated_admin_customer.DelegatedAdminCustomer]]
        """
        return self._delegated_admin_customers
    
    @delegated_admin_customers.setter
    def delegated_admin_customers(self,value: Optional[List[delegated_admin_customer.DelegatedAdminCustomer]] = None) -> None:
        """
        Sets the delegatedAdminCustomers property value. The customer who has a delegated admin relationship with a Microsoft partner.
        Args:
            value: Value to set for the delegatedAdminCustomers property.
        """
        self._delegated_admin_customers = value
    
    @property
    def delegated_admin_relationships(self,) -> Optional[List[delegated_admin_relationship.DelegatedAdminRelationship]]:
        """
        Gets the delegatedAdminRelationships property value. The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
        Returns: Optional[List[delegated_admin_relationship.DelegatedAdminRelationship]]
        """
        return self._delegated_admin_relationships
    
    @delegated_admin_relationships.setter
    def delegated_admin_relationships(self,value: Optional[List[delegated_admin_relationship.DelegatedAdminRelationship]] = None) -> None:
        """
        Sets the delegatedAdminRelationships property value. The details of the delegated administrative privileges that a Microsoft partner has in a customer tenant.
        Args:
            value: Value to set for the delegatedAdminRelationships property.
        """
        self._delegated_admin_relationships = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "delegated_admin_customers": lambda n : setattr(self, 'delegated_admin_customers', n.get_collection_of_object_values(delegated_admin_customer.DelegatedAdminCustomer)),
            "delegated_admin_relationships": lambda n : setattr(self, 'delegated_admin_relationships', n.get_collection_of_object_values(delegated_admin_relationship.DelegatedAdminRelationship)),
            "managed_tenants": lambda n : setattr(self, 'managed_tenants', n.get_object_value(managed_tenant.ManagedTenant)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_tenants(self,) -> Optional[managed_tenant.ManagedTenant]:
        """
        Gets the managedTenants property value. The operations available to interact with the multi-tenant management platform.
        Returns: Optional[managed_tenant.ManagedTenant]
        """
        return self._managed_tenants
    
    @managed_tenants.setter
    def managed_tenants(self,value: Optional[managed_tenant.ManagedTenant] = None) -> None:
        """
        Sets the managedTenants property value. The operations available to interact with the multi-tenant management platform.
        Args:
            value: Value to set for the managedTenants property.
        """
        self._managed_tenants = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("delegatedAdminCustomers", self.delegated_admin_customers)
        writer.write_collection_of_object_values("delegatedAdminRelationships", self.delegated_admin_relationships)
        writer.write_object_value("managedTenants", self.managed_tenants)
    

