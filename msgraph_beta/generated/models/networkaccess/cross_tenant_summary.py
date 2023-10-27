from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CrossTenantSummary(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Total numbers of authentication sessions in the time frame between startDateTime and endDateTime.
    auth_transaction_count: Optional[int] = None
    # Count of unique devices that performed cross-tenant access, in the time frame between startDateTime and endDateTime.
    device_count: Optional[int] = None
    # Count of unique tenants that were accessed in the time frame between endDateTime to discoveryPivotDateTime, but haven't been accessed in the time frame between discoveryPivotDateTime to startDateTime.
    new_tenant_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The rarelyUsedTenantCount property
    rarely_used_tenant_count: Optional[int] = None
    # Count of unique tenants that were accessed, that are different from the device's home tenant, in the time frame between startDateTime and endDateTime.
    tenant_count: Optional[int] = None
    # Count of unique users that performed cross-tenant access, in the time frame between startDateTime and endDateTime.
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "authTransactionCount": lambda n : setattr(self, 'auth_transaction_count', n.get_int_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "newTenantCount": lambda n : setattr(self, 'new_tenant_count', n.get_int_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rarelyUsedTenantCount": lambda n : setattr(self, 'rarely_used_tenant_count', n.get_int_value()),
            "tenantCount": lambda n : setattr(self, 'tenant_count', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
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
        writer.write_int_value("authTransactionCount", self.auth_transaction_count)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_int_value("newTenantCount", self.new_tenant_count)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("rarelyUsedTenantCount", self.rarely_used_tenant_count)
        writer.write_int_value("tenantCount", self.tenant_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

