from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

embedded_s_i_m_device_state_value = lazy_import('msgraph.generated.models.embedded_s_i_m_device_state_value')
entity = lazy_import('msgraph.generated.models.entity')

class EmbeddedSIMDeviceState(entity.Entity):
    """
    Describes the embedded SIM activation code deployment state in relation to a device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new embeddedSIMDeviceState and sets the default values.
        """
        super().__init__()
        # The time the embedded SIM device status was created. Generated service side.
        self._created_date_time: Optional[datetime] = None
        # Device name to which the subscription was provisioned e.g. DESKTOP-JOE
        self._device_name: Optional[str] = None
        # The time the embedded SIM device last checked in. Updated service side.
        self._last_sync_date_time: Optional[datetime] = None
        # The time the embedded SIM device status was last modified. Updated service side.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Describes the various states for an embedded SIM activation code.
        self._state: Optional[embedded_s_i_m_device_state_value.EmbeddedSIMDeviceStateValue] = None
        # String description of the provisioning state.
        self._state_details: Optional[str] = None
        # The Universal Integrated Circuit Card Identifier (UICCID) identifying the hardware onto which a profile is to be deployed.
        self._universal_integrated_circuit_card_identifier: Optional[str] = None
        # Username which the subscription was provisioned to e.g. joe@contoso.com
        self._user_name: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The time the embedded SIM device status was created. Generated service side.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The time the embedded SIM device status was created. Generated service side.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmbeddedSIMDeviceState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedSIMDeviceState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EmbeddedSIMDeviceState()
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Device name to which the subscription was provisioned e.g. DESKTOP-JOE
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Device name to which the subscription was provisioned e.g. DESKTOP-JOE
        Args:
            value: Value to set for the deviceName property.
        """
        self._device_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "last_sync_date_time": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(embedded_s_i_m_device_state_value.EmbeddedSIMDeviceStateValue)),
            "state_details": lambda n : setattr(self, 'state_details', n.get_str_value()),
            "universal_integrated_circuit_card_identifier": lambda n : setattr(self, 'universal_integrated_circuit_card_identifier', n.get_str_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. The time the embedded SIM device last checked in. Updated service side.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. The time the embedded SIM device last checked in. Updated service side.
        Args:
            value: Value to set for the lastSyncDateTime property.
        """
        self._last_sync_date_time = value
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The time the embedded SIM device status was last modified. Updated service side.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The time the embedded SIM device status was last modified. Updated service side.
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_datetime_value("lastSyncDateTime", self.last_sync_date_time)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("stateDetails", self.state_details)
        writer.write_str_value("universalIntegratedCircuitCardIdentifier", self.universal_integrated_circuit_card_identifier)
        writer.write_str_value("userName", self.user_name)
    
    @property
    def state(self,) -> Optional[embedded_s_i_m_device_state_value.EmbeddedSIMDeviceStateValue]:
        """
        Gets the state property value. Describes the various states for an embedded SIM activation code.
        Returns: Optional[embedded_s_i_m_device_state_value.EmbeddedSIMDeviceStateValue]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[embedded_s_i_m_device_state_value.EmbeddedSIMDeviceStateValue] = None) -> None:
        """
        Sets the state property value. Describes the various states for an embedded SIM activation code.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def state_details(self,) -> Optional[str]:
        """
        Gets the stateDetails property value. String description of the provisioning state.
        Returns: Optional[str]
        """
        return self._state_details
    
    @state_details.setter
    def state_details(self,value: Optional[str] = None) -> None:
        """
        Sets the stateDetails property value. String description of the provisioning state.
        Args:
            value: Value to set for the stateDetails property.
        """
        self._state_details = value
    
    @property
    def universal_integrated_circuit_card_identifier(self,) -> Optional[str]:
        """
        Gets the universalIntegratedCircuitCardIdentifier property value. The Universal Integrated Circuit Card Identifier (UICCID) identifying the hardware onto which a profile is to be deployed.
        Returns: Optional[str]
        """
        return self._universal_integrated_circuit_card_identifier
    
    @universal_integrated_circuit_card_identifier.setter
    def universal_integrated_circuit_card_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the universalIntegratedCircuitCardIdentifier property value. The Universal Integrated Circuit Card Identifier (UICCID) identifying the hardware onto which a profile is to be deployed.
        Args:
            value: Value to set for the universalIntegratedCircuitCardIdentifier property.
        """
        self._universal_integrated_circuit_card_identifier = value
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. Username which the subscription was provisioned to e.g. joe@contoso.com
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. Username which the subscription was provisioned to e.g. joe@contoso.com
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

