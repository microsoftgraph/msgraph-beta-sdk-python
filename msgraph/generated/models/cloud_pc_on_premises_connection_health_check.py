from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

cloud_pc_on_premises_connection_health_check_error_type = lazy_import('msgraph.generated.models.cloud_pc_on_premises_connection_health_check_error_type')
cloud_pc_on_premises_connection_status = lazy_import('msgraph.generated.models.cloud_pc_on_premises_connection_status')

class CloudPcOnPremisesConnectionHealthCheck(AdditionalDataHolder, Parsable):
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
    def additional_details(self,) -> Optional[str]:
        """
        Gets the additionalDetails property value. Additional details about the health check or the recommended action.
        Returns: Optional[str]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalDetails property value. Additional details about the health check or the recommended action.
        Args:
            value: Value to set for the additionalDetails property.
        """
        self._additional_details = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new cloudPcOnPremisesConnectionHealthCheck and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Additional details about the health check or the recommended action.
        self._additional_details: Optional[str] = None
        # The display name for this health check item.
        self._display_name: Optional[str] = None
        # The end time of the health check item. Read-only.
        self._end_date_time: Optional[datetime] = None
        # The type of error that occurred during this health check.
        self._error_type: Optional[cloud_pc_on_premises_connection_health_check_error_type.CloudPcOnPremisesConnectionHealthCheckErrorType] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The recommended action to fix the corresponding error.
        self._recommended_action: Optional[str] = None
        # The start time of the health check item. Read-only.
        self._start_date_time: Optional[datetime] = None
        # The status property
        self._status: Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcOnPremisesConnectionHealthCheck:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnectionHealthCheck
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudPcOnPremisesConnectionHealthCheck()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for this health check item.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for this health check item.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. The end time of the health check item. Read-only.
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. The end time of the health check item. Read-only.
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    @property
    def error_type(self,) -> Optional[cloud_pc_on_premises_connection_health_check_error_type.CloudPcOnPremisesConnectionHealthCheckErrorType]:
        """
        Gets the errorType property value. The type of error that occurred during this health check.
        Returns: Optional[cloud_pc_on_premises_connection_health_check_error_type.CloudPcOnPremisesConnectionHealthCheckErrorType]
        """
        return self._error_type
    
    @error_type.setter
    def error_type(self,value: Optional[cloud_pc_on_premises_connection_health_check_error_type.CloudPcOnPremisesConnectionHealthCheckErrorType] = None) -> None:
        """
        Sets the errorType property value. The type of error that occurred during this health check.
        Args:
            value: Value to set for the errorType property.
        """
        self._error_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "error_type": lambda n : setattr(self, 'error_type', n.get_enum_value(cloud_pc_on_premises_connection_health_check_error_type.CloudPcOnPremisesConnectionHealthCheckErrorType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommended_action": lambda n : setattr(self, 'recommended_action', n.get_str_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus)),
        }
        return fields
    
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
    
    @property
    def recommended_action(self,) -> Optional[str]:
        """
        Gets the recommendedAction property value. The recommended action to fix the corresponding error.
        Returns: Optional[str]
        """
        return self._recommended_action
    
    @recommended_action.setter
    def recommended_action(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendedAction property value. The recommended action to fix the corresponding error.
        Args:
            value: Value to set for the recommendedAction property.
        """
        self._recommended_action = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("additionalDetails", self.additional_details)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_enum_value("errorType", self.error_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recommendedAction", self.recommended_action)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The start time of the health check item. Read-only.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The start time of the health check item. Read-only.
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def status(self,) -> Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[cloud_pc_on_premises_connection_status.CloudPcOnPremisesConnectionStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

