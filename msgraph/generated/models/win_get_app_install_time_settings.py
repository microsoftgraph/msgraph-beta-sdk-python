from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class WinGetAppInstallTimeSettings(AdditionalDataHolder, Parsable):
    """
    Contains properties used to determine when to offer an app to devices and when to install the app on devices.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new winGetAppInstallTimeSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The time at which the app should be installed.
        self._deadline_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Whether the local device time or UTC time should be used when determining the deadline times.
        self._use_local_time: Optional[bool] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WinGetAppInstallTimeSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WinGetAppInstallTimeSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WinGetAppInstallTimeSettings()
    
    @property
    def deadline_date_time(self,) -> Optional[datetime]:
        """
        Gets the deadlineDateTime property value. The time at which the app should be installed.
        Returns: Optional[datetime]
        """
        return self._deadline_date_time
    
    @deadline_date_time.setter
    def deadline_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deadlineDateTime property value. The time at which the app should be installed.
        Args:
            value: Value to set for the deadline_date_time property.
        """
        self._deadline_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deadlineDateTime": lambda n : setattr(self, 'deadline_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "useLocalTime": lambda n : setattr(self, 'use_local_time', n.get_bool_value()),
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
        writer.write_datetime_value("deadlineDateTime", self.deadline_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("useLocalTime", self.use_local_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def use_local_time(self,) -> Optional[bool]:
        """
        Gets the useLocalTime property value. Whether the local device time or UTC time should be used when determining the deadline times.
        Returns: Optional[bool]
        """
        return self._use_local_time
    
    @use_local_time.setter
    def use_local_time(self,value: Optional[bool] = None) -> None:
        """
        Sets the useLocalTime property value. Whether the local device time or UTC time should be used when determining the deadline times.
        Args:
            value: Value to set for the use_local_time property.
        """
        self._use_local_time = value
    

