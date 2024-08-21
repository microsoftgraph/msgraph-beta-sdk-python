from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aggregation_type import AggregationType
    from .condition_category import ConditionCategory
    from .operator_type import OperatorType
    from .relationship_type import RelationshipType

@dataclass
class RuleCondition(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The built-in aggregation method for the rule condition. The possible values are: count, percentage, affectedCloudPcCount, affectedCloudPcPercentage, unknownFutureValue.
    aggregation: Optional[AggregationType] = None
    # The property that the rule condition monitors. Possible values are:  provisionFailures, imageUploadFailures, azureNetworkConnectionCheckFailures, cloudPcInGracePeriod, frontlineInsufficientLicenses, cloudPcConnectionErrors, cloudPcHostHealthCheckFailures, cloudPcZoneOutage, unknownFutureValue.
    condition_category: Optional[ConditionCategory] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The built-in operator for the rule condition. The possible values are: greaterOrEqual, equal, greater, less, lessOrEqual, notEqual, unknownFutureValue.
    operator: Optional[OperatorType] = None
    # The relationship type.  Possible values are: and, or.
    relationship_type: Optional[RelationshipType] = None
    # The threshold value of the alert condition. The threshold value can be a number in string form or string like 'WestUS'.
    threshold_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RuleCondition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RuleCondition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RuleCondition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aggregation_type import AggregationType
        from .condition_category import ConditionCategory
        from .operator_type import OperatorType
        from .relationship_type import RelationshipType

        from .aggregation_type import AggregationType
        from .condition_category import ConditionCategory
        from .operator_type import OperatorType
        from .relationship_type import RelationshipType

        fields: Dict[str, Callable[[Any], None]] = {
            "aggregation": lambda n : setattr(self, 'aggregation', n.get_enum_value(AggregationType)),
            "conditionCategory": lambda n : setattr(self, 'condition_category', n.get_enum_value(ConditionCategory)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_enum_value(OperatorType)),
            "relationshipType": lambda n : setattr(self, 'relationship_type', n.get_enum_value(RelationshipType)),
            "thresholdValue": lambda n : setattr(self, 'threshold_value', n.get_str_value()),
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
        writer.write_enum_value("aggregation", self.aggregation)
        writer.write_enum_value("conditionCategory", self.condition_category)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operator", self.operator)
        writer.write_enum_value("relationshipType", self.relationship_type)
        writer.write_str_value("thresholdValue", self.threshold_value)
        writer.write_additional_data_value(self.additional_data)
    

