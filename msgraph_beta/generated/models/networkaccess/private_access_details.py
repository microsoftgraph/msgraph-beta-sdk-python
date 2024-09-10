from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_type import AccessType
    from .connection_status import ConnectionStatus
    from .third_party_token_details import ThirdPartyTokenDetails

@dataclass
class PrivateAccessDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The accessType property
    access_type: Optional[AccessType] = None
    # The appSegmentId property
    app_segment_id: Optional[str] = None
    # The connectionStatus property
    connection_status: Optional[ConnectionStatus] = None
    # The connectorId property
    connector_id: Optional[str] = None
    # The connectorIp property
    connector_ip: Optional[str] = None
    # The connectorName property
    connector_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingRegion property
    processing_region: Optional[str] = None
    # The thirdPartyTokenDetails property
    third_party_token_details: Optional[ThirdPartyTokenDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivateAccessDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivateAccessDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivateAccessDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_type import AccessType
        from .connection_status import ConnectionStatus
        from .third_party_token_details import ThirdPartyTokenDetails

        from .access_type import AccessType
        from .connection_status import ConnectionStatus
        from .third_party_token_details import ThirdPartyTokenDetails

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(AccessType)),
            "appSegmentId": lambda n : setattr(self, 'app_segment_id', n.get_str_value()),
            "connectionStatus": lambda n : setattr(self, 'connection_status', n.get_enum_value(ConnectionStatus)),
            "connectorId": lambda n : setattr(self, 'connector_id', n.get_str_value()),
            "connectorIp": lambda n : setattr(self, 'connector_ip', n.get_str_value()),
            "connectorName": lambda n : setattr(self, 'connector_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "processingRegion": lambda n : setattr(self, 'processing_region', n.get_str_value()),
            "thirdPartyTokenDetails": lambda n : setattr(self, 'third_party_token_details', n.get_object_value(ThirdPartyTokenDetails)),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("appSegmentId", self.app_segment_id)
        writer.write_enum_value("connectionStatus", self.connection_status)
        writer.write_str_value("connectorId", self.connector_id)
        writer.write_str_value("connectorIp", self.connector_ip)
        writer.write_str_value("connectorName", self.connector_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("processingRegion", self.processing_region)
        writer.write_object_value("thirdPartyTokenDetails", self.third_party_token_details)
        writer.write_additional_data_value(self.additional_data)
    

