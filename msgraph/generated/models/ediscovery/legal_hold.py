from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
legal_hold_status = lazy_import('msgraph.generated.models.ediscovery.legal_hold_status')
site_source = lazy_import('msgraph.generated.models.ediscovery.site_source')
unified_group_source = lazy_import('msgraph.generated.models.ediscovery.unified_group_source')
user_source = lazy_import('msgraph.generated.models.ediscovery.user_source')

class LegalHold(entity.Entity):
    """
    Provides operations to manage the collection of accessReview entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new legalHold and sets the default values.
        """
        super().__init__()
        # KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
        self._content_query: Optional[str] = None
        # The user who created the legal hold.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The date and time the legal hold was created.
        self._created_date_time: Optional[datetime] = None
        # The legal hold description.
        self._description: Optional[str] = None
        # The display name of the legal hold.
        self._display_name: Optional[str] = None
        # Lists any errors that happened while placing the hold.
        self._errors: Optional[List[str]] = None
        # Indicates whether the hold is enabled and actively holding content.
        self._is_enabled: Optional[bool] = None
        # the user who last modified the legal hold.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The date and time the legal hold was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Data source entity for SharePoint sites associated with the legal hold.
        self._site_sources: Optional[List[site_source.SiteSource]] = None
        # The status of the legal hold. Possible values are: Pending, Error, Success, UnknownFutureValue.
        self._status: Optional[legal_hold_status.LegalHoldStatus] = None
        # The unifiedGroupSources property
        self._unified_group_sources: Optional[List[unified_group_source.UnifiedGroupSource]] = None
        # Data source entity for a the legal hold. This is the container for a mailbox and OneDrive for Business site.
        self._user_sources: Optional[List[user_source.UserSource]] = None
    
    @property
    def content_query(self,) -> Optional[str]:
        """
        Gets the contentQuery property value. KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
        Returns: Optional[str]
        """
        return self._content_query
    
    @content_query.setter
    def content_query(self,value: Optional[str] = None) -> None:
        """
        Sets the contentQuery property value. KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
        Args:
            value: Value to set for the contentQuery property.
        """
        self._content_query = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user who created the legal hold.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user who created the legal hold.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the legal hold was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the legal hold was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LegalHold:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LegalHold
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LegalHold()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The legal hold description.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The legal hold description.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the legal hold.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the legal hold.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def errors(self,) -> Optional[List[str]]:
        """
        Gets the errors property value. Lists any errors that happened while placing the hold.
        Returns: Optional[List[str]]
        """
        return self._errors
    
    @errors.setter
    def errors(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the errors property value. Lists any errors that happened while placing the hold.
        Args:
            value: Value to set for the errors property.
        """
        self._errors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "content_query": lambda n : setattr(self, 'content_query', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "site_sources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(site_source.SiteSource)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(legal_hold_status.LegalHoldStatus)),
            "unified_group_sources": lambda n : setattr(self, 'unified_group_sources', n.get_collection_of_object_values(unified_group_source.UnifiedGroupSource)),
            "user_sources": lambda n : setattr(self, 'user_sources', n.get_collection_of_object_values(user_source.UserSource)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether the hold is enabled and actively holding content.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether the hold is enabled and actively holding content.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. the user who last modified the legal hold.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. the user who last modified the legal hold.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time the legal hold was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time the legal hold was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("contentQuery", self.content_query)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_enum_value("status", self.status)
        writer.write_collection_of_object_values("unifiedGroupSources", self.unified_group_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    
    @property
    def site_sources(self,) -> Optional[List[site_source.SiteSource]]:
        """
        Gets the siteSources property value. Data source entity for SharePoint sites associated with the legal hold.
        Returns: Optional[List[site_source.SiteSource]]
        """
        return self._site_sources
    
    @site_sources.setter
    def site_sources(self,value: Optional[List[site_source.SiteSource]] = None) -> None:
        """
        Sets the siteSources property value. Data source entity for SharePoint sites associated with the legal hold.
        Args:
            value: Value to set for the siteSources property.
        """
        self._site_sources = value
    
    @property
    def status(self,) -> Optional[legal_hold_status.LegalHoldStatus]:
        """
        Gets the status property value. The status of the legal hold. Possible values are: Pending, Error, Success, UnknownFutureValue.
        Returns: Optional[legal_hold_status.LegalHoldStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[legal_hold_status.LegalHoldStatus] = None) -> None:
        """
        Sets the status property value. The status of the legal hold. Possible values are: Pending, Error, Success, UnknownFutureValue.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def unified_group_sources(self,) -> Optional[List[unified_group_source.UnifiedGroupSource]]:
        """
        Gets the unifiedGroupSources property value. The unifiedGroupSources property
        Returns: Optional[List[unified_group_source.UnifiedGroupSource]]
        """
        return self._unified_group_sources
    
    @unified_group_sources.setter
    def unified_group_sources(self,value: Optional[List[unified_group_source.UnifiedGroupSource]] = None) -> None:
        """
        Sets the unifiedGroupSources property value. The unifiedGroupSources property
        Args:
            value: Value to set for the unifiedGroupSources property.
        """
        self._unified_group_sources = value
    
    @property
    def user_sources(self,) -> Optional[List[user_source.UserSource]]:
        """
        Gets the userSources property value. Data source entity for a the legal hold. This is the container for a mailbox and OneDrive for Business site.
        Returns: Optional[List[user_source.UserSource]]
        """
        return self._user_sources
    
    @user_sources.setter
    def user_sources(self,value: Optional[List[user_source.UserSource]] = None) -> None:
        """
        Sets the userSources property value. Data source entity for a the legal hold. This is the container for a mailbox and OneDrive for Business site.
        Args:
            value: Value to set for the userSources property.
        """
        self._user_sources = value
    

