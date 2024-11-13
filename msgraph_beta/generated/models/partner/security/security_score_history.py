from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity

from ...entity import Entity

@dataclass
class SecurityScoreHistory(Entity, Parsable):
    # The number of compliant security requirements at the time.
    compliant_requirements_count: Optional[int] = None
    # The date the history entry was created.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The score recorded at the time.
    score: Optional[float] = None
    # The total number of requirements at the time.
    total_requirements_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityScoreHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityScoreHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityScoreHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity

        from ...entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "compliantRequirementsCount": lambda n : setattr(self, 'compliant_requirements_count', n.get_int_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "score": lambda n : setattr(self, 'score', n.get_float_value()),
            "totalRequirementsCount": lambda n : setattr(self, 'total_requirements_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from ...entity import Entity

        writer.write_int_value("compliantRequirementsCount", self.compliant_requirements_count)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_float_value("score", self.score)
        writer.write_int_value("totalRequirementsCount", self.total_requirements_count)
    

