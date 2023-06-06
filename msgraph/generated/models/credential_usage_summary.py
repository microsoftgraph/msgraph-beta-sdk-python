from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, feature_type, usage_auth_method

from . import entity

@dataclass
class CredentialUsageSummary(entity.Entity):
    # The authMethod property
    auth_method: Optional[usage_auth_method.UsageAuthMethod] = None
    # Provides the count of failed resets or registration data.
    failure_activity_count: Optional[int] = None
    # The feature property
    feature: Optional[feature_type.FeatureType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the count of successful registrations or resets.
    successful_activity_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUsageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUsageSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CredentialUsageSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, feature_type, usage_auth_method

        fields: Dict[str, Callable[[Any], None]] = {
            "authMethod": lambda n : setattr(self, 'auth_method', n.get_enum_value(usage_auth_method.UsageAuthMethod)),
            "failureActivityCount": lambda n : setattr(self, 'failure_activity_count', n.get_int_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(feature_type.FeatureType)),
            "successfulActivityCount": lambda n : setattr(self, 'successful_activity_count', n.get_int_value()),
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
        writer.write_enum_value("authMethod", self.auth_method)
        writer.write_int_value("failureActivityCount", self.failure_activity_count)
        writer.write_enum_value("feature", self.feature)
        writer.write_int_value("successfulActivityCount", self.successful_activity_count)
    

