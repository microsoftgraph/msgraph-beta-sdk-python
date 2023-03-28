from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_applicability_settings, expedite_settings, monitoring_settings, schedule_settings, user_experience_settings

class DeploymentSettings(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new deploymentSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Settings for governing whether content is applicable to a device.
        self._content_applicability: Optional[content_applicability_settings.ContentApplicabilitySettings] = None
        # Settings for governing whether updates should be expedited.
        self._expedite: Optional[expedite_settings.ExpediteSettings] = None
        # Settings for governing conditions to monitor and automated actions to take.
        self._monitoring: Optional[monitoring_settings.MonitoringSettings] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Settings for governing how and when the content is rolled out.
        self._schedule: Optional[schedule_settings.ScheduleSettings] = None
        # Settings for governing end user update experience.
        self._user_experience: Optional[user_experience_settings.UserExperienceSettings] = None
    
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
    def content_applicability(self,) -> Optional[content_applicability_settings.ContentApplicabilitySettings]:
        """
        Gets the contentApplicability property value. Settings for governing whether content is applicable to a device.
        Returns: Optional[content_applicability_settings.ContentApplicabilitySettings]
        """
        return self._content_applicability
    
    @content_applicability.setter
    def content_applicability(self,value: Optional[content_applicability_settings.ContentApplicabilitySettings] = None) -> None:
        """
        Sets the contentApplicability property value. Settings for governing whether content is applicable to a device.
        Args:
            value: Value to set for the content_applicability property.
        """
        self._content_applicability = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeploymentSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeploymentSettings()
    
    @property
    def expedite(self,) -> Optional[expedite_settings.ExpediteSettings]:
        """
        Gets the expedite property value. Settings for governing whether updates should be expedited.
        Returns: Optional[expedite_settings.ExpediteSettings]
        """
        return self._expedite
    
    @expedite.setter
    def expedite(self,value: Optional[expedite_settings.ExpediteSettings] = None) -> None:
        """
        Sets the expedite property value. Settings for governing whether updates should be expedited.
        Args:
            value: Value to set for the expedite property.
        """
        self._expedite = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import content_applicability_settings, expedite_settings, monitoring_settings, schedule_settings, user_experience_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "contentApplicability": lambda n : setattr(self, 'content_applicability', n.get_object_value(content_applicability_settings.ContentApplicabilitySettings)),
            "expedite": lambda n : setattr(self, 'expedite', n.get_object_value(expedite_settings.ExpediteSettings)),
            "monitoring": lambda n : setattr(self, 'monitoring', n.get_object_value(monitoring_settings.MonitoringSettings)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(schedule_settings.ScheduleSettings)),
            "userExperience": lambda n : setattr(self, 'user_experience', n.get_object_value(user_experience_settings.UserExperienceSettings)),
        }
        return fields
    
    @property
    def monitoring(self,) -> Optional[monitoring_settings.MonitoringSettings]:
        """
        Gets the monitoring property value. Settings for governing conditions to monitor and automated actions to take.
        Returns: Optional[monitoring_settings.MonitoringSettings]
        """
        return self._monitoring
    
    @monitoring.setter
    def monitoring(self,value: Optional[monitoring_settings.MonitoringSettings] = None) -> None:
        """
        Sets the monitoring property value. Settings for governing conditions to monitor and automated actions to take.
        Args:
            value: Value to set for the monitoring property.
        """
        self._monitoring = value
    
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
    
    @property
    def schedule(self,) -> Optional[schedule_settings.ScheduleSettings]:
        """
        Gets the schedule property value. Settings for governing how and when the content is rolled out.
        Returns: Optional[schedule_settings.ScheduleSettings]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[schedule_settings.ScheduleSettings] = None) -> None:
        """
        Sets the schedule property value. Settings for governing how and when the content is rolled out.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("contentApplicability", self.content_applicability)
        writer.write_object_value("expedite", self.expedite)
        writer.write_object_value("monitoring", self.monitoring)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("userExperience", self.user_experience)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_experience(self,) -> Optional[user_experience_settings.UserExperienceSettings]:
        """
        Gets the userExperience property value. Settings for governing end user update experience.
        Returns: Optional[user_experience_settings.UserExperienceSettings]
        """
        return self._user_experience
    
    @user_experience.setter
    def user_experience(self,value: Optional[user_experience_settings.UserExperienceSettings] = None) -> None:
        """
        Sets the userExperience property value. Settings for governing end user update experience.
        Args:
            value: Value to set for the user_experience property.
        """
        self._user_experience = value
    

