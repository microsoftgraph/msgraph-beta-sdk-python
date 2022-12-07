from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
planner_plan_configuration_bucket_definition = lazy_import('msgraph.generated.models.planner_plan_configuration_bucket_definition')
planner_plan_configuration_localization = lazy_import('msgraph.generated.models.planner_plan_configuration_localization')

class PlannerPlanConfiguration(entity.Entity):
    @property
    def buckets(self,) -> Optional[List[planner_plan_configuration_bucket_definition.PlannerPlanConfigurationBucketDefinition]]:
        """
        Gets the buckets property value. The buckets property
        Returns: Optional[List[planner_plan_configuration_bucket_definition.PlannerPlanConfigurationBucketDefinition]]
        """
        return self._buckets
    
    @buckets.setter
    def buckets(self,value: Optional[List[planner_plan_configuration_bucket_definition.PlannerPlanConfigurationBucketDefinition]] = None) -> None:
        """
        Sets the buckets property value. The buckets property
        Args:
            value: Value to set for the buckets property.
        """
        self._buckets = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerPlanConfiguration and sets the default values.
        """
        super().__init__()
        # The buckets property
        self._buckets: Optional[List[planner_plan_configuration_bucket_definition.PlannerPlanConfigurationBucketDefinition]] = None
        # The createdBy property
        self._created_by: Optional[identity_set.IdentitySet] = None
        # The createdDateTime property
        self._created_date_time: Optional[datetime] = None
        # The defaultLanguage property
        self._default_language: Optional[str] = None
        # The lastModifiedBy property
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # The lastModifiedDateTime property
        self._last_modified_date_time: Optional[datetime] = None
        # The localizations property
        self._localizations: Optional[List[planner_plan_configuration_localization.PlannerPlanConfigurationLocalization]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerPlanConfiguration()
    
    @property
    def default_language(self,) -> Optional[str]:
        """
        Gets the defaultLanguage property value. The defaultLanguage property
        Returns: Optional[str]
        """
        return self._default_language
    
    @default_language.setter
    def default_language(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultLanguage property value. The defaultLanguage property
        Args:
            value: Value to set for the defaultLanguage property.
        """
        self._default_language = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(planner_plan_configuration_bucket_definition.PlannerPlanConfigurationBucketDefinition)),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "default_language": lambda n : setattr(self, 'default_language', n.get_str_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(planner_plan_configuration_localization.PlannerPlanConfigurationLocalization)),
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
    def localizations(self,) -> Optional[List[planner_plan_configuration_localization.PlannerPlanConfigurationLocalization]]:
        """
        Gets the localizations property value. The localizations property
        Returns: Optional[List[planner_plan_configuration_localization.PlannerPlanConfigurationLocalization]]
        """
        return self._localizations
    
    @localizations.setter
    def localizations(self,value: Optional[List[planner_plan_configuration_localization.PlannerPlanConfigurationLocalization]] = None) -> None:
        """
        Sets the localizations property value. The localizations property
        Args:
            value: Value to set for the localizations property.
        """
        self._localizations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("defaultLanguage", self.default_language)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("localizations", self.localizations)
    

