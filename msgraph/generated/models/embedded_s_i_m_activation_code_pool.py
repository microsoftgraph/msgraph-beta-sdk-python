from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

embedded_s_i_m_activation_code = lazy_import('msgraph.generated.models.embedded_s_i_m_activation_code')
embedded_s_i_m_activation_code_pool_assignment = lazy_import('msgraph.generated.models.embedded_s_i_m_activation_code_pool_assignment')
embedded_s_i_m_device_state = lazy_import('msgraph.generated.models.embedded_s_i_m_device_state')
entity = lazy_import('msgraph.generated.models.entity')

class EmbeddedSIMActivationCodePool(entity.Entity):
    """
    A pool represents a group of embedded SIM activation codes.
    """
    @property
    def activation_code_count(self,) -> Optional[int]:
        """
        Gets the activationCodeCount property value. The total count of activation codes which belong to this pool.
        Returns: Optional[int]
        """
        return self._activation_code_count
    
    @activation_code_count.setter
    def activation_code_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activationCodeCount property value. The total count of activation codes which belong to this pool.
        Args:
            value: Value to set for the activationCodeCount property.
        """
        self._activation_code_count = value
    
    @property
    def activation_codes(self,) -> Optional[List[embedded_s_i_m_activation_code.EmbeddedSIMActivationCode]]:
        """
        Gets the activationCodes property value. The activation codes which belong to this pool. This navigation property is used to post activation codes to Intune but cannot be used to read activation codes from Intune.
        Returns: Optional[List[embedded_s_i_m_activation_code.EmbeddedSIMActivationCode]]
        """
        return self._activation_codes
    
    @activation_codes.setter
    def activation_codes(self,value: Optional[List[embedded_s_i_m_activation_code.EmbeddedSIMActivationCode]] = None) -> None:
        """
        Sets the activationCodes property value. The activation codes which belong to this pool. This navigation property is used to post activation codes to Intune but cannot be used to read activation codes from Intune.
        Args:
            value: Value to set for the activationCodes property.
        """
        self._activation_codes = value
    
    @property
    def assignments(self,) -> Optional[List[embedded_s_i_m_activation_code_pool_assignment.EmbeddedSIMActivationCodePoolAssignment]]:
        """
        Gets the assignments property value. Navigational property to a list of targets to which this pool is assigned.
        Returns: Optional[List[embedded_s_i_m_activation_code_pool_assignment.EmbeddedSIMActivationCodePoolAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[embedded_s_i_m_activation_code_pool_assignment.EmbeddedSIMActivationCodePoolAssignment]] = None) -> None:
        """
        Sets the assignments property value. Navigational property to a list of targets to which this pool is assigned.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new embeddedSIMActivationCodePool and sets the default values.
        """
        super().__init__()
        # The total count of activation codes which belong to this pool.
        self._activation_code_count: Optional[int] = None
        # The activation codes which belong to this pool. This navigation property is used to post activation codes to Intune but cannot be used to read activation codes from Intune.
        self._activation_codes: Optional[List[embedded_s_i_m_activation_code.EmbeddedSIMActivationCode]] = None
        # Navigational property to a list of targets to which this pool is assigned.
        self._assignments: Optional[List[embedded_s_i_m_activation_code_pool_assignment.EmbeddedSIMActivationCodePoolAssignment]] = None
        # The time the embedded SIM activation code pool was created. Generated service side.
        self._created_date_time: Optional[datetime] = None
        # Navigational property to a list of device states for this pool.
        self._device_states: Optional[List[embedded_s_i_m_device_state.EmbeddedSIMDeviceState]] = None
        # The admin defined name of the embedded SIM activation code pool.
        self._display_name: Optional[str] = None
        # The time the embedded SIM activation code pool was last modified. Updated service side.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time the embedded SIM activation code pool was created. Generated service side.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time the embedded SIM activation code pool was created. Generated service side.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmbeddedSIMActivationCodePool:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedSIMActivationCodePool
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmbeddedSIMActivationCodePool()
    
    @property
    def device_states(self,) -> Optional[List[embedded_s_i_m_device_state.EmbeddedSIMDeviceState]]:
        """
        Gets the deviceStates property value. Navigational property to a list of device states for this pool.
        Returns: Optional[List[embedded_s_i_m_device_state.EmbeddedSIMDeviceState]]
        """
        return self._device_states
    
    @device_states.setter
    def device_states(self,value: Optional[List[embedded_s_i_m_device_state.EmbeddedSIMDeviceState]] = None) -> None:
        """
        Sets the deviceStates property value. Navigational property to a list of device states for this pool.
        Args:
            value: Value to set for the deviceStates property.
        """
        self._device_states = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The admin defined name of the embedded SIM activation code pool.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The admin defined name of the embedded SIM activation code pool.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "activation_code_count": lambda n : setattr(self, 'activation_code_count', n.get_int_value()),
            "activation_codes": lambda n : setattr(self, 'activation_codes', n.get_collection_of_object_values(embedded_s_i_m_activation_code.EmbeddedSIMActivationCode)),
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(embedded_s_i_m_activation_code_pool_assignment.EmbeddedSIMActivationCodePoolAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_states": lambda n : setattr(self, 'device_states', n.get_collection_of_object_values(embedded_s_i_m_device_state.EmbeddedSIMDeviceState)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The time the embedded SIM activation code pool was last modified. Updated service side.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The time the embedded SIM activation code pool was last modified. Updated service side.
        Args:
            value: Value to set for the modifiedDateTime property.
        """
        self._modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("activationCodeCount", self.activation_code_count)
        writer.write_collection_of_object_values("activationCodes", self.activation_codes)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("deviceStates", self.device_states)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
    

