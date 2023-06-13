from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import risk_detail, risk_event_type

@dataclass
class RiskUserActivity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The possible values are none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue.
    detail: Optional[risk_detail.RiskDetail] = None
    # The eventTypes property
    event_types: Optional[List[risk_event_type.RiskEventType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskEventTypes property
    risk_event_types: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskUserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RiskUserActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RiskUserActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import risk_detail, risk_event_type

        fields: Dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(risk_detail.RiskDetail)),
            "eventTypes": lambda n : setattr(self, 'event_types', n.get_collection_of_enum_values(risk_event_type.RiskEventType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskEventTypes": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("detail", self.detail)
        writer.write_enum_value("eventTypes", self.event_types)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("riskEventTypes", self.risk_event_types)
        writer.write_additional_data_value(self.additional_data)
    

