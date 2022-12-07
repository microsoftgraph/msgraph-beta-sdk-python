from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class UserExperienceAnalyticsAppHealthDevicePerformanceDetails(entity.Entity):
    """
    The user experience analytics device performance entity contains device performance details.
    """
    @property
    def app_display_name(self,) -> Optional[str]:
        """
        Gets the appDisplayName property value. The friendly name of the application for which the event occurred.
        Returns: Optional[str]
        """
        return self._app_display_name
    
    @app_display_name.setter
    def app_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the appDisplayName property value. The friendly name of the application for which the event occurred.
        Args:
            value: Value to set for the appDisplayName property.
        """
        self._app_display_name = value
    
    @property
    def app_publisher(self,) -> Optional[str]:
        """
        Gets the appPublisher property value. The publisher of the application.
        Returns: Optional[str]
        """
        return self._app_publisher
    
    @app_publisher.setter
    def app_publisher(self,value: Optional[str] = None) -> None:
        """
        Sets the appPublisher property value. The publisher of the application.
        Args:
            value: Value to set for the appPublisher property.
        """
        self._app_publisher = value
    
    @property
    def app_version(self,) -> Optional[str]:
        """
        Gets the appVersion property value. The version of the application.
        Returns: Optional[str]
        """
        return self._app_version
    
    @app_version.setter
    def app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the appVersion property value. The version of the application.
        Args:
            value: Value to set for the appVersion property.
        """
        self._app_version = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userExperienceAnalyticsAppHealthDevicePerformanceDetails and sets the default values.
        """
        super().__init__()
        # The friendly name of the application for which the event occurred.
        self._app_display_name: Optional[str] = None
        # The publisher of the application.
        self._app_publisher: Optional[str] = None
        # The version of the application.
        self._app_version: Optional[str] = None
        # The name of the device.
        self._device_display_name: Optional[str] = None
        # The id of the device.
        self._device_id: Optional[str] = None
        # The time the event occurred.
        self._event_date_time: Optional[datetime] = None
        # The type of the event.
        self._event_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthDevicePerformanceDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserExperienceAnalyticsAppHealthDevicePerformanceDetails()
    
    @property
    def device_display_name(self,) -> Optional[str]:
        """
        Gets the deviceDisplayName property value. The name of the device.
        Returns: Optional[str]
        """
        return self._device_display_name
    
    @device_display_name.setter
    def device_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceDisplayName property value. The name of the device.
        Args:
            value: Value to set for the deviceDisplayName property.
        """
        self._device_display_name = value
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. The id of the device.
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. The id of the device.
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    @property
    def event_date_time(self,) -> Optional[datetime]:
        """
        Gets the eventDateTime property value. The time the event occurred.
        Returns: Optional[datetime]
        """
        return self._event_date_time
    
    @event_date_time.setter
    def event_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the eventDateTime property value. The time the event occurred.
        Args:
            value: Value to set for the eventDateTime property.
        """
        self._event_date_time = value
    
    @property
    def event_type(self,) -> Optional[str]:
        """
        Gets the eventType property value. The type of the event.
        Returns: Optional[str]
        """
        return self._event_type
    
    @event_type.setter
    def event_type(self,value: Optional[str] = None) -> None:
        """
        Sets the eventType property value. The type of the event.
        Args:
            value: Value to set for the eventType property.
        """
        self._event_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_display_name": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "app_publisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "app_version": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "event_date_time": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "event_type": lambda n : setattr(self, 'event_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_str_value("appVersion", self.app_version)
        writer.write_str_value("deviceDisplayName", self.device_display_name)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("eventType", self.event_type)
    

