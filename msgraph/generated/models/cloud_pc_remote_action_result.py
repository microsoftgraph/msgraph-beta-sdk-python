from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_state = lazy_import('msgraph.generated.models.action_state')
cloud_pc_status_details = lazy_import('msgraph.generated.models.cloud_pc_status_details')

class CloudPcRemoteActionResult(AdditionalDataHolder, Parsable):
    @property
    def action_name(self,) -> Optional[str]:
        """
        Gets the actionName property value. The specified action. Supported values in the Microsoft Endpoint Manager portal are: Reprovision, Resize, Restore. Supported values in enterprise Cloud PC devices are: Reboot, Rename, Reprovision, Troubleshoot.
        Returns: Optional[str]
        """
        return self._action_name
    
    @action_name.setter
    def action_name(self,value: Optional[str] = None) -> None:
        """
        Sets the actionName property value. The specified action. Supported values in the Microsoft Endpoint Manager portal are: Reprovision, Resize, Restore. Supported values in enterprise Cloud PC devices are: Reboot, Rename, Reprovision, Troubleshoot.
        Args:
            value: Value to set for the actionName property.
        """
        self._action_name = value
    
    @property
    def action_state(self,) -> Optional[action_state.ActionState]:
        """
        Gets the actionState property value. State of the action. Possible values are: None, pending, canceled, active, done, failed, notSupported. Read-only.
        Returns: Optional[action_state.ActionState]
        """
        return self._action_state
    
    @action_state.setter
    def action_state(self,value: Optional[action_state.ActionState] = None) -> None:
        """
        Sets the actionState property value. State of the action. Possible values are: None, pending, canceled, active, done, failed, notSupported. Read-only.
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
    
    @property
    def cloud_pc_id(self,) -> Optional[str]:
        """
        Gets the cloudPcId property value. The ID of the Cloud PC device on which the remote action is performed. Read-only.
        Returns: Optional[str]
        """
        return self._cloud_pc_id
    
    @cloud_pc_id.setter
    def cloud_pc_id(self,value: Optional[str] = None) -> None:
        """
        Sets the cloudPcId property value. The ID of the Cloud PC device on which the remote action is performed. Read-only.
        Args:
            value: Value to set for the cloudPcId property.
        """
        self._cloud_pc_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcRemoteActionResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The specified action. Supported values in the Microsoft Endpoint Manager portal are: Reprovision, Resize, Restore. Supported values in enterprise Cloud PC devices are: Reboot, Rename, Reprovision, Troubleshoot.
        self._action_name: Optional[str] = None
        # State of the action. Possible values are: None, pending, canceled, active, done, failed, notSupported. Read-only.
        self._action_state: Optional[action_state.ActionState] = None
        # The ID of the Cloud PC device on which the remote action is performed. Read-only.
        self._cloud_pc_id: Optional[str] = None
        # Last update time for action. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
        self._last_updated_date_time: Optional[datetime] = None
        # The ID of the Intune managed device on which the remote action is performed. Read-only.
        self._managed_device_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Time the action was initiated. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
        self._start_date_time: Optional[datetime] = None
        # The details of the Cloud PC status.
        self._status_details: Optional[cloud_pc_status_details.CloudPcStatusDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcRemoteActionResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcRemoteActionResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcRemoteActionResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_name": lambda n : setattr(self, 'action_name', n.get_str_value()),
            "action_state": lambda n : setattr(self, 'action_state', n.get_enum_value(action_state.ActionState)),
            "cloud_pc_id": lambda n : setattr(self, 'cloud_pc_id', n.get_str_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "managed_device_id": lambda n : setattr(self, 'managed_device_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status_details": lambda n : setattr(self, 'status_details', n.get_object_value(cloud_pc_status_details.CloudPcStatusDetails)),
        }
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Last update time for action. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Last update time for action. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
    @property
    def managed_device_id(self,) -> Optional[str]:
        """
        Gets the managedDeviceId property value. The ID of the Intune managed device on which the remote action is performed. Read-only.
        Returns: Optional[str]
        """
        return self._managed_device_id
    
    @managed_device_id.setter
    def managed_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceId property value. The ID of the Intune managed device on which the remote action is performed. Read-only.
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
        writer.write_str_value("actionName", self.action_name)
        writer.write_enum_value("actionState", self.action_state)
        writer.write_str_value("cloudPcId", self.cloud_pc_id)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("managedDeviceId", self.managed_device_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_object_value("statusDetails", self.status_details)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Time the action was initiated. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Time the action was initiated. The Timestamp is shown in ISO 8601 format and Coordinated Universal Time (UTC). For example, midnight UTC on Jan 1, 2014 appears as '2014-01-01T00:00:00Z'.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status_details(self,) -> Optional[cloud_pc_status_details.CloudPcStatusDetails]:
        """
        Gets the statusDetails property value. The details of the Cloud PC status.
        Returns: Optional[cloud_pc_status_details.CloudPcStatusDetails]
        """
        return self._status_details
    
    @status_details.setter
    def status_details(self,value: Optional[cloud_pc_status_details.CloudPcStatusDetails] = None) -> None:
        """
        Sets the statusDetails property value. The details of the Cloud PC status.
        Args:
            value: Value to set for the statusDetails property.
        """
        self._status_details = value
    

