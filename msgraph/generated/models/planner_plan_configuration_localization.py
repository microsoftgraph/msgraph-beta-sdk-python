from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_plan_configuration_bucket_localization import PlannerPlanConfigurationBucketLocalization

from .entity import Entity

@dataclass
class PlannerPlanConfigurationLocalization(Entity):
    # Localized names for configured buckets in the plan configuration.
    buckets: Optional[List[PlannerPlanConfigurationBucketLocalization]] = None
    # The language code associated with the localized names in this object.
    language_tag: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Localized title of the plan.
    plan_title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerPlanConfigurationLocalization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanConfigurationLocalization
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PlannerPlanConfigurationLocalization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_plan_configuration_bucket_localization import PlannerPlanConfigurationBucketLocalization

        from .entity import Entity
        from .planner_plan_configuration_bucket_localization import PlannerPlanConfigurationBucketLocalization

        fields: Dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(PlannerPlanConfigurationBucketLocalization)),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "planTitle": lambda n : setattr(self, 'plan_title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("planTitle", self.plan_title)
    

