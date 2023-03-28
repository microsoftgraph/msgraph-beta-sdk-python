from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_management_troubleshooting_error_details, mobile_app_troubleshooting_app_policy_creation_history, mobile_app_troubleshooting_app_state_history, mobile_app_troubleshooting_app_target_history, mobile_app_troubleshooting_app_update_history, mobile_app_troubleshooting_device_checkin_history

class MobileAppTroubleshootingHistoryItem(AdditionalDataHolder, Parsable):
    """
    History Item contained in the Mobile App Troubleshooting Event.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new mobileAppTroubleshootingHistoryItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Time when the history item occurred.
        self._occurrence_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Object containing detailed information about the error and its remediation.
        self._troubleshooting_error_details: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingHistoryItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.mobileAppTroubleshootingAppPolicyCreationHistory":
                from . import mobile_app_troubleshooting_app_policy_creation_history

                return mobile_app_troubleshooting_app_policy_creation_history.MobileAppTroubleshootingAppPolicyCreationHistory()
            if mapping_value == "#microsoft.graph.mobileAppTroubleshootingAppStateHistory":
                from . import mobile_app_troubleshooting_app_state_history

                return mobile_app_troubleshooting_app_state_history.MobileAppTroubleshootingAppStateHistory()
            if mapping_value == "#microsoft.graph.mobileAppTroubleshootingAppTargetHistory":
                from . import mobile_app_troubleshooting_app_target_history

                return mobile_app_troubleshooting_app_target_history.MobileAppTroubleshootingAppTargetHistory()
            if mapping_value == "#microsoft.graph.mobileAppTroubleshootingAppUpdateHistory":
                from . import mobile_app_troubleshooting_app_update_history

                return mobile_app_troubleshooting_app_update_history.MobileAppTroubleshootingAppUpdateHistory()
            if mapping_value == "#microsoft.graph.mobileAppTroubleshootingDeviceCheckinHistory":
                from . import mobile_app_troubleshooting_device_checkin_history

                return mobile_app_troubleshooting_device_checkin_history.MobileAppTroubleshootingDeviceCheckinHistory()
        return MobileAppTroubleshootingHistoryItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_management_troubleshooting_error_details, mobile_app_troubleshooting_app_policy_creation_history, mobile_app_troubleshooting_app_state_history, mobile_app_troubleshooting_app_target_history, mobile_app_troubleshooting_app_update_history, mobile_app_troubleshooting_device_checkin_history

        fields: Dict[str, Callable[[Any], None]] = {
            "occurrenceDateTime": lambda n : setattr(self, 'occurrence_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "troubleshootingErrorDetails": lambda n : setattr(self, 'troubleshooting_error_details', n.get_object_value(device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails)),
        }
        return fields
    
    @property
    def occurrence_date_time(self,) -> Optional[datetime]:
        """
        Gets the occurrenceDateTime property value. Time when the history item occurred.
        Returns: Optional[datetime]
        """
        return self._occurrence_date_time
    
    @occurrence_date_time.setter
    def occurrence_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the occurrenceDateTime property value. Time when the history item occurred.
        Args:
            value: Value to set for the occurrence_date_time property.
        """
        self._occurrence_date_time = value
    
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
            value: Value to set for the odata_type property.
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
        writer.write_datetime_value("occurrenceDateTime", self.occurrence_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("troubleshootingErrorDetails", self.troubleshooting_error_details)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def troubleshooting_error_details(self,) -> Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails]:
        """
        Gets the troubleshootingErrorDetails property value. Object containing detailed information about the error and its remediation.
        Returns: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails]
        """
        return self._troubleshooting_error_details
    
    @troubleshooting_error_details.setter
    def troubleshooting_error_details(self,value: Optional[device_management_troubleshooting_error_details.DeviceManagementTroubleshootingErrorDetails] = None) -> None:
        """
        Sets the troubleshootingErrorDetails property value. Object containing detailed information about the error and its remediation.
        Args:
            value: Value to set for the troubleshooting_error_details property.
        """
        self._troubleshooting_error_details = value
    

