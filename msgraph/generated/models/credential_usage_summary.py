from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .feature_type import FeatureType
    from .usage_auth_method import UsageAuthMethod

from .entity import Entity

@dataclass
class CredentialUsageSummary(Entity):
    # The authMethod property
    auth_method: Optional[UsageAuthMethod] = None
    # Provides the count of failed resets or registration data.
    failure_activity_count: Optional[int] = None
    # The feature property
    feature: Optional[FeatureType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Provides the count of successful registrations or resets.
    successful_activity_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CredentialUsageSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CredentialUsageSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CredentialUsageSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .feature_type import FeatureType
        from .usage_auth_method import UsageAuthMethod

        from .entity import Entity
        from .feature_type import FeatureType
        from .usage_auth_method import UsageAuthMethod

        fields: Dict[str, Callable[[Any], None]] = {
            "authMethod": lambda n : setattr(self, 'auth_method', n.get_enum_value(UsageAuthMethod)),
            "failureActivityCount": lambda n : setattr(self, 'failure_activity_count', n.get_int_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(FeatureType)),
            "successfulActivityCount": lambda n : setattr(self, 'successful_activity_count', n.get_int_value()),
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
        writer.write_enum_value("authMethod", self.auth_method)
        writer.write_int_value("failureActivityCount", self.failure_activity_count)
        writer.write_enum_value("feature", self.feature)
        writer.write_int_value("successfulActivityCount", self.successful_activity_count)
    

