from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CrossTenantSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The authTransactionCount property
    auth_transaction_count: Optional[int] = None
    # The deviceCount property
    device_count: Optional[int] = None
    # The newTenantCount property
    new_tenant_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tenantCount property
    tenant_count: Optional[int] = None
    # The userCount property
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
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
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenantCount": lambda n : setattr(self, 'tenant_count', n.get_int_value()),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("authTransactionCount", self.auth_transaction_count)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_int_value("newTenantCount", self.new_tenant_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("tenantCount", self.tenant_count)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

