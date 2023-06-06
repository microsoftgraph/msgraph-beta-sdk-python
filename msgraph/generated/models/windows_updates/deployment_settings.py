from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import content_applicability_settings, expedite_settings, monitoring_settings, schedule_settings, user_experience_settings

@dataclass
class DeploymentSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Settings for governing whether content is applicable to a device.
    content_applicability: Optional[content_applicability_settings.ContentApplicabilitySettings] = None
    # Settings for governing whether updates should be expedited.
    expedite: Optional[expedite_settings.ExpediteSettings] = None
    # Settings for governing conditions to monitor and automated actions to take.
    monitoring: Optional[monitoring_settings.MonitoringSettings] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Settings for governing how and when the content is rolled out.
    schedule: Optional[schedule_settings.ScheduleSettings] = None
    # Settings for governing end user update experience.
    user_experience: Optional[user_experience_settings.UserExperienceSettings] = None
    
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
    

