from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aws_identity import AwsIdentity
    from .aws_user import AwsUser

from .aws_identity import AwsIdentity

@dataclass
class AwsAccessKey(AwsIdentity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.awsAccessKey"
    # The owner property
    owner: Optional[AwsUser] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AwsAccessKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AwsAccessKey
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AwsAccessKey()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .aws_identity import AwsIdentity
        from .aws_user import AwsUser

        from .aws_identity import AwsIdentity
        from .aws_user import AwsUser

        fields: Dict[str, Callable[[Any], None]] = {
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(AwsUser)),
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
        writer.write_object_value("owner", self.owner)
    

