from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import data_source_hold_status, site_source, unified_group_source, user_source
    from .. import entity, identity_set

from .. import entity

class DataSource(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new dataSource and sets the default values.
        """
        super().__init__()
        # The user who created the dataSource.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The date and time the dataSource was created.
        self._created_date_time: Optional[datetime] = None
        # The display name of the dataSource. This will be the name of the SharePoint site.
        self._display_name: Optional[str] = None
        # The hold status of the dataSource.The possible values are: notApplied, applied, applying, removing, partial
        self._hold_status: Optional[data_source_hold_status.DataSourceHoldStatus] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The user who created the dataSource.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The user who created the dataSource.
        Args:
            value: Value to set for the created_by property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time the dataSource was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time the dataSource was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.security.siteSource":
                from . import site_source

                return site_source.SiteSource()
            if mapping_value == "#microsoft.graph.security.unifiedGroupSource":
                from . import unified_group_source

                return unified_group_source.UnifiedGroupSource()
            if mapping_value == "#microsoft.graph.security.userSource":
                from . import user_source

                return user_source.UserSource()
        return DataSource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the dataSource. This will be the name of the SharePoint site.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the dataSource. This will be the name of the SharePoint site.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import data_source_hold_status, site_source, unified_group_source, user_source
        from .. import entity, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "holdStatus": lambda n : setattr(self, 'hold_status', n.get_enum_value(data_source_hold_status.DataSourceHoldStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hold_status(self,) -> Optional[data_source_hold_status.DataSourceHoldStatus]:
        """
        Gets the holdStatus property value. The hold status of the dataSource.The possible values are: notApplied, applied, applying, removing, partial
        Returns: Optional[data_source_hold_status.DataSourceHoldStatus]
        """
        return self._hold_status
    
    @hold_status.setter
    def hold_status(self,value: Optional[data_source_hold_status.DataSourceHoldStatus] = None) -> None:
        """
        Sets the holdStatus property value. The hold status of the dataSource.The possible values are: notApplied, applied, applying, removing, partial
        Args:
            value: Value to set for the hold_status property.
        """
        self._hold_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("holdStatus", self.hold_status)
    

