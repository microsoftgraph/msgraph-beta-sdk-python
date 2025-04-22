from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CloudPcSupportedRegionRestrictionDetail(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Indicates that the region is restricted for Cloud PC CPU provisioning. True indicates that Cloud PC provisioning with CPU isn't available in this region. false indicates that it's available. The default value is false. Read-only.
    c_p_u_restricted: Optional[bool] = None
    # Indicates that the region is restricted for Cloud PC GPU provisioning. True indicates that Cloud PC provisioning with GPU isn't available in this region. false indicates that it's available. The default value is false. Read-only.
    g_p_u_restricted: Optional[bool] = None
    # Indicates that the region is restricted for Cloud PC nested virtualization provisioning. True indicates that Cloud PC provisioning with nested virtualization isn't available in this region; false indicates that it's available. The default value is false. Read-only.
    nested_virtualization_restricted: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcSupportedRegionRestrictionDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcSupportedRegionRestrictionDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcSupportedRegionRestrictionDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cPURestricted": lambda n : setattr(self, 'c_p_u_restricted', n.get_bool_value()),
            "gPURestricted": lambda n : setattr(self, 'g_p_u_restricted', n.get_bool_value()),
            "nestedVirtualizationRestricted": lambda n : setattr(self, 'nested_virtualization_restricted', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("cPURestricted", self.c_p_u_restricted)
        writer.write_bool_value("gPURestricted", self.g_p_u_restricted)
        writer.write_bool_value("nestedVirtualizationRestricted", self.nested_virtualization_restricted)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

