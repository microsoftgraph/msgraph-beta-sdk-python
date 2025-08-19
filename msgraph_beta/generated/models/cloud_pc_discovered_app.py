from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_cloud_app_detail import CloudPcCloudAppDetail

@dataclass
class CloudPcDiscoveredApp(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The appDetail property
    app_detail: Optional[CloudPcCloudAppDetail] = None
    # The name of the discovered app; for example, Paint. Read-only.
    app_name: Optional[str] = None
    # The unique identifier of the discovered app. Read-only.
    discovered_app_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the source of the discovered app. For example, if the source is a custom device image, the sourceId value is the ID of that image. For example, 3035e17f-c0f7-49c1-9502-5990afcaf86f. Read-only.
    source_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcDiscoveredApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcDiscoveredApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcDiscoveredApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_cloud_app_detail import CloudPcCloudAppDetail

        from .cloud_pc_cloud_app_detail import CloudPcCloudAppDetail

        fields: dict[str, Callable[[Any], None]] = {
            "appDetail": lambda n : setattr(self, 'app_detail', n.get_object_value(CloudPcCloudAppDetail)),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "discoveredAppId": lambda n : setattr(self, 'discovered_app_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
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
        writer.write_object_value("appDetail", self.app_detail)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("discoveredAppId", self.discovered_app_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_additional_data_value(self.additional_data)
    

