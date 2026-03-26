from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_activity import ApplicationActivity

@dataclass
class GenerativeAIInsight(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The activity property
    activity: Optional[ApplicationActivity] = None
    # The content property
    content: Optional[str] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The destinationUrl property
    destination_url: Optional[str] = None
    # The eventId property
    event_id: Optional[str] = None
    # The eventType property
    event_type: Optional[str] = None
    # The mcpClientName property
    mcp_client_name: Optional[str] = None
    # The mcpServerName property
    mcp_server_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sessionId property
    session_id: Optional[str] = None
    # The subactivity property
    subactivity: Optional[str] = None
    # The transactionId property
    transaction_id: Optional[str] = None
    # The userPrincipalName property
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GenerativeAIInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GenerativeAIInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GenerativeAIInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_activity import ApplicationActivity

        from .application_activity import ApplicationActivity

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_enum_value(ApplicationActivity)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "destinationUrl": lambda n : setattr(self, 'destination_url', n.get_str_value()),
            "eventId": lambda n : setattr(self, 'event_id', n.get_str_value()),
            "eventType": lambda n : setattr(self, 'event_type', n.get_str_value()),
            "mcpClientName": lambda n : setattr(self, 'mcp_client_name', n.get_str_value()),
            "mcpServerName": lambda n : setattr(self, 'mcp_server_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sessionId": lambda n : setattr(self, 'session_id', n.get_str_value()),
            "subactivity": lambda n : setattr(self, 'subactivity', n.get_str_value()),
            "transactionId": lambda n : setattr(self, 'transaction_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("activity", self.activity)
        writer.write_str_value("content", self.content)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("destinationUrl", self.destination_url)
        writer.write_str_value("eventId", self.event_id)
        writer.write_str_value("eventType", self.event_type)
        writer.write_str_value("mcpClientName", self.mcp_client_name)
        writer.write_str_value("mcpServerName", self.mcp_server_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sessionId", self.session_id)
        writer.write_str_value("subactivity", self.subactivity)
        writer.write_str_value("transactionId", self.transaction_id)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    

