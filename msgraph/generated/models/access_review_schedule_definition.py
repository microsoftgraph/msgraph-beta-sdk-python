from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_instance, access_review_notification_recipient_item, access_review_reviewer_scope, access_review_schedule_settings, access_review_scope, access_review_stage_settings, entity, user_identity

from . import entity

class AccessReviewScheduleDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewScheduleDefinition and sets the default values.
        """
        super().__init__()
        # Defines the list of additional users or group members to be notified of the access review progress.
        self._additional_notification_recipients: Optional[List[access_review_notification_recipient_item.AccessReviewNotificationRecipientItem]] = None
        # The backupReviewers property
        self._backup_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # User who created this review. Read-only.
        self._created_by: Optional[user_identity.UserIdentity] = None
        # Timestamp when the access review series was created. Supports $select. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Description provided by review creators to provide more context of the review to admins. Supports $select.
        self._description_for_admins: Optional[str] = None
        # Description provided  by review creators to provide more context of the review to reviewers. Reviewers will see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.
        self._description_for_reviewers: Optional[str] = None
        # Name of the access review series. Supports $select and $orderBy. Required on create.
        self._display_name: Optional[str] = None
        # This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.
        self._fallback_reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group will become a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.
        self._instance_enumeration_scope: Optional[access_review_scope.AccessReviewScope] = None
        # Set of access reviews instances for this access review series. Access reviews that do not recur will only have one instance; otherwise, there is an instance for each recurrence.
        self._instances: Optional[List[access_review_instance.AccessReviewInstance]] = None
        # Timestamp when the access review series was last modified. Supports $select. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.
        self._reviewers: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None
        # Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.
        self._scope: Optional[access_review_scope.AccessReviewScope] = None
        # The settings for an access review series, see type definition below. Supports $select. Required on create.
        self._settings: Optional[access_review_schedule_settings.AccessReviewScheduleSettings] = None
        # Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages will be created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.
        self._stage_settings: Optional[List[access_review_stage_settings.AccessReviewStageSettings]] = None
        # This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.
        self._status: Optional[str] = None
    
    @property
    def additional_notification_recipients(self,) -> Optional[List[access_review_notification_recipient_item.AccessReviewNotificationRecipientItem]]:
        """
        Gets the additionalNotificationRecipients property value. Defines the list of additional users or group members to be notified of the access review progress.
        Returns: Optional[List[access_review_notification_recipient_item.AccessReviewNotificationRecipientItem]]
        """
        return self._additional_notification_recipients
    
    @additional_notification_recipients.setter
    def additional_notification_recipients(self,value: Optional[List[access_review_notification_recipient_item.AccessReviewNotificationRecipientItem]] = None) -> None:
        """
        Sets the additionalNotificationRecipients property value. Defines the list of additional users or group members to be notified of the access review progress.
        Args:
            value: Value to set for the additional_notification_recipients property.
        """
        self._additional_notification_recipients = value
    
    @property
    def backup_reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the backupReviewers property value. The backupReviewers property
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._backup_reviewers
    
    @backup_reviewers.setter
    def backup_reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the backupReviewers property value. The backupReviewers property
        Args:
            value: Value to set for the backup_reviewers property.
        """
        self._backup_reviewers = value
    
    @property
    def created_by(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the createdBy property value. User who created this review. Read-only.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the createdBy property value. User who created this review. Read-only.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp when the access review series was created. Supports $select. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp when the access review series was created. Supports $select. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewScheduleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewScheduleDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewScheduleDefinition()
    
    @property
    def description_for_admins(self,) -> Optional[str]:
        """
        Gets the descriptionForAdmins property value. Description provided by review creators to provide more context of the review to admins. Supports $select.
        Returns: Optional[str]
        """
        return self._description_for_admins
    
    @description_for_admins.setter
    def description_for_admins(self,value: Optional[str] = None) -> None:
        """
        Sets the descriptionForAdmins property value. Description provided by review creators to provide more context of the review to admins. Supports $select.
        Args:
            value: Value to set for the description_for_admins property.
        """
        self._description_for_admins = value
    
    @property
    def description_for_reviewers(self,) -> Optional[str]:
        """
        Gets the descriptionForReviewers property value. Description provided  by review creators to provide more context of the review to reviewers. Reviewers will see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.
        Returns: Optional[str]
        """
        return self._description_for_reviewers
    
    @description_for_reviewers.setter
    def description_for_reviewers(self,value: Optional[str] = None) -> None:
        """
        Sets the descriptionForReviewers property value. Description provided  by review creators to provide more context of the review to reviewers. Reviewers will see this description in the email sent to them requesting their review. Email notifications support up to 256 characters. Supports $select.
        Args:
            value: Value to set for the description_for_reviewers property.
        """
        self._description_for_reviewers = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Name of the access review series. Supports $select and $orderBy. Required on create.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Name of the access review series. Supports $select and $orderBy. Required on create.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def fallback_reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the fallbackReviewers property value. This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._fallback_reviewers
    
    @fallback_reviewers.setter
    def fallback_reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the fallbackReviewers property value. This collection of reviewer scopes is used to define the list of fallback reviewers. These fallback reviewers will be notified to take action if no users are found from the list of reviewers specified. This could occur when either the group owner is specified as the reviewer but the group owner does not exist, or manager is specified as reviewer but a user's manager does not exist. See accessReviewReviewerScope. Replaces backupReviewers. Supports $select. NOTE: The value of this property will be ignored if fallback reviewers are assigned through the stageSettings property.
        Args:
            value: Value to set for the fallback_reviewers property.
        """
        self._fallback_reviewers = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_instance, access_review_notification_recipient_item, access_review_reviewer_scope, access_review_schedule_settings, access_review_scope, access_review_stage_settings, entity, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalNotificationRecipients": lambda n : setattr(self, 'additional_notification_recipients', n.get_collection_of_object_values(access_review_notification_recipient_item.AccessReviewNotificationRecipientItem)),
            "backupReviewers": lambda n : setattr(self, 'backup_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(user_identity.UserIdentity)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "descriptionForAdmins": lambda n : setattr(self, 'description_for_admins', n.get_str_value()),
            "descriptionForReviewers": lambda n : setattr(self, 'description_for_reviewers', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "fallbackReviewers": lambda n : setattr(self, 'fallback_reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "instances": lambda n : setattr(self, 'instances', n.get_collection_of_object_values(access_review_instance.AccessReviewInstance)),
            "instanceEnumerationScope": lambda n : setattr(self, 'instance_enumeration_scope', n.get_object_value(access_review_scope.AccessReviewScope)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "reviewers": lambda n : setattr(self, 'reviewers', n.get_collection_of_object_values(access_review_reviewer_scope.AccessReviewReviewerScope)),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(access_review_scope.AccessReviewScope)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(access_review_schedule_settings.AccessReviewScheduleSettings)),
            "stageSettings": lambda n : setattr(self, 'stage_settings', n.get_collection_of_object_values(access_review_stage_settings.AccessReviewStageSettings)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def instance_enumeration_scope(self,) -> Optional[access_review_scope.AccessReviewScope]:
        """
        Gets the instanceEnumerationScope property value. This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group will become a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.
        Returns: Optional[access_review_scope.AccessReviewScope]
        """
        return self._instance_enumeration_scope
    
    @instance_enumeration_scope.setter
    def instance_enumeration_scope(self,value: Optional[access_review_scope.AccessReviewScope] = None) -> None:
        """
        Sets the instanceEnumerationScope property value. This property is required when scoping a review to guest users' access across all Microsoft 365 groups and determines which Microsoft 365 groups are reviewed. Each group will become a unique accessReviewInstance of the access review series.  For supported scopes, see accessReviewScope. Supports $select. For examples of options for configuring instanceEnumerationScope, see Configure the scope of your access review definition using the Microsoft Graph API.
        Args:
            value: Value to set for the instance_enumeration_scope property.
        """
        self._instance_enumeration_scope = value
    
    @property
    def instances(self,) -> Optional[List[access_review_instance.AccessReviewInstance]]:
        """
        Gets the instances property value. Set of access reviews instances for this access review series. Access reviews that do not recur will only have one instance; otherwise, there is an instance for each recurrence.
        Returns: Optional[List[access_review_instance.AccessReviewInstance]]
        """
        return self._instances
    
    @instances.setter
    def instances(self,value: Optional[List[access_review_instance.AccessReviewInstance]] = None) -> None:
        """
        Sets the instances property value. Set of access reviews instances for this access review series. Access reviews that do not recur will only have one instance; otherwise, there is an instance for each recurrence.
        Args:
            value: Value to set for the instances property.
        """
        self._instances = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Timestamp when the access review series was last modified. Supports $select. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Timestamp when the access review series was last modified. Supports $select. Read-only.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def reviewers(self,) -> Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]:
        """
        Gets the reviewers property value. This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.
        Returns: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]]
        """
        return self._reviewers
    
    @reviewers.setter
    def reviewers(self,value: Optional[List[access_review_reviewer_scope.AccessReviewReviewerScope]] = None) -> None:
        """
        Sets the reviewers property value. This collection of access review scopes is used to define who are the reviewers. The reviewers property is only updatable if individual users are assigned as reviewers. Required on create. Supports $select. For examples of options for assigning reviewers, see Assign reviewers to your access review definition using the Microsoft Graph API. NOTE: The value of this property will be ignored if reviewers are assigned through the stageSettings property.
        Args:
            value: Value to set for the reviewers property.
        """
        self._reviewers = value
    
    @property
    def scope(self,) -> Optional[access_review_scope.AccessReviewScope]:
        """
        Gets the scope property value. Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.
        Returns: Optional[access_review_scope.AccessReviewScope]
        """
        return self._scope
    
    @scope.setter
    def scope(self,value: Optional[access_review_scope.AccessReviewScope] = None) -> None:
        """
        Sets the scope property value. Defines the entities whose access is reviewed. For supported scopes, see accessReviewScope. Required on create. Supports $select and $filter (contains only). For examples of options for configuring scope, see Configure the scope of your access review definition using the Microsoft Graph API.
        Args:
            value: Value to set for the scope property.
        """
        self._scope = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("additionalNotificationRecipients", self.additional_notification_recipients)
        writer.write_collection_of_object_values("backupReviewers", self.backup_reviewers)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("descriptionForAdmins", self.description_for_admins)
        writer.write_str_value("descriptionForReviewers", self.description_for_reviewers)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("fallbackReviewers", self.fallback_reviewers)
        writer.write_collection_of_object_values("instances", self.instances)
        writer.write_object_value("instanceEnumerationScope", self.instance_enumeration_scope)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("reviewers", self.reviewers)
        writer.write_object_value("scope", self.scope)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("stageSettings", self.stage_settings)
        writer.write_str_value("status", self.status)
    
    @property
    def settings(self,) -> Optional[access_review_schedule_settings.AccessReviewScheduleSettings]:
        """
        Gets the settings property value. The settings for an access review series, see type definition below. Supports $select. Required on create.
        Returns: Optional[access_review_schedule_settings.AccessReviewScheduleSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[access_review_schedule_settings.AccessReviewScheduleSettings] = None) -> None:
        """
        Sets the settings property value. The settings for an access review series, see type definition below. Supports $select. Required on create.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def stage_settings(self,) -> Optional[List[access_review_stage_settings.AccessReviewStageSettings]]:
        """
        Gets the stageSettings property value. Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages will be created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.
        Returns: Optional[List[access_review_stage_settings.AccessReviewStageSettings]]
        """
        return self._stage_settings
    
    @stage_settings.setter
    def stage_settings(self,value: Optional[List[access_review_stage_settings.AccessReviewStageSettings]] = None) -> None:
        """
        Sets the stageSettings property value. Required only for a multi-stage access review to define the stages and their settings. You can break down each review instance into up to three sequential stages, where each stage can have a different set of reviewers, fallback reviewers, and settings. Stages will be created sequentially based on the dependsOn property. Optional.  When this property is defined, its settings are used instead of the corresponding settings in the accessReviewScheduleDefinition object and its settings, reviewers, and fallbackReviewers properties.
        Args:
            value: Value to set for the stage_settings property.
        """
        self._stage_settings = value
    
    @property
    def status(self,) -> Optional[str]:
        """
        Gets the status property value. This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.
        Returns: Optional[str]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[str] = None) -> None:
        """
        Sets the status property value. This read-only field specifies the status of an access review. The typical states include Initializing, NotStarted, Starting, InProgress, Completing, Completed, AutoReviewing, and AutoReviewed.  Supports $select, $orderby, and $filter (eq only). Read-only.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

