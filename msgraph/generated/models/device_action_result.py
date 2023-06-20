from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import action_state, activate_device_esim_action_result, configuration_manager_action_result, delete_user_from_shared_apple_device_action_result, locate_device_action_result, remote_lock_action_result, reset_passcode_action_result, revoke_apple_vpp_licenses_action_result, rotate_bit_locker_keys_device_action_result, windows_defender_scan_action_result

@dataclass
class DeviceActionResult(AdditionalDataHolder, Parsable):
    """
    Device action result
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Action name
    action_name: Optional[str] = None
    # The actionState property
    action_state: Optional[action_state.ActionState] = None
    # Time the action state was last updated
    last_updated_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Time the action was initiated
    start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceActionResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activateDeviceEsimActionResult".casefold():
            from . import activate_device_esim_action_result

            return activate_device_esim_action_result.ActivateDeviceEsimActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.configurationManagerActionResult".casefold():
            from . import configuration_manager_action_result

            return configuration_manager_action_result.ConfigurationManagerActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deleteUserFromSharedAppleDeviceActionResult".casefold():
            from . import delete_user_from_shared_apple_device_action_result

            return delete_user_from_shared_apple_device_action_result.DeleteUserFromSharedAppleDeviceActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.locateDeviceActionResult".casefold():
            from . import locate_device_action_result

            return locate_device_action_result.LocateDeviceActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteLockActionResult".casefold():
            from . import remote_lock_action_result

            return remote_lock_action_result.RemoteLockActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resetPasscodeActionResult".casefold():
            from . import reset_passcode_action_result

            return reset_passcode_action_result.ResetPasscodeActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.revokeAppleVppLicensesActionResult".casefold():
            from . import revoke_apple_vpp_licenses_action_result

            return revoke_apple_vpp_licenses_action_result.RevokeAppleVppLicensesActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rotateBitLockerKeysDeviceActionResult".casefold():
            from . import rotate_bit_locker_keys_device_action_result

            return rotate_bit_locker_keys_device_action_result.RotateBitLockerKeysDeviceActionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderScanActionResult".casefold():
            from . import windows_defender_scan_action_result

            return windows_defender_scan_action_result.WindowsDefenderScanActionResult()
        return DeviceActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import action_state, activate_device_esim_action_result, configuration_manager_action_result, delete_user_from_shared_apple_device_action_result, locate_device_action_result, remote_lock_action_result, reset_passcode_action_result, revoke_apple_vpp_licenses_action_result, rotate_bit_locker_keys_device_action_result, windows_defender_scan_action_result

        from . import action_state, activate_device_esim_action_result, configuration_manager_action_result, delete_user_from_shared_apple_device_action_result, locate_device_action_result, remote_lock_action_result, reset_passcode_action_result, revoke_apple_vpp_licenses_action_result, rotate_bit_locker_keys_device_action_result, windows_defender_scan_action_result

        fields: Dict[str, Callable[[Any], None]] = {
            "actionName": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "actionState": lambda n : setattr(self, 'action_state', n.get_enum_value(action_state.ActionState)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

