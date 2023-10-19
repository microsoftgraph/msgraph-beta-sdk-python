from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hunting_rule_error_code import HuntingRuleErrorCode
    from .hunting_rule_run_status import HuntingRuleRunStatus

@dataclass
class RunDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The errorCode property
    error_code: Optional[HuntingRuleErrorCode] = None
    # The failureReason property
    failure_reason: Optional[str] = None
    # The lastRunDateTime property
    last_run_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[HuntingRuleRunStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RunDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RunDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RunDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .hunting_rule_error_code import HuntingRuleErrorCode
        from .hunting_rule_run_status import HuntingRuleRunStatus

        from .hunting_rule_error_code import HuntingRuleErrorCode
        from .hunting_rule_run_status import HuntingRuleRunStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "errorCode": lambda n : setattr(self, 'error_code', n.get_enum_value(HuntingRuleErrorCode)),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "lastRunDateTime": lambda n : setattr(self, 'last_run_date_time', n.get_datetime_value()),
            "OdataType": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(HuntingRuleRunStatus)),
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
        writer.write_enum_value("errorCode", self.error_code)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_datetime_value("lastRunDateTime", self.last_run_date_time)
        writer.write_str_value("OdataType", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

