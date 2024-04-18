from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connectivity_configuration_link import ConnectivityConfigurationLink

@dataclass
class RemoteNetworkConnectivityConfiguration(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # List of connectivity configurations for deviceLink objects.
    links: Optional[List[ConnectivityConfigurationLink]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier or a specific reference assigned to a branchSite. Key.
    remote_network_id: Optional[str] = None
    # Display name assigned to a branchSite.
    remote_network_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteNetworkConnectivityConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemoteNetworkConnectivityConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RemoteNetworkConnectivityConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .connectivity_configuration_link import ConnectivityConfigurationLink

        from .connectivity_configuration_link import ConnectivityConfigurationLink

        fields: Dict[str, Callable[[Any], None]] = {
            "links": lambda n : setattr(self, 'links', n.get_collection_of_object_values(ConnectivityConfigurationLink)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remoteNetworkId": lambda n : setattr(self, 'remote_network_id', n.get_str_value()),
            "remoteNetworkName": lambda n : setattr(self, 'remote_network_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("links", self.links)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("remoteNetworkId", self.remote_network_id)
        writer.write_str_value("remoteNetworkName", self.remote_network_name)
        writer.write_additional_data_value(self.additional_data)
    

