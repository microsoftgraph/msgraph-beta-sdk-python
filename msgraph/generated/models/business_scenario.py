from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

business_scenario_planner = lazy_import('msgraph.generated.models.business_scenario_planner')
entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')

class BusinessScenario(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new BusinessScenario and sets the default values.
        """
        super().__init__()
        # The createdBy property
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ownerAppIds property
        self._owner_app_ids: Optional[List[str]] = None
        # The planner property
        self._planner: Optional[business_scenario_planner.BusinessScenarioPlanner] = None
        # The uniqueName property
        self._unique_name: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BusinessScenario:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BusinessScenario
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BusinessScenario()
    
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
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "owner_app_ids": lambda n : setattr(self, 'owner_app_ids', n.get_collection_of_primitive_values(str)),
            "planner": lambda n : setattr(self, 'planner', n.get_object_value(business_scenario_planner.BusinessScenarioPlanner)),
            "unique_name": lambda n : setattr(self, 'unique_name', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. The lastModifiedBy property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
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
    def owner_app_ids(self,) -> Optional[List[str]]:
        """
        Gets the ownerAppIds property value. The ownerAppIds property
        Returns: Optional[List[str]]
        """
        return self._owner_app_ids
    
    @owner_app_ids.setter
    def owner_app_ids(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the ownerAppIds property value. The ownerAppIds property
        Args:
            value: Value to set for the ownerAppIds property.
        """
        self._owner_app_ids = value
    
    @property
    def planner(self,) -> Optional[business_scenario_planner.BusinessScenarioPlanner]:
        """
        Gets the planner property value. The planner property
        Returns: Optional[business_scenario_planner.BusinessScenarioPlanner]
        """
        return self._planner
    
    @planner.setter
    def planner(self,value: Optional[business_scenario_planner.BusinessScenarioPlanner] = None) -> None:
        """
        Sets the planner property value. The planner property
        Args:
            value: Value to set for the planner property.
        """
        self._planner = value
    
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
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("ownerAppIds", self.owner_app_ids)
        writer.write_object_value("planner", self.planner)
        writer.write_str_value("uniqueName", self.unique_name)
    
    @property
    def unique_name(self,) -> Optional[str]:
        """
        Gets the uniqueName property value. The uniqueName property
        Returns: Optional[str]
        """
        return self._unique_name
    
    @unique_name.setter
    def unique_name(self,value: Optional[str] = None) -> None:
        """
        Sets the uniqueName property value. The uniqueName property
        Args:
            value: Value to set for the uniqueName property.
        """
        self._unique_name = value
    

