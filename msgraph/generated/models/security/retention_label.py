from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
action_after_retention_period = lazy_import('msgraph.generated.models.security.action_after_retention_period')
behavior_during_retention_period = lazy_import('msgraph.generated.models.security.behavior_during_retention_period')
default_record_behavior = lazy_import('msgraph.generated.models.security.default_record_behavior')
disposition_review_stage = lazy_import('msgraph.generated.models.security.disposition_review_stage')
retention_duration = lazy_import('msgraph.generated.models.security.retention_duration')
retention_event_type = lazy_import('msgraph.generated.models.security.retention_event_type')
retention_trigger = lazy_import('msgraph.generated.models.security.retention_trigger')

class RetentionLabel(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def action_after_retention_period(self,) -> Optional[action_after_retention_period.ActionAfterRetentionPeriod]:
        """
        Gets the actionAfterRetentionPeriod property value. Specifies the action to take on a document with this label applied during the retention period. The possible values are: none, delete, startDispositionReview, unknownFutureValue.
        Returns: Optional[action_after_retention_period.ActionAfterRetentionPeriod]
        """
        return self._action_after_retention_period
    
    @action_after_retention_period.setter
    def action_after_retention_period(self,value: Optional[action_after_retention_period.ActionAfterRetentionPeriod] = None) -> None:
        """
        Sets the actionAfterRetentionPeriod property value. Specifies the action to take on a document with this label applied during the retention period. The possible values are: none, delete, startDispositionReview, unknownFutureValue.
        Args:
            value: Value to set for the actionAfterRetentionPeriod property.
        """
        self._action_after_retention_period = value
    
    @property
    def behavior_during_retention_period(self,) -> Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod]:
        """
        Gets the behaviorDuringRetentionPeriod property value. Specifies how the behavior of a document with this label should be during the retention period. The possible values are: doNotRetain, retain, retainAsRecord, retainAsRegulatoryRecord, unknownFutureValue.
        Returns: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod]
        """
        return self._behavior_during_retention_period
    
    @behavior_during_retention_period.setter
    def behavior_during_retention_period(self,value: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod] = None) -> None:
        """
        Sets the behaviorDuringRetentionPeriod property value. Specifies how the behavior of a document with this label should be during the retention period. The possible values are: doNotRetain, retain, retainAsRecord, retainAsRegulatoryRecord, unknownFutureValue.
        Args:
            value: Value to set for the behaviorDuringRetentionPeriod property.
        """
        self._behavior_during_retention_period = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new retentionLabel and sets the default values.
        """
        super().__init__()
        # Specifies the action to take on a document with this label applied during the retention period. The possible values are: none, delete, startDispositionReview, unknownFutureValue.
        self._action_after_retention_period: Optional[action_after_retention_period.ActionAfterRetentionPeriod] = None
        # Specifies how the behavior of a document with this label should be during the retention period. The possible values are: doNotRetain, retain, retainAsRecord, retainAsRegulatoryRecord, unknownFutureValue.
        self._behavior_during_retention_period: Optional[behavior_during_retention_period.BehaviorDuringRetentionPeriod] = None
        # Represents the user who created the retentionLabel.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Represents the date and time in which the retentionLabel is created.
        self._created_date_time: Optional[datetime] = None
        # Specifies the locked or unlocked state of a record label when it is created.The possible values are: startLocked, startUnlocked, unknownFutureValue.
        self._default_record_behavior: Optional[default_record_behavior.DefaultRecordBehavior] = None
        # Provides label information for the admin. Optional.
        self._description_for_admins: Optional[str] = None
        # Provides the label information for the user. Optional.
        self._description_for_users: Optional[str] = None
        # Unique string that defines a label name.
        self._display_name: Optional[str] = None
        # Review stages during which reviewers are notified to determine whether a document must be deleted or retained.
        self._disposition_review_stages: Optional[List[disposition_review_stage.DispositionReviewStage]] = None
        # Specifies whether the label is currently being used.
        self._is_in_use: Optional[bool] = None
        # Specifies the replacement label to be applied automatically after the retention period of the current label ends.
        self._label_to_be_applied: Optional[str] = None
        # The user who last modified the retentionLabel.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The latest date time when the retentionLabel was modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Specifies the number of days to retain the content.
        self._retention_duration: Optional[retention_duration.RetentionDuration] = None
        # The retentionEventType property
        self._retention_event_type: Optional[retention_event_type.RetentionEventType] = None
        # Specifies whether the retention duration is calculated from the content creation date, labeled date, or last modification date. The possible values are: dateLabeled, dateCreated, dateModified, dateOfEvent, unknownFutureValue.
        self._retention_trigger: Optional[retention_trigger.RetentionTrigger] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Represents the user who created the retentionLabel.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Represents the user who created the retentionLabel.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Represents the date and time in which the retentionLabel is created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Represents the date and time in which the retentionLabel is created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RetentionLabel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RetentionLabel
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RetentionLabel()
    
    @property
    def default_record_behavior(self,) -> Optional[default_record_behavior.DefaultRecordBehavior]:
        """
        Gets the defaultRecordBehavior property value. Specifies the locked or unlocked state of a record label when it is created.The possible values are: startLocked, startUnlocked, unknownFutureValue.
        Returns: Optional[default_record_behavior.DefaultRecordBehavior]
        """
        return self._default_record_behavior
    
    @default_record_behavior.setter
    def default_record_behavior(self,value: Optional[default_record_behavior.DefaultRecordBehavior] = None) -> None:
        """
        Sets the defaultRecordBehavior property value. Specifies the locked or unlocked state of a record label when it is created.The possible values are: startLocked, startUnlocked, unknownFutureValue.
        Args:
            value: Value to set for the defaultRecordBehavior property.
        """
        self._default_record_behavior = value
    
    @property
    def description_for_admins(self,) -> Optional[str]:
        """
        Gets the descriptionForAdmins property value. Provides label information for the admin. Optional.
        Returns: Optional[str]
        """
        return self._description_for_admins
    
    @description_for_admins.setter
    def description_for_admins(self,value: Optional[str] = None) -> None:
        """
        Sets the descriptionForAdmins property value. Provides label information for the admin. Optional.
        Args:
            value: Value to set for the descriptionForAdmins property.
        """
        self._description_for_admins = value
    
    @property
    def description_for_users(self,) -> Optional[str]:
        """
        Gets the descriptionForUsers property value. Provides the label information for the user. Optional.
        Returns: Optional[str]
        """
        return self._description_for_users
    
    @description_for_users.setter
    def description_for_users(self,value: Optional[str] = None) -> None:
        """
        Sets the descriptionForUsers property value. Provides the label information for the user. Optional.
        Args:
            value: Value to set for the descriptionForUsers property.
        """
        self._description_for_users = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Unique string that defines a label name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Unique string that defines a label name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def disposition_review_stages(self,) -> Optional[List[disposition_review_stage.DispositionReviewStage]]:
        """
        Gets the dispositionReviewStages property value. Review stages during which reviewers are notified to determine whether a document must be deleted or retained.
        Returns: Optional[List[disposition_review_stage.DispositionReviewStage]]
        """
        return self._disposition_review_stages
    
    @disposition_review_stages.setter
    def disposition_review_stages(self,value: Optional[List[disposition_review_stage.DispositionReviewStage]] = None) -> None:
        """
        Sets the dispositionReviewStages property value. Review stages during which reviewers are notified to determine whether a document must be deleted or retained.
        Args:
            value: Value to set for the dispositionReviewStages property.
        """
        self._disposition_review_stages = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_after_retention_period": lambda n : setattr(self, 'action_after_retention_period', n.get_enum_value(action_after_retention_period.ActionAfterRetentionPeriod)),
            "behavior_during_retention_period": lambda n : setattr(self, 'behavior_during_retention_period', n.get_enum_value(behavior_during_retention_period.BehaviorDuringRetentionPeriod)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "default_record_behavior": lambda n : setattr(self, 'default_record_behavior', n.get_enum_value(default_record_behavior.DefaultRecordBehavior)),
            "description_for_admins": lambda n : setattr(self, 'description_for_admins', n.get_str_value()),
            "description_for_users": lambda n : setattr(self, 'description_for_users', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "disposition_review_stages": lambda n : setattr(self, 'disposition_review_stages', n.get_collection_of_object_values(disposition_review_stage.DispositionReviewStage)),
            "is_in_use": lambda n : setattr(self, 'is_in_use', n.get_bool_value()),
            "label_to_be_applied": lambda n : setattr(self, 'label_to_be_applied', n.get_str_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "retention_duration": lambda n : setattr(self, 'retention_duration', n.get_object_value(retention_duration.RetentionDuration)),
            "retention_event_type": lambda n : setattr(self, 'retention_event_type', n.get_object_value(retention_event_type.RetentionEventType)),
            "retention_trigger": lambda n : setattr(self, 'retention_trigger', n.get_enum_value(retention_trigger.RetentionTrigger)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_in_use(self,) -> Optional[bool]:
        """
        Gets the isInUse property value. Specifies whether the label is currently being used.
        Returns: Optional[bool]
        """
        return self._is_in_use
    
    @is_in_use.setter
    def is_in_use(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInUse property value. Specifies whether the label is currently being used.
        Args:
            value: Value to set for the isInUse property.
        """
        self._is_in_use = value
    
    @property
    def label_to_be_applied(self,) -> Optional[str]:
        """
        Gets the labelToBeApplied property value. Specifies the replacement label to be applied automatically after the retention period of the current label ends.
        Returns: Optional[str]
        """
        return self._label_to_be_applied
    
    @label_to_be_applied.setter
    def label_to_be_applied(self,value: Optional[str] = None) -> None:
        """
        Sets the labelToBeApplied property value. Specifies the replacement label to be applied automatically after the retention period of the current label ends.
        Args:
            value: Value to set for the labelToBeApplied property.
        """
        self._label_to_be_applied = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The user who last modified the retentionLabel.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. The user who last modified the retentionLabel.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The latest date time when the retentionLabel was modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The latest date time when the retentionLabel was modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def retention_duration(self,) -> Optional[retention_duration.RetentionDuration]:
        """
        Gets the retentionDuration property value. Specifies the number of days to retain the content.
        Returns: Optional[retention_duration.RetentionDuration]
        """
        return self._retention_duration
    
    @retention_duration.setter
    def retention_duration(self,value: Optional[retention_duration.RetentionDuration] = None) -> None:
        """
        Sets the retentionDuration property value. Specifies the number of days to retain the content.
        Args:
            value: Value to set for the retentionDuration property.
        """
        self._retention_duration = value
    
    @property
    def retention_event_type(self,) -> Optional[retention_event_type.RetentionEventType]:
        """
        Gets the retentionEventType property value. The retentionEventType property
        Returns: Optional[retention_event_type.RetentionEventType]
        """
        return self._retention_event_type
    
    @retention_event_type.setter
    def retention_event_type(self,value: Optional[retention_event_type.RetentionEventType] = None) -> None:
        """
        Sets the retentionEventType property value. The retentionEventType property
        Args:
            value: Value to set for the retentionEventType property.
        """
        self._retention_event_type = value
    
    @property
    def retention_trigger(self,) -> Optional[retention_trigger.RetentionTrigger]:
        """
        Gets the retentionTrigger property value. Specifies whether the retention duration is calculated from the content creation date, labeled date, or last modification date. The possible values are: dateLabeled, dateCreated, dateModified, dateOfEvent, unknownFutureValue.
        Returns: Optional[retention_trigger.RetentionTrigger]
        """
        return self._retention_trigger
    
    @retention_trigger.setter
    def retention_trigger(self,value: Optional[retention_trigger.RetentionTrigger] = None) -> None:
        """
        Sets the retentionTrigger property value. Specifies whether the retention duration is calculated from the content creation date, labeled date, or last modification date. The possible values are: dateLabeled, dateCreated, dateModified, dateOfEvent, unknownFutureValue.
        Args:
            value: Value to set for the retentionTrigger property.
        """
        self._retention_trigger = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("actionAfterRetentionPeriod", self.action_after_retention_period)
        writer.write_enum_value("behaviorDuringRetentionPeriod", self.behavior_during_retention_period)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("defaultRecordBehavior", self.default_record_behavior)
        writer.write_str_value("descriptionForAdmins", self.description_for_admins)
        writer.write_str_value("descriptionForUsers", self.description_for_users)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("dispositionReviewStages", self.disposition_review_stages)
        writer.write_bool_value("isInUse", self.is_in_use)
        writer.write_str_value("labelToBeApplied", self.label_to_be_applied)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("retentionDuration", self.retention_duration)
        writer.write_object_value("retentionEventType", self.retention_event_type)
        writer.write_enum_value("retentionTrigger", self.retention_trigger)
    

