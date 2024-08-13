from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .content_format import ContentFormat
    from .content_state import ContentState
    from .key_value_pair import KeyValuePair

@dataclass
class ContentInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The format property
    format: Optional[ContentFormat] = None
    # Identifier used for Azure Information Protection Analytics.
    identifier: Optional[str] = None
    # Existing Microsoft Purview Information Protection metadata is passed as key/value pairs, where the key is the MSIPLabelGUID_PropName.
    metadata: Optional[List[KeyValuePair]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[ContentState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .content_format import ContentFormat
        from .content_state import ContentState
        from .key_value_pair import KeyValuePair

        from .content_format import ContentFormat
        from .content_state import ContentState
        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "format": lambda n : setattr(self, 'format', n.get_enum_value(ContentFormat)),
            "identifier": lambda n : setattr(self, 'identifier', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(KeyValuePair)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ContentState)),
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
        writer.write_enum_value("format", self.format)
        writer.write_str_value("identifier", self.identifier)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

