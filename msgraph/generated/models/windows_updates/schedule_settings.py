from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

gradual_rollout_settings = lazy_import('msgraph.generated.models.windows_updates.gradual_rollout_settings')

class ScheduleSettings(AdditionalDataHolder, Parsable):
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
        Instantiates a new scheduleSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The gradualRollout property
        self._gradual_rollout: Optional[gradual_rollout_settings.GradualRolloutSettings] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The startDateTime property
        self._start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ScheduleSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "gradualRollout": lambda n : setattr(self, 'gradual_rollout', n.get_object_value(gradual_rollout_settings.GradualRolloutSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
        }
        return fields
    
    @property
    def gradual_rollout(self,) -> Optional[gradual_rollout_settings.GradualRolloutSettings]:
        """
        Gets the gradualRollout property value. The gradualRollout property
        Returns: Optional[gradual_rollout_settings.GradualRolloutSettings]
        """
        return self._gradual_rollout
    
    @gradual_rollout.setter
    def gradual_rollout(self,value: Optional[gradual_rollout_settings.GradualRolloutSettings] = None) -> None:
        """
        Sets the gradualRollout property value. The gradualRollout property
        Args:
            value: Value to set for the gradual_rollout property.
        """
        self._gradual_rollout = value
    
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
        writer.write_object_value("gradualRollout", self.gradual_rollout)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    

