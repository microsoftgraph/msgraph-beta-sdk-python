from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

dlp_evaluation_input = lazy_import('msgraph.generated.models.dlp_evaluation_input')
dlp_notification = lazy_import('msgraph.generated.models.dlp_notification')

class EvaluatePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the evaluate method.
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
        Instantiates a new evaluatePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The evaluationInput property
        self._evaluation_input: Optional[dlp_evaluation_input.DlpEvaluationInput] = None
        # The notificationInfo property
        self._notification_info: Optional[dlp_notification.DlpNotification] = None
        # The target property
        self._target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EvaluatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EvaluatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EvaluatePostRequestBody()
    
    @property
    def evaluation_input(self,) -> Optional[dlp_evaluation_input.DlpEvaluationInput]:
        """
        Gets the evaluationInput property value. The evaluationInput property
        Returns: Optional[dlp_evaluation_input.DlpEvaluationInput]
        """
        return self._evaluation_input
    
    @evaluation_input.setter
    def evaluation_input(self,value: Optional[dlp_evaluation_input.DlpEvaluationInput] = None) -> None:
        """
        Sets the evaluationInput property value. The evaluationInput property
        Args:
            value: Value to set for the evaluationInput property.
        """
        self._evaluation_input = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "evaluation_input": lambda n : setattr(self, 'evaluation_input', n.get_object_value(dlp_evaluation_input.DlpEvaluationInput)),
            "notification_info": lambda n : setattr(self, 'notification_info', n.get_object_value(dlp_notification.DlpNotification)),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
    @property
    def notification_info(self,) -> Optional[dlp_notification.DlpNotification]:
        """
        Gets the notificationInfo property value. The notificationInfo property
        Returns: Optional[dlp_notification.DlpNotification]
        """
        return self._notification_info
    
    @notification_info.setter
    def notification_info(self,value: Optional[dlp_notification.DlpNotification] = None) -> None:
        """
        Sets the notificationInfo property value. The notificationInfo property
        Args:
            value: Value to set for the notificationInfo property.
        """
        self._notification_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("evaluationInput", self.evaluation_input)
        writer.write_object_value("notificationInfo", self.notification_info)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target(self,) -> Optional[str]:
        """
        Gets the target property value. The target property
        Returns: Optional[str]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[str] = None) -> None:
        """
        Sets the target property value. The target property
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

