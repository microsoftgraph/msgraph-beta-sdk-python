from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
key_value = lazy_import('msgraph.generated.models.key_value')
recommendation_status = lazy_import('msgraph.generated.models.recommendation_status')

class RecommendationResource(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def added_date_time(self,) -> Optional[datetime]:
        """
        Gets the addedDateTime property value. The addedDateTime property
        Returns: Optional[datetime]
        """
        return self._added_date_time
    
    @added_date_time.setter
    def added_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the addedDateTime property value. The addedDateTime property
        Args:
            value: Value to set for the addedDateTime property.
        """
        self._added_date_time = value
    
    @property
    def additional_details(self,) -> Optional[List[key_value.KeyValue]]:
        """
        Gets the additionalDetails property value. The additionalDetails property
        Returns: Optional[List[key_value.KeyValue]]
        """
        return self._additional_details
    
    @additional_details.setter
    def additional_details(self,value: Optional[List[key_value.KeyValue]] = None) -> None:
        """
        Sets the additionalDetails property value. The additionalDetails property
        Args:
            value: Value to set for the additionalDetails property.
        """
        self._additional_details = value
    
    @property
    def api_url(self,) -> Optional[str]:
        """
        Gets the apiUrl property value. The apiUrl property
        Returns: Optional[str]
        """
        return self._api_url
    
    @api_url.setter
    def api_url(self,value: Optional[str] = None) -> None:
        """
        Sets the apiUrl property value. The apiUrl property
        Args:
            value: Value to set for the apiUrl property.
        """
        self._api_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new recommendationResource and sets the default values.
        """
        super().__init__()
        # The addedDateTime property
        self._added_date_time: Optional[datetime] = None
        # The additionalDetails property
        self._additional_details: Optional[List[key_value.KeyValue]] = None
        # The apiUrl property
        self._api_url: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The owner property
        self._owner: Optional[str] = None
        # The portalUrl property
        self._portal_url: Optional[str] = None
        # The rank property
        self._rank: Optional[int] = None
        # The recommendationId property
        self._recommendation_id: Optional[str] = None
        # The resourceType property
        self._resource_type: Optional[str] = None
        # The status property
        self._status: Optional[recommendation_status.RecommendationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RecommendationResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RecommendationResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RecommendationResource()
    
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
            "added_date_time": lambda n : setattr(self, 'added_date_time', n.get_datetime_value()),
            "additional_details": lambda n : setattr(self, 'additional_details', n.get_collection_of_object_values(key_value.KeyValue)),
            "api_url": lambda n : setattr(self, 'api_url', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "portal_url": lambda n : setattr(self, 'portal_url', n.get_str_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "recommendation_id": lambda n : setattr(self, 'recommendation_id', n.get_str_value()),
            "resource_type": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(recommendation_status.RecommendationStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def owner(self,) -> Optional[str]:
        """
        Gets the owner property value. The owner property
        Returns: Optional[str]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[str] = None) -> None:
        """
        Sets the owner property value. The owner property
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def portal_url(self,) -> Optional[str]:
        """
        Gets the portalUrl property value. The portalUrl property
        Returns: Optional[str]
        """
        return self._portal_url
    
    @portal_url.setter
    def portal_url(self,value: Optional[str] = None) -> None:
        """
        Sets the portalUrl property value. The portalUrl property
        Args:
            value: Value to set for the portalUrl property.
        """
        self._portal_url = value
    
    @property
    def rank(self,) -> Optional[int]:
        """
        Gets the rank property value. The rank property
        Returns: Optional[int]
        """
        return self._rank
    
    @rank.setter
    def rank(self,value: Optional[int] = None) -> None:
        """
        Sets the rank property value. The rank property
        Args:
            value: Value to set for the rank property.
        """
        self._rank = value
    
    @property
    def recommendation_id(self,) -> Optional[str]:
        """
        Gets the recommendationId property value. The recommendationId property
        Returns: Optional[str]
        """
        return self._recommendation_id
    
    @recommendation_id.setter
    def recommendation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the recommendationId property value. The recommendationId property
        Args:
            value: Value to set for the recommendationId property.
        """
        self._recommendation_id = value
    
    @property
    def resource_type(self,) -> Optional[str]:
        """
        Gets the resourceType property value. The resourceType property
        Returns: Optional[str]
        """
        return self._resource_type
    
    @resource_type.setter
    def resource_type(self,value: Optional[str] = None) -> None:
        """
        Sets the resourceType property value. The resourceType property
        Args:
            value: Value to set for the resourceType property.
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
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("portalUrl", self.portal_url)
        writer.write_int_value("rank", self.rank)
        writer.write_str_value("recommendationId", self.recommendation_id)
        writer.write_str_value("resourceType", self.resource_type)
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
    

