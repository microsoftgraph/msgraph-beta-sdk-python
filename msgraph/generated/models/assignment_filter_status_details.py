from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

assignment_filter_evaluation_summary = lazy_import('msgraph.generated.models.assignment_filter_evaluation_summary')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')

class AssignmentFilterStatusDetails(AdditionalDataHolder, Parsable):
    """
    Represent status details for device and payload and all associated applied filters.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new assignmentFilterStatusDetails and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Device properties used for filter evaluation during device check-in time.
        self._device_properties: Optional[List[key_value_pair.KeyValuePair]] = None
        # Evaluation result summaries for each filter associated to device and payload
        self._evalution_summaries: Optional[List[assignment_filter_evaluation_summary.AssignmentFilterEvaluationSummary]] = None
        # Unique identifier for the device object.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Unique identifier for payload object.
        self._payload_id: Optional[str] = None
        # Unique identifier for UserId object. Can be null
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AssignmentFilterStatusDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AssignmentFilterStatusDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AssignmentFilterStatusDetails()
    
    @property
    def device_properties(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the deviceProperties property value. Device properties used for filter evaluation during device check-in time.
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._device_properties
    
    @device_properties.setter
    def device_properties(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the deviceProperties property value. Device properties used for filter evaluation during device check-in time.
        Args:
            value: Value to set for the deviceProperties property.
        """
        self._device_properties = value
    
    @property
    def evalution_summaries(self,) -> Optional[List[assignment_filter_evaluation_summary.AssignmentFilterEvaluationSummary]]:
        """
        Gets the evalutionSummaries property value. Evaluation result summaries for each filter associated to device and payload
        Returns: Optional[List[assignment_filter_evaluation_summary.AssignmentFilterEvaluationSummary]]
        """
        return self._evalution_summaries
    
    @evalution_summaries.setter
    def evalution_summaries(self,value: Optional[List[assignment_filter_evaluation_summary.AssignmentFilterEvaluationSummary]] = None) -> None:
        """
        Sets the evalutionSummaries property value. Evaluation result summaries for each filter associated to device and payload
        Args:
            value: Value to set for the evalutionSummaries property.
        """
        self._evalution_summaries = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_properties": lambda n : setattr(self, 'device_properties', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "evalution_summaries": lambda n : setattr(self, 'evalution_summaries', n.get_collection_of_object_values(assignment_filter_evaluation_summary.AssignmentFilterEvaluationSummary)),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "payload_id": lambda n : setattr(self, 'payload_id', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        return fields
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Unique identifier for the device object.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Unique identifier for the device object.
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def payload_id(self,) -> Optional[str]:
        """
        Gets the payloadId property value. Unique identifier for payload object.
        Returns: Optional[str]
        """
        return self._payload_id
    
    @payload_id.setter
    def payload_id(self,value: Optional[str] = None) -> None:
        """
        Sets the payloadId property value. Unique identifier for payload object.
        Args:
            value: Value to set for the payloadId property.
        """
        self._payload_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("deviceProperties", self.device_properties)
        writer.write_collection_of_object_values("evalutionSummaries", self.evalution_summaries)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("payloadId", self.payload_id)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Unique identifier for UserId object. Can be null
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Unique identifier for UserId object. Can be null
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

