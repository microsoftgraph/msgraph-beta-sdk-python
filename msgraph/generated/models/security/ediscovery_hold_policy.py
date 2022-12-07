from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

policy_base = lazy_import('msgraph.generated.models.security.policy_base')
site_source = lazy_import('msgraph.generated.models.security.site_source')
user_source = lazy_import('msgraph.generated.models.security.user_source')

class EdiscoveryHoldPolicy(policy_base.PolicyBase):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryHoldPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryHoldPolicy"
        # KQL query that specifies content to be held in the specified locations. To learn more, see Keyword queries and search conditions for Content Search and eDiscovery.  To hold all content in the specified locations, leave contentQuery blank.
        self._content_query: Optional[str] = None
        # Lists any errors that happened while placing the hold.
        self._errors: Optional[List[str]] = None
        # Indicates whether the hold is enabled and actively holding content.
        self._is_enabled: Optional[bool] = None
        # Data sources that represent SharePoint sites.
        self._site_sources: Optional[List[site_source.SiteSource]] = None
        # Data sources that represent Exchange mailboxes.
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryHoldPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryHoldPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryHoldPolicy()
    
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
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_primitive_values(str)),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "site_sources": lambda n : setattr(self, 'site_sources', n.get_collection_of_object_values(site_source.SiteSource)),
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
        writer.write_collection_of_primitive_values("errors", self.errors)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_object_values("siteSources", self.site_sources)
        writer.write_collection_of_object_values("userSources", self.user_sources)
    
    @property
    def site_sources(self,) -> Optional[List[site_source.SiteSource]]:
        """
        Gets the siteSources property value. Data sources that represent SharePoint sites.
        Returns: Optional[List[site_source.SiteSource]]
        """
        return self._site_sources
    
    @site_sources.setter
    def site_sources(self,value: Optional[List[site_source.SiteSource]] = None) -> None:
        """
        Sets the siteSources property value. Data sources that represent SharePoint sites.
        Args:
            value: Value to set for the siteSources property.
        """
        self._site_sources = value
    
    @property
    def user_sources(self,) -> Optional[List[user_source.UserSource]]:
        """
        Gets the userSources property value. Data sources that represent Exchange mailboxes.
        Returns: Optional[List[user_source.UserSource]]
        """
        return self._user_sources
    
    @user_sources.setter
    def user_sources(self,value: Optional[List[user_source.UserSource]] = None) -> None:
        """
        Sets the userSources property value. Data sources that represent Exchange mailboxes.
        Args:
            value: Value to set for the userSources property.
        """
        self._user_sources = value
    

