from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
tenant_contract = lazy_import('msgraph.generated.models.managed_tenants.tenant_contract')
tenant_status_information = lazy_import('msgraph.generated.models.managed_tenants.tenant_status_information')

class Tenant(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new tenant and sets the default values.
        """
        super().__init__()
        # The relationship details for the tenant with the managing entity.
        self._contract: Optional[tenant_contract.TenantContract] = None
        # The date and time the tenant was created in the multi-tenant management platform. Optional. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The display name for the tenant. Required. Read-only.
        self._display_name: Optional[str] = None
        # The date and time the tenant was last updated within the multi-tenant management platform. Optional. Read-only.
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        self._tenant_id: Optional[str] = None
        # The onboarding status information for the tenant. Optional. Read-only.
        self._tenant_status_information: Optional[tenant_status_information.TenantStatusInformation] = None
    
    @property
    def contract(self,) -> Optional[tenant_contract.TenantContract]:
        """
        Gets the contract property value. The relationship details for the tenant with the managing entity.
        Returns: Optional[tenant_contract.TenantContract]
        """
        return self._contract
    
    @contract.setter
    def contract(self,value: Optional[tenant_contract.TenantContract] = None) -> None:
        """
        Sets the contract property value. The relationship details for the tenant with the managing entity.
        Args:
            value: Value to set for the contract property.
        """
        self._contract = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the tenant was created in the multi-tenant management platform. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the tenant was created in the multi-tenant management platform. Optional. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Tenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Tenant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Tenant()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the tenant. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the tenant. Required. Read-only.
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
            "contract": lambda n : setattr(self, 'contract', n.get_object_value(tenant_contract.TenantContract)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "tenant_status_information": lambda n : setattr(self, 'tenant_status_information', n.get_object_value(tenant_status_information.TenantStatusInformation)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. The date and time the tenant was last updated within the multi-tenant management platform. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. The date and time the tenant was last updated within the multi-tenant management platform. Optional. Read-only.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("contract", self.contract)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("tenantStatusInformation", self.tenant_status_information)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The Azure Active Directory tenant identifier for the managed tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def tenant_status_information(self,) -> Optional[tenant_status_information.TenantStatusInformation]:
        """
        Gets the tenantStatusInformation property value. The onboarding status information for the tenant. Optional. Read-only.
        Returns: Optional[tenant_status_information.TenantStatusInformation]
        """
        return self._tenant_status_information
    
    @tenant_status_information.setter
    def tenant_status_information(self,value: Optional[tenant_status_information.TenantStatusInformation] = None) -> None:
        """
        Sets the tenantStatusInformation property value. The onboarding status information for the tenant. Optional. Read-only.
        Args:
            value: Value to set for the tenantStatusInformation property.
        """
        self._tenant_status_information = value
    

