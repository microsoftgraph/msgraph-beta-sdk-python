from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class UpdateWindow(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updateWindow and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # End of a time window during which agents can receive updates
        self._update_window_end_time: Optional[time] = None
        # Start of a time window during which agents can receive updates
        self._update_window_start_time: Optional[time] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateWindow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateWindow
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateWindow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "updateWindowEndTime": lambda n : setattr(self, 'update_window_end_time', n.get_time_value()),
            "updateWindowStartTime": lambda n : setattr(self, 'update_window_start_time', n.get_time_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("updateWindowEndTime", self.update_window_end_time)
        writer.write_time_value("updateWindowStartTime", self.update_window_start_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def update_window_end_time(self,) -> Optional[time]:
        """
        Gets the updateWindowEndTime property value. End of a time window during which agents can receive updates
        Returns: Optional[time]
        """
        return self._update_window_end_time
    
    @update_window_end_time.setter
    def update_window_end_time(self,value: Optional[time] = None) -> None:
        """
        Sets the updateWindowEndTime property value. End of a time window during which agents can receive updates
        Args:
            value: Value to set for the update_window_end_time property.
        """
        self._update_window_end_time = value
    
    @property
    def update_window_start_time(self,) -> Optional[time]:
        """
        Gets the updateWindowStartTime property value. Start of a time window during which agents can receive updates
        Returns: Optional[time]
        """
        return self._update_window_start_time
    
    @update_window_start_time.setter
    def update_window_start_time(self,value: Optional[time] = None) -> None:
        """
        Sets the updateWindowStartTime property value. Start of a time window during which agents can receive updates
        Args:
            value: Value to set for the update_window_start_time property.
        """
        self._update_window_start_time = value
    

