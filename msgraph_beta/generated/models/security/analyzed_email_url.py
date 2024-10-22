from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .detonation_details import DetonationDetails
    from .threat_type import ThreatType

@dataclass
class AnalyzedEmailUrl(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The method used to detect threats in the URL.
    detection_method: Optional[str] = None
    # Detonation data associated with the URL.
    detonation_details: Optional[DetonationDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of threat associated with the URL. The possible values are: unknown, spam, malware, phishing, none, unknownFutureValue.
    threat_type: Optional[ThreatType] = None
    # The URL that is found in the email. This is full URL string, including query parameters.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AnalyzedEmailUrl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AnalyzedEmailUrl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AnalyzedEmailUrl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .detonation_details import DetonationDetails
        from .threat_type import ThreatType

        from .detonation_details import DetonationDetails
        from .threat_type import ThreatType

        fields: Dict[str, Callable[[Any], None]] = {
            "detectionMethod": lambda n : setattr(self, 'detection_method', n.get_str_value()),
            "detonationDetails": lambda n : setattr(self, 'detonation_details', n.get_object_value(DetonationDetails)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "threatType": lambda n : setattr(self, 'threat_type', n.get_enum_value(ThreatType)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        from .detonation_details import DetonationDetails
        from .threat_type import ThreatType

        writer.write_str_value("detectionMethod", self.detection_method)
        writer.write_object_value("detonationDetails", self.detonation_details)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("threatType", self.threat_type)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

