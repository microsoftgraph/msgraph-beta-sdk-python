from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
tenant_info = lazy_import('msgraph.generated.models.managed_tenants.tenant_info')

class TenantTag(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new tenantTag and sets the default values.
        """
        super().__init__()
        # The identifier for the account that created the tenant tag. Required. Read-only.
        self._created_by_user_id: Optional[str] = None
        # The date and time when the tenant tag was created. Required. Read-only.
        self._created_date_time: Optional[datetime] = None
        # The date and time when the tenant tag was deleted. Required. Read-only.
        self._deleted_date_time: Optional[datetime] = None
        # The description for the tenant tag. Optional. Read-only.
        self._description: Optional[str] = None
        # The display name for the tenant tag. Required. Read-only.
        self._display_name: Optional[str] = None
        # The identifier for the account that lasted on the tenant tag. Optional. Read-only.
        self._last_action_by_user_id: Optional[str] = None
        # The date and time the last action was performed against the tenant tag. Optional. Read-only.
        self._last_action_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of managed tenants associated with the tenant tag. Optional.
        self._tenants: Optional[List[tenant_info.TenantInfo]] = None
    
    @property
    def created_by_user_id(self,) -> Optional[str]:
        """
        Gets the createdByUserId property value. The identifier for the account that created the tenant tag. Required. Read-only.
        Returns: Optional[str]
        """
        return self._created_by_user_id
    
    @created_by_user_id.setter
    def created_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the createdByUserId property value. The identifier for the account that created the tenant tag. Required. Read-only.
        Args:
            value: Value to set for the createdByUserId property.
        """
        self._created_by_user_id = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the tenant tag was created. Required. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the tenant tag was created. Required. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantTag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantTag()
    
    @property
    def deleted_date_time(self,) -> Optional[datetime]:
        """
        Gets the deletedDateTime property value. The date and time when the tenant tag was deleted. Required. Read-only.
        Returns: Optional[datetime]
        """
        return self._deleted_date_time
    
    @deleted_date_time.setter
    def deleted_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the deletedDateTime property value. The date and time when the tenant tag was deleted. Required. Read-only.
        Args:
            value: Value to set for the deletedDateTime property.
        """
        self._deleted_date_time = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the tenant tag. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the tenant tag. Optional. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the tenant tag. Required. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the tenant tag. Required. Read-only.
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
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deleted_date_time": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "tenants": lambda n : setattr(self, 'tenants', n.get_collection_of_object_values(tenant_info.TenantInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_action_by_user_id(self,) -> Optional[str]:
        """
        Gets the lastActionByUserId property value. The identifier for the account that lasted on the tenant tag. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._last_action_by_user_id
    
    @last_action_by_user_id.setter
    def last_action_by_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the lastActionByUserId property value. The identifier for the account that lasted on the tenant tag. Optional. Read-only.
        Args:
            value: Value to set for the lastActionByUserId property.
        """
        self._last_action_by_user_id = value
    
    @property
    def last_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastActionDateTime property value. The date and time the last action was performed against the tenant tag. Optional. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_action_date_time
    
    @last_action_date_time.setter
    def last_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastActionDateTime property value. The date and time the last action was performed against the tenant tag. Optional. Read-only.
        Args:
            value: Value to set for the lastActionDateTime property.
        """
        self._last_action_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_collection_of_object_values("tenants", self.tenants)
    
    @property
    def tenants(self,) -> Optional[List[tenant_info.TenantInfo]]:
        """
        Gets the tenants property value. The collection of managed tenants associated with the tenant tag. Optional.
        Returns: Optional[List[tenant_info.TenantInfo]]
        """
        return self._tenants
    
    @tenants.setter
    def tenants(self,value: Optional[List[tenant_info.TenantInfo]] = None) -> None:
        """
        Sets the tenants property value. The collection of managed tenants associated with the tenant tag. Optional.
        Args:
            value: Value to set for the tenants property.
        """
        self._tenants = value
    

