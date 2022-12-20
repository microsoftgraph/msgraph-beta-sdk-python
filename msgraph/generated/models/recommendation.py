from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

action_step = lazy_import('msgraph.generated.models.action_step')
entity = lazy_import('msgraph.generated.models.entity')
recommendation_category = lazy_import('msgraph.generated.models.recommendation_category')
recommendation_priority = lazy_import('msgraph.generated.models.recommendation_priority')
recommendation_resource = lazy_import('msgraph.generated.models.recommendation_resource')
recommendation_status = lazy_import('msgraph.generated.models.recommendation_status')

class Recommendation(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def action_steps(self,) -> Optional[List[action_step.ActionStep]]:
        """
        Gets the actionSteps property value. The actionSteps property
        Returns: Optional[List[action_step.ActionStep]]
        """
        return self._action_steps
    
    @action_steps.setter
    def action_steps(self,value: Optional[List[action_step.ActionStep]] = None) -> None:
        """
        Sets the actionSteps property value. The actionSteps property
        Args:
            value: Value to set for the actionSteps property.
        """
        self._action_steps = value
    
    @property
    def benefits(self,) -> Optional[str]:
        """
        Gets the benefits property value. The benefits property
        Returns: Optional[str]
        """
        return self._benefits
    
    @benefits.setter
    def benefits(self,value: Optional[str] = None) -> None:
        """
        Sets the benefits property value. The benefits property
        Args:
            value: Value to set for the benefits property.
        """
        self._benefits = value
    
    @property
    def category(self,) -> Optional[recommendation_category.RecommendationCategory]:
        """
        Gets the category property value. The category property
        Returns: Optional[recommendation_category.RecommendationCategory]
        """
        return self._category
    
    @category.setter
    def category(self,value: Optional[recommendation_category.RecommendationCategory] = None) -> None:
        """
        Sets the category property value. The category property
        Args:
            value: Value to set for the category property.
        """
        self._category = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new recommendation and sets the default values.
        """
        super().__init__()
        # The actionSteps property
        self._action_steps: Optional[List[action_step.ActionStep]] = None
        # The benefits property
        self._benefits: Optional[str] = None
        # The category property
        self._category: Optional[recommendation_category.RecommendationCategory] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The impactedResources property
        self._impacted_resources: Optional[List[recommendation_resource.RecommendationResource]] = None
        # The impactStartDateTime property
        self._impact_start_date_time: Optional[datetime] = None
        # The impactType property
        self._impact_type: Optional[str] = None
        # The insights property
        self._insights: Optional[str] = None
        # The lastCheckedDateTime property
        self._last_checked_date_time: Optional[datetime] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[str] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The postponeUntilDateTime property
        self._postpone_until_date_time: Optional[datetime] = None
        # The priority property
        self._priority: Optional[recommendation_priority.RecommendationPriority] = None
        # The status property
        self._status: Optional[recommendation_status.RecommendationStatus] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Recommendation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Recommendation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Recommendation()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action_steps": lambda n : setattr(self, 'action_steps', n.get_collection_of_object_values(action_step.ActionStep)),
            "benefits": lambda n : setattr(self, 'benefits', n.get_str_value()),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(recommendation_category.RecommendationCategory)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "impacted_resources": lambda n : setattr(self, 'impacted_resources', n.get_collection_of_object_values(recommendation_resource.RecommendationResource)),
            "impact_start_date_time": lambda n : setattr(self, 'impact_start_date_time', n.get_datetime_value()),
            "impact_type": lambda n : setattr(self, 'impact_type', n.get_str_value()),
            "insights": lambda n : setattr(self, 'insights', n.get_str_value()),
            "last_checked_date_time": lambda n : setattr(self, 'last_checked_date_time', n.get_datetime_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "postpone_until_date_time": lambda n : setattr(self, 'postpone_until_date_time', n.get_datetime_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_enum_value(recommendation_priority.RecommendationPriority)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(recommendation_status.RecommendationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def impacted_resources(self,) -> Optional[List[recommendation_resource.RecommendationResource]]:
        """
        Gets the impactedResources property value. The impactedResources property
        Returns: Optional[List[recommendation_resource.RecommendationResource]]
        """
        return self._impacted_resources
    
    @impacted_resources.setter
    def impacted_resources(self,value: Optional[List[recommendation_resource.RecommendationResource]] = None) -> None:
        """
        Sets the impactedResources property value. The impactedResources property
        Args:
            value: Value to set for the impactedResources property.
        """
        self._impacted_resources = value
    
    @property
    def impact_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the impactStartDateTime property value. The impactStartDateTime property
        Returns: Optional[datetime]
        """
        return self._impact_start_date_time
    
    @impact_start_date_time.setter
    def impact_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the impactStartDateTime property value. The impactStartDateTime property
        Args:
            value: Value to set for the impactStartDateTime property.
        """
        self._impact_start_date_time = value
    
    @property
    def impact_type(self,) -> Optional[str]:
        """
        Gets the impactType property value. The impactType property
        Returns: Optional[str]
        """
        return self._impact_type
    
    @impact_type.setter
    def impact_type(self,value: Optional[str] = None) -> None:
        """
        Sets the impactType property value. The impactType property
        Args:
            value: Value to set for the impactType property.
        """
        self._impact_type = value
    
    @property
    def insights(self,) -> Optional[str]:
        """
        Gets the insights property value. The insights property
        Returns: Optional[str]
        """
        return self._insights
    
    @insights.setter
    def insights(self,value: Optional[str] = None) -> None:
        """
        Sets the insights property value. The insights property
        Args:
            value: Value to set for the insights property.
        """
        self._insights = value
    
    @property
    def last_checked_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastCheckedDateTime property value. The lastCheckedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_checked_date_time
    
    @last_checked_date_time.setter
    def last_checked_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastCheckedDateTime property value. The lastCheckedDateTime property
        Args:
            value: Value to set for the lastCheckedDateTime property.
        """
        self._last_checked_date_time = value
    
    @property
    def last_modified_by(self,) -> Optional[str]:
        """
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[str]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModifiedBy property value. The lastModifiedBy property
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The lastModifiedDateTime property
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def postpone_until_date_time(self,) -> Optional[datetime]:
        """
        Gets the postponeUntilDateTime property value. The postponeUntilDateTime property
        Returns: Optional[datetime]
        """
        return self._postpone_until_date_time
    
    @postpone_until_date_time.setter
    def postpone_until_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the postponeUntilDateTime property value. The postponeUntilDateTime property
        Args:
            value: Value to set for the postponeUntilDateTime property.
        """
        self._postpone_until_date_time = value
    
    @property
    def priority(self,) -> Optional[recommendation_priority.RecommendationPriority]:
        """
        Gets the priority property value. The priority property
        Returns: Optional[recommendation_priority.RecommendationPriority]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[recommendation_priority.RecommendationPriority] = None) -> None:
        """
        Sets the priority property value. The priority property
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("actionSteps", self.action_steps)
        writer.write_str_value("benefits", self.benefits)
        writer.write_enum_value("category", self.category)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("impactedResources", self.impacted_resources)
        writer.write_datetime_value("impactStartDateTime", self.impact_start_date_time)
        writer.write_str_value("impactType", self.impact_type)
        writer.write_str_value("insights", self.insights)
        writer.write_datetime_value("lastCheckedDateTime", self.last_checked_date_time)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("postponeUntilDateTime", self.postpone_until_date_time)
        writer.write_enum_value("priority", self.priority)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[recommendation_status.RecommendationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[recommendation_status.RecommendationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[recommendation_status.RecommendationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

