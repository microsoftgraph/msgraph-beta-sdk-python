from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

update_window = lazy_import('msgraph.generated.models.update_window')

class HybridAgentUpdaterConfiguration(AdditionalDataHolder, Parsable):
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
    def allow_update_configuration_override(self,) -> Optional[bool]:
        """
        Gets the allowUpdateConfigurationOverride property value. Indicates if updater configuration will be skipped and the agent will receive an update when the next version of the agent is available.
        Returns: Optional[bool]
        """
        return self._allow_update_configuration_override
    
    @allow_update_configuration_override.setter
    def allow_update_configuration_override(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUpdateConfigurationOverride property value. Indicates if updater configuration will be skipped and the agent will receive an update when the next version of the agent is available.
        Args:
            value: Value to set for the allowUpdateConfigurationOverride property.
        """
        self._allow_update_configuration_override = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new hybridAgentUpdaterConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates if updater configuration will be skipped and the agent will receive an update when the next version of the agent is available.
        self._allow_update_configuration_override: Optional[bool] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._defer_update_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The updateWindow property
        self._update_window: Optional[update_window.UpdateWindow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HybridAgentUpdaterConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HybridAgentUpdaterConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HybridAgentUpdaterConfiguration()
    
    @property
    def defer_update_date_time(self,) -> Optional[datetime]:
        """
        Gets the deferUpdateDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._defer_update_date_time
    
    @defer_update_date_time.setter
    def defer_update_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deferUpdateDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the deferUpdateDateTime property.
        """
        self._defer_update_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_update_configuration_override": lambda n : setattr(self, 'allow_update_configuration_override', n.get_bool_value()),
            "defer_update_date_time": lambda n : setattr(self, 'defer_update_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "update_window": lambda n : setattr(self, 'update_window', n.get_object_value(update_window.UpdateWindow)),
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowUpdateConfigurationOverride", self.allow_update_configuration_override)
        writer.write_datetime_value("deferUpdateDateTime", self.defer_update_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("updateWindow", self.update_window)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def update_window(self,) -> Optional[update_window.UpdateWindow]:
        """
        Gets the updateWindow property value. The updateWindow property
        Returns: Optional[update_window.UpdateWindow]
        """
        return self._update_window
    
    @update_window.setter
    def update_window(self,value: Optional[update_window.UpdateWindow] = None) -> None:
        """
        Sets the updateWindow property value. The updateWindow property
        Args:
            value: Value to set for the updateWindow property.
        """
        self._update_window = value
    

