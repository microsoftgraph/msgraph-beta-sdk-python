from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_log_collection_request = lazy_import('msgraph.generated.models.app_log_collection_request')
device_management_troubleshooting_event = lazy_import('msgraph.generated.models.device_management_troubleshooting_event')
mobile_app_troubleshooting_history_item = lazy_import('msgraph.generated.models.mobile_app_troubleshooting_history_item')

class MobileAppTroubleshootingEvent(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent):
    @property
    def application_id(self,) -> Optional[str]:
        """
        Gets the applicationId property value. Intune application identifier.
        Returns: Optional[str]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationId property value. Intune application identifier.
        Args:
            value: Value to set for the applicationId property.
        """
        self._application_id = value
    
    @property
    def app_log_collection_requests(self,) -> Optional[List[app_log_collection_request.AppLogCollectionRequest]]:
        """
        Gets the appLogCollectionRequests property value. The collection property of AppLogUploadRequest.
        Returns: Optional[List[app_log_collection_request.AppLogCollectionRequest]]
        """
        return self._app_log_collection_requests
    
    @app_log_collection_requests.setter
    def app_log_collection_requests(self,value: Optional[List[app_log_collection_request.AppLogCollectionRequest]] = None) -> None:
        """
        Sets the appLogCollectionRequests property value. The collection property of AppLogUploadRequest.
        Args:
            value: Value to set for the appLogCollectionRequests property.
        """
        self._app_log_collection_requests = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new MobileAppTroubleshootingEvent and sets the default values.
        """
        super().__init__()
        # Intune application identifier.
        self._application_id: Optional[str] = None
        # The collection property of AppLogUploadRequest.
        self._app_log_collection_requests: Optional[List[app_log_collection_request.AppLogCollectionRequest]] = None
        # Intune Mobile Application Troubleshooting History Item
        self._history: Optional[List[mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem]] = None
        # Device identifier created or collected by Intune.
        self._managed_device_identifier: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Identifier for the user that tried to enroll the device.
        self._user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MobileAppTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingEvent
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MobileAppTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_id": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "app_log_collection_requests": lambda n : setattr(self, 'app_log_collection_requests', n.get_collection_of_object_values(app_log_collection_request.AppLogCollectionRequest)),
            "history": lambda n : setattr(self, 'history', n.get_collection_of_object_values(mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem)),
            "managed_device_identifier": lambda n : setattr(self, 'managed_device_identifier', n.get_str_value()),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def history(self,) -> Optional[List[mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem]]:
        """
        Gets the history property value. Intune Mobile Application Troubleshooting History Item
        Returns: Optional[List[mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem]]
        """
        return self._history
    
    @history.setter
    def history(self,value: Optional[List[mobile_app_troubleshooting_history_item.MobileAppTroubleshootingHistoryItem]] = None) -> None:
        """
        Sets the history property value. Intune Mobile Application Troubleshooting History Item
        Args:
            value: Value to set for the history property.
        """
        self._history = value
    
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
            value: Value to set for the managedDeviceIdentifier property.
        """
        self._managed_device_identifier = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_collection_of_object_values("appLogCollectionRequests", self.app_log_collection_requests)
        writer.write_collection_of_object_values("history", self.history)
        writer.write_str_value("managedDeviceIdentifier", self.managed_device_identifier)
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
            value: Value to set for the userId property.
        """
        self._user_id = value
    

