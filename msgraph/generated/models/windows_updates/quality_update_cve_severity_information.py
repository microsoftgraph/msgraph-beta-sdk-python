from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cve_information import CveInformation
    from .cve_severity_level import CveSeverityLevel

@dataclass
class QualityUpdateCveSeverityInformation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The exploitedCves property
    exploited_cves: Optional[List[CveInformation]] = None
    # Highest base score that occurs of any CVE addressed by the quality update. Read-only.
    max_base_score: Optional[float] = None
    # The maxSeverity property
    max_severity: Optional[CveSeverityLevel] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> QualityUpdateCveSeverityInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QualityUpdateCveSeverityInformation
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return QualityUpdateCveSeverityInformation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cve_information import CveInformation
        from .cve_severity_level import CveSeverityLevel

        from .cve_information import CveInformation
        from .cve_severity_level import CveSeverityLevel

        fields: Dict[str, Callable[[Any], None]] = {
            "exploitedCves": lambda n : setattr(self, 'exploited_cves', n.get_collection_of_object_values(CveInformation)),
            "maxBaseScore": lambda n : setattr(self, 'max_base_score', n.get_float_value()),
            "maxSeverity": lambda n : setattr(self, 'max_severity', n.get_enum_value(CveSeverityLevel)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("exploitedCves", self.exploited_cves)
        writer.write_float_value("maxBaseScore", self.max_base_score)
        writer.write_enum_value("maxSeverity", self.max_severity)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

