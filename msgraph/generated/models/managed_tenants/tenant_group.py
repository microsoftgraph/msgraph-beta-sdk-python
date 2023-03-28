from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import management_action_info, management_intent_info
    from .. import entity

from .. import entity

class TenantGroup(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new tenantGroup and sets the default values.
        """
        super().__init__()
        # A flag indicating whether all managed tenant are included in the tenant group. Required. Read-only.
        self._all_tenants_included: Optional[bool] = None
        # The display name for the tenant group. Optional. Read-only.
        self._display_name: Optional[str] = None
        # The collection of management action associated with the tenant group. Optional. Read-only.
        self._management_actions: Optional[List[management_action_info.ManagementActionInfo]] = None
        # The collection of management intents associated with the tenant group. Optional. Read-only.
        self._management_intents: Optional[List[management_intent_info.ManagementIntentInfo]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of managed tenant identifiers include in the tenant group. Optional. Read-only.
        self._tenant_ids: Optional[List[str]] = None
    
    @property
    def all_tenants_included(self,) -> Optional[bool]:
        """
        Gets the allTenantsIncluded property value. A flag indicating whether all managed tenant are included in the tenant group. Required. Read-only.
        Returns: Optional[bool]
        """
        return self._all_tenants_included
    
    @all_tenants_included.setter
    def all_tenants_included(self,value: Optional[bool] = None) -> None:
        """
        Sets the allTenantsIncluded property value. A flag indicating whether all managed tenant are included in the tenant group. Required. Read-only.
        Args:
            value: Value to set for the all_tenants_included property.
        """
        self._all_tenants_included = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TenantGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TenantGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TenantGroup()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the tenant group. Optional. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the tenant group. Optional. Read-only.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import management_action_info, management_intent_info
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "allTenantsIncluded": lambda n : setattr(self, 'all_tenants_included', n.get_bool_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "managementActions": lambda n : setattr(self, 'management_actions', n.get_collection_of_object_values(management_action_info.ManagementActionInfo)),
            "managementIntents": lambda n : setattr(self, 'management_intents', n.get_collection_of_object_values(management_intent_info.ManagementIntentInfo)),
            "tenantIds": lambda n : setattr(self, 'tenant_ids', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def management_actions(self,) -> Optional[List[management_action_info.ManagementActionInfo]]:
        """
        Gets the managementActions property value. The collection of management action associated with the tenant group. Optional. Read-only.
        Returns: Optional[List[management_action_info.ManagementActionInfo]]
        """
        return self._management_actions
    
    @management_actions.setter
    def management_actions(self,value: Optional[List[management_action_info.ManagementActionInfo]] = None) -> None:
        """
        Sets the managementActions property value. The collection of management action associated with the tenant group. Optional. Read-only.
        Args:
            value: Value to set for the management_actions property.
        """
        self._management_actions = value
    
    @property
    def management_intents(self,) -> Optional[List[management_intent_info.ManagementIntentInfo]]:
        """
        Gets the managementIntents property value. The collection of management intents associated with the tenant group. Optional. Read-only.
        Returns: Optional[List[management_intent_info.ManagementIntentInfo]]
        """
        return self._management_intents
    
    @management_intents.setter
    def management_intents(self,value: Optional[List[management_intent_info.ManagementIntentInfo]] = None) -> None:
        """
        Sets the managementIntents property value. The collection of management intents associated with the tenant group. Optional. Read-only.
        Args:
            value: Value to set for the management_intents property.
        """
        self._management_intents = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allTenantsIncluded", self.all_tenants_included)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("managementActions", self.management_actions)
        writer.write_collection_of_object_values("managementIntents", self.management_intents)
        writer.write_collection_of_primitive_values("tenantIds", self.tenant_ids)
    
    @property
    def tenant_ids(self,) -> Optional[List[str]]:
        """
        Gets the tenantIds property value. The collection of managed tenant identifiers include in the tenant group. Optional. Read-only.
        Returns: Optional[List[str]]
        """
        return self._tenant_ids
    
    @tenant_ids.setter
    def tenant_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the tenantIds property value. The collection of managed tenant identifiers include in the tenant group. Optional. Read-only.
        Args:
            value: Value to set for the tenant_ids property.
        """
        self._tenant_ids = value
    

