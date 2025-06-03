from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .compromise_indicator import CompromiseIndicator
    from .detonation_behaviour_details import DetonationBehaviourDetails
    from .detonation_chain import DetonationChain
    from .detonation_observables import DetonationObservables

@dataclass
class DetonationDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The time of detonation.
    analysis_date_time: Optional[datetime.datetime] = None
    # Represents indicators and its associated verdict that suggests whether an email is compromised.
    compromise_indicators: Optional[list[CompromiseIndicator]] = None
    # Shows the exact events that took place during detonation, and problematic or benign observations that contain URLs, IPs, domains, and files that were found during detonation
    detonation_behaviour_details: Optional[DetonationBehaviourDetails] = None
    # The chain of detonation.
    detonation_chain: Optional[DetonationChain] = None
    # All observables in the detonation tree.
    detonation_observables: Optional[DetonationObservables] = None
    # Show any screenshots that were captured during detonation. No screenshots are captured if the URL opens into a link that directly downloads a file. However, you see the downloaded file in the detonation chain.
    detonation_screenshot_uri: Optional[str] = None
    # The verdict of the detonation.
    detonation_verdict: Optional[str] = None
    # The reason for the verdict of the detonation.
    detonation_verdict_reason: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetonationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetonationDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetonationDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .compromise_indicator import CompromiseIndicator
        from .detonation_behaviour_details import DetonationBehaviourDetails
        from .detonation_chain import DetonationChain
        from .detonation_observables import DetonationObservables

        from .compromise_indicator import CompromiseIndicator
        from .detonation_behaviour_details import DetonationBehaviourDetails
        from .detonation_chain import DetonationChain
        from .detonation_observables import DetonationObservables

        fields: dict[str, Callable[[Any], None]] = {
            "analysisDateTime": lambda n : setattr(self, 'analysis_date_time', n.get_datetime_value()),
            "compromiseIndicators": lambda n : setattr(self, 'compromise_indicators', n.get_collection_of_object_values(CompromiseIndicator)),
            "detonationBehaviourDetails": lambda n : setattr(self, 'detonation_behaviour_details', n.get_object_value(DetonationBehaviourDetails)),
            "detonationChain": lambda n : setattr(self, 'detonation_chain', n.get_object_value(DetonationChain)),
            "detonationObservables": lambda n : setattr(self, 'detonation_observables', n.get_object_value(DetonationObservables)),
            "detonationScreenshotUri": lambda n : setattr(self, 'detonation_screenshot_uri', n.get_str_value()),
            "detonationVerdict": lambda n : setattr(self, 'detonation_verdict', n.get_str_value()),
            "detonationVerdictReason": lambda n : setattr(self, 'detonation_verdict_reason', n.get_str_value()),
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
        writer.write_datetime_value("analysisDateTime", self.analysis_date_time)
        writer.write_collection_of_object_values("compromiseIndicators", self.compromise_indicators)
        writer.write_object_value("detonationBehaviourDetails", self.detonation_behaviour_details)
        writer.write_object_value("detonationChain", self.detonation_chain)
        writer.write_object_value("detonationObservables", self.detonation_observables)
        writer.write_str_value("detonationScreenshotUri", self.detonation_screenshot_uri)
        writer.write_str_value("detonationVerdict", self.detonation_verdict)
        writer.write_str_value("detonationVerdictReason", self.detonation_verdict_reason)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

