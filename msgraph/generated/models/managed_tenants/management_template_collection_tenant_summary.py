from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ManagementTemplateCollectionTenantSummary(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def complete_steps_count(self,) -> Optional[int]:
        """
        Gets the completeStepsCount property value. The completeStepsCount property
        Returns: Optional[int]
        """
        return self._complete_steps_count
    
    @complete_steps_count.setter
    def complete_steps_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completeStepsCount property value. The completeStepsCount property
        Args:
            value: Value to set for the completeStepsCount property.
        """
        self._complete_steps_count = value
    
    @property
    def complete_users_count(self,) -> Optional[int]:
        """
        Gets the completeUsersCount property value. The completeUsersCount property
        Returns: Optional[int]
        """
        return self._complete_users_count
    
    @complete_users_count.setter
    def complete_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completeUsersCount property value. The completeUsersCount property
        Args:
            value: Value to set for the completeUsersCount property.
        """
        self._complete_users_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplateCollectionTenantSummary and sets the default values.
        """
        super().__init__()
        # The completeStepsCount property
        self._complete_steps_count: Optional[int] = None
        # The completeUsersCount property
        self._complete_users_count: Optional[int] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The dismissedStepsCount property
        self._dismissed_steps_count: Optional[int] = None
        # The excludedUsersCount property
        self._excluded_users_count: Optional[int] = None
        # The excludedUsersDistinctCount property
        self._excluded_users_distinct_count: Optional[int] = None
        # The incompleteStepsCount property
        self._incomplete_steps_count: Optional[int] = None
        # The incompleteUsersCount property
        self._incomplete_users_count: Optional[int] = None
        # The ineligibleStepsCount property
        self._ineligible_steps_count: Optional[int] = None
        # The isComplete property
        self._is_complete: Optional[bool] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The managementTemplateCollectionDisplayName property
        self._management_template_collection_display_name: Optional[str] = None
        # The managementTemplateCollectionId property
        self._management_template_collection_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The createdByUserId property
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The createdByUserId property
        Args:
            value: Value to set for the createdByUserId property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The createdDateTime property
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The createdDateTime property
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateCollectionTenantSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateCollectionTenantSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplateCollectionTenantSummary()
    
    @property
    def dismissed_steps_count(self,) -> Optional[int]:
        """
        Gets the dismissedStepsCount property value. The dismissedStepsCount property
        Returns: Optional[int]
        """
        return self._dismissed_steps_count
    
    @dismissed_steps_count.setter
    def dismissed_steps_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dismissedStepsCount property value. The dismissedStepsCount property
        Args:
            value: Value to set for the dismissedStepsCount property.
        """
        self._dismissed_steps_count = value
    
    @property
    def excluded_users_count(self,) -> Optional[int]:
        """
        Gets the excludedUsersCount property value. The excludedUsersCount property
        Returns: Optional[int]
        """
        return self._excluded_users_count
    
    @excluded_users_count.setter
    def excluded_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the excludedUsersCount property value. The excludedUsersCount property
        Args:
            value: Value to set for the excludedUsersCount property.
        """
        self._excluded_users_count = value
    
    @property
    def excluded_users_distinct_count(self,) -> Optional[int]:
        """
        Gets the excludedUsersDistinctCount property value. The excludedUsersDistinctCount property
        Returns: Optional[int]
        """
        return self._excluded_users_distinct_count
    
    @excluded_users_distinct_count.setter
    def excluded_users_distinct_count(self,value: Optional[int] = None) -> None:
        """
        Sets the excludedUsersDistinctCount property value. The excludedUsersDistinctCount property
        Args:
            value: Value to set for the excludedUsersDistinctCount property.
        """
        self._excluded_users_distinct_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "complete_steps_count": lambda n : setattr(self, 'complete_steps_count', n.get_int_value()),
            "complete_users_count": lambda n : setattr(self, 'complete_users_count', n.get_int_value()),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dismissed_steps_count": lambda n : setattr(self, 'dismissed_steps_count', n.get_int_value()),
            "excluded_users_count": lambda n : setattr(self, 'excluded_users_count', n.get_int_value()),
            "excluded_users_distinct_count": lambda n : setattr(self, 'excluded_users_distinct_count', n.get_int_value()),
            "incomplete_steps_count": lambda n : setattr(self, 'incomplete_steps_count', n.get_int_value()),
            "incomplete_users_count": lambda n : setattr(self, 'incomplete_users_count', n.get_int_value()),
            "ineligible_steps_count": lambda n : setattr(self, 'ineligible_steps_count', n.get_int_value()),
            "is_complete": lambda n : setattr(self, 'is_complete', n.get_bool_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "management_template_collection_display_name": lambda n : setattr(self, 'management_template_collection_display_name', n.get_str_value()),
            "management_template_collection_id": lambda n : setattr(self, 'management_template_collection_id', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incomplete_steps_count(self,) -> Optional[int]:
        """
        Gets the incompleteStepsCount property value. The incompleteStepsCount property
        Returns: Optional[int]
        """
        return self._incomplete_steps_count
    
    @incomplete_steps_count.setter
    def incomplete_steps_count(self,value: Optional[int] = None) -> None:
        """
        Sets the incompleteStepsCount property value. The incompleteStepsCount property
        Args:
            value: Value to set for the incompleteStepsCount property.
        """
        self._incomplete_steps_count = value
    
    @property
    def incomplete_users_count(self,) -> Optional[int]:
        """
        Gets the incompleteUsersCount property value. The incompleteUsersCount property
        Returns: Optional[int]
        """
        return self._incomplete_users_count
    
    @incomplete_users_count.setter
    def incomplete_users_count(self,value: Optional[int] = None) -> None:
        """
        Sets the incompleteUsersCount property value. The incompleteUsersCount property
        Args:
            value: Value to set for the incompleteUsersCount property.
        """
        self._incomplete_users_count = value
    
    @property
    def ineligible_steps_count(self,) -> Optional[int]:
        """
        Gets the ineligibleStepsCount property value. The ineligibleStepsCount property
        Returns: Optional[int]
        """
        return self._ineligible_steps_count
    
    @ineligible_steps_count.setter
    def ineligible_steps_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ineligibleStepsCount property value. The ineligibleStepsCount property
        Args:
            value: Value to set for the ineligibleStepsCount property.
        """
        self._ineligible_steps_count = value
    
    @property
    def is_complete(self,) -> Optional[bool]:
        """
        Gets the isComplete property value. The isComplete property
        Returns: Optional[bool]
        """
        return self._is_complete
    
    @is_complete.setter
    def is_complete(self,value: Optional[bool] = None) -> None:
        """
        Sets the isComplete property value. The isComplete property
        Args:
            value: Value to set for the isComplete property.
        """
        self._is_complete = value
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The lastActionByUserId property
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The lastActionByUserId property
        Args:
            value: Value to set for the lastActionByUserId property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The lastActionDateTime property
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The lastActionDateTime property
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    @property
    def management_template_collection_display_name(self,) -> Optional[str]:
        """
        Gets the managementTemplateCollectionDisplayName property value. The managementTemplateCollectionDisplayName property
        Returns: Optional[str]
        """
        return self._management_template_collection_display_name
    
    @management_template_collection_display_name.setter
    def management_template_collection_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateCollectionDisplayName property value. The managementTemplateCollectionDisplayName property
        Args:
            value: Value to set for the managementTemplateCollectionDisplayName property.
        """
        self._management_template_collection_display_name = value
    
    @property
    def management_template_collection_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateCollectionId property value. The managementTemplateCollectionId property
        Returns: Optional[str]
        """
        return self._management_template_collection_id
    
    @management_template_collection_id.setter
    def management_template_collection_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateCollectionId property value. The managementTemplateCollectionId property
        Args:
            value: Value to set for the managementTemplateCollectionId property.
        """
        self._management_template_collection_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("completeStepsCount", self.complete_steps_count)
        writer.write_int_value("completeUsersCount", self.complete_users_count)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("dismissedStepsCount", self.dismissed_steps_count)
        writer.write_int_value("excludedUsersCount", self.excluded_users_count)
        writer.write_int_value("excludedUsersDistinctCount", self.excluded_users_distinct_count)
        writer.write_int_value("incompleteStepsCount", self.incomplete_steps_count)
        writer.write_int_value("incompleteUsersCount", self.incomplete_users_count)
        writer.write_int_value("ineligibleStepsCount", self.ineligible_steps_count)
        writer.write_bool_value("isComplete", self.is_complete)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("managementTemplateCollectionDisplayName", self.management_template_collection_display_name)
        writer.write_str_value("managementTemplateCollectionId", self.management_template_collection_id)
        writer.write_str_value("tenantId", self.tenant_id)
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    

