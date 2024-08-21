from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_audience_reason import ConditionalAccessAudienceReason

@dataclass
class ConditionalAccessAudience(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The ID of the application.
    application_id: Optional[str] = None
    # Indicates the reasons this audience was included for a sign-in request.
    audience_reasons: Optional[ConditionalAccessAudienceReason] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessAudience:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessAudience
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessAudience()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_audience_reason import ConditionalAccessAudienceReason

        from .conditional_access_audience_reason import ConditionalAccessAudienceReason

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "audienceReasons": lambda n : setattr(self, 'audience_reasons', n.get_collection_of_enum_values(ConditionalAccessAudienceReason)),
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
        writer.write_str_value("applicationId", self.application_id)
        writer.write_enum_value("audienceReasons", self.audience_reasons)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

