from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .assignment_filter_evaluation_summary import AssignmentFilterEvaluationSummary
    from .key_value_pair import KeyValuePair

@dataclass
class AssignmentFilterStatusDetails(AdditionalDataHolder, BackedModel, Parsable):
    """
    Represent status details for device and payload and all associated applied filters.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Device properties used for filter evaluation during device check-in time.
    device_properties: Optional[List[KeyValuePair]] = None
    # Evaluation result summaries for each filter associated to device and payload
    evalution_summaries: Optional[List[AssignmentFilterEvaluationSummary]] = None
    # Unique identifier for the device object.
    managed_device_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Unique identifier for payload object.
    payload_id: Optional[str] = None
    # Unique identifier for UserId object. Can be null
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AssignmentFilterStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterStatusDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AssignmentFilterStatusDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .assignment_filter_evaluation_summary import AssignmentFilterEvaluationSummary
        from .key_value_pair import KeyValuePair

        from .assignment_filter_evaluation_summary import AssignmentFilterEvaluationSummary
        from .key_value_pair import KeyValuePair

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceProperties": lambda n : setattr(self, 'device_properties', n.get_collection_of_object_values(KeyValuePair)),
            "evalutionSummaries": lambda n : setattr(self, 'evalution_summaries', n.get_collection_of_object_values(AssignmentFilterEvaluationSummary)),
            "managedDeviceId": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payloadId": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("deviceProperties", self.device_properties)
        writer.write_collection_of_object_values("evalutionSummaries", self.evalution_summaries)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

