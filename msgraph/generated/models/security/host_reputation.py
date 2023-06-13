from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import host_reputation_classification, host_reputation_rule
    from .. import entity

from .. import entity

@dataclass
class HostReputation(entity.Entity):
    # The classification property
    classification: Optional[host_reputation_classification.HostReputationClassification] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of rules that have been used to calculate the classification and score.
    rules: Optional[List[host_reputation_rule.HostReputationRule]] = None
    # The calculated score (0-100) of the requested host. A higher value indicates that this host is more likely to be suspicious or malicious.
    score: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostReputation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HostReputation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HostReputation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import host_reputation_classification, host_reputation_rule
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "classification": lambda n : setattr(self, 'classification', n.get_enum_value(host_reputation_classification.HostReputationClassification)),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(host_reputation_rule.HostReputationRule)),
            "score": lambda n : setattr(self, 'score', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("classification", self.classification)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_int_value("score", self.score)
    

