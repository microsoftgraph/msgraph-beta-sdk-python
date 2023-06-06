from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_plan_configuration_bucket_localization

from . import entity

@dataclass
class PlannerPlanConfigurationLocalization(entity.Entity):
    # Localized names for configured buckets in the plan configuration.
    buckets: Optional[List[planner_plan_configuration_bucket_localization.PlannerPlanConfigurationBucketLocalization]] = None
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
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlanConfigurationLocalization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerPlanConfigurationLocalization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_plan_configuration_bucket_localization

        fields: Dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(planner_plan_configuration_bucket_localization.PlannerPlanConfigurationBucketLocalization)),
            "languageTag": lambda n : setattr(self, 'language_tag', n.get_str_value()),
            "planTitle": lambda n : setattr(self, 'plan_title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
        writer.write_str_value("languageTag", self.language_tag)
        writer.write_str_value("planTitle", self.plan_title)
    

