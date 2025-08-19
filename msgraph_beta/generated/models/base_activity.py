from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity_status import ActivityStatus
    from .activity_transport import ActivityTransport
    from .result_info import ResultInfo
    from .transcript_activity import TranscriptActivity

@dataclass
class BaseActivity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # The resultInfo property
    result_info: Optional[ResultInfo] = None
    # The status property
    status: Optional[ActivityStatus] = None
    # The transport property
    transport: Optional[ActivityTransport] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BaseActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.transcriptActivity".casefold():
            from .transcript_activity import TranscriptActivity

            return TranscriptActivity()
        return BaseActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .activity_status import ActivityStatus
        from .activity_transport import ActivityTransport
        from .result_info import ResultInfo
        from .transcript_activity import TranscriptActivity

        from .activity_status import ActivityStatus
        from .activity_transport import ActivityTransport
        from .result_info import ResultInfo
        from .transcript_activity import TranscriptActivity

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(ResultInfo)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ActivityStatus)),
            "transport": lambda n : setattr(self, 'transport', n.get_object_value(ActivityTransport)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("transport", self.transport)
        writer.write_additional_data_value(self.additional_data)
    

