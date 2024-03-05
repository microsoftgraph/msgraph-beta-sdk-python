from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_target_content import AccountTargetContent
    from .campaign_schedule import CampaignSchedule
    from .email_identity import EmailIdentity
    from .end_user_notification_setting import EndUserNotificationSetting
    from .entity import Entity
    from .training_campaign_report import TrainingCampaignReport
    from .training_setting import TrainingSetting

from .entity import Entity

@dataclass
class TrainingCampaign(Entity):
    # The campaignSchedule property
    campaign_schedule: Optional[CampaignSchedule] = None
    # The createdBy property
    created_by: Optional[EmailIdentity] = None
    # The createdDateTime property
    created_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The endUserNotificationSetting property
    end_user_notification_setting: Optional[EndUserNotificationSetting] = None
    # The excludedAccountTarget property
    excluded_account_target: Optional[AccountTargetContent] = None
    # The includedAccountTarget property
    included_account_target: Optional[AccountTargetContent] = None
    # The lastModifiedBy property
    last_modified_by: Optional[EmailIdentity] = None
    # The lastModifiedDateTime property
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The report property
    report: Optional[TrainingCampaignReport] = None
    # The trainingSetting property
    training_setting: Optional[TrainingSetting] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TrainingCampaign:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingCampaign
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return TrainingCampaign()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .account_target_content import AccountTargetContent
        from .campaign_schedule import CampaignSchedule
        from .email_identity import EmailIdentity
        from .end_user_notification_setting import EndUserNotificationSetting
        from .entity import Entity
        from .training_campaign_report import TrainingCampaignReport
        from .training_setting import TrainingSetting

        from .account_target_content import AccountTargetContent
        from .campaign_schedule import CampaignSchedule
        from .email_identity import EmailIdentity
        from .end_user_notification_setting import EndUserNotificationSetting
        from .entity import Entity
        from .training_campaign_report import TrainingCampaignReport
        from .training_setting import TrainingSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "campaignSchedule": lambda n : setattr(self, 'campaign_schedule', n.get_object_value(CampaignSchedule)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmailIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endUserNotificationSetting": lambda n : setattr(self, 'end_user_notification_setting', n.get_object_value(EndUserNotificationSetting)),
            "excludedAccountTarget": lambda n : setattr(self, 'excluded_account_target', n.get_object_value(AccountTargetContent)),
            "includedAccountTarget": lambda n : setattr(self, 'included_account_target', n.get_object_value(AccountTargetContent)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(EmailIdentity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "report": lambda n : setattr(self, 'report', n.get_object_value(TrainingCampaignReport)),
            "trainingSetting": lambda n : setattr(self, 'training_setting', n.get_object_value(TrainingSetting)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("campaignSchedule", self.campaign_schedule)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("endUserNotificationSetting", self.end_user_notification_setting)
        writer.write_object_value("excludedAccountTarget", self.excluded_account_target)
        writer.write_object_value("includedAccountTarget", self.included_account_target)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("report", self.report)
        writer.write_object_value("trainingSetting", self.training_setting)
    

