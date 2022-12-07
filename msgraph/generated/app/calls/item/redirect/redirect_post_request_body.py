from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

call_disposition = lazy_import('msgraph.generated.models.call_disposition')
invitation_participant_info = lazy_import('msgraph.generated.models.invitation_participant_info')

class RedirectPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the redirect method.
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
    
    @property
    def callback_uri(self,) -> Optional[str]:
        """
        Gets the callbackUri property value. The callbackUri property
        Returns: Optional[str]
        """
        return self._callback_uri
    
    @callback_uri.setter
    def callback_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the callbackUri property value. The callbackUri property
        Args:
            value: Value to set for the callbackUri property.
        """
        self._callback_uri = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new redirectPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The callbackUri property
        self._callback_uri: Optional[str] = None
        # The maskCallee property
        self._mask_callee: Optional[bool] = None
        # The maskCaller property
        self._mask_caller: Optional[bool] = None
        # The targetDisposition property
        self._target_disposition: Optional[call_disposition.CallDisposition] = None
        # The targets property
        self._targets: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None
        # The timeout property
        self._timeout: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RedirectPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RedirectPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RedirectPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "callback_uri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "mask_callee": lambda n : setattr(self, 'mask_callee', n.get_bool_value()),
            "mask_caller": lambda n : setattr(self, 'mask_caller', n.get_bool_value()),
            "target_disposition": lambda n : setattr(self, 'target_disposition', n.get_enum_value(call_disposition.CallDisposition)),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(invitation_participant_info.InvitationParticipantInfo)),
            "timeout": lambda n : setattr(self, 'timeout', n.get_int_value()),
        }
        return fields
    
    @property
    def mask_callee(self,) -> Optional[bool]:
        """
        Gets the maskCallee property value. The maskCallee property
        Returns: Optional[bool]
        """
        return self._mask_callee
    
    @mask_callee.setter
    def mask_callee(self,value: Optional[bool] = None) -> None:
        """
        Sets the maskCallee property value. The maskCallee property
        Args:
            value: Value to set for the maskCallee property.
        """
        self._mask_callee = value
    
    @property
    def mask_caller(self,) -> Optional[bool]:
        """
        Gets the maskCaller property value. The maskCaller property
        Returns: Optional[bool]
        """
        return self._mask_caller
    
    @mask_caller.setter
    def mask_caller(self,value: Optional[bool] = None) -> None:
        """
        Sets the maskCaller property value. The maskCaller property
        Args:
            value: Value to set for the maskCaller property.
        """
        self._mask_caller = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_bool_value("maskCallee", self.mask_callee)
        writer.write_bool_value("maskCaller", self.mask_caller)
        writer.write_enum_value("targetDisposition", self.target_disposition)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_int_value("timeout", self.timeout)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target_disposition(self,) -> Optional[call_disposition.CallDisposition]:
        """
        Gets the targetDisposition property value. The targetDisposition property
        Returns: Optional[call_disposition.CallDisposition]
        """
        return self._target_disposition
    
    @target_disposition.setter
    def target_disposition(self,value: Optional[call_disposition.CallDisposition] = None) -> None:
        """
        Sets the targetDisposition property value. The targetDisposition property
        Args:
            value: Value to set for the targetDisposition property.
        """
        self._target_disposition = value
    
    @property
    def targets(self,) -> Optional[List[invitation_participant_info.InvitationParticipantInfo]]:
        """
        Gets the targets property value. The targets property
        Returns: Optional[List[invitation_participant_info.InvitationParticipantInfo]]
        """
        return self._targets
    
    @targets.setter
    def targets(self,value: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None) -> None:
        """
        Sets the targets property value. The targets property
        Args:
            value: Value to set for the targets property.
        """
        self._targets = value
    
    @property
    def timeout(self,) -> Optional[int]:
        """
        Gets the timeout property value. The timeout property
        Returns: Optional[int]
        """
        return self._timeout
    
    @timeout.setter
    def timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the timeout property value. The timeout property
        Args:
            value: Value to set for the timeout property.
        """
        self._timeout = value
    

