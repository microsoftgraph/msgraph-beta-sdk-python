from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_state = lazy_import('msgraph.generated.models.action_state')
vpp_token_action_failure_reason = lazy_import('msgraph.generated.models.vpp_token_action_failure_reason')

class MacOsVppAppRevokeLicensesActionResult(AdditionalDataHolder, Parsable):
    """
    Defines results for actions on MacOS Vpp Apps, contains inherited properties for ActionResult.
    """
    @property
    def action_failure_reason(self,) -> Optional[vpp_token_action_failure_reason.VppTokenActionFailureReason]:
        """
        Gets the actionFailureReason property value. Possible types of reasons for an Apple Volume Purchase Program token action failure.
        Returns: Optional[vpp_token_action_failure_reason.VppTokenActionFailureReason]
        """
        return self._action_failure_reason
    
    @action_failure_reason.setter
    def action_failure_reason(self,value: Optional[vpp_token_action_failure_reason.VppTokenActionFailureReason] = None) -> None:
        """
        Sets the actionFailureReason property value. Possible types of reasons for an Apple Volume Purchase Program token action failure.
        Args:
            value: Value to set for the actionFailureReason property.
        """
        self._action_failure_reason = value
    
    @property
    def action_name(self,) -> Optional[str]:
        """
        Gets the actionName property value. Action name
        Returns: Optional[str]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[str] = None) -> None:
        """
        Sets the actionName property value. Action name
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
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
        Instantiates a new macOsVppAppRevokeLicensesActionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Possible types of reasons for an Apple Volume Purchase Program token action failure.
        self._action_failure_reason: Optional[vpp_token_action_failure_reason.VppTokenActionFailureReason] = None
        # Action name
        self._action_name: Optional[str] = None
        # The actionState property
        self._action_state: Optional[action_state.ActionState] = None
        # A count of the number of licenses for which revoke failed.
        self._failed_licenses_count: Optional[int] = None
        # Time the action state was last updated
        self._last_updated_date_time: Optional[datetime] = None
        # DeviceId associated with the action.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Time the action was initiated
        self._start_date_time: Optional[datetime] = None
        # A count of the number of licenses for which revoke was attempted.
        self._total_licenses_count: Optional[int] = None
        # UserId associated with the action.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MacOsVppAppRevokeLicensesActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MacOsVppAppRevokeLicensesActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MacOsVppAppRevokeLicensesActionResult()
    
    @property
    def failed_licenses_count(self,) -> Optional[int]:
        """
        Gets the failedLicensesCount property value. A count of the number of licenses for which revoke failed.
        Returns: Optional[int]
        """
        return self._failed_licenses_count
    
    @failed_licenses_count.setter
    def failed_licenses_count(self,value: Optional[int] = None) -> None:
        """
        Sets the failedLicensesCount property value. A count of the number of licenses for which revoke failed.
        Args:
            value: Value to set for the failedLicensesCount property.
        """
        self._failed_licenses_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_failure_reason": lambda n : setattr(self, 'action_failure_reason', n.get_enum_value(vpp_token_action_failure_reason.VppTokenActionFailureReason)),
            "action_name": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "action_state": lambda n : setattr(self, 'action_state', n.get_enum_value(action_state.ActionState)),
            "failed_licenses_count": lambda n : setattr(self, 'failed_licenses_count', n.get_int_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "total_licenses_count": lambda n : setattr(self, 'total_licenses_count', n.get_int_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Time the action state was last updated
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Time the action state was last updated
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. DeviceId associated with the action.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. DeviceId associated with the action.
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("actionFailureReason", self.action_failure_reason)
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_int_value("failedLicensesCount", self.failed_licenses_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_int_value("totalLicensesCount", self.total_licenses_count)
        writer.write_str_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Time the action was initiated
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Time the action was initiated
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def total_licenses_count(self,) -> Optional[int]:
        """
        Gets the totalLicensesCount property value. A count of the number of licenses for which revoke was attempted.
        Returns: Optional[int]
        """
        return self._total_licenses_count
    
    @total_licenses_count.setter
    def total_licenses_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalLicensesCount property value. A count of the number of licenses for which revoke was attempted.
        Args:
            value: Value to set for the totalLicensesCount property.
        """
        self._total_licenses_count = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. UserId associated with the action.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. UserId associated with the action.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

