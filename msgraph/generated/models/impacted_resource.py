from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, key_value, recommendation_status

from . import entity

class ImpactedResource(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new impactedResource and sets the default values.
        """
        super().__init__()
        # The date and time when the impactedResource object was initially associated with the recommendation.
        self._added_date_time: Optional[datetime] = None
        # Additional information unique to the impactedResource to help contextualize the recommendation.
        self._additional_details: Optional[List[key_value.KeyValue]] = None
        # The URL link to the corresponding Azure AD resource.
        self._api_url: Optional[str] = None
        # Friendly name of the Azure AD resource.
        self._display_name: Optional[str] = None
        # Name of the user or service that last updated the status.
        self._last_modified_by: Optional[str] = None
        # The date and time when the status was last updated.
        self._last_modified_date_time: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The user responsible for maintaining the resource.
        self._owner: Optional[str] = None
        # The URL link to the corresponding Azure AD portal page of the resource.
        self._portal_url: Optional[str] = None
        # The future date and time when the status of a postponed impactedResource will be active again.
        self._postpone_until_date_time: Optional[datetime] = None
        # Indicates the importance of the resource. A resource with a rank equal to 1 is of the highest importance.
        self._rank: Optional[int] = None
        # The unique identifier of the recommendation that the resource is associated with.
        self._recommendation_id: Optional[str] = None
        # Indicates the type of Azure AD resource. Examples include user, application.
        self._resource_type: Optional[str] = None
        # The status property
        self._status: Optional[recommendation_status.RecommendationStatus] = None
        # The related unique identifier, depending on the resourceType. For example, this property is set to the applicationId if the resourceType is an application.
        self._subject_id: Optional[str] = None
    
    @property
    def added_date_time(self,) -> Optional[datetime]:
        """
        Gets the addedDateTime property value. The date and time when the impactedResource object was initially associated with the recommendation.
        Returns: Optional[datetime]
        """
        return self._added_date_time
    
    @added_date_time.setter
    def added_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the addedDateTime property value. The date and time when the impactedResource object was initially associated with the recommendation.
        Args:
            value: Value to set for the added_date_time property.
        """
        self._added_date_time = value
    
    @property
    def additional_details(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the additionalDetails property value. Additional information unique to the impactedResource to help contextualize the recommendation.
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the additionalDetails property value. Additional information unique to the impactedResource to help contextualize the recommendation.
        Args:
            value: Value to set for the additional_details property.
        """
        self._additional_details = value
    
    @property
    def api_url(self,) -> Optional[str]:
        """
        Gets the apiUrl property value. The URL link to the corresponding Azure AD resource.
        Returns: Optional[str]
        """
        return self._api_url
    
    @api_url.setter
    def api_url(self,value: Optional[str] = None) -> None:
        """
        Sets the apiUrl property value. The URL link to the corresponding Azure AD resource.
        Args:
            value: Value to set for the api_url property.
        """
        self._api_url = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImpactedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImpactedResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImpactedResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Friendly name of the Azure AD resource.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Friendly name of the Azure AD resource.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, key_value, recommendation_status

        fields: Dict[str, Callable[[Any], None]] = {
            "addedDateTime": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "additionalDetails": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(key_value.KeyValue)),
            "apiUrl": lambda n : setattr(self, 'api_url', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "portalUrl": lambda n : setattr(self, 'portal_url', n.get_str_value()),
            "postponeUntilDateTime": lambda n : setattr(self, 'postpone_until_date_time', n.get_datetime_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "recommendationId": lambda n : setattr(self, 'recommendation_id', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(recommendation_status.RecommendationStatus)),
            "subjectId": lambda n : setattr(self, 'subject_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[str]:
        """
        Gets the lastModifiedBy property value. Name of the user or service that last updated the status.
        Returns: Optional[str]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModifiedBy property value. Name of the user or service that last updated the status.
        Args:
            value: Value to set for the last_modified_by property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[str]:
        """
        Gets the lastModifiedDateTime property value. The date and time when the status was last updated.
        Returns: Optional[str]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[str] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time when the status was last updated.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The user responsible for maintaining the resource.
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The user responsible for maintaining the resource.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def portal_url(self,) -> Optional[str]:
        """
        Gets the portalUrl property value. The URL link to the corresponding Azure AD portal page of the resource.
        Returns: Optional[str]
        """
        return self._portal_url
    
    @portal_url.setter
    def portal_url(self,value: Optional[str] = None) -> None:
        """
        Sets the portalUrl property value. The URL link to the corresponding Azure AD portal page of the resource.
        Args:
            value: Value to set for the portal_url property.
        """
        self._portal_url = value
    
    @property
    def postpone_until_date_time(self,) -> Optional[datetime]:
        """
        Gets the postponeUntilDateTime property value. The future date and time when the status of a postponed impactedResource will be active again.
        Returns: Optional[datetime]
        """
        return self._postpone_until_date_time
    
    @postpone_until_date_time.setter
    def postpone_until_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the postponeUntilDateTime property value. The future date and time when the status of a postponed impactedResource will be active again.
        Args:
            value: Value to set for the postpone_until_date_time property.
        """
        self._postpone_until_date_time = value
    
    @property
    def rank(self,) -> Optional[int]:
        """
        Gets the rank property value. Indicates the importance of the resource. A resource with a rank equal to 1 is of the highest importance.
        Returns: Optional[int]
        """
        return self._rank
    
    @rank.setter
    def rank(self,value: Optional[int] = None) -> None:
        """
        Sets the rank property value. Indicates the importance of the resource. A resource with a rank equal to 1 is of the highest importance.
        Args:
            value: Value to set for the rank property.
        """
        self._rank = value
    
    @property
    def recommendation_id(self,) -> Optional[str]:
        """
        Gets the recommendationId property value. The unique identifier of the recommendation that the resource is associated with.
        Returns: Optional[str]
        """
        return self._recommendation_id
    
    @recommendation_id.setter
    def recommendation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendationId property value. The unique identifier of the recommendation that the resource is associated with.
        Args:
            value: Value to set for the recommendation_id property.
        """
        self._recommendation_id = value
    
    @property
    def resource_type(self,) -> Optional[str]:
        """
        Gets the resourceType property value. Indicates the type of Azure AD resource. Examples include user, application.
        Returns: Optional[str]
        """
        return self._resource_type
    
    @resource_type.setter
    def resource_type(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceType property value. Indicates the type of Azure AD resource. Examples include user, application.
        Args:
            value: Value to set for the resource_type property.
        """
        self._resource_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("addedDateTime", self.added_date_time)
        writer.write_collection_of_object_values("additionalDetails", self.additional_details)
        writer.write_str_value("apiUrl", self.api_url)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastModifiedBy", self.last_modified_by)
        writer.write_str_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("portalUrl", self.portal_url)
        writer.write_datetime_value("postponeUntilDateTime", self.postpone_until_date_time)
        writer.write_int_value("rank", self.rank)
        writer.write_str_value("recommendationId", self.recommendation_id)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subjectId", self.subject_id)
    
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
    
    @property
    def subject_id(self,) -> Optional[str]:
        """
        Gets the subjectId property value. The related unique identifier, depending on the resourceType. For example, this property is set to the applicationId if the resourceType is an application.
        Returns: Optional[str]
        """
        return self._subject_id
    
    @subject_id.setter
    def subject_id(self,value: Optional[str] = None) -> None:
        """
        Sets the subjectId property value. The related unique identifier, depending on the resourceType. For example, this property is set to the applicationId if the resourceType is an application.
        Args:
            value: Value to set for the subject_id property.
        """
        self._subject_id = value
    

