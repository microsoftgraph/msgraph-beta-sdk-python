from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

zebra_fota_deployment_state = lazy_import('msgraph.generated.models.zebra_fota_deployment_state')

class ZebraFotaDeploymentStatus(AdditionalDataHolder, Parsable):
    """
    Describes the status for a single FOTA deployment.
    """
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
    def cancel_requested(self,) -> Optional[bool]:
        """
        Gets the cancelRequested property value. A boolean that indicates if a cancellation was requested on the deployment. NOTE: A cancellation request does not guarantee that the deployment was canceled.
        Returns: Optional[bool]
        """
        return self._cancel_requested
    
    @cancel_requested.setter
    def cancel_requested(self,value: Optional[bool] = None) -> None:
        """
        Sets the cancelRequested property value. A boolean that indicates if a cancellation was requested on the deployment. NOTE: A cancellation request does not guarantee that the deployment was canceled.
        Args:
            value: Value to set for the cancelRequested property.
        """
        self._cancel_requested = value
    
    @property
    def complete_or_canceled_date_time(self,) -> Optional[datetime]:
        """
        Gets the completeOrCanceledDateTime property value. The date and time when this deployment was completed or canceled. The actual date time is determined by the value of state. If the state is canceled, this property holds the cancellation date/time. If the the state is completed, this property holds the completion date/time. If the deployment is not completed before the deployment end date, then completed date/time and end date/time are the same. This is always in the deployment timezone. Note: An installation that is in progress can continue past the deployment end date.
        Returns: Optional[datetime]
        """
        return self._complete_or_canceled_date_time
    
    @complete_or_canceled_date_time.setter
    def complete_or_canceled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completeOrCanceledDateTime property value. The date and time when this deployment was completed or canceled. The actual date time is determined by the value of state. If the state is canceled, this property holds the cancellation date/time. If the the state is completed, this property holds the completion date/time. If the deployment is not completed before the deployment end date, then completed date/time and end date/time are the same. This is always in the deployment timezone. Note: An installation that is in progress can continue past the deployment end date.
        Args:
            value: Value to set for the completeOrCanceledDateTime property.
        """
        self._complete_or_canceled_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new zebraFotaDeploymentStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A boolean that indicates if a cancellation was requested on the deployment. NOTE: A cancellation request does not guarantee that the deployment was canceled.
        self._cancel_requested: Optional[bool] = None
        # The date and time when this deployment was completed or canceled. The actual date time is determined by the value of state. If the state is canceled, this property holds the cancellation date/time. If the the state is completed, this property holds the completion date/time. If the deployment is not completed before the deployment end date, then completed date/time and end date/time are the same. This is always in the deployment timezone. Note: An installation that is in progress can continue past the deployment end date.
        self._complete_or_canceled_date_time: Optional[datetime] = None
        # Date and time when the deployment status was updated from Zebra
        self._last_updated_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents the state of Zebra FOTA deployment.
        self._state: Optional[zebra_fota_deployment_state.ZebraFotaDeploymentState] = None
        # An integer that indicates the total number of devices where installation was successful.
        self._total_awaiting_install: Optional[int] = None
        # An integer that indicates the total number of devices where installation was canceled.
        self._total_canceled: Optional[int] = None
        # An integer that indicates the total number of devices that have a job in the CREATED state. Typically indicates jobs that did not reach the devices.
        self._total_created: Optional[int] = None
        # An integer that indicates the total number of devices in the deployment.
        self._total_devices: Optional[int] = None
        # An integer that indicates the total number of devices where installation was successful.
        self._total_downloading: Optional[int] = None
        # An integer that indicates the total number of devices that have failed to download the new OS file.
        self._total_failed_download: Optional[int] = None
        # An integer that indicates the total number of devices that have failed to install the new OS file.
        self._total_failed_install: Optional[int] = None
        # An integer that indicates the total number of devices that received the json and are scheduled.
        self._total_scheduled: Optional[int] = None
        # An integer that indicates the total number of devices where installation was successful.
        self._total_succeeded_install: Optional[int] = None
        # An integer that indicates the total number of devices where no deployment status or end state has not received, even after the scheduled end date was reached.
        self._total_unknown: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ZebraFotaDeploymentStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ZebraFotaDeploymentStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ZebraFotaDeploymentStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cancel_requested": lambda n : setattr(self, 'cancel_requested', n.get_bool_value()),
            "complete_or_canceled_date_time": lambda n : setattr(self, 'complete_or_canceled_date_time', n.get_datetime_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(zebra_fota_deployment_state.ZebraFotaDeploymentState)),
            "total_awaiting_install": lambda n : setattr(self, 'total_awaiting_install', n.get_int_value()),
            "total_canceled": lambda n : setattr(self, 'total_canceled', n.get_int_value()),
            "total_created": lambda n : setattr(self, 'total_created', n.get_int_value()),
            "total_devices": lambda n : setattr(self, 'total_devices', n.get_int_value()),
            "total_downloading": lambda n : setattr(self, 'total_downloading', n.get_int_value()),
            "total_failed_download": lambda n : setattr(self, 'total_failed_download', n.get_int_value()),
            "total_failed_install": lambda n : setattr(self, 'total_failed_install', n.get_int_value()),
            "total_scheduled": lambda n : setattr(self, 'total_scheduled', n.get_int_value()),
            "total_succeeded_install": lambda n : setattr(self, 'total_succeeded_install', n.get_int_value()),
            "total_unknown": lambda n : setattr(self, 'total_unknown', n.get_int_value()),
        }
        return fields
    
    @property
    def last_updated_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastUpdatedDateTime property value. Date and time when the deployment status was updated from Zebra
        Returns: Optional[datetime]
        """
        return self._last_updated_date_time
    
    @last_updated_date_time.setter
    def last_updated_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastUpdatedDateTime property value. Date and time when the deployment status was updated from Zebra
        Args:
            value: Value to set for the lastUpdatedDateTime property.
        """
        self._last_updated_date_time = value
    
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
        writer.write_bool_value("cancelRequested", self.cancel_requested)
        writer.write_datetime_value("completeOrCanceledDateTime", self.complete_or_canceled_date_time)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_int_value("totalAwaitingInstall", self.total_awaiting_install)
        writer.write_int_value("totalCanceled", self.total_canceled)
        writer.write_int_value("totalCreated", self.total_created)
        writer.write_int_value("totalDevices", self.total_devices)
        writer.write_int_value("totalDownloading", self.total_downloading)
        writer.write_int_value("totalFailedDownload", self.total_failed_download)
        writer.write_int_value("totalFailedInstall", self.total_failed_install)
        writer.write_int_value("totalScheduled", self.total_scheduled)
        writer.write_int_value("totalSucceededInstall", self.total_succeeded_install)
        writer.write_int_value("totalUnknown", self.total_unknown)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[zebra_fota_deployment_state.ZebraFotaDeploymentState]:
        """
        Gets the state property value. Represents the state of Zebra FOTA deployment.
        Returns: Optional[zebra_fota_deployment_state.ZebraFotaDeploymentState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[zebra_fota_deployment_state.ZebraFotaDeploymentState] = None) -> None:
        """
        Sets the state property value. Represents the state of Zebra FOTA deployment.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def total_awaiting_install(self,) -> Optional[int]:
        """
        Gets the totalAwaitingInstall property value. An integer that indicates the total number of devices where installation was successful.
        Returns: Optional[int]
        """
        return self._total_awaiting_install
    
    @total_awaiting_install.setter
    def total_awaiting_install(self,value: Optional[int] = None) -> None:
        """
        Sets the totalAwaitingInstall property value. An integer that indicates the total number of devices where installation was successful.
        Args:
            value: Value to set for the totalAwaitingInstall property.
        """
        self._total_awaiting_install = value
    
    @property
    def total_canceled(self,) -> Optional[int]:
        """
        Gets the totalCanceled property value. An integer that indicates the total number of devices where installation was canceled.
        Returns: Optional[int]
        """
        return self._total_canceled
    
    @total_canceled.setter
    def total_canceled(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCanceled property value. An integer that indicates the total number of devices where installation was canceled.
        Args:
            value: Value to set for the totalCanceled property.
        """
        self._total_canceled = value
    
    @property
    def total_created(self,) -> Optional[int]:
        """
        Gets the totalCreated property value. An integer that indicates the total number of devices that have a job in the CREATED state. Typically indicates jobs that did not reach the devices.
        Returns: Optional[int]
        """
        return self._total_created
    
    @total_created.setter
    def total_created(self,value: Optional[int] = None) -> None:
        """
        Sets the totalCreated property value. An integer that indicates the total number of devices that have a job in the CREATED state. Typically indicates jobs that did not reach the devices.
        Args:
            value: Value to set for the totalCreated property.
        """
        self._total_created = value
    
    @property
    def total_devices(self,) -> Optional[int]:
        """
        Gets the totalDevices property value. An integer that indicates the total number of devices in the deployment.
        Returns: Optional[int]
        """
        return self._total_devices
    
    @total_devices.setter
    def total_devices(self,value: Optional[int] = None) -> None:
        """
        Sets the totalDevices property value. An integer that indicates the total number of devices in the deployment.
        Args:
            value: Value to set for the totalDevices property.
        """
        self._total_devices = value
    
    @property
    def total_downloading(self,) -> Optional[int]:
        """
        Gets the totalDownloading property value. An integer that indicates the total number of devices where installation was successful.
        Returns: Optional[int]
        """
        return self._total_downloading
    
    @total_downloading.setter
    def total_downloading(self,value: Optional[int] = None) -> None:
        """
        Sets the totalDownloading property value. An integer that indicates the total number of devices where installation was successful.
        Args:
            value: Value to set for the totalDownloading property.
        """
        self._total_downloading = value
    
    @property
    def total_failed_download(self,) -> Optional[int]:
        """
        Gets the totalFailedDownload property value. An integer that indicates the total number of devices that have failed to download the new OS file.
        Returns: Optional[int]
        """
        return self._total_failed_download
    
    @total_failed_download.setter
    def total_failed_download(self,value: Optional[int] = None) -> None:
        """
        Sets the totalFailedDownload property value. An integer that indicates the total number of devices that have failed to download the new OS file.
        Args:
            value: Value to set for the totalFailedDownload property.
        """
        self._total_failed_download = value
    
    @property
    def total_failed_install(self,) -> Optional[int]:
        """
        Gets the totalFailedInstall property value. An integer that indicates the total number of devices that have failed to install the new OS file.
        Returns: Optional[int]
        """
        return self._total_failed_install
    
    @total_failed_install.setter
    def total_failed_install(self,value: Optional[int] = None) -> None:
        """
        Sets the totalFailedInstall property value. An integer that indicates the total number of devices that have failed to install the new OS file.
        Args:
            value: Value to set for the totalFailedInstall property.
        """
        self._total_failed_install = value
    
    @property
    def total_scheduled(self,) -> Optional[int]:
        """
        Gets the totalScheduled property value. An integer that indicates the total number of devices that received the json and are scheduled.
        Returns: Optional[int]
        """
        return self._total_scheduled
    
    @total_scheduled.setter
    def total_scheduled(self,value: Optional[int] = None) -> None:
        """
        Sets the totalScheduled property value. An integer that indicates the total number of devices that received the json and are scheduled.
        Args:
            value: Value to set for the totalScheduled property.
        """
        self._total_scheduled = value
    
    @property
    def total_succeeded_install(self,) -> Optional[int]:
        """
        Gets the totalSucceededInstall property value. An integer that indicates the total number of devices where installation was successful.
        Returns: Optional[int]
        """
        return self._total_succeeded_install
    
    @total_succeeded_install.setter
    def total_succeeded_install(self,value: Optional[int] = None) -> None:
        """
        Sets the totalSucceededInstall property value. An integer that indicates the total number of devices where installation was successful.
        Args:
            value: Value to set for the totalSucceededInstall property.
        """
        self._total_succeeded_install = value
    
    @property
    def total_unknown(self,) -> Optional[int]:
        """
        Gets the totalUnknown property value. An integer that indicates the total number of devices where no deployment status or end state has not received, even after the scheduled end date was reached.
        Returns: Optional[int]
        """
        return self._total_unknown
    
    @total_unknown.setter
    def total_unknown(self,value: Optional[int] = None) -> None:
        """
        Sets the totalUnknown property value. An integer that indicates the total number of devices where no deployment status or end state has not received, even after the scheduled end date was reached.
        Args:
            value: Value to set for the totalUnknown property.
        """
        self._total_unknown = value
    

