from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.exchange_online_cross_tenant_migration_settings import ExchangeOnlineCrossTenantMigrationSettings

@dataclass
class ValidatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The completeAfterDateTime property
    complete_after_date_time: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The exchangeSettings property
    exchange_settings: Optional[ExchangeOnlineCrossTenantMigrationSettings] = None
    # The resourceType property
    resource_type: Optional[str] = None
    # The resources property
    resources: Optional[list[str]] = None
    # The sourceTenantId property
    source_tenant_id: Optional[str] = None
    # The workloads property
    workloads: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ValidatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ValidatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ValidatePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.exchange_online_cross_tenant_migration_settings import ExchangeOnlineCrossTenantMigrationSettings

        from .....models.exchange_online_cross_tenant_migration_settings import ExchangeOnlineCrossTenantMigrationSettings

        fields: dict[str, Callable[[Any], None]] = {
            "completeAfterDateTime": lambda n : setattr(self, 'complete_after_date_time', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exchangeSettings": lambda n : setattr(self, 'exchange_settings', n.get_object_value(ExchangeOnlineCrossTenantMigrationSettings)),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_primitive_values(str)),
            "sourceTenantId": lambda n : setattr(self, 'source_tenant_id', n.get_str_value()),
            "workloads": lambda n : setattr(self, 'workloads', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("completeAfterDateTime", self.complete_after_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("exchangeSettings", self.exchange_settings)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_collection_of_primitive_values("resources", self.resources)
        writer.write_str_value("sourceTenantId", self.source_tenant_id)
        writer.write_collection_of_primitive_values("workloads", self.workloads)
        writer.write_additional_data_value(self.additional_data)
    

