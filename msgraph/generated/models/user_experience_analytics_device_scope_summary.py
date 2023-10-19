from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UserExperienceAnalyticsDeviceScopeSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    The user experience analytics tenant level information for all the device scope configurations
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # A collection of the user experience analytics device scope Unique Identifiers that are enabled and finished recalculating the report metric.
    completed_device_scope_ids: Optional[List[str]] = None
    # A collection of user experience analytics device scope Unique Identitfiers that are enabled but there is insufficient data to calculate results.
    insufficient_data_device_scope_ids: Optional[List[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of user experience analytics device scopes. Valid values -2147483648 to 2147483647
    total_device_scopes: Optional[int] = None
    # The total number of user experience analytics device scopes that are enabled. Valid values -2147483648 to 2147483647
    total_device_scopes_enabled: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDeviceScopeSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceScopeSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceScopeSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "completedDeviceScopeIds": lambda n : setattr(self, 'completed_device_scope_ids', n.get_collection_of_primitive_values(str)),
            "insufficientDataDeviceScopeIds": lambda n : setattr(self, 'insufficient_data_device_scope_ids', n.get_collection_of_primitive_values(str)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "totalDeviceScopes": lambda n : setattr(self, 'total_device_scopes', n.get_int_value()),
            "totalDeviceScopesEnabled": lambda n : setattr(self, 'total_device_scopes_enabled', n.get_int_value()),
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
        writer.write_collection_of_primitive_values("completedDeviceScopeIds", self.completed_device_scope_ids)
        writer.write_collection_of_primitive_values("insufficientDataDeviceScopeIds", self.insufficient_data_device_scope_ids)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_int_value("totalDeviceScopes", self.total_device_scopes)
        writer.write_int_value("totalDeviceScopesEnabled", self.total_device_scopes_enabled)
        writer.write_additional_data_value(self.additional_data)
    

