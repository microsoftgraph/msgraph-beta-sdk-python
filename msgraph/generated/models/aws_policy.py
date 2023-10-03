from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_policy_type import AwsPolicyType
    from .entity import Entity

from .entity import Entity

@dataclass
class AwsPolicy(Entity):
    # The awsPolicyType property
    aws_policy_type: Optional[AwsPolicyType] = None
    # The displayName property
    display_name: Optional[str] = None
    # The externalId property
    external_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AwsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsPolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AwsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_policy_type import AwsPolicyType
        from .entity import Entity

        from .aws_policy_type import AwsPolicyType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "awsPolicyType": lambda n : setattr(self, 'aws_policy_type', n.get_enum_value(AwsPolicyType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
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
        writer.write_enum_value("awsPolicyType", self.aws_policy_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("externalId", self.external_id)
    

