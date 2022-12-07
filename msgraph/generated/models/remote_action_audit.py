from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_state = lazy_import('msgraph.generated.models.action_state')
entity = lazy_import('msgraph.generated.models.entity')
remote_action = lazy_import('msgraph.generated.models.remote_action')

class RemoteActionAudit(entity.Entity):
    """
    Report of remote actions initiated on the devices belonging to a certain tenant.
    """
    @property
    def action(self,) -> Optional[remote_action.RemoteAction]:
        """
        Gets the action property value. Remote actions Intune supports.
        Returns: Optional[remote_action.RemoteAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[remote_action.RemoteAction] = None) -> None:
        """
        Sets the action property value. Remote actions Intune supports.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def action_state(self,) -> Optional[action_state.ActionState]:
        """
        Gets the actionState property value. The actionState property
        Returns: Optional[action_state.ActionState]
        """
        return self._action_state
    
    @action_state.setter
    def action_state(self,value: Optional[action_state.ActionState] = None) -> None:
        """
        Sets the actionState property value. The actionState property
        Args:
            value: Value to set for the actionState property.
        """
        self._action_state = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new remoteActionAudit and sets the default values.
        """
        super().__init__()
        # Remote actions Intune supports.
        self._action: Optional[remote_action.RemoteAction] = None
        # The actionState property
        self._action_state: Optional[action_state.ActionState] = None
        # Intune device name.
        self._device_display_name: Optional[str] = None
        # IMEI of the device.
        self._device_i_m_e_i: Optional[str] = None
        # Upn of the device owner.
        self._device_owner_user_principal_name: Optional[str] = None
        # User who initiated the device action, format is UPN.
        self._initiated_by_user_principal_name: Optional[str] = None
        # Action target.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Time when the action was issued, given in UTC.
        self._request_date_time: Optional[datetime] = None
        # [deprecated] Please use InitiatedByUserPrincipalName instead.
        self._user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteActionAudit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteActionAudit
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoteActionAudit()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. Intune device name.
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. Intune device name.
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_i_m_e_i(self,) -> Optional[str]:
        """
        Gets the deviceIMEI property value. IMEI of the device.
        Returns: Optional[str]
        """
        return self._device_i_m_e_i
    
    @device_i_m_e_i.setter
    def device_i_m_e_i(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceIMEI property value. IMEI of the device.
        Args:
            value: Value to set for the deviceIMEI property.
        """
        self._device_i_m_e_i = value
    
    @property
    def device_owner_user_principal_name(self,) -> Optional[str]:
        """
        Gets the deviceOwnerUserPrincipalName property value. Upn of the device owner.
        Returns: Optional[str]
        """
        return self._device_owner_user_principal_name
    
    @device_owner_user_principal_name.setter
    def device_owner_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceOwnerUserPrincipalName property value. Upn of the device owner.
        Args:
            value: Value to set for the deviceOwnerUserPrincipalName property.
        """
        self._device_owner_user_principal_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(remote_action.RemoteAction)),
            "action_state": lambda n : setattr(self, 'action_state', n.get_enum_value(action_state.ActionState)),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_i_m_e_i": lambda n : setattr(self, 'device_i_m_e_i', n.get_str_value()),
            "device_owner_user_principal_name": lambda n : setattr(self, 'device_owner_user_principal_name', n.get_str_value()),
            "initiated_by_user_principal_name": lambda n : setattr(self, 'initiated_by_user_principal_name', n.get_str_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "request_date_time": lambda n : setattr(self, 'request_date_time', n.get_datetime_value()),
            "user_name": lambda n : setattr(self, 'user_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiated_by_user_principal_name(self,) -> Optional[str]:
        """
        Gets the initiatedByUserPrincipalName property value. User who initiated the device action, format is UPN.
        Returns: Optional[str]
        """
        return self._initiated_by_user_principal_name
    
    @initiated_by_user_principal_name.setter
    def initiated_by_user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the initiatedByUserPrincipalName property value. User who initiated the device action, format is UPN.
        Args:
            value: Value to set for the initiatedByUserPrincipalName property.
        """
        self._initiated_by_user_principal_name = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. Action target.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. Action target.
        Args:
            value: Value to set for the managedDeviceId property.
        """
        self._managed_device_id = value
    
    @property
    def request_date_time(self,) -> Optional[datetime]:
        """
        Gets the requestDateTime property value. Time when the action was issued, given in UTC.
        Returns: Optional[datetime]
        """
        return self._request_date_time
    
    @request_date_time.setter
    def request_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the requestDateTime property value. Time when the action was issued, given in UTC.
        Args:
            value: Value to set for the requestDateTime property.
        """
        self._request_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceIMEI", self.device_i_m_e_i)
        writer.write_str_value("deviceOwnerUserPrincipalName", self.device_owner_user_principal_name)
        writer.write_str_value("initiatedByUserPrincipalName", self.initiated_by_user_principal_name)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_datetime_value("requestDateTime", self.request_date_time)
        writer.write_str_value("userName", self.user_name)
    
    @property
    def user_name(self,) -> Optional[str]:
        """
        Gets the userName property value. [deprecated] Please use InitiatedByUserPrincipalName instead.
        Returns: Optional[str]
        """
        return self._user_name
    
    @user_name.setter
    def user_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userName property value. [deprecated] Please use InitiatedByUserPrincipalName instead.
        Args:
            value: Value to set for the userName property.
        """
        self._user_name = value
    

