from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .usage_status import UsageStatus

@dataclass
class CrossTenantAccess(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The number of devices that accessed the external tenant.
    device_count: Optional[int] = None
    # The timestamp of the most recent access to the external tenant.
    last_access_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tenant ID of the external tenant.
    resource_tenant_id: Optional[str] = None
    # The name of the external tenant.
    resource_tenant_name: Optional[str] = None
    # The domain of the external tenant.
    resource_tenant_primary_domain: Optional[str] = None
    # The usageStatus property
    usage_status: Optional[UsageStatus] = None
    # The number of users that accessed the external tenant.
    user_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantAccess:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccess
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccess()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .usage_status import UsageStatus

        from .usage_status import UsageStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "lastAccessDateTime": lambda n : setattr(self, 'last_access_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceTenantId": lambda n : setattr(self, 'resource_tenant_id', n.get_str_value()),
            "resourceTenantName": lambda n : setattr(self, 'resource_tenant_name', n.get_str_value()),
            "resourceTenantPrimaryDomain": lambda n : setattr(self, 'resource_tenant_primary_domain', n.get_str_value()),
            "usageStatus": lambda n : setattr(self, 'usage_status', n.get_enum_value(UsageStatus)),
            "userCount": lambda n : setattr(self, 'user_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_datetime_value("lastAccessDateTime", self.last_access_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceTenantId", self.resource_tenant_id)
        writer.write_str_value("resourceTenantName", self.resource_tenant_name)
        writer.write_str_value("resourceTenantPrimaryDomain", self.resource_tenant_primary_domain)
        writer.write_enum_value("usageStatus", self.usage_status)
        writer.write_int_value("userCount", self.user_count)
        writer.write_additional_data_value(self.additional_data)
    

