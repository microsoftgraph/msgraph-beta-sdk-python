from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, mobile_app_intent_and_state_detail

from . import entity

class MobileAppIntentAndState(entity.Entity):
    """
    MobileApp Intent and Install State for a given device.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppIntentAndState and sets the default values.
        """
        super().__init__()
        # Device identifier created or collected by Intune.
        self._managed_device_identifier: Optional[str] = None
        # The list of payload intents and states for the tenant.
        self._mobile_app_list: Optional[List[mobile_app_intent_and_state_detail.MobileAppIntentAndStateDetail]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Identifier for the user that tried to enroll the device.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppIntentAndState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppIntentAndState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppIntentAndState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, mobile_app_intent_and_state_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "managedDeviceIdentifier": lambda n : setattr(self, 'managed_device_identifier', n.get_str_value()),
            "mobileAppList": lambda n : setattr(self, 'mobile_app_list', n.get_collection_of_object_values(mobile_app_intent_and_state_detail.MobileAppIntentAndStateDetail)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_device_identifier(self,) -> Optional[str]:
        """
        Gets the managedDeviceIdentifier property value. Device identifier created or collected by Intune.
        Returns: Optional[str]
        """
        return self._managed_device_identifier
    
    @managed_device_identifier.setter
    def managed_device_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceIdentifier property value. Device identifier created or collected by Intune.
        Args:
            value: Value to set for the managed_device_identifier property.
        """
        self._managed_device_identifier = value
    
    @property
    def mobile_app_list(self,) -> Optional[List[mobile_app_intent_and_state_detail.MobileAppIntentAndStateDetail]]:
        """
        Gets the mobileAppList property value. The list of payload intents and states for the tenant.
        Returns: Optional[List[mobile_app_intent_and_state_detail.MobileAppIntentAndStateDetail]]
        """
        return self._mobile_app_list
    
    @mobile_app_list.setter
    def mobile_app_list(self,value: Optional[List[mobile_app_intent_and_state_detail.MobileAppIntentAndStateDetail]] = None) -> None:
        """
        Sets the mobileAppList property value. The list of payload intents and states for the tenant.
        Args:
            value: Value to set for the mobile_app_list property.
        """
        self._mobile_app_list = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("managedDeviceIdentifier", self.managed_device_identifier)
        writer.write_collection_of_object_values("mobileAppList", self.mobile_app_list)
        writer.write_str_value("userId", self.user_id)
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Identifier for the user that tried to enroll the device.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Identifier for the user that tried to enroll the device.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    

