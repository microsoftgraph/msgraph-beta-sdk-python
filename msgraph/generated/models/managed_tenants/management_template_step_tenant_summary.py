from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class ManagementTemplateStepTenantSummary(entity.Entity):
    """
    Provides operations to manage the collection of accessReviewDecision entities.
    """
    @property
    def assigned_tenants_count(self,) -> Optional[int]:
        """
        Gets the assignedTenantsCount property value. The assignedTenantsCount property
        Returns: Optional[int]
        """
        return self._assigned_tenants_count
    
    @assigned_tenants_count.setter
    def assigned_tenants_count(self,value: Optional[int] = None) -> None:
        """
        Sets the assignedTenantsCount property value. The assignedTenantsCount property
        Args:
            value: Value to set for the assignedTenantsCount property.
        """
        self._assigned_tenants_count = value
    
    @property
    def compliant_tenants_count(self,) -> Optional[int]:
        """
        Gets the compliantTenantsCount property value. The compliantTenantsCount property
        Returns: Optional[int]
        """
        return self._compliant_tenants_count
    
    @compliant_tenants_count.setter
    def compliant_tenants_count(self,value: Optional[int] = None) -> None:
        """
        Sets the compliantTenantsCount property value. The compliantTenantsCount property
        Args:
            value: Value to set for the compliantTenantsCount property.
        """
        self._compliant_tenants_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managementTemplateStepTenantSummary and sets the default values.
        """
        super().__init__()
        # The assignedTenantsCount property
        self._assigned_tenants_count: Optional[int] = None
        # The compliantTenantsCount property
        self._compliant_tenants_count: Optional[int] = None
        # The createdByUserId property
        self._created_by_user_id: Optional[str] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The dismissedTenantsCount property
        self._dismissed_tenants_count: Optional[int] = None
        # The ineligibleTenantsCount property
        self._ineligible_tenants_count: Optional[int] = None
        # The lastActionByUserId property
        self._last_action_by_user_id: Optional[str] = None
        # The lastActionDateTime property
        self._last_action_date_time: Optional[datetime] = None
        # The managementTemplateCollectionDisplayName property
        self._management_template_collection_display_name: Optional[str] = None
        # The managementTemplateCollectionId property
        self._management_template_collection_id: Optional[str] = None
        # The managementTemplateDisplayName property
        self._management_template_display_name: Optional[str] = None
        # The managementTemplateId property
        self._management_template_id: Optional[str] = None
        # The managementTemplateStepDisplayName property
        self._management_template_step_display_name: Optional[str] = None
        # The managementTemplateStepId property
        self._management_template_step_id: Optional[str] = None
        # The notCompliantTenantsCount property
        self._not_compliant_tenants_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagementTemplateStepTenantSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagementTemplateStepTenantSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagementTemplateStepTenantSummary()
    
    @property
    def dismissed_tenants_count(self,) -> Optional[int]:
        """
        Gets the dismissedTenantsCount property value. The dismissedTenantsCount property
        Returns: Optional[int]
        """
        return self._dismissed_tenants_count
    
    @dismissed_tenants_count.setter
    def dismissed_tenants_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dismissedTenantsCount property value. The dismissedTenantsCount property
        Args:
            value: Value to set for the dismissedTenantsCount property.
        """
        self._dismissed_tenants_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assigned_tenants_count": lambda n : setattr(self, 'assigned_tenants_count', n.get_int_value()),
            "compliant_tenants_count": lambda n : setattr(self, 'compliant_tenants_count', n.get_int_value()),
            "created_by_user_id": lambda n : setattr(self, 'created_by_user_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dismissed_tenants_count": lambda n : setattr(self, 'dismissed_tenants_count', n.get_int_value()),
            "ineligible_tenants_count": lambda n : setattr(self, 'ineligible_tenants_count', n.get_int_value()),
            "last_action_by_user_id": lambda n : setattr(self, 'last_action_by_user_id', n.get_str_value()),
            "last_action_date_time": lambda n : setattr(self, 'last_action_date_time', n.get_datetime_value()),
            "management_template_collection_display_name": lambda n : setattr(self, 'management_template_collection_display_name', n.get_str_value()),
            "management_template_collection_id": lambda n : setattr(self, 'management_template_collection_id', n.get_str_value()),
            "management_template_display_name": lambda n : setattr(self, 'management_template_display_name', n.get_str_value()),
            "management_template_id": lambda n : setattr(self, 'management_template_id', n.get_str_value()),
            "management_template_step_display_name": lambda n : setattr(self, 'management_template_step_display_name', n.get_str_value()),
            "management_template_step_id": lambda n : setattr(self, 'management_template_step_id', n.get_str_value()),
            "not_compliant_tenants_count": lambda n : setattr(self, 'not_compliant_tenants_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ineligible_tenants_count(self,) -> Optional[int]:
        """
        Gets the ineligibleTenantsCount property value. The ineligibleTenantsCount property
        Returns: Optional[int]
        """
        return self._ineligible_tenants_count
    
    @ineligible_tenants_count.setter
    def ineligible_tenants_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ineligibleTenantsCount property value. The ineligibleTenantsCount property
        Args:
            value: Value to set for the ineligibleTenantsCount property.
        """
        self._ineligible_tenants_count = value
    
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
    
    @property
    def management_template_display_name(self,) -> Optional[str]:
        """
        Gets the managementTemplateDisplayName property value. The managementTemplateDisplayName property
        Returns: Optional[str]
        """
        return self._management_template_display_name
    
    @management_template_display_name.setter
    def management_template_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateDisplayName property value. The managementTemplateDisplayName property
        Args:
            value: Value to set for the managementTemplateDisplayName property.
        """
        self._management_template_display_name = value
    
    @property
    def management_template_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateId property value. The managementTemplateId property
        Returns: Optional[str]
        """
        return self._management_template_id
    
    @management_template_id.setter
    def management_template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateId property value. The managementTemplateId property
        Args:
            value: Value to set for the managementTemplateId property.
        """
        self._management_template_id = value
    
    @property
    def management_template_step_display_name(self,) -> Optional[str]:
        """
        Gets the managementTemplateStepDisplayName property value. The managementTemplateStepDisplayName property
        Returns: Optional[str]
        """
        return self._management_template_step_display_name
    
    @management_template_step_display_name.setter
    def management_template_step_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateStepDisplayName property value. The managementTemplateStepDisplayName property
        Args:
            value: Value to set for the managementTemplateStepDisplayName property.
        """
        self._management_template_step_display_name = value
    
    @property
    def management_template_step_id(self,) -> Optional[str]:
        """
        Gets the managementTemplateStepId property value. The managementTemplateStepId property
        Returns: Optional[str]
        """
        return self._management_template_step_id
    
    @management_template_step_id.setter
    def management_template_step_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managementTemplateStepId property value. The managementTemplateStepId property
        Args:
            value: Value to set for the managementTemplateStepId property.
        """
        self._management_template_step_id = value
    
    @property
    def not_compliant_tenants_count(self,) -> Optional[int]:
        """
        Gets the notCompliantTenantsCount property value. The notCompliantTenantsCount property
        Returns: Optional[int]
        """
        return self._not_compliant_tenants_count
    
    @not_compliant_tenants_count.setter
    def not_compliant_tenants_count(self,value: Optional[int] = None) -> None:
        """
        Sets the notCompliantTenantsCount property value. The notCompliantTenantsCount property
        Args:
            value: Value to set for the notCompliantTenantsCount property.
        """
        self._not_compliant_tenants_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("assignedTenantsCount", self.assigned_tenants_count)
        writer.write_int_value("compliantTenantsCount", self.compliant_tenants_count)
        writer.write_str_value("createdByUserId", self.created_by_user_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_int_value("dismissedTenantsCount", self.dismissed_tenants_count)
        writer.write_int_value("ineligibleTenantsCount", self.ineligible_tenants_count)
        writer.write_str_value("lastActionByUserId", self.last_action_by_user_id)
        writer.write_datetime_value("lastActionDateTime", self.last_action_date_time)
        writer.write_str_value("managementTemplateCollectionDisplayName", self.management_template_collection_display_name)
        writer.write_str_value("managementTemplateCollectionId", self.management_template_collection_id)
        writer.write_str_value("managementTemplateDisplayName", self.management_template_display_name)
        writer.write_str_value("managementTemplateId", self.management_template_id)
        writer.write_str_value("managementTemplateStepDisplayName", self.management_template_step_display_name)
        writer.write_str_value("managementTemplateStepId", self.management_template_step_id)
        writer.write_int_value("notCompliantTenantsCount", self.not_compliant_tenants_count)
    

