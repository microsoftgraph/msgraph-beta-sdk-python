from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ConfigManagerCollection(entity.Entity):
    """
    A ConfigManager defined collection of devices or users.
    """
    @property
    def collection_identifier(self,) -> Optional[str]:
        """
        Gets the collectionIdentifier property value. The collection identifier in SCCM.
        Returns: Optional[str]
        """
        return self._collection_identifier
    
    @collection_identifier.setter
    def collection_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the collectionIdentifier property value. The collection identifier in SCCM.
        Args:
            value: Value to set for the collectionIdentifier property.
        """
        self._collection_identifier = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new configManagerCollection and sets the default values.
        """
        super().__init__()
        # The collection identifier in SCCM.
        self._collection_identifier: Optional[str] = None
        # The created date.
        self._created_date_time: Optional[datetime] = None
        # The DisplayName.
        self._display_name: Optional[str] = None
        # The Hierarchy Identifier.
        self._hierarchy_identifier: Optional[str] = None
        # The HierarchyName.
        self._hierarchy_name: Optional[str] = None
        # The last modified date.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The created date.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The created date.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConfigManagerCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConfigManagerCollection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConfigManagerCollection()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The DisplayName.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The DisplayName.
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
            "collection_identifier": lambda n : setattr(self, 'collection_identifier', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hierarchy_identifier": lambda n : setattr(self, 'hierarchy_identifier', n.get_str_value()),
            "hierarchy_name": lambda n : setattr(self, 'hierarchy_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hierarchy_identifier(self,) -> Optional[str]:
        """
        Gets the hierarchyIdentifier property value. The Hierarchy Identifier.
        Returns: Optional[str]
        """
        return self._hierarchy_identifier
    
    @hierarchy_identifier.setter
    def hierarchy_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the hierarchyIdentifier property value. The Hierarchy Identifier.
        Args:
            value: Value to set for the hierarchyIdentifier property.
        """
        self._hierarchy_identifier = value
    
    @property
    def hierarchy_name(self,) -> Optional[str]:
        """
        Gets the hierarchyName property value. The HierarchyName.
        Returns: Optional[str]
        """
        return self._hierarchy_name
    
    @hierarchy_name.setter
    def hierarchy_name(self,value: Optional[str] = None) -> None:
        """
        Sets the hierarchyName property value. The HierarchyName.
        Args:
            value: Value to set for the hierarchyName property.
        """
        self._hierarchy_name = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The last modified date.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The last modified date.
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
        writer.write_str_value("collectionIdentifier", self.collection_identifier)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("hierarchyIdentifier", self.hierarchy_identifier)
        writer.write_str_value("hierarchyName", self.hierarchy_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

