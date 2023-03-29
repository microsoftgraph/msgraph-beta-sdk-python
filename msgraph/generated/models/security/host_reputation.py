from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import host_reputation_classification, host_reputation_rule
    from .. import entity

from .. import entity

class HostReputation(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new hostReputation and sets the default values.
        """
        super().__init__()
        # The classification property
        self._classification: Optional[host_reputation_classification.HostReputationClassification] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of rules that have been used to calculate the classification and score.
        self._rules: Optional[List[host_reputation_rule.HostReputationRule]] = None
        # The calculated score (0-100) of the requested host. A higher value indicates that this host is more likely to be suspicious or malicious.
        self._score: Optional[int] = None
    
    @property
    def classification(self,) -> Optional[host_reputation_classification.HostReputationClassification]:
        """
        Gets the classification property value. The classification property
        Returns: Optional[host_reputation_classification.HostReputationClassification]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[host_reputation_classification.HostReputationClassification] = None) -> None:
        """
        Sets the classification property value. The classification property
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
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
    
    @property
    def rules(self,) -> Optional[List[host_reputation_rule.HostReputationRule]]:
        """
        Gets the rules property value. A collection of rules that have been used to calculate the classification and score.
        Returns: Optional[List[host_reputation_rule.HostReputationRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[host_reputation_rule.HostReputationRule]] = None) -> None:
        """
        Sets the rules property value. A collection of rules that have been used to calculate the classification and score.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    @property
    def score(self,) -> Optional[int]:
        """
        Gets the score property value. The calculated score (0-100) of the requested host. A higher value indicates that this host is more likely to be suspicious or malicious.
        Returns: Optional[int]
        """
        return self._score
    
    @score.setter
    def score(self,value: Optional[int] = None) -> None:
        """
        Sets the score property value. The calculated score (0-100) of the requested host. A higher value indicates that this host is more likely to be suspicious or malicious.
        Args:
            value: Value to set for the score property.
        """
        self._score = value
    
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
    

