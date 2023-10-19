from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .risk_detail import RiskDetail
    from .risk_event_type import RiskEventType

@dataclass
class RiskUserActivity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The possible values are none, adminGeneratedTemporaryPassword, userPerformedSecuredPasswordChange, userPerformedSecuredPasswordReset, adminConfirmedSigninSafe, aiConfirmedSigninSafe, userPassedMFADrivenByRiskBasedPolicy, adminDismissedAllRiskForUser, adminConfirmedSigninCompromised, hidden, adminConfirmedUserCompromised, unknownFutureValue.
    detail: Optional[RiskDetail] = None
    # The eventTypes property
    event_types: Optional[List[RiskEventType]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The riskEventTypes property
    risk_event_types: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RiskUserActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RiskUserActivity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RiskUserActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .risk_detail import RiskDetail
        from .risk_event_type import RiskEventType

        from .risk_detail import RiskDetail
        from .risk_event_type import RiskEventType

        fields: Dict[str, Callable[[Any], None]] = {
            "detail": lambda n : setattr(self, 'detail', n.get_enum_value(RiskDetail)),
            "eventTypes": lambda n : setattr(self, 'event_types', n.get_collection_of_enum_values(RiskEventType)),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskEventTypes": lambda n : setattr(self, 'risk_event_types', n.get_collection_of_primitive_values(str)),
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
        writer.write_enum_value("detail", self.detail)
        writer.write_collection_of_enum_values("eventTypes", self.event_types)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_collection_of_primitive_values("riskEventTypes", self.risk_event_types)
        writer.write_additional_data_value(self.additional_data)
    

