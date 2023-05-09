from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import endpoint, user_feedback
    from .. import identity_set

from . import endpoint

class ParticipantEndpoint(endpoint.Endpoint):
    def __init__(self,) -> None:
        """
        Instantiates a new ParticipantEndpoint and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callRecords.participantEndpoint"
        # CPU number of cores used by the media endpoint.
        self._cpu_cores_count: Optional[int] = None
        # CPU name used by the media endpoint.
        self._cpu_name: Optional[str] = None
        # CPU processor speed used by the media endpoint.
        self._cpu_processor_speed_in_mhz: Optional[int] = None
        # The feedback provided by the user of this endpoint about the quality of the session.
        self._feedback: Optional[user_feedback.UserFeedback] = None
        # Identity associated with the endpoint.
        self._identity: Optional[identity_set.IdentitySet] = None
        # Name of the device used by the media endpoint.
        self._name: Optional[str] = None
    
    @property
    def cpu_cores_count(self,) -> Optional[int]:
        """
        Gets the cpuCoresCount property value. CPU number of cores used by the media endpoint.
        Returns: Optional[int]
        """
        return self._cpu_cores_count
    
    @cpu_cores_count.setter
    def cpu_cores_count(self,value: Optional[int] = None) -> None:
        """
        Sets the cpuCoresCount property value. CPU number of cores used by the media endpoint.
        Args:
            value: Value to set for the cpu_cores_count property.
        """
        self._cpu_cores_count = value
    
    @property
    def cpu_name(self,) -> Optional[str]:
        """
        Gets the cpuName property value. CPU name used by the media endpoint.
        Returns: Optional[str]
        """
        return self._cpu_name
    
    @cpu_name.setter
    def cpu_name(self,value: Optional[str] = None) -> None:
        """
        Sets the cpuName property value. CPU name used by the media endpoint.
        Args:
            value: Value to set for the cpu_name property.
        """
        self._cpu_name = value
    
    @property
    def cpu_processor_speed_in_mhz(self,) -> Optional[int]:
        """
        Gets the cpuProcessorSpeedInMhz property value. CPU processor speed used by the media endpoint.
        Returns: Optional[int]
        """
        return self._cpu_processor_speed_in_mhz
    
    @cpu_processor_speed_in_mhz.setter
    def cpu_processor_speed_in_mhz(self,value: Optional[int] = None) -> None:
        """
        Sets the cpuProcessorSpeedInMhz property value. CPU processor speed used by the media endpoint.
        Args:
            value: Value to set for the cpu_processor_speed_in_mhz property.
        """
        self._cpu_processor_speed_in_mhz = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ParticipantEndpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ParticipantEndpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ParticipantEndpoint()
    
    @property
    def feedback(self,) -> Optional[user_feedback.UserFeedback]:
        """
        Gets the feedback property value. The feedback provided by the user of this endpoint about the quality of the session.
        Returns: Optional[user_feedback.UserFeedback]
        """
        return self._feedback
    
    @feedback.setter
    def feedback(self,value: Optional[user_feedback.UserFeedback] = None) -> None:
        """
        Sets the feedback property value. The feedback provided by the user of this endpoint about the quality of the session.
        Args:
            value: Value to set for the feedback property.
        """
        self._feedback = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import endpoint, user_feedback
        from .. import identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "cpuCoresCount": lambda n : setattr(self, 'cpu_cores_count', n.get_int_value()),
            "cpuName": lambda n : setattr(self, 'cpu_name', n.get_str_value()),
            "cpuProcessorSpeedInMhz": lambda n : setattr(self, 'cpu_processor_speed_in_mhz', n.get_int_value()),
            "feedback": lambda n : setattr(self, 'feedback', n.get_object_value(user_feedback.UserFeedback)),
            "identity": lambda n : setattr(self, 'identity', n.get_object_value(identity_set.IdentitySet)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def identity(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the identity property value. Identity associated with the endpoint.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._identity
    
    @identity.setter
    def identity(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the identity property value. Identity associated with the endpoint.
        Args:
            value: Value to set for the identity property.
        """
        self._identity = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Name of the device used by the media endpoint.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Name of the device used by the media endpoint.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("cpuCoresCount", self.cpu_cores_count)
        writer.write_str_value("cpuName", self.cpu_name)
        writer.write_int_value("cpuProcessorSpeedInMhz", self.cpu_processor_speed_in_mhz)
        writer.write_object_value("feedback", self.feedback)
        writer.write_object_value("identity", self.identity)
        writer.write_str_value("name", self.name)
    

