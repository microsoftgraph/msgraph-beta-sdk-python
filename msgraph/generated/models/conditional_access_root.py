from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_context_class_reference import AuthenticationContextClassReference
    from .authentication_strength_root import AuthenticationStrengthRoot
    from .conditional_access_policy import ConditionalAccessPolicy
    from .conditional_access_template import ConditionalAccessTemplate
    from .entity import Entity
    from .named_location import NamedLocation

from .entity import Entity

@dataclass
class ConditionalAccessRoot(Entity):
    # Read-only. Nullable. Returns a collection of the specified authentication context class references.
    authentication_context_class_references: Optional[List[AuthenticationContextClassReference]] = None
    # Defines the authentication strength policies, valid authentication method combinations, and authentication method mode details that can be required by a conditional access policy.
    authentication_strength: Optional[AuthenticationStrengthRoot] = None
    # The authenticationStrengths property
    authentication_strengths: Optional[AuthenticationStrengthRoot] = None
    # Read-only. Nullable. Returns a collection of the specified named locations.
    named_locations: Optional[List[NamedLocation]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Nullable. Returns a collection of the specified Conditional Access policies.
    policies: Optional[List[ConditionalAccessPolicy]] = None
    # Read-only. Nullable. Returns a collection of the specified Conditional Access templates.
    templates: Optional[List[ConditionalAccessTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_template import ConditionalAccessTemplate
        from .entity import Entity
        from .named_location import NamedLocation

        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_template import ConditionalAccessTemplate
        from .entity import Entity
        from .named_location import NamedLocation

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationContextClassReferences": lambda n : setattr(self, 'authentication_context_class_references', n.get_collection_of_object_values(AuthenticationContextClassReference)),
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(AuthenticationStrengthRoot)),
            "authenticationStrengths": lambda n : setattr(self, 'authentication_strengths', n.get_object_value(AuthenticationStrengthRoot)),
            "namedLocations": lambda n : setattr(self, 'named_locations', n.get_collection_of_object_values(NamedLocation)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(ConditionalAccessPolicy)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(ConditionalAccessTemplate)),
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
        writer.write_collection_of_object_values("authenticationContextClassReferences", self.authentication_context_class_references)
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_object_value("authenticationStrengths", self.authentication_strengths)
        writer.write_collection_of_object_values("namedLocations", self.named_locations)
        writer.write_collection_of_object_values("policies", self.policies)
        writer.write_collection_of_object_values("templates", self.templates)
    

